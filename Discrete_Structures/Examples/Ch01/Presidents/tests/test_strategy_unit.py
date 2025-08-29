# tests/test_strategy_unit.py
import pytest
from cards import Card
from engine import Play
from strategy import generate_options, best_move, ranks_strictly_higher_than

def ranks_of_options(hand, opts):
    """Helper: return set of ranks for any list of index-lists."""
    r = set()
    for idxs in opts:
        r.add(hand[idxs[0]].rank)
    return r

def test_ranks_strictly_higher_than():
    # sanity checks at extremes
    assert "4" in ranks_strictly_higher_than("3")
    assert "2" not in ranks_strictly_higher_than("2")  # nothing beats 2

def test_generate_options_leading_prefers_true_singletons_only():
    hand = [
        Card("3", "♣"),            # singleton
        Card("5", "♣"), Card("5", "♦"),  # pair
        Card("9", "♣"), Card("9", "♦"), Card("9", "♥"),  # triple
    ]
    plays = generate_options(hand, None)
    # singles: only the true singleton 3
    assert 1 in plays
    assert len(plays[1]) == 1
    assert hand[plays[1][0][0]].rank == "3"
    # pairs and triples listed
    assert 2 in plays and 3 in plays
    assert hand[plays[2][0][0]].rank == "5"
    assert hand[plays[3][0][0]].rank == "9"

def test_generate_options_follow_single_lists_higher_singles_even_if_breaks():
    hand = [
        Card("8", "♣"),
        Card("9", "♣"), Card("9", "♦"),  # would break a pair, but allowed when following single
        Card("J", "♣"),
    ]
    cur = Play(size=1, rank="7")
    plays = generate_options(hand, cur)
    assert 1 in plays
    ranks = ranks_of_options(hand, plays[1])
    # only strictly higher than 7 appear
    assert "8" in ranks and "9" in ranks and "J" in ranks
    assert "7" not in ranks and "3" not in ranks

def test_generate_options_follow_pair_lists_only_pairs_higher():
    hand = [
        Card("9", "♣"), Card("9", "♦"),
        Card("10", "♣"), Card("10", "♦"),
        Card("J", "♣"), Card("J", "♦"), Card("J", "♥"),
    ]
    cur = Play(size=2, rank="9")
    plays = generate_options(hand, cur)
    assert 1 not in plays and 3 not in plays and 4 not in plays
    assert 2 in plays
    ranks = ranks_of_options(hand, plays[2])
    # both 10 and J should be available as pairs that beat 9
    assert "10" in ranks and "J" in ranks

def test_generate_options_no_legal_follow_returns_empty():
    # Hand has only a low pair and a low single; current play is a high pair
    hand = [Card("3", "♣"), Card("3", "♦"), Card("4", "♣")]
    cur = Play(size=2, rank="9")
    assert generate_options(hand, cur) == {}


def test_best_move_lead_prefers_lowest_singleton_then_pairs():
    hand = [
        Card("3", "♣"),            # singleton (lowest)
        Card("5", "♣"), Card("5", "♦"),
        Card("9", "♣"), Card("9", "♦"), Card("9", "♥"),
    ]
    plays = generate_options(hand, None)
    chosen = best_move(hand, None, plays)
    size, idxs = chosen
    assert size == 1
    assert hand[idxs[0]].rank == "3"

def test_best_move_follow_single_prefers_true_singleton_else_from_largest_group():
    # No true singletons higher than 7; only a pair and a triple
    hand = [
        Card("8", "♣"), Card("8", "♦"),
        Card("Q", "♣"), Card("Q", "♦"), Card("Q", "♥"),
    ]
    cur = Play(size=1, rank="7")
    plays = generate_options(hand, cur)
    size, idxs = best_move(hand, cur, plays)
    assert size == 1
    # should take from the largest group first (Q triple)
    assert hand[idxs[0]].rank == "Q"

def test_best_move_follow_pair_picks_lowest_beating_pair():
    hand = [
        Card("9", "♣"), Card("9", "♦"),
        Card("10", "♣"), Card("10", "♦"),
        Card("J", "♣"), Card("J", "♦"),
    ]
    cur = Play(size=2, rank="9")
    plays = generate_options(hand, cur)
    size, idxs = best_move(hand, cur, plays)
    assert size == 2
    assert hand[idxs[0]].rank == "10"


def test_best_move_none_when_no_plays():
    assert best_move(hand=[], current_play=None, plays_by_size={}) is None
