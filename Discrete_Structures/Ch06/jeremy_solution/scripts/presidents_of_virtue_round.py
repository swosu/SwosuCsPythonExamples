"""
Presidents of Virtue – multi-round simulator with detailed logging.

Features:
- 5 NPC players with different strategies.
- Prints:
  - starting hands,
  - trick-by-trick table state,
  - plays and passes.
- Writes a CSV file with one row per action:
  presidents_of_virtue_plays.csv

Columns include:
- round, trick, step
- player_name, strategy
- action ("play" or "pass")
- cards_played
- hand_size_before, hand_size_after
- current_size_before, current_rank_before
- is_lead, is_justice_burst, is_revolution_trigger, revolution_state_after
- finish_position, ended_on_bomb
"""

import csv
import os
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
# Player + Strategies
# ---------------------------------------------------------------------------

@dataclass
class Player:
    name: str
    strategy: "Strategy"
    hand: List[Card] = field(default_factory=list)
    finished: bool = False
    finish_position: Optional[int] = None
    ended_on_bomb: bool = False  # True if final play contained a 2

    def remove_cards(self, cards: List[Card]) -> None:
        for c in cards:
            self.hand.remove(c)


class Strategy:
    def choose_play(
        self,
        player: Player,
        legal_plays: List[List[Card]],
        can_lead: bool,
        rank_order: List[str],
        revolution: bool,
    ) -> Optional[List[Card]]:
        raise NotImplementedError


class CautiousStrategy(Strategy):
    """Lowest legal play, avoids 2s if possible."""

    def choose_play(self, player, legal_plays, can_lead, rank_order, revolution):
        if not legal_plays:
            return None

        def play_key(play: List[Card]):
            ranks = [rank_index(c.rank, rank_order) for c in play]
            return (len(play), max(ranks))

        legal_sorted = sorted(legal_plays, key=play_key)
        for play in legal_sorted:
            if all(c.rank != '2' for c in play):
                return play
        return legal_sorted[0]


class GreedyStrategy(Strategy):
    """Highest legal play."""

    def choose_play(self, player, legal_plays, can_lead, rank_order, revolution):
        if not legal_plays:
            return None

        def play_key(play: List[Card]):
            ranks = [rank_index(c.rank, rank_order) for c in play]
            return (len(play), max(ranks))

        return max(legal_plays, key=play_key)


class PairLoverStrategy(Strategy):
    """Prefers multi-card plays (pairs, triples, quads) over singles."""

    def choose_play(self, player, legal_plays, can_lead, rank_order, revolution):
        if not legal_plays:
            return None

        multi = [p for p in legal_plays if len(p) >= 2]
        if multi:
            def play_key(play: List[Card]):
                ranks = [rank_index(c.rank, rank_order) for c in play]
                return (len(play), max(ranks))

            return min(multi, key=play_key)

        # Fallback: lowest single
        def single_key(play: List[Card]):
            ranks = [rank_index(c.rank, rank_order) for c in play]
            return max(ranks)

        return min(legal_plays, key=single_key)


class ChaosRevolutionaryStrategy(Strategy):
    """Loves bombs and revolutions: tries to play 4-of-a-kind or 2s."""

    def choose_play(self, player, legal_plays, can_lead, rank_order, revolution):
        if not legal_plays:
            return None

        bombs: List[List[Card]] = []
        for play in legal_plays:
            ranks = {c.rank for c in play}
            # Four-of-a-kind
            if len(play) == 4 and len(ranks) == 1:
                bombs.append(play)
            elif any(c.rank == '2' for c in play):
                bombs.append(play)

        if bombs:
            def bomb_key(play: List[Card]):
                return len(play)

            return max(bombs, key=bomb_key)

        # Otherwise greedy
        def play_key(play: List[Card]):
            ranks = [rank_index(c.rank, rank_order) for c in play]
            return (len(play), max(ranks))

        return max(legal_plays, key=play_key)


class RandomStrategy(Strategy):
    """Picks any legal play at random."""

    def choose_play(self, player, legal_plays, can_lead, rank_order, revolution):
        if not legal_plays:
            return None
        return random.choice(legal_plays)


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
    grouped = group_by_rank(hand)
    plays: List[List[Card]] = []
    for rank, cards in grouped.items():
        if rank == '2':
            continue  # no leading with 2s
        for size in range(1, min(4, len(cards)) + 1):
            plays.append(cards[:size])
    return plays


def generate_responses(
    hand: List[Card],
    current_size: int,
    current_rank: str,
    rank_order: List[str],
) -> List[List[Card]]:
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
    return " ".join(str(c) for c in sorted(hand, key=lambda c: rank_index(c.rank, rank_order)))


# ---------------------------------------------------------------------------
# Round engine (with logging)
# ---------------------------------------------------------------------------

