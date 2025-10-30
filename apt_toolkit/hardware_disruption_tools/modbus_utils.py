"""Utilities for providing a Modbus client abstraction in tests."""

from __future__ import annotations

try:  # pymodbus is optional; expose a lightweight stub when missing.
    from pymodbus.client import ModbusTcpClient as _ModbusTcpClient  # type: ignore
except ImportError:  # pragma: no cover - executed when pymodbus is unavailable
    class _ModbusTcpClient:  # type: ignore[override]
        """Minimal stub to emulate the pymodbus ModbusTcpClient API."""

        def __init__(self, host: str, port: int = 502) -> None:
            self.host = host
            self.port = port
            self.connected = False

        def connect(self) -> bool:
            self.connected = True
            return self.connected

        def write_register(self, address: int, value: int) -> None:
            if not self.connected:
                raise RuntimeError("Client not connected")
            # No-op for the stub; real implementation would send a Modbus frame.

        def close(self) -> None:
            self.connected = False


ModbusTcpClient = _ModbusTcpClient

__all__ = ["ModbusTcpClient"]
