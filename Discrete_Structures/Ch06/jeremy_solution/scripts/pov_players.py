# scripts/pov_players.py
"""
Player factory functions for Presidents of Virtue.
"""

from typing import List

from presidents_engine import Player
from pov_strategies import (
    CautiousStrategy,
    GreedyStrategy,
    PairLoverStrategy,
    ChaosRevolutionaryStrategy,
    RandomStrategy,
    SmartGreedyStrategy,
    HumanStrategy,
)


def create_oklahoma_players() -> List[Player]:
    """
    Default AI-only table with familiar western Oklahoma names.
    """
    return [
        Player("Savannah", GreedyStrategy()),
        Player("Cody", CautiousStrategy()),
        Player("Tyler", PairLoverStrategy()),
        Player("Hadley", ChaosRevolutionaryStrategy()),
        Player("Blake", RandomStrategy()),
    ]


def create_oklahoma_with_human(
    human_name: str = "Jeremy",
    human_position: int = 0,
    use_smart_bot: bool = True,
) -> List[Player]:
    """
    Same cast, but one seat is controlled by a human.

    human_position is the index (0–4) where the human sits.
    Optionally uses SmartGreedyStrategy for Cody.
    """
    bots = [
        Player("Savannah", GreedyStrategy()),
        Player("Cody", SmartGreedyStrategy() if use_smart_bot else CautiousStrategy()),
        Player("Tyler", PairLoverStrategy()),
        Player("Hadley", ChaosRevolutionaryStrategy()),
        Player("Blake", RandomStrategy()),
    ]

    players = bots
    human_player = Player(human_name, HumanStrategy())
    players[human_position] = human_player
    return players

