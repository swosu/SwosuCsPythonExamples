import pytest
from cards import Card, RANK_TO_VALUE
from engine import new_round

def _find_multiset_indices(hand, min_size=2):
    """Return first indices list of a pair/triple/quad from hand, else None."""
    by_rank = {}
    for i, c in enumerate(hand):
        by_rank.setdefault(c.rank, []).append(i)
    for size in (4, 3, 2):
        if size < min_size:
            continue
        for idxs in by_rank.values():
            if len(idxs) >= size:
                return idxs[:size]
    return None

def test_cannot_pass_when_leading():
    rnd = new_round(3, seed=1)
    leader = rnd.current_player()
    # Passing on a fresh lead should be illegal
    with pytest.raises(Exception):
        rnd.pass_turn(leader)

def test_all_others_pass_clears_pile_and_last_player_leads_next():
    rnd = new_round(3, seed=2)
    p0 = rnd.current_player()
    # Lead any single (index 0 is always a single play, even if it breaks a set)
    rnd.play_cards(p0, [0])
    # Everyone else passes exactly once
    for _ in range(2):
        nxt = rnd.current_player()
        assert nxt != p0
        rnd.pass_turn(nxt)
    # Trick should clear; last player to play (p0) leads the next trick
    assert rnd.current_play is None
    assert rnd.current_player() == p0

def test_wrong_size_follow_is_rejected():
    rnd = new_round(3, seed=3)
    p0 = rnd.current_player()
    lead = _find_multiset_indices(rnd.hands[p0], min_size=2)
    if not lead:
        pytest.skip("Seed gave no pair/triple/quad to lead with; try another seed")
    rnd.play_cards(p0, lead)   # lead a pair/triple/quad
    p1 = rnd.current_player()
    # Now attempt an illegal follow (wrong size): play a single
    with pytest.raises(Exception):
        rnd.play_cards(p1, [0])

def test_follow_single_with_higher_single_updates_current_play():
    rnd = new_round(3, seed=4)
    p0 = rnd.current_player()
    lead_card = rnd.hands[p0][0]
    rnd.play_cards(p0, [0])  # lead any single
    p1 = rnd.current_player()
    # Find any strictly higher single in p1's hand
    target = RANK_TO_VALUE[lead_card.rank]
    idx = None
    for i, c in enumerate(rnd.hands[p1]):
        if RANK_TO_VALUE[c.rank] > target:
            idx = i
            break
    if idx is None:
        pytest.skip("Next player had no higher single under this seed")
    rnd.play_cards(p1, [idx])
    assert rnd.current_play.size == 1
    assert RANK_TO_VALUE[rnd.current_play.rank] > target

def test_cannot_play_out_of_turn():
    rnd = new_round(3, seed=5)
    p0 = rnd.current_player()
    p1 = (p0 + 1) % 3
    # It's p0's turn; p1 trying to play should be rejected
    with pytest.raises(Exception):
        rnd.play_cards(p1, [0])

