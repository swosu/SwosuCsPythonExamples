"""
cards.py — Core card primitives for Presidents.

Design notes:
- Rank strength: 3 (lowest) … A < 2 (highest)
- Suits are cosmetic for Presidents, but we keep them for readability.
- Provides: Card, new_deck(), sort_hand(), deal_hands()
"""

from typing import List, Optional
from dataclasses import dataclass
from functools import total_ordering
from typing import List, Iterable
import random

# Presidents rank order: 3 < 4 < ... < 10 < J < Q < K < A < 2
RANKS: List[str] = ["3","4","5","6","7","8","9","10","J","Q","K","A","2"]
SUITS: List[str] = ["♣", "♦", "♥", "♠"]   # purely cosmetic in this game

RANK_TO_VALUE = {r: i for i, r in enumerate(RANKS)}
SUIT_TO_VALUE = {s: i for i, s in enumerate(SUITS)}  # stable tie-break for sorting

@total_ordering
@dataclass(frozen=True)
class Card:
    rank: str
    suit: str

    def __post_init__(self):
        if self.rank not in RANK_TO_VALUE:
            raise ValueError(f"Invalid rank: {self.rank!r}")
        if self.suit not in SUITS:
            raise ValueError(f"Invalid suit: {self.suit!r}")

    @property
    def value(self) -> int:
        """Rank strength index (higher = stronger)."""
        return RANK_TO_VALUE[self.rank]

    def __lt__(self, other: "Card") -> bool:
        if not isinstance(other, Card):
            return NotImplemented
        if self.value != other.value:
            return self.value < other.value
        # suits don’t matter for legality; this is only for deterministic sorting/printing
        return SUIT_TO_VALUE[self.suit] < SUIT_TO_VALUE[other.suit]

    def __str__(self) -> str:
        return f"{self.rank}{self.suit}"

    def __repr__(self) -> str:
        return f"Card({self.rank!r}, {self.suit!r})"

def new_deck() -> List[Card]:
    """Return a fresh 52-card deck (no jokers)."""
    return [Card(r, s) for r in RANKS for s in SUITS]

def sort_hand(cards: Iterable[Card]) -> List[Card]:
    """Return a new list of cards sorted by game strength (3..2), then suit."""
    return sorted(cards)


def deal_hands(num_players: int, rng: Optional[random.Random] = None) -> List[List[Card]]:
    """
    Deal the entire deck one card at a time, clockwise.
    Some players may get one extra card when 52 % num_players != 0.
    """
    if num_players < 2:
        raise ValueError("Need at least 2 players.")
    if num_players > 10:
        # You *can* play with more, but the hands get tiny and sad.
        raise ValueError("Let’s cap at 10 players for now.")

    rng = rng or random.Random()
    deck = new_deck()
    rng.shuffle(deck)

    hands: List[List[Card]] = [[] for _ in range(num_players)]
    for i, card in enumerate(deck):
        hands[i % num_players].append(card)

    # Sort each hand for easier human reading
    hands = [sort_hand(h) for h in hands]
    return hands

# Tiny smoke test so you can run `python cards.py` and see something friendly.
if __name__ == "__main__":
    hands = deal_hands(num_players=4)
    for i, h in enumerate(hands, start=1):
        print(f"Player {i} ({len(h)} cards):", " ".join(map(str, h)))
