"""
environment.py
---------------
Blackjack game mechanics for bots.

This file defines:
- draw_card(): deal a card (1–13, face cards count as 10, Ace = 1 or 11)
- hand_value(): compute the best hand value with Ace adjustment
- dealer_play(): simulate dealer strategy (hit < 17, stay otherwise)
- play_hand(): simulate one round between a bot and dealer
"""

import random


def draw_card():
    """Draw a random card (1–13). Face cards count as 10, Ace as 1."""
    card = random.randint(1, 13)
    return min(card, 10)


def hand_value(hand):
    """Return the best blackjack value for a hand (Aces = 1 or 11)."""
    total = sum(hand)
    aces = hand.count(1)

    # Promote some Aces to 11 if it doesn't bust
    while aces > 0 and total + 10 <= 21:
        total += 10
        aces -= 1

    return total


def dealer_play():
    """
    Dealer draws two cards, hits until 17 or higher.
    Returns the final hand value.
    """
    hand = [draw_card(), draw_card()]
    while hand_value(hand) < 17:
        hand.append(draw_card())
    return hand_value(hand)


def play_hand(bot):
    """
    Play one hand of blackjack between the given bot and the dealer.

    Parameters
    ----------
    bot : object with method act(player_total, dealer_card)
        Returns "hit" or "stay".

    Returns
    -------
    int : outcome reward
        +1 = player win
         0 = tie
        -1 = player loss
    """
    player = [draw_card(), draw_card()]
    dealer = [draw_card(), draw_card()]

    # Player's turn
    while True:
        action = bot.act(hand_value(player), dealer[0])
        if action == "hit":
            player.append(draw_card())
            if hand_value(player) > 21:
                return -1  # player bust
        else:
            break

    # Dealer's turn
    dealer_total = dealer_play()
    player_total = hand_value(player)

    # Final outcome
    if dealer_total > 21 or player_total > dealer_total:
        return +1
    elif player_total == dealer_total:
        return 0
    else:
        return -1
