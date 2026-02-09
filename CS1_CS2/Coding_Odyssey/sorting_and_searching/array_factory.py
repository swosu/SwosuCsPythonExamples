# array_factory.py
from __future__ import annotations

import random
from typing import Optional, List


class RandomArrayFactory:
    """
    Generates random integer arrays.

    Defaults ensure that 0 is never generated, so target=0 is guaranteed "not found".
    """

    def __init__(self, rng: Optional[random.Random] = None) -> None:
        self._rng = rng or random.Random()

    def build(self, size: int, low: int = 1, high_multiplier: int = 10) -> List[int]:
        if size <= 0:
            raise ValueError("size must be > 0")

        high = max(low, size * high_multiplier)
        return [self._rng.randint(low, high) for _ in range(size)]
