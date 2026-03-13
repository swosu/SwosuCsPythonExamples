from src.dice import roll_dice

def play_pass_line_round():

    rolls = []

    # Come-out roll
    die1, die2, total = roll_dice()
    rolls.append(total)

    if total in (7,11):
        return "win", rolls

    if total in (2,3,12):
        return "lose", rolls

    point = total

    # Point phase
    while True:

        die1, die2, total = roll_dice()
        rolls.append(total)

        if total == point:
            return "win", rolls

        if total == 7:
            return "lose", rolls