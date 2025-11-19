# scripts/test_presidents_engine.py

from presidents_engine import (
    Card,
    Player,
    Strategy,
    PresidentsOfVirtueRound,
    generate_leads,
    RANKS_NORMAL,
)


class AllInStrategy(Strategy):
    """
    Very simple test strategy:
    - If there are legal plays, always pick the largest one.
    - Otherwise PASS.
    """

    def description(self) -> str:
        return "Test strategy: always plays the largest legal set."

    def choose_play(self, player, legal_plays, can_lead, rank_order, revolution):
        if not legal_plays:
            return None
        # pick the largest play (by number of cards)
        return max(legal_plays, key=len)


def test_generate_leads_only_twos():
    """Check that a hand with only 2s can still lead something."""
    hand = [Card('2', '♣'), Card('2', '♥'), Card('2', '♦')]
    plays = generate_leads(hand)
    print("Hand:", [str(c) for c in hand])
    print("Generated leads:", [[str(c) for c in p] for p in plays])
    if not plays:
        print("❌ ERROR: No leads generated for only-2s hand!")
    else:
        print("✅ OK: Leads generated for only-2s hand.")


def test_round_all_twos():
    """
    Build a tiny 'weird' round where each player has only 2s
    and verify that the round terminates instead of looping forever.
    """
    players = [
        Player("Alice", AllInStrategy()),
        Player("Bob", AllInStrategy()),
        Player("Charlie", AllInStrategy()),
    ]

    # Give them only 2s
    players[0].hand = [Card('2', '♣')]
    players[1].hand = [Card('2', '♥'), Card('2', '♦')]
    players[2].hand = [Card('2', '♠')]

    # Run a single round
    round_game = PresidentsOfVirtueRound(players, round_index=1)
    round_game.run()

    print("\nFinish order:")
    for p in round_game.finish_order:
        print(f"  position {p.finish_position}: {p.name} (ended_on_bomb={p.ended_on_bomb})")

    if all(p.finished for p in players):
        print("✅ OK: all players finished; no infinite loop.")
    else:
        print("❌ ERROR: some players did not finish.")


if __name__ == "__main__":
    print("=== Test: generate_leads with only 2s ===")
    test_generate_leads_only_twos()

    print("\n=== Test: round with only 2s in all hands ===")
    test_round_all_twos()

