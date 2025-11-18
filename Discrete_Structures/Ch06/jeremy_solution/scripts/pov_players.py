# scripts/pov_players.py
"""
Player factory for Presidents of Virtue.

Provides:
- create_oklahoma_players(): returns a list of 5 Player objects
  with western-Oklahoma-flavored names and different strategies.
"""

import random
from typing import List

from presidents_engine import (
    Player,
    GreedyStrategy,
    CautiousStrategy,
    PairLoverStrategy,
    ChaosRevolutionaryStrategy,
    RandomStrategy,
)


def create_oklahoma_players() -> List[Player]:
    name_pool = [
        "Cody", "Savannah", "Rhett", "Kaylee", "Tyler",
        "Maggie", "Blake", "Cheyenne", "Jace", "Hadley"
    ]
    chosen_names = random.sample(name_pool, 5)

    strategies = [
        GreedyStrategy(),
        CautiousStrategy(),
        PairLoverStrategy(),
        ChaosRevolutionaryStrategy(),
        RandomStrategy(),
    ]

    players: List[Player] = []
    for name, strat in zip(chosen_names, strategies):
        players.append(Player(name=name, strategy=strat))
    return players

