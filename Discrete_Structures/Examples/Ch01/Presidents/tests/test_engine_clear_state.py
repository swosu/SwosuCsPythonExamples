from engine import new_round
from cards import Card

def test_clear_resets_follow_constraints():
    rnd = new_round(3, seed=13)
    leader = rnd.current_player()
    # Lead a single
    rnd.play_cards(leader, [0])
    # Everyone else passes -> clear
    for _ in range(2):
        rnd.pass_turn(rnd.current_player())
    assert rnd.current_play is None
    assert rnd.current_player() == leader
    # Now leader may legally play a pair if they have it (wasn't legal on the follow)
    hand = rnd.hands[leader]
    by_rank = {}
    for i,c in enumerate(hand):
        by_rank.setdefault(c.rank, []).append(i)
    pair = next((idxs[:2] for idxs in by_rank.values() if len(idxs) >= 2), None)
    if pair:
        # Should not raise
        rnd.play_cards(leader, pair)

