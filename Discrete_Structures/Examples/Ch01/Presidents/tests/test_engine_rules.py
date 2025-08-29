# tests/test_engine_rules.py
import pytest
from cards import Card
from engine import classify_play, is_legal_follow, Play

def test_classify_play_single_pair_triple_quad_and_invalid():
    # single
    assert classify_play([Card("5", "♣")]) == Play(size=1, rank="5")
    # pair
    assert classify_play([Card("9", "♣"), Card("9", "♦")]) == Play(size=2, rank="9")
    # triple
    assert classify_play([Card("J", "♣"), Card("J", "♦"), Card("J", "♥")]) == Play(size=3, rank="J")
    # quad
    assert classify_play([
        Card("K", "♣"), Card("K", "♦"), Card("K", "♥"), Card("K", "♠")
    ]) == Play(size=4, rank="K")
    # invalid (mixed ranks) -> raises
    with pytest.raises(ValueError):
        classify_play([Card("4", "♣"), Card("5", "♣")])

def test_is_legal_follow_basic_rules():
    prev = Play(size=1, rank="10")
    assert is_legal_follow(prev, Play(size=1, rank="J")) is True   # higher ok
    assert is_legal_follow(prev, Play(size=1, rank="9")) is False  # lower no
    assert is_legal_follow(prev, Play(size=1, rank="10")) is False # equal no
    assert is_legal_follow(prev, Play(size=2, rank="10")) is False # wrong size no
    assert is_legal_follow(None, Play(size=3, rank="4")) is True   # leading: any size

