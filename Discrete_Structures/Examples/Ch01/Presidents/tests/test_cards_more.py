import copy
import itertools
import random
import pytest
import dataclasses


from cards import Card, new_deck, sort_hand, deal_hands, RANKS, SUITS, RANK_TO_VALUE, SUIT_TO_VALUE


def test_card_is_hashable_and_frozen():
    c = Card("A", "♠")
    s = {c}
    assert c in s
    # Try normal assignment, which should fail
    with pytest.raises((AttributeError, dataclasses.FrozenInstanceError)):
        c.rank = "3"

def test_ordering_transitivity_and_tiebreaker():
    # rank ordering
    c3 = Card("3","♣"); c4 = Card("4","♣"); cA = Card("A","♣"); c2 = Card("2","♣")
    assert c3 < c4 < cA < c2
    # antisymmetry
    assert not (c4 < c4) and not (c4 > c4)
    # suit tiebreaker: same rank, suit order by SUIT_TO_VALUE
    same_rank = [Card("Q", s) for s in SUITS]
    expected = sorted(same_rank, key=lambda c: SUIT_TO_VALUE[c.suit])
    assert sorted(same_rank) == expected

def test_sort_hand_does_not_mutate_input():
    original = [Card("A","♠"), Card("3","♦"), Card("A","♣"), Card("2","♦")]
    snapshot = copy.deepcopy(original)
    sorted_copy = sort_hand(original)
    assert original == snapshot              # input unchanged
    assert sorted_copy != original           # new, sorted list returned

def test_new_deck_counts_by_rank_and_suit():
    deck = new_deck()
    # 4 cards of each rank
    for r in RANKS:
        assert sum(c.rank == r for c in deck) == 4
    # 13 cards of each suit
    for s in SUITS:
        assert sum(c.suit == s for c in deck) == 13
    # exactly these ranks/suits, no jokers
    assert {c.rank for c in deck} == set(RANKS)
    assert {c.suit for c in deck} == set(SUITS)

@pytest.mark.parametrize("n", [2,3,4,5,6,7,8,9,10])
def test_deal_hands_balanced_for_any_player_count(n):
    hands = deal_hands(n, rng=random.Random(7))
    lengths = sorted(len(h) for h in hands)
    assert sum(lengths) == 52
    assert lengths[-1] - lengths[0] <= 1     # size diff at most 1

def test_deal_hands_invalid_player_counts():
    with pytest.raises(ValueError):
        deal_hands(1)
    with pytest.raises(ValueError):
        deal_hands(11)

def test_deal_is_deterministic_with_seed():
    rng1 = random.Random(123)
    rng2 = random.Random(123)
    h1 = deal_hands(4, rng=rng1)
    h2 = deal_hands(4, rng=rng2)
    # Compare stringified to avoid object identity noise
    assert [[str(c) for c in hand] for hand in h1] == [[str(c) for c in hand] for hand in h2]
