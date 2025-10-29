import unittest
from argparse import Namespace
from datetime import datetime
from unittest.mock import patch

from apt_toolkit.american_targets import analyze_american_targets
from apt_toolkit.cli import handle_command


class AmericanTargetsAnalysisTests(unittest.TestCase):
    def test_analysis_includes_profiles_and_supply_chain(self):
        with patch("apt_toolkit.american_targets.datetime") as mock_datetime, patch(
            "apt_toolkit.initial_access_enhanced.datetime"
        ) as mock_initial_datetime:
            mock_datetime.now.return_value = datetime(2024, 1, 1, 0, 0, 0)
            mock_initial_datetime.now.return_value = datetime(2024, 1, 1, 20, 0, 0)

            analysis = analyze_american_targets()

        self.assertIn("american_networks", analysis)
        self.assertIn("target_profiles", analysis)
        self.assertIn("supply_chain_readiness", analysis)
        self.assertGreater(len(analysis["american_networks"]), 0)
        self.assertEqual(
            len(analysis["target_profiles"]), len(analysis["american_networks"])
        )
        self.assertEqual(
            len(analysis["supply_chain_readiness"]),
            len(analysis["american_networks"]),
        )
        for profile in analysis["target_profiles"]:
            self.assertIn("target_domain", profile)
            self.assertIn("target_email", profile)
            self.assertIn("lure", profile)

    def test_handle_command_routes_to_american_targets(self):
        args = Namespace(module="american", action="targets", json=False)

        with patch(
            "apt_toolkit.cli.analyze_american_targets", return_value={"mock": True}
        ) as mock_analyze:
            result = handle_command(args)

        self.assertEqual(result, {"american_targets": {"mock": True}})
        mock_analyze.assert_called_once_with()


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
