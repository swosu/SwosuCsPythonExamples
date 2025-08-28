# engine.py — round engine for Presidents (turns, passes, clears, finishes)
from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional, Tuple
from cards import Card, RANK_TO_VALUE, deal_hands, sort_hand

@dataclass(frozen=True)
class Play:
    """A play is N cards (1..4) of the SAME rank."""
    rank: str
    size: int

    @property
    def value(self) -> int:
        return RANK_TO_VALUE[self.rank]

def classify_play(cards: List[Card]) -> Play:
    if not cards:
        raise ValueError("Empty selection is not a play; use pass instead.")
    ranks = {c.rank for c in cards}
    if len(ranks) != 1:
        raise ValueError("All cards in a play must share the same rank.")
    size = len(cards)
    if size not in (1, 2, 3, 4):
        raise ValueError("Play size must be 1..4.")
    return Play(rank=cards[0].rank, size=size)

def is_legal_follow(prev: Optional[Play], cand: Play) -> bool:
    """Rules: leading (prev=None) = any play; otherwise size must match and rank strictly higher."""
    if prev is None:
        return True
    if cand.size != prev.size:
        return False
    return cand.value > prev.value

class RoundEngine:
    """
    Manages a single round:
      - players take turns
      - each turn: play (single/pair/triple/quad) or pass
      - after a play, others must beat with same-size higher rank or pass
      - when everyone else passes, pile clears; last player to play leads next
      - when a hand empties, that player is removed from rotation; record finishing order
    """
    def __init__(self, hands: List[List[Card]]):
        if len(hands) < 2:
            raise ValueError("Need at least 2 players.")
        # Copy and sort for readability
        self.hands: List[List[Card]] = [sort_hand(list(h)) for h in hands]
        self.active: List[int] = list(range(len(hands)))  # indices of players still in
        self.turn_idx: int = 0  # index into self.active, not absolute player id
        self.current_play: Optional[Play] = None
        self.passes_since_play: int = 0
        self.leader_index_absolute: int = self.active[self.turn_idx]
        self.last_player_who_played: Optional[int] = None
        self.finished_order: List[int] = []  # absolute player indices in finish order

    def current_player(self) -> int:
        return self.active[self.turn_idx]

    def _advance_turn(self):
        if not self.active:
            return
        self.turn_idx %= len(self.active)

    def _remove_finished(self, pid: int):
        # Remove from rotation
        idx = self.active.index(pid)
        del self.active[idx]
        # Adjust turn pointer if needed
        if idx < self.turn_idx or self.turn_idx == len(self.active):
            self.turn_idx = self.turn_idx % (len(self.active) or 1)

    def play_cards(self, player_id: int, card_indices: List[int]) -> Play:
        """Player chooses specific cards (by indices in their hand). Validates and applies play."""
        assert player_id == self.current_player(), "Not this player's turn."
        hand = self.hands[player_id]
        if any(i < 0 or i >= len(hand) for i in card_indices):
            raise IndexError("Card index out of range.")
        chosen = [hand[i] for i in card_indices]
        # Must be same rank group 1..4
        play = classify_play(chosen)
        # Must legally follow current play
        if not is_legal_follow(self.current_play, play):
            raise ValueError("Illegal play against current pile.")
        # Apply: remove chosen (by index, careful with shifting)
        for i in sorted(card_indices, reverse=True):
            del hand[i]
        # Update pile state
        self.current_play = play
        self.passes_since_play = 0
        self.last_player_who_played = player_id
        # Check finish
        if not hand:
            self.finished_order.append(player_id)
            self._remove_finished(player_id)
            # If only one left, they finish last
            if len(self.active) == 1:
                self.finished_order.append(self.active[0])
                self.active.clear()
        # Advance turn
        if self.active:
            # Find next player index relative to possibly changed rotation
            if player_id in self.active:
                self.turn_idx = (self.active.index(player_id) + 1) % len(self.active)
            else:
                # player left rotation; previous index stays pointing at the next person already
                self.turn_idx %= len(self.active)
            self._advance_turn()
        return play

    def pass_turn(self, player_id: int):
        assert player_id == self.current_player(), "Not this player's turn."
        if self.current_play is None:
            raise ValueError("Cannot pass when leading a fresh trick.")
        self.passes_since_play += 1
        # Did everyone else pass?
        # That is: number of consecutive passes equals (#active_players - 1) since the last play
        if self.passes_since_play >= max(0, len(self.active) - 1):
            # Clear pile; the last player who played leads next
            leader = self.last_player_who_played
            self.current_play = None
            self.passes_since_play = 0
            if leader is not None and leader in self.active:
                self.turn_idx = self.active.index(leader)
        else:
            # Normal advance
            self.turn_idx = (self.turn_idx + 1) % len(self.active)
        self._advance_turn()

    def is_round_over(self) -> bool:
        return len(self.active) == 0

