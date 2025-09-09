def card_value(card):
    if card.rank in ["J", "Q", "K"]:
        return 10
    if card.rank == "A":
        return 11  # default as 11, adjust later in hand logic
    return int(card.rank)