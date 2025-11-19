# scripts/presidents_engine.py
"""
Core engine for the 'Presidents of Virtue' card game.

Contains:
- Card + deck utilities
- Strategy base class (concrete strategies live in pov_strategies.py)
- Player dataclass
- Round engine (PresidentsOfVirtueRound) that:
  * prints table state
  * logs all actions into a play_log list of dicts
"""

import random
from dataclasses import dataclass, field
from typing import List, Optional, Dict

# ---------------------------------------------------------------------------
# Card model
# ---------------------------------------------------------------------------

RANKS_NORMAL = ['3', '4', '5', '6', '7', '8',
                '9', '10', 'J', 'Q', 'K', 'A', '2']
SUITS = ['♣', '♦', '♥', '♠']


def rank_index(rank: str, order: List[str]) -> int:
    return order.index(rank)


@dataclass(frozen=True)
class Card:
    rank: str
    suit: str

    def __str__(self) -> str:
        return f"{self.rank}{self.suit}"


# ---------------------------------------------------------------------------
# Player + Strategy base
# ---------------------------------------------------------------------------

@dataclass
class Player:
    name: str
    strategy: "Strategy"   # concrete strategies come from pov_strategies
    hand: List[Card] = field(default_factory=list)
    finished: bool = False
    finish_position: Optional[int] = None
    ended_on_bomb: bool = False  # True if final play contained a 2

    def remove_cards(self, cards: List[Card]) -> None:
        for c in cards:
            self.hand.remove(c)


class Strategy:
    """Base class that all strategies (NPC + human) should subclass."""

    def description(self) -> str:
        """One-line explanation for humans."""
        return "Mysterious strategy. (Probably chaos.)"

    def short_label(self) -> str:
        """Short tag to show in logs."""
        return self.__class__.__name__.replace("Strategy", "")

    def choose_play(
        self,
        player: Player,
        legal_plays: List[List[Card]],
        can_lead: bool,
        rank_order: List[str],
        revolution: bool,
    ) -> Optional[List[Card]]:
        """
        Must be implemented by subclasses.

        Returns:
            - a list of Card objects to play, OR
            - None to indicate PASS.
        """
        raise NotImplementedError


# ---------------------------------------------------------------------------
# Helper functions: deck + move generation
# ---------------------------------------------------------------------------

def make_deck() -> List[Card]:
    return [Card(rank, suit) for rank in RANKS_NORMAL for suit in SUITS]


def deal_deck(deck: List[Card], players: List[Player]) -> None:
    random.shuffle(deck)
    n_players = len(players)
    for p in players:
        p.hand.clear()
    for i, card in enumerate(deck):
        players[i % n_players].hand.append(card)


def group_by_rank(cards: List[Card]) -> Dict[str, List[Card]]:
    grouped: Dict[str, List[Card]] = {}
    for c in cards:
        grouped.setdefault(c.rank, []).append(c)
    return grouped


def generate_leads(hand: List[Card]) -> List[List[Card]]:
    """
    Generate all legal leading plays from a given hand.

    Normal rule:
      - You cannot lead with 2s.

    Exception:
      - If your hand consists ONLY of 2s, you ARE allowed to lead with them,
        otherwise the game can get stuck in an infinite "everyone passes with 2s" loop.
    """
    grouped = group_by_rank(hand)
    plays: List[List[Card]] = []

    # Do we have any non-2 ranks?
    non_two_ranks = [rank for rank in grouped.keys() if rank != '2']

    if non_two_ranks:
        ranks_to_consider = non_two_ranks
    else:
        # Hand is ONLY 2s -> allow leading with 2s
        ranks_to_consider = ['2']

    for rank in ranks_to_consider:
        cards = grouped[rank]
        for size in range(1, min(4, len(cards)) + 1):
            plays.append(cards[:size])

    return plays