class PresidentsOfVirtueRound:
    def __init__(self, players: List[Player], round_index: int):
        self.players = players
        self.round_index = round_index
        self.rank_order = list(RANKS_NORMAL)
        self.revolution = False
        self.finish_order: List[Player] = []
        # play_log: one dict per action
        self.play_log: List[Dict[str, object]] = []

    def find_starting_player_index(self) -> int:
        for i, p in enumerate(self.players):
            for c in p.hand:
                if c.rank == '3' and c.suit == '♣':
                    return i
        return 0

    def all_finished(self) -> bool:
        return all(p.finished for p in self.players)

    def active_players_indices(self) -> List[int]:
        return [i for i, p in enumerate(self.players) if not p.finished]

    def run(self) -> None:
        for p in self.players:
            p.finished = False
            p.finish_position = None
            p.ended_on_bomb = False

        self.finish_order = []
        self.play_log.clear()
        self.rank_order = list(RANKS_NORMAL)
        self.revolution = False

        # Show starting hands
        print(f"\n=== ROUND {self.round_index} – Starting hands ===")
        for p in self.players:
            print(f"{p.name:18s} ({p.strategy.__class__.__name__}): "
                  f"{hand_to_str(p.hand, self.rank_order)}")

        leader_index = self.find_starting_player_index()
        next_finish_pos = 1
        trick_id = 0

        while not self.all_finished():
            trick_id += 1
            print(f"\n--- Round {self.round_index}, Trick {trick_id} "
                  f"(leader: {self.players[leader_index].name}) ---")

            current_size: Optional[int] = None
            current_rank: Optional[str] = None
            last_player_to_play: Optional[int] = None
            passed = {i: False for i in self.active_players_indices()}
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
                    print(f"{player.name:18s} passes. "
                          f"(hand: {hand_to_str(player.hand, self.rank_order)})")

                    self.play_log.append({
                        "round": self.round_index,
                        "trick": trick_id,
                        "step": step_in_trick,
                        "player_name": player.name,
                        "strategy": player.strategy.__class__.__name__,
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
                        "finish_position": None,        # filled after round
                        "ended_on_bomb": None,          # filled after round
                    })

                    active_idxs = self.active_players_indices()
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
                print(f"{player.name:18s} plays: {play_str:<12s} "
                      f" | table: {table_str}")

                self.play_log.append({
                    "round": self.round_index,
                    "trick": trick_id,
                    "step": step_in_trick,
                    "player_name": player.name,
                    "strategy": player.strategy.__class__.__name__,
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
                    "finish_position": None,        # filled after round
                    "ended_on_bomb": None,          # filled after round
                })

                # Did the player just go out?
                if not player.hand and not player.finished:
                    player.finished = True
                    player.finish_position = next_finish_pos
                    if any(c.rank == '2' for c in play):
                        player.ended_on_bomb = True
                    print(f"--> {player.name} is OUT and takes position "
                          f"{next_finish_pos} "
                          f"{'(ended on 2)' if player.ended_on_bomb else ''}")
                    self.finish_order.append(player)
                    next_finish_pos += 1

                    if len(self.active_players_indices()) == 1:
                        last_idx = self.active_players_indices()[0]
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


# ---------------------------------------------------------------------------
# Game driver + CSV export
# ---------------------------------------------------------------------------

def create_oklahoma_players() -> List[Player]:
    # Just a fun list of names that "feel" western Oklahoma-ish
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


def write_play_log_csv(play_logs: List[Dict[str, object]], filename: str) -> None:
    if not play_logs:
        return

    fieldnames = [
        "round", "trick", "step",
        "player_name", "strategy",
        "action", "cards_played",
        "hand_size_before", "hand_size_after",
        "current_size_before", "current_rank_before",
        "is_lead", "is_justice_burst", "is_revolution_trigger",
        "revolution_state_after",
        "finish_position", "ended_on_bomb",
    ]

    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in play_logs:
            writer.writerow(row)


def simulate_game(num_rounds: int = 3, seed: int = 0) -> None:
    random.seed(seed)
    players = create_oklahoma_players()

    print("Players and strategies:")
    for p in players:
        print(f"  {p.name:18s} -> {p.strategy.__class__.__name__}")
    print()

    all_play_logs: List[Dict[str, object]] = []

    for r in range(1, num_rounds + 1):
        deck = make_deck()
        deal_deck(deck, players)
        round_game = PresidentsOfVirtueRound(players, round_index=r)
        round_game.run()

        # Fill in finish info for that round's logs
        finish_map = {
            p.name: (p.finish_position, p.ended_on_bomb)
            for p in players
        }

        for entry in round_game.play_log:
            name = entry["player_name"]
            fp, bomb = finish_map.get(name, (None, None))
            entry["finish_position"] = fp
            entry["ended_on_bomb"] = bomb
            all_play_logs.append(entry)

        print("\nRound", r, "results:")
        for p in sorted(players, key=lambda pl: pl.finish_position or 99):
            bomb_note = " (ended on bomb)" if p.ended_on_bomb else ""
            print(f"  {p.finish_position}: {p.name}{bomb_note}")
        print("-" * 60)

    csv_name = "presidents_of_virtue_plays.csv"
    write_play_log_csv(all_play_logs, csv_name)
    print(f"\nWrote detailed play log to {csv_name}")


if __name__ == "__main__":
    # Adjust num_rounds as you like
    simulate_game(num_rounds=3, seed=42)
