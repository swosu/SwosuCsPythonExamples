# tests/test_cards.py
import itertools
import random
import pytest

from Presidents.cards import deal_hands, new_deck, RANKS, SUITS, Card, sort_hand

from cards import deal_hands, new_deck, RANKS, SUITS, Card, sort_hand

def test_new_deck_has_52_unique_cards():
    deck = new_deck()
    assert len(deck) == 52
    assert len(set(deck)) == 52
    assert {c.rank for c in deck} == set(RANKS)
    assert {c.suit for c in deck} == set(SUITS)

@pytest.mark.parametrize("n", [2,3,4,5,6,7,8,9,10])
def test_deal_hands_uses_all_cards_and_balances_sizes(n):
    rng = random.Random(12345)
    hands = deal_hands(n, rng=rng)
    flat = list(itertools.chain.from_iterable(hands))
    assert len(flat) == 52
    assert len(set(flat)) == 52
    sizes = sorted(len(h) for h in hands)
    assert max(sizes) - min(sizes) <= 1

def test_card_ordering_and_sort_hand():
    c3 = Card("3", "♣")
    c4 = Card("4", "♣")
    cA = Card("A", "♣")
    c2 = Card("2", "♣")
    assert c3 < c4 < cA < c2

    hand = [Card("A","♠"), Card("3","♦"), Card("A","♣"), Card("2","♦")]
    assert [str(c) for c in sort_hand(hand)] == ["3♦", "A♣", "A♠", "2♦"]

def test_invalid_card_raises():
    with pytest.raises(ValueError):
        Card("🦄", "♣")
    with pytest.raises(ValueError):
        Card("3", "🦄")
