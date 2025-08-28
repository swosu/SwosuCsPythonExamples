# Presidents/trick.py
"""
trick.py — Move representation & legality for Presidents (baseline rules).

Rules (baseline, no bombs/jokers yet):
- A play is a set of 1–4 cards of the SAME RANK (single, pair, triple, quad).
- When LEADING a new trick (previous_play is None), any valid play is allowed.
- When FOLLOWING, you must match the SIZE and beat the RANK strictly.
- Ranks use the same ordering as cards.py: 3 < ... < A < 2.
"""

from dataclasses import dataclass
from typing import List, Optional, Literal
from cards import Card, RANK_TO_VALUE

PlayKind = Literal["single", "pair", "triple", "quad"]

COUNT_TO_KIND = {1: "single", 2: "pair", 3: "triple", 4: "quad"}

@dataclass(frozen=True)
class Play:
    kind: PlayKind
    rank: str     # e.g., "7"
    count: int    # 1..4, redundant with kind but handy to keep

    def strength(self) -> int:
        """Numeric strength for comparison (rank only; higher is stronger)."""
        return RANK_TO_VALUE[self.rank]

def _all_same_rank(cards: List[Card]) -> bool:
    return len(cards) > 0 and len({c.rank for c in cards}) == 1

def make_play(cards: List[Card]) -> Play:
    """
    Convert 1–4 cards of the same rank into a Play.
    Raises ValueError if invalid (size or mixed ranks).
    """
    n = len(cards)
    if n < 1 or n > 4:
        raise ValueError(f"Play must contain 1–4 cards, got {n}.")
    if not _all_same_rank(cards):
        raise ValueError("All cards in a play must have the same rank.")
    kind = COUNT_TO_KIND[n]  # type: ignore[index]
    return Play(kind=kind, rank=cards[0].rank, count=n)

def is_legal_lead(candidate: Play) -> bool:
    """Any valid 1–4-of-a-kind is fine on lead (baseline rules)."""
    return candidate.count in (1, 2, 3, 4)

def is_legal_follow(previous: Optional[Play], candidate: Play) -> bool:
    """
    True if candidate can be played after previous:
    - If previous is None (new trick), any legal lead works.
    - Otherwise: same size and strictly higher rank.
    """
    if previous is None:
        return is_legal_lead(candidate)
    # Must match size
    if candidate.count != previous.count:
        return False
    # Must beat rank strictly
    return candidate.strength() > previous.strength()

def compare_plays(a: Play, b: Play) -> int:
    """
    Compare two plays of the SAME SIZE by rank strength.
    Returns: -1 if a<b, 0 if equal rank, +1 if a>b.
    Raises ValueError if sizes differ.
    """
    if a.count != b.count:
        raise ValueError("Cannot compare plays of different sizes.")
    va, vb = a.strength(), b.strength()
    return (va > vb) - (va < vb)