def new_round(num_players: int, seed: int = 123) -> RoundEngine:
    import random
    rng = random.Random(seed)
    hands = deal_hands(num_players, rng=rng)
    return RoundEngine(hands)



# === Presidents CLI helpers: non-breaking vs. breaking choices =================
# These are additive utilities for the CLI. They do not alter engine behavior.
# Safe to paste into engine.py without touching existing functions.
# ------------------------------------------------------------------------------
from collections import Counter
from typing import List, Tuple, Optional

# If your project already defines a Card type, we just use its interface:
# - hashable / comparable, supports sorted(hand)
# - has .rank for equality-by-rank grouping (whatever your cards.py uses)
# No import here on purpose to avoid circulars; engine.py already imports cards.

def _count_by_rank(hand) -> Counter:
    """
    Return Counter mapping rank -> count in hand.
    Works with whatever 'rank' type your Card uses, so long as equality works.
    """
    return Counter(getattr(c, "rank") for c in hand)

def _break_label_for_count(cnt: int) -> Optional[str]:
    """
    Given total copies of a rank in hand, return the label describing
    what stronger set you'd be breaking by taking a subset.
    """
    if cnt >= 4:
        return "breaks quad"
    if cnt == 3:
        return "breaks triple"
    if cnt == 2:
        return "breaks pair"
    return None

def singles_with_break_info(hand) -> List[Tuple[object, Optional[str]]]:
    """
    Return a list of (card, break_label_or_None) for every card in hand.
    - If playing this single would reduce a pair/triple/quad at that rank,
      label it accordingly.
    - The list is sorted by your existing Card ordering (sorted(hand)).
    """
    counts = _count_by_rank(hand)
    out = []
    for c in sorted(hand):
        cnt = counts[getattr(c, "rank")]
        out.append((c, _break_label_for_count(cnt)))
    return out

def n_kind_with_break_info(hand, n: int) -> List[Tuple[List[object], Optional[str]]]:
    """
    Return all n-of-a-kind options in the hand as a list of (cards_list, label).
    - For each rank with count >= n, we produce exactly one n-card option
      (first n cards in that rank by the existing hand order).
    - If the rank has more than n copies, taking n will 'break' a higher set,
      so we label it ('breaks triple' / 'breaks quad').
    - Results are sorted by the rank order implied by your Card comparator.
    """
    if n not in (2, 3, 4):
        raise ValueError("n_kind_with_break_info supports n in {2,3,4}")

    # Group cards by rank, preserving overall sorted order for stability.
    grouped = {}
    for c in sorted(hand):
        r = getattr(c, "rank")
        grouped.setdefault(r, []).append(c)

    out = []
    # Iterate ranks in the same order as they appear in the sorted hand.
    # Using an ordered pass over unique ranks as they first occur:
    seen = set()
    ordered_ranks = []
    for c in sorted(hand):
        r = getattr(c, "rank")
        if r not in seen:
            seen.add(r)
            ordered_ranks.append(r)

    for r in ordered_ranks:
        cards = grouped[r]
        cnt = len(cards)
        if cnt >= n:
            label = _break_label_for_count(cnt) if cnt > n else None
            out.append((cards[:n], label))
    return out

def best_non_breaking_single(hand):
    """
    Convenience helper: return the first single that does NOT break a pair/triple/quad.
    Returns (card) or None if all singles would break something.
    """
    for c, label in singles_with_break_info(hand):
        if label is None:
            return c
    return None

def best_non_breaking_n_kind(hand, n: int):
    """
    Convenience helper for pairs/triples/quads: first n-kind that doesn't break a higher set.
    Returns (cards_list) or None.
    """
    for cards, label in n_kind_with_break_info(hand, n):
        if label is None:
            return cards
    return None
# ===============================================================================

