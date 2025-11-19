# scripts/pov_strategies.py
"""
Strategy implementations for Presidents of Virtue.

This module depends on:
- Card, Player from presidents_engine
"""

from __future__ import annotations

import random
from typing import List, Optional

from presidents_engine import Card, Player


def rank_index(rank: str, order: List[str]) -> int:
    """Local helper: where does this rank sit in the current rank_order?"""
    return order.index(rank)


class Strategy:
    """Base class for all strategies (NPC + human)."""

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
        raise NotImplementedError


# ---------------------------------------------------------------------------
# Existing bots
# ---------------------------------------------------------------------------

class CautiousStrategy(Strategy):
    """Lowest legal play, avoids 2s if possible."""

    def description(self) -> str:
        return ("Cautious: usually plays the smallest legal set and "
                "tries NOT to spend 2s (Justice Bursts) unless forced.")

    def choose_play(self, player, legal_plays, can_lead, rank_order, revolution):
        if not legal_plays:
            return None

        def play_key(play: List[Card]):
            ranks = [rank_index(c.rank, rank_order) for c in play]
            return (len(play), max(ranks))

        legal_sorted = sorted(legal_plays, key=play_key)
        # Avoid any play containing a 2 if possible
        for play in legal_sorted:
            if all(c.rank != '2' for c in play):
                return play
        return legal_sorted[0]


class GreedyStrategy(Strategy):
    """Highest legal play."""

    def description(self) -> str:
        return ("Greedy: tries to play the biggest, highest-ranked legal set "
                "to seize control of the table.")

    def choose_play(self, player, legal_plays, can_lead, rank_order, revolution):
        if not legal_plays:
            return None

        def play_key(play: List[Card]):
            ranks = [rank_index(c.rank, rank_order) for c in play]
            return (len(play), max(ranks))

        return max(legal_plays, key=play_key)


class PairLoverStrategy(Strategy):
    """Prefers multi-card plays (pairs, triples, quads) over singles."""

    def description(self) -> str:
        return ("PairLover: prefers to play pairs/triples/quads when possible, "
                "even if singles could also be played.")

    def choose_play(self, player, legal_plays, can_lead, rank_order, revolution):
        if not legal_plays:
            return None

        multi = [p for p in legal_plays if len(p) >= 2]
        if multi:
            def play_key(play: List[Card]):
                ranks = [rank_index(c.rank, rank_order) for c in play]
                return (len(play), max(ranks))
            # Smaller multi-sets, lower rank first
            return min(multi, key=play_key)

        # Fallback: lowest single
        def single_key(play: List[Card]):
            ranks = [rank_index(c.rank, rank_order) for c in play]
            return max(ranks)

        return min(legal_plays, key=single_key)


class ChaosRevolutionaryStrategy(Strategy):
    """Loves bombs and revolutions: tries to play 4-of-a-kind or 2s."""

    def description(self) -> str:
        return ("ChaosRevolutionary: actively looks for Bacon Revolutions "
                "(four-of-a-kind) and Justice Bursts (2s) to flip the table.")

    def choose_play(self, player, legal_plays, can_lead, rank_order, revolution):
        if not legal_plays:
            return None

        bombs: List[List[Card]] = []
        for play in legal_plays:
            ranks = {c.rank for c in play}
            if len(play) == 4 and len(ranks) == 1:
                bombs.append(play)  # Bacon Revolution
            elif any(c.rank == '2' for c in play):
                bombs.append(play)  # Justice Burst

        if bombs:
            # Prefer bigger bombs (quads over just throwing a single 2)
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

    def description(self) -> str:
        return ("Random: chooses uniformly among all legal plays. "
                "Pure chaos, no deeper plan.")

    def choose_play(self, player, legal_plays, can_lead, rank_order, revolution):
        if not legal_plays:
            return None
        return random.choice(legal_plays)


# ---------------------------------------------------------------------------
# New: smarter bot
# ---------------------------------------------------------------------------

