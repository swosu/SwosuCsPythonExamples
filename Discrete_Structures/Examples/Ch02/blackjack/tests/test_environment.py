# blackjack/tests/test_environment.py

from blackjack.cards import Deck
from blackjack.hand import card_value

def test_deck_has_52_unique_cards():
    """The deck must contain exactly 52 unique cards (no duplicates)."""
    deck = Deck()
    assert len(deck.cards) == 52, "Deck should contain 52 cards"

    unique_cards = {(card.rank, card.suit) for card in deck.cards}
    assert len(unique_cards) == 52, "Deck should have 52 unique cards"

def test_shuffle_preserves_count_but_changes_order():
    deck = Deck()
    original_order = deck.cards.copy()
    deck.shuffle()
    # Deck should still have 52 cards
    assert len(deck.cards) == 52, "Shuffled deck should still have 52 cards"
    # Order should usually be different (not guaranteed every time, but very likely)
    assert deck.cards != original_order, "Deck order should change after shuffle"

def test_face_cards_value():
    for rank in ["J", "Q", "K"]:
        card = Card(rank, "hearts")
        assert card_value(card) == 10, f"{rank} should count as 10"

