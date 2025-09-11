"""
bots.py
--------
Collection of blackjack bots.

Available bots:
- RandomBot: chooses hit/stay at random
- ThresholdBot: always hit below threshold, stay otherwise
- DealerBot: mimics dealer rules (hit <17, stay otherwise)
- QLearningBot (stub): placeholder for reinforcement learning bot
"""

import random
from environment import play_hand


class RandomBot:
    """A bot that chooses randomly between hit and stay."""

    def act(self, player_total, dealer_card):
        return random.choice(["hit", "stay"])


class ThresholdBot:
    """
    Always hits below a threshold, stays otherwise.
    Example: threshold=17 means hit <17, stay at 17+.
    """

    def __init__(self, threshold):
        self.threshold = threshold

    def act(self, player_total, dealer_card):
        return "hit" if player_total < self.threshold else "stay"


class DealerBot:
    """Plays like the dealer: hit <17, stay otherwise."""

    def act(self, player_total, dealer_card):
        return "hit" if player_total < 17 else "stay"


class QLearningBot:
    """
    Placeholder for Q-learning agent.
    To be implemented later.
    """

    def act(self, player_total, dealer_card):
        # TODO: implement Q-learning policy
        return random.choice(["hit", "stay"])


# ----------------------------------------------------------------------
# Quick test harness
# ----------------------------------------------------------------------

def evaluate_bot(bot, games=1000):
    """Run bot through a number of games and return win/loss/tie counts."""
    wins = losses = ties = 0
    for _ in range(games):
        result = play_hand(bot)
        if result == 1:
            wins += 1
        elif result == -1:
            losses += 1
        else:
            ties += 1
    return wins, losses, ties


if __name__ == "__main__":
    bots_to_test = [
        ("RandomBot", RandomBot()),
        ("DealerBot", DealerBot()),
    ]

    # Add ThresholdBots from 12–20
    for t in range(12, 21):
        bots_to_test.append((f"ThresholdBot({t})", ThresholdBot(t)))

    # Run evaluation
    print(f"{'Bot':<20} {'Wins':>6} {'Losses':>8} {'Ties':>6}")
    print("-" * 42)
    for name, bot in bots_to_test:
        w, l, t = evaluate_bot(bot, games=1000)
        print(f"{name:<20} {w:>6} {l:>8} {t:>6}")
