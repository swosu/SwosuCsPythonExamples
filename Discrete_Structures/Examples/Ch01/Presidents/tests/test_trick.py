# Presidents/tests/test_trick.py
import pytest
from cards import Card
from trick import make_play, is_legal_follow, compare_plays, is_legal_lead

def test_make_play_valid_sizes_and_same_rank():
    p1 = make_play([Card("7","♣")])
    assert p1.kind == "single" and p1.rank == "7" and p1.count == 1

    p2 = make_play([Card("Q","♣"), Card("Q","♦")])
    assert p2.kind == "pair" and p2.rank == "Q" and p2.count == 2

    p3 = make_play([Card("9","♣"), Card("9","♦"), Card("9","♥")])
    assert p3.kind == "triple" and p3.rank == "9" and p3.count == 3

    p4 = make_play([Card("A","♣"), Card("A","♦"), Card("A","♥"), Card("A","♠")])
    assert p4.kind == "quad" and p4.rank == "A" and p4.count == 4

def test_make_play_rejects_mixed_ranks_and_bad_sizes():
    with pytest.raises(ValueError):
        make_play([])  # 0 cards
    with pytest.raises(ValueError):
        make_play([Card("5","♣"), Card("6","♣")])  # mixed ranks
    with pytest.raises(ValueError):
        make_play([Card("K","♣")] * 5)  # >4 not allowed (no bombs yet)

def test_is_legal_lead_allows_any_valid_play():
    assert is_legal_lead(make_play([Card("3","♣")]))
    assert is_legal_lead(make_play([Card("7","♣"), Card("7","♦")]))
    assert is_legal_lead(make_play([Card("Q","♣"), Card("Q","♦"), Card("Q","♥")]))
    assert is_legal_lead(make_play([Card("A","♣"), Card("A","♦"), Card("A","♥"), Card("A","♠")]))

def test_is_legal_follow_requires_same_size_and_higher_rank():
    prev = make_play([Card("7","♣")])  # single 7
    assert is_legal_follow(prev, make_play([Card("8","♦")]))  # higher single ok
    assert not is_legal_follow(prev, make_play([Card("7","♦")]))  # equal rank not ok
    assert not is_legal_follow(prev, make_play([Card("9","♦"), Card("9","♣")]))  # size mismatch

    prev_pair = make_play([Card("10","♣"), Card("10","♦")])
    assert is_legal_follow(prev_pair, make_play([Card("J","♣"), Card("J","♦")]))
    assert not is_legal_follow(prev_pair, make_play([Card("J","♣")]))   # single cannot beat pair
    assert not is_legal_follow(prev_pair, make_play([Card("10","♥"), Card("10","♠")]))  # equal pair not ok

def test_compare_plays_only_same_size():
    a = make_play([Card("Q","♣")])
    b = make_play([Card("K","♣")])
    assert compare_plays(a, b) == -1
    assert compare_plays(b, a) == 1
    assert compare_plays(a, make_play([Card("Q","♦")])) == 0

    with pytest.raises(ValueError):
        compare_plays(make_play([Card("9","♣")]),
                      make_play([Card("9","♣"), Card("9","♦")]))