class SmartGreedyStrategy(Strategy):
    """
    Smarter version of Greedy:
    - Tries to win with the *smallest* winning play (conservative).
    - Avoids using 2s and four-of-a-kind bombs early.
    - Only spends bombs when the hand is getting short.
    """

    def description(self) -> str:
        return ("SmartGreedy: wins with the smallest play that works, "
                "saves 2s and bombs for emergencies or endgame.")

    def choose_play(
        self,
        player: Player,
        legal_plays: List[List[Card]],
        can_lead: bool,
        rank_order: List[str],
        revolution: bool,
    ) -> Optional[List[Card]]:
        if not legal_plays:
            return None

        hand_size = len(player.hand)

        def uses_bomb(play: List[Card]) -> bool:
            ranks = {c.rank for c in play}
            if any(c.rank == '2' for c in play):
                return True
            if len(play) == 4 and len(ranks) == 1:
                return True
            return False

        if can_lead:
            non_bomb_multis = [
                p for p in legal_plays if len(p) >= 2 and not uses_bomb(p)
            ]
            if non_bomb_multis:
                def key_nb(p: List[Card]):
                    ranks = [rank_index(c.rank, rank_order) for c in p]
                    return (len(p), max(ranks))
                return min(non_bomb_multis, key=key_nb)

            non_bomb_singles = [
                p for p in legal_plays if len(p) == 1 and not uses_bomb(p)
            ]
            if non_bomb_singles:
                def key_s(p: List[Card]):
                    ranks = [rank_index(c.rank, rank_order) for c in p]
                    return max(ranks)
                return min(non_bomb_singles, key=key_s)

            bomb_plays = [p for p in legal_plays if uses_bomb(p)]
            if hand_size > 5:
                return None  # save bombs for later

            def key_b(p: List[Card]):
                return len(p)
            return min(bomb_plays, key=key_b)

        # responding (not leading)
        non_bomb_responses = [p for p in legal_plays if not uses_bomb(p)]
        if non_bomb_responses:
            def key_resp(p: List[Card]):
                ranks = [rank_index(c.rank, rank_order) for c in p]
                return (len(p), max(ranks))
            return min(non_bomb_responses, key=key_resp)

        bomb_responses = [p for p in legal_plays if uses_bomb(p)]
        if bomb_responses and hand_size <= 4:
            def key_b2(p: List[Card]):
                return len(p)
            return min(bomb_responses, key=key_b2)

        return None


# ---------------------------------------------------------------------------
# New: human-controlled player
# ---------------------------------------------------------------------------

class HumanStrategy(Strategy):
    """Interactive human-controlled player via stdin."""

    def description(self) -> str:
        return ("Human: asks you which legal play to make each turn, "
                "or lets you pass even when a play exists.")

    def short_label(self) -> str:
        return "Human"

    def choose_play(
        self,
        player: Player,
        legal_plays: List[List[Card]],
        can_lead: bool,
        rank_order: List[str],
        revolution: bool,
    ) -> Optional[List[Card]]:
        if not legal_plays:
            input(f"\n[{player.name}] No legal play, press <Enter> to PASS...")
            return None

        print("\n" + "=" * 70)
        print(f"[{player.name}] – Your turn "
              f"({'LEAD' if can_lead else 'RESPOND'})")
        print(f"Strategy: {self.short_label()} (Human-controlled)")
        print(f"Revolution active? {'YES' if revolution else 'no'}")

        sorted_hand = sorted(
            player.hand,
            key=lambda c: rank_index(c.rank, rank_order)
        )
        hand_str = " ".join(str(c) for c in sorted_hand)
        print(f"Your hand: {hand_str}")

        print("\nLegal options:")
        print("  0: PASS (even though you *could* play)")
        for i, play in enumerate(legal_plays, start=1):
            play_str = " ".join(str(c) for c in play)
            size = len(play)
            if size == 1:
                kind = "single"
            elif size == 2:
                kind = "pair"
            elif size == 3:
                kind = "triple"
            elif size == 4:
                kind = "quad"
            else:
                kind = f"{size}-set"
            print(f"  {i}: {play_str:<15s}  ({kind})")

        while True:
            choice_str = input("Choose an option number (0 to pass): ").strip()
            try:
                choice = int(choice_str)
            except ValueError:
                print("Please type an integer like 0, 1, 2, ...")
                continue

            if choice == 0:
                print(f"[{player.name}] chooses to PASS.")
                return None
            if 1 <= choice <= len(legal_plays):
                chosen_play = legal_plays[choice - 1]
                play_str = " ".join(str(c) for c in chosen_play)
                print(f"[{player.name}] chooses to play: {play_str}")
                return chosen_play

            print(f"{choice} is not a valid option. Try again.")

