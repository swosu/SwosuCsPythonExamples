import pytest
from cards import Card
from engine import classify_play, new_round

def test_classify_play_empty_raises():
    with pytest.raises(ValueError):
        classify_play([])

def test_play_cards_mixed_ranks_rejected():
    rnd = new_round(3, seed=11)
    p0 = rnd.current_player()
    # try to play two different ranks -> engine should reject
    # build indices [i,j] with distinct ranks
    hand = rnd.hands[p0]
    i, j = None, None
    for a in range(len(hand)):
        for b in range(a+1, len(hand)):
            if hand[a].rank != hand[b].rank:
                i, j = a, b
                break
        if i is not None:
            break
    assert i is not None, "seed unlucky, try another"
    with pytest.raises(Exception):
        rnd.play_cards(p0, [i, j])

def test_pass_turn_not_your_turn_rejected():
    rnd = new_round(3, seed=12)
    p0 = rnd.current_player()
    p1 = (p0 + 1) % 3
    with pytest.raises(Exception):
        rnd.pass_turn(p1)  # cannot pass when it's not your turn

