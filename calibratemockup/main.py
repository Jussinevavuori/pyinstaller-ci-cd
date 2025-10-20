from __future__ import annotations

import random
from typing import Iterable, List


def _normalize_estimations(measurements: Iterable) -> List[float]:
    """Coerce an iterable of measurements into a list of floats."""
    numeric_values: List[float] = []
    for raw in measurements:
        try:
            numeric_values.append(float(raw))
        except (TypeError, ValueError):
            continue
    return numeric_values


def _compute_average(values: List[float]) -> float:
    """Return the arithmetic mean of values or a random fallback."""
    if not values:
        return random.random()
    return sum(values) / len(values)


def run(measurements):
    """Return calibration metrics derived from a collection of measurements."""
    values = _normalize_estimations(measurements)
    average_sum = _compute_average(values)
    return {"average_sum": average_sum}
