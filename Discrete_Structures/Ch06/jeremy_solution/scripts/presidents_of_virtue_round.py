"""
Presidents of Virtue: one simulated round with 5 NPCs.

Matches the LaTeX universe description:
- Standard 52-card deck, ranks 3 < 4 < ... < A < 2.
- Shedding game like President.
- Cannot lead with 2 (Justice Burst).
- Playing 2s as a response acts as a Justice Burst: clears the table and
  the same player leads the next quest.
- Playing four-of-a-kind triggers a Bacon Revolution: rank order reverses
  for the rest of the round.
- If a player’s LAST play contains a 2, we mark them as "ended_on_bomb"
  so they would be AntiSpank next round by the story rules.

This file is the "first script": get the game running with 5 NPCs.
"""

import random
from dataclasses import dataclass, field
from typing import List, Optional, Dict

# ---------------------------------------------------------------------------
# Card model
# ---------------------------------------------------------------------------

# Normal rank order: 3 lowest, 2 highest (until a Bacon Revolution flips it)
RANKS_NORMAL = ['3', '4', '5', '6', '7', '8',
                '9', '10', 'J', 'Q', 'K', 'A', '2']
SUITS = ['♣', '♦', '♥', '♠']  # cosmetic only


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
    ended_on_bomb: bool = False  # True if their final play contained a 2

    def remove_cards(self, cards: List[Card]) -> None:
        for c in cards:
            self.hand.remove(c)


class Strategy:
    """Base class for NPC strategies."""

    def choose_play(
        self,
        player: Player,
        legal_plays: List[List[Card]],
        can_lead: bool,
        rank_order: List[str],
        revolution: bool,
    ) -> Optional[List[Card]]:
        """Return a list of Cards to play, or None to pass."""
        raise NotImplementedError


class CautiousStrategy(Strategy):
    """Plays the lowest legal set, avoids bombs (2s) if possible."""

    def choose_play(self, player, legal_plays, can_lead, rank_order, revolution):
        if not legal_plays:
            return None

        # Sort by: smaller sets first, then lower rank
        def play_key(play: List[Card]):
            ranks = [rank_index(c.rank, rank_order) for c in play]
            return (len(play), max(ranks))

        legal_plays_sorted = sorted(legal_plays, key=play_key)

        # Avoid 2s if possible
        for play in legal_plays_sorted:
            if all(c.rank != '2' for c in play):
                return play
        return legal_plays_sorted[0]


class GreedyStrategy(Strategy):
    """Plays the highest legal set to try to seize control."""

    def choose_play(self, player, legal_plays, can_lead, rank_order, revolution):
        if not legal_plays:
            return None

        def play_key(play: List[Card]):
            ranks = [rank_index(c.rank, rank_order) for c in play]
            return (len(play), max(ranks))

        return max(legal_plays, key=play_key)


class PairLoverStrategy(Strategy):
    """Prefers pairs or triples over singles when possible."""

    def choose_play(self, player, legal_plays, can_lead, rank_order, revolution):
        if not legal_plays:
            return None

        multi = [p for p in legal_plays if len(p) >= 2]
        if multi:
            # Among multi-card plays, prefer smaller size and lower rank
            def play_key(play: List[Card]):
                ranks = [rank_index(c.rank, rank_order) for c in play]
                return (len(play), max(ranks))

            return min(multi, key=play_key)

        # Fallback: lowest single
        def play_key(play: List[Card]):
            ranks = [rank_index(c.rank, rank_order) for c in play]
            return max(ranks)

        return min(legal_plays, key=play_key)


class ChaosRevolutionaryStrategy(Strategy):
    """Loves bombs and revolutions: tries to play 4-of-a-kind or 2s when possible."""

    def choose_play(self, player, legal_plays, can_lead, rank_order, revolution):
        if not legal_plays:
            return None

        bombs: List[List[Card]] = []
        for play in legal_plays:
            ranks = {c.rank for c in play}
            # Four-of-a-kind = Bacon Revolution
            if len(play) == 4 and len(ranks) == 1:
                bombs.append(play)
            # Any play containing a 2 = Justice Burst
            elif any(c.rank == '2' for c in play):
                bombs.append(play)

        if bombs:
            # Larger bombs first (prefer 4-of-a-kind over just tossing a single 2)
            def bomb_key(play: List[Card]):
                return len(play)

            return max(bombs, key=bomb_key)

        # Otherwise behave like Greedy
        def play_key(play: List[Card]):
            ranks = [rank_index(c.rank, rank_order) for c in play]
            return (len(play), max(ranks))

        return max(legal_plays, key=play_key)


class RandomStrategy(Strategy):
    """Just vibes. Picks a random legal play."""

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
    for i, card in enumerate(deck):
        players[i % n_players].hand.append(card)


def group_by_rank(cards: List[Card]) -> Dict[str, List[Card]]:
    grouped: Dict[str, List[Card]] = {}
    for c in cards:
        grouped.setdefault(c.rank, []).append(c)
    return grouped


def generate_leads(hand: List[Card], rank_order: List[str]) -> List[List[Card]]:
    """
    All legal leading plays:
    - One to four of the same rank.
    - Cannot lead with rank '2' (Justice Burst cards cannot start a quest).
    """
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
    rank_order: List[str]
) -> List[List[Card]]:
    """
    Legal responses:
    - Must match the current_size.
    - Rank must be strictly higher in the current rank order.
    """
    grouped = group_by_rank(hand)
    plays: List[List[Card]] = []
    current_idx = rank_index(current_rank, rank_order)
    for rank, cards in grouped.items():
        if len(cards) < current_size:
            continue
        if rank_index(rank, rank_order) > current_idx:
            plays.append(cards[:current_size])
    return plays


