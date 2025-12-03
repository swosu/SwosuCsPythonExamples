"""
monty_hall/rng.py

A small wrapper around Python's random module to:
- keep randomness centralized
- make runs reproducible via seeding
- make unit testing easier (you can swap/mock this later if desired)
"""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Sequence, TypeVar

T = TypeVar("T")


@dataclass(slots=True)
class RNG:
    seed: int

    def __post_init__(self) -> None:
        self._r = random.Random(self.seed)

    def randint(self, a: int, b: int) -> int:
        """Return random integer in [a, b], inclusive."""
        return self._r.randint(a, b)

    def choice(self, seq: Sequence[T]) -> T:
        """Return a random element from a non-empty sequence."""
        if not seq:
            raise ValueError("choice() requires a non-empty sequence")
        return self._r.choice(seq)

    def random(self) -> float:
        """Return float in [0.0, 1.0)."""
        return self._r.random()

    def coinflip(self) -> bool:
        """Return True/False with 50/50 probability."""
        return self.random() < 0.5
