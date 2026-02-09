# sizes.py
from __future__ import annotations


def log_sizes(start: int = 10, decades: int = 6) -> list[int]:
    """
    Log-ish growth sizes: start, start*10, start*100, ...
    decades=6 -> 10, 100, 1000, 10000, 100000, 1000000
    """
    if start <= 0:
        raise ValueError("start must be > 0")
    if decades < 1:
        raise ValueError("decades must be >= 1")

    sizes: list[int] = []
    value = start
    for _ in range(decades):
        sizes.append(value)
        value *= 10
    return sizes
