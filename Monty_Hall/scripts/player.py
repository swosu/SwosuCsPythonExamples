# player.py
from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Optional, Sequence


@dataclass
class PlayerDecision:
    """Optional convenience bundle if you ever want to return both decisions together."""
    initial_pick: int
    switch: bool


class Player:
    """
    Player makes two RANDOM decisions:
      1) choose_initial_door(): uniform among doors
      2) decide_switch_or_stay(): 50/50 switch vs stay
    """

    def __init__(self, rng: Optional[random.Random] = None, doors: Sequence[int] = (1, 2, 3)) -> None:
        self._rng = rng or random.Random()
        self._doors = tuple(doors)
        if len(self._doors) < 2:
            raise ValueError("doors must contain at least 2 options.")
        if len(set(self._doors)) != len(self._doors):
            raise ValueError("doors must not contain duplicates.")

    def choose_initial_door(self) -> int:
        """Uniform random choice over available doors."""
        return self._rng.choice(self._doors)

    def decide_switch_or_stay(self) -> bool:
        """
        Uniform random boolean:
          - True  => switch
          - False => stay
        """
        # getrandbits(1) is an efficient unbiased 0/1
        return bool(self._rng.getrandbits(1))

    def make_decision(self) -> PlayerDecision:
        """Convenience method (optional): make both decisions."""
        return PlayerDecision(
            initial_pick=self.choose_initial_door(),
            switch=self.decide_switch_or_stay(),
        )


if __name__ == "__main__":
    # Quick sanity demo (optional)
    p = Player()
    print("Initial door:", p.choose_initial_door())
    print("Switch?:", p.decide_switch_or_stay())
    print("Both:", p.make_decision())
