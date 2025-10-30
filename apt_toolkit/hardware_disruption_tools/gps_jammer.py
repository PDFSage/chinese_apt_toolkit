"""GPS jamming signal generation utilities."""

from __future__ import annotations

import math
from typing import Callable

import numpy as np

try:  # SciPy is optional; provide a lightweight fallback when missing.
    from scipy.signal import chirp as _scipy_chirp  # type: ignore
except ImportError:  # pragma: no cover - exercised when SciPy is unavailable
    _scipy_chirp = None


def _linear_chirp(
    t: np.ndarray,
    f0: float,
    f1: float,
    t1: float,
    method: str = "linear",
) -> np.ndarray:
    """Minimal linear chirp implementation used when SciPy is unavailable."""
    if method != "linear":
        raise ValueError("Fallback chirp implementation only supports linear sweeps")

    sweep_rate = (f1 - f0) / t1
    # Integrate instantaneous frequency to produce the linear chirp waveform.
    phase = 2.0 * math.pi * (f0 * t + 0.5 * sweep_rate * t**2)
    return np.cos(phase, dtype=np.float64)


def _get_chirp() -> Callable[..., np.ndarray]:
    """Return the available chirp implementation."""
    if _scipy_chirp is not None:
        return _scipy_chirp
    return _linear_chirp


def generate_gps_jamming_signal() -> np.ndarray:
    """Generate a synthetic GPS jamming signal suitable for simulations/tests."""
    # In a real scenario, you would use a software-defined radio to transmit this signal.
    t = np.linspace(0.0, 1.0, 1000, dtype=np.float64)
    chirp_fn = _get_chirp()
    signal = chirp_fn(t, f0=1575.42e6 - 1e6, f1=1575.42e6 + 1e6, t1=1.0, method="linear")
    print("GPS jamming signal generated")
    return signal


def main() -> None:
    """CLI entry point for manual execution."""
    generate_gps_jamming_signal()


if __name__ == "__main__":
    main()