# ---------------------------------------------------------------------------
# Round engine
# ---------------------------------------------------------------------------

class PresidentsOfVirtueRound:
    """
    Simulates a single round of Presidents of Virtue with given players.

    This is *one round* in the campaign described in the LaTeX universe writeup;
    it outputs the finishing positions and whether anyone ended on a Justice Burst.
    """

    def __init__(self, players: List[Player]):
        self.players = players
        self.rank_order = list(RANKS_NORMAL)
        self.revolution = False
        self.finish_order: List[Player] = []

    def find_starting_player_index(self) -> int:
        """First-round rule: whoever has the 3 of Clubs leads."""
        for i, p in enumerate(self.players):
            for c in p.hand:
                if c.rank == '3' and c.suit == '♣':
                    return i
        # Fallback: player 0 if for some reason 3♣ is missing
        return 0

    def all_finished(self) -> bool:
        return all(p.finished for p in self.players)

    def active_players_indices(self) -> List[int]:
        return [i for i, p in enumerate(self.players) if not p.finished]

    def run(self) -> None:
        # Reset flags for safety
        for p in self.players:
            p.finished = False
            p.finish_position = None
            p.ended_on_bomb = False

        self.finish_order = []
        self.rank_order = list(RANKS_NORMAL)
        self.revolution = False

        leader_index = self.find_starting_player_index()
        next_finish_pos = 1

        while not self.all_finished():
            # New quest (trick)
            current_size: Optional[int] = None
            current_rank: Optional[str] = None
            last_player_to_play: Optional[int] = None
            passed = {i: False for i in self.active_players_indices()}

            turn_index = leader_index

            while True:
                player = self.players[turn_index]
                if player.finished:
                    # Skip finished players
                    turn_index = (turn_index + 1) % len(self.players)
                    continue

                # Determine legal plays
                if current_size is None:
                    legal_plays = generate_leads(player.hand, self.rank_order)
                    can_lead = True
                else:
                    legal_plays = generate_responses(
                        player.hand, current_size, current_rank, self.rank_order
                    )
                    can_lead = False

                # Strategy chooses a play or pass
                play = player.strategy.choose_play(
                    player, legal_plays, can_lead, self.rank_order, self.revolution
                )

                if play is None:
                    # Player passes on this quest
                    passed[turn_index] = True

                    # If everyone except last_player_to_play has passed, quest ends
                    active_idxs = self.active_players_indices()
                    if last_player_to_play is not None and all(
                        (idx == last_player_to_play)
                        or passed.get(idx, False)
                        or self.players[idx].finished
                        for idx in active_idxs
                    ):
                        leader_index = last_player_to_play
                        break

                    # Otherwise, move to next player
                    turn_index = (turn_index + 1) % len(self.players)
                    continue

                # Apply the play
                player.remove_cards(play)

                # Detect Bacon Revolution (four-of-a-kind)
                ranks = {c.rank for c in play}
                if len(play) == 4 and len(ranks) == 1:
                    # Flip the rank order
                    self.rank_order = list(reversed(self.rank_order))
                    self.revolution = not self.revolution

                # Justice Burst: any 2s played as a response (cannot lead with 2)
                is_justice_burst = any(c.rank == '2' for c in play) and not can_lead

                # Update trick state if NOT a Justice Burst
                if not is_justice_burst:
                    current_size = len(play) if current_size is None else current_size
                    current_rank = play[0].rank  # all cards same rank
                    last_player_to_play = turn_index

                # Did the player just go out?
                if not player.hand and not player.finished:
                    player.finished = True
                    player.finish_position = next_finish_pos

                    # If their last play contained a 2, mark them as ending on a bomb
                    if any(c.rank == '2' for c in play):
                        player.ended_on_bomb = True

                    self.finish_order.append(player)
                    next_finish_pos += 1

                    # If only one active player remains, we can finish the round
                    if len(self.active_players_indices()) == 1:
                        last_idx = self.active_players_indices()[0]
                        last_player = self.players[last_idx]
                        last_player.finished = True
                        last_player.finish_position = next_finish_pos
                        self.finish_order.append(last_player)
                        return

                if is_justice_burst:
                    # Quest ends immediately; this player leads the next quest
                    leader_index = turn_index
                    break

                # Otherwise, move to next player
                turn_index = (turn_index + 1) % len(self.players)


# ---------------------------------------------------------------------------
# Demo / entry point
# ---------------------------------------------------------------------------

def demo_single_round(seed: int = 0) -> None:
    random.seed(seed)

    # Five NPCs with distinct personalities
    players = [
        Player("DeathSpank (Greedy)", GreedyStrategy()),
        Player("Sparkles (Cautious)", CautiousStrategy()),
        Player("Steve (Pair Lover)", PairLoverStrategy()),
        Player("Clerk of Bacon (Chaos)", ChaosRevolutionaryStrategy()),
        Player("Random Adventurer", RandomStrategy()),
    ]

    deck = make_deck()
    deal_deck(deck, players)

    game = PresidentsOfVirtueRound(players)
    game.run()

    print("=== Presidents of Virtue – Round finished ===")
    for p in sorted(players, key=lambda pl: pl.finish_position or 99):
        bomb_note = ""
        if p.ended_on_bomb:
            bomb_note = "  (ended on Justice Burst → would be AntiSpank next round!)"
        print(f"{p.finish_position}: {p.name}{bomb_note}")


if __name__ == "__main__":
    demo_single_round()