def generate_responses(
    hand: List[Card],
    current_size: int,
    current_rank: str,
    rank_order: List[str],
) -> List[List[Card]]:
    """Generate all responses that beat the current table play."""
    grouped = group_by_rank(hand)
    plays: List[List[Card]] = []
    current_idx = rank_index(current_rank, rank_order)
    for rank, cards in grouped.items():
        if len(cards) < current_size:
            continue
        if rank_index(rank, rank_order) > current_idx:
            plays.append(cards[:current_size])
    return plays


def hand_to_str(hand: List[Card], rank_order: List[str]) -> str:
    return " ".join(
        str(c)
        for c in sorted(hand, key=lambda c: rank_index(c.rank, rank_order))
    )


# ---------------------------------------------------------------------------
# Round engine (with in-memory logging)
# ---------------------------------------------------------------------------

class PresidentsOfVirtueRound:
    """
    Simulates a single round of Presidents of Virtue.

    Public attributes after run():
    - finish_order (list of Players by finishing position)
    - play_log (list of dicts; each dict describes one action)
    - rank_order, revolution (final state)
    """

    def __init__(self, players: List[Player], round_index: int):
        self.players = players
        self.round_index = round_index
        self.rank_order = list(RANKS_NORMAL)
        self.revolution = False
        self.finish_order: List[Player] = []
        self.play_log: List[Dict[str, object]] = []

    # -------------------- internal helpers --------------------

    def _find_starting_player_index(self) -> int:
        for i, p in enumerate(self.players):
            for c in p.hand:
                if c.rank == '3' and c.suit == '♣':
                    return i
        return 0

    def _all_finished(self) -> bool:
        return all(p.finished for p in self.players)

    def _active_players_indices(self) -> List[int]:
        return [i for i, p in enumerate(self.players) if not p.finished]

    # -------------------- main round loop ---------------------

    def run(self) -> None:
        # Reset per-round state
        for p in self.players:
            p.finished = False
            p.finish_position = None
            p.ended_on_bomb = False

        self.finish_order = []
        self.play_log.clear()
        self.rank_order = list(RANKS_NORMAL)
        self.revolution = False

        # Print strategy blurbs once at the top of the round
        print(f"\n=== ROUND {self.round_index} – Strategy overview ===")
        for p in self.players:
            print(f"{p.name:18s} [{p.strategy.short_label():12s}] "
                  f"- {p.strategy.description()}")

        # Show starting hands
        print(f"\n=== ROUND {self.round_index} – Starting hands ===")
        for p in self.players:
            print(f"{p.name:18s}: {hand_to_str(p.hand, self.rank_order)}")

        leader_index = self._find_starting_player_index()
        next_finish_pos = 1
        trick_id = 0

        while not self._all_finished():
            trick_id += 1
            print(f"\n--- Round {self.round_index}, Trick {trick_id} "
                  f"(leader: {self.players[leader_index].name}) ---")

            current_size: Optional[int] = None
            current_rank: Optional[str] = None
            last_player_to_play: Optional[int] = None
            passed = {i: False for i in self._active_players_indices()}
            pile_cards: List[Card] = []
            step_in_trick = 0

            turn_index = leader_index

            while True:
                player = self.players[turn_index]
                if player.finished:
                    turn_index = (turn_index + 1) % len(self.players)
                    continue

                step_in_trick += 1
                hand_before = list(player.hand)

                if current_size is None:
                    legal_plays = generate_leads(player.hand)
                    can_lead = True
                else:
                    legal_plays = generate_responses(
                        player.hand, current_size, current_rank, self.rank_order
                    )
                    can_lead = False

                play = player.strategy.choose_play(
                    player, legal_plays, can_lead, self.rank_order, self.revolution
                )

                current_size_before = current_size if current_size is not None else 0
                current_rank_before = current_rank if current_rank is not None else ""

                if play is None:
                    # PASS
                    passed[turn_index] = True
                    print(f"{player.name:18s} [{player.strategy.short_label():12s}] "
                          f"passes. (hand: {hand_to_str(player.hand, self.rank_order)})")

                    self.play_log.append({
                        "round": self.round_index,
                        "trick": trick_id,
                        "step": step_in_trick,
                        "player_name": player.name,
                        "strategy": player.strategy.short_label(),
                        "action": "pass",
                        "cards_played": "",
                        "hand_size_before": len(hand_before),
                        "hand_size_after": len(player.hand),
                        "current_size_before": current_size_before,
                        "current_rank_before": current_rank_before,
                        "is_lead": can_lead,
                        "is_justice_burst": False,
                        "is_revolution_trigger": False,
                        "revolution_state_after": self.revolution,
                        "finish_position": None,
                        "ended_on_bomb": None,
                    })

                    active_idxs = self._active_players_indices()
                    if last_player_to_play is not None and all(
                        (idx == last_player_to_play)
                        or passed.get(idx, False)
                        or self.players[idx].finished
                        for idx in active_idxs
                    ):
                        leader_index = last_player_to_play
                        break

                    turn_index = (turn_index + 1) % len(self.players)
                    continue

                # PLAY
                player.remove_cards(play)
                pile_cards.extend(play)

                is_revolution_trigger = False
                ranks_set = {c.rank for c in play}
                if len(play) == 4 and len(ranks_set) == 1:
                    # Bacon Revolution
                    self.rank_order = list(reversed(self.rank_order))
                    self.revolution = not self.revolution
                    is_revolution_trigger = True
                    print(f"*** BACON REVOLUTION triggered by {player.name}! "
                          f"Rank order reversed. ***")

                is_justice_burst = any(c.rank == '2' for c in play) and not can_lead

                if not is_justice_burst:
                    current_size = len(play) if current_size is None else current_size
                    current_rank = play[0].rank
                    last_player_to_play = turn_index

                table_str = " ".join(str(c) for c in pile_cards)
                play_str = " ".join(str(c) for c in play)
                lead_tag = " (lead)" if can_lead else ""
                extra_note = ""
                if is_justice_burst:
                    extra_note = " [Justice Burst: clears table]"
                elif is_revolution_trigger:
                    extra_note = " [Bacon Revolution: rank order flipped]"

                print(f"{player.name:18s} [{player.strategy.short_label():12s}] "
                      f"plays: {play_str:<12s}{lead_tag} | table: {table_str}{extra_note}")

                self.play_log.append({
                    "round": self.round_index,
                    "trick": trick_id,
                    "step": step_in_trick,
                    "player_name": player.name,
                    "strategy": player.strategy.short_label(),
                    "action": "play",
                    "cards_played": play_str,
                    "hand_size_before": len(hand_before),
                    "hand_size_after": len(player.hand),
                    "current_size_before": current_size_before,
                    "current_rank_before": current_rank_before,
                    "is_lead": can_lead,
                    "is_justice_burst": is_justice_burst,
                    "is_revolution_trigger": is_revolution_trigger,
                    "revolution_state_after": self.revolution,
                    "finish_position": None,
                    "ended_on_bomb": None,
                })

                # Did the player just go out?
                if not player.hand and not player.finished:
                    player.finished = True
                    player.finish_position = next_finish_pos
                    if any(c.rank == '2' for c in play):
                        player.ended_on_bomb = True
                    bomb_note = " (ended on a 2: bomb!)" if player.ended_on_bomb else ""
                    print(f"--> {player.name} is OUT and takes position "
                          f"{next_finish_pos}{bomb_note}")
                    self.finish_order.append(player)
                    next_finish_pos += 1

                    if len(self._active_players_indices()) == 1:
                        last_idx = self._active_players_indices()[0]
                        last_player = self.players[last_idx]
                        last_player.finished = True
                        last_player.finish_position = next_finish_pos
                        print(f"--> {last_player.name} is last and takes position "
                              f"{next_finish_pos}.")
                        self.finish_order.append(last_player)
                        return

                if is_justice_burst:
                    print(f"*** JUSTICE BURST by {player.name}! "
                          f"Table cleared; {player.name} leads next trick. ***")
                    leader_index = turn_index
                    break

                turn_index = (turn_index + 1) % len(self.players)

