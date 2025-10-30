import importlib.util
from contextlib import ExitStack
from pathlib import Path
from unittest import mock

import pytest


RUN_CAMPAIGN_FILES = sorted(
    Path("campaigns").glob("*/run_campaign.py"),
    key=lambda path: path.parent.name,
)

PYTHON_TOOL_FILES = sorted(
    {
        *Path("campaigns").rglob("*.py"),
        *Path("tools").rglob("*.py"),
    },
    key=lambda path: (path.parts, path.name),
)


def _load_module_from_path(module_path: Path):
    module_name = f"{module_path.parent.name}_run_module"
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize("run_script", RUN_CAMPAIGN_FILES, ids=lambda p: str(p))
def test_run_campaign_invokes_existing_scripts(run_script: Path):
    module = _load_module_from_path(run_script)
    assert hasattr(module, "main"), f"{run_script} does not define a main() entry point"

    calls = []

    def fake_run(cmd, *args, **kwargs):  # noqa: ANN001
        calls.append(cmd)
        return mock.Mock(returncode=0)

    if hasattr(module, "subprocess") and hasattr(module.subprocess, "run"):
        with mock.patch.object(module.subprocess, "run", side_effect=fake_run):
            module.main()

        assert calls, f"{run_script} did not invoke any subprocess commands"

        for cmd in calls:
            assert isinstance(cmd, list), f"{run_script} subprocess command is not a list"
            assert len(cmd) >= 2, f"{run_script} subprocess command is missing a target script"
            interpreter = cmd[0]
            assert interpreter in {"python3", "python"}, f"Unexpected interpreter '{interpreter}' in {run_script}"
            target = Path(cmd[1])
            assert target.is_file(), f"Target script {target} referenced by {run_script} is missing"
    else:
        campaign_stub = mock.Mock(return_value={"status": "ok"})
        targets_stub = mock.Mock(return_value=["target"])

        with ExitStack() as stack:
            if hasattr(module, "simulate_campaign"):
                stack.enter_context(mock.patch.object(module, "simulate_campaign", campaign_stub))
            if hasattr(module, "read_targets"):
                stack.enter_context(mock.patch.object(module, "read_targets", targets_stub))
            result = module.main()

        if hasattr(module, "read_targets"):
            targets_stub.assert_called_once()
        if hasattr(module, "simulate_campaign"):
            campaign_stub.assert_called_once()
            assert result == campaign_stub.return_value


@pytest.mark.parametrize("script_path", PYTHON_TOOL_FILES, ids=lambda p: str(p))
def test_campaign_and_tool_python_scripts_compile(script_path: Path):
    source = script_path.read_text(encoding="utf-8")
    compile(source, str(script_path), "exec")
