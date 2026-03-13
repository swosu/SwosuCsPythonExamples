import random

def generate_dice_rolls(num_rolls):
    """
    Generate a list of dice roll results.
    Each result is a tuple (die1, die2, total)
    """

    rolls = []

    for _ in range(num_rolls):

        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)

        total = die1 + die2

        rolls.append((die1, die2, total))

    return rolls


if __name__ == "__main__":

    print("Generating dice rolls directly...")

    number_of_rolls = 10000

    data = generate_dice_rolls(number_of_rolls)

    print("First 10 rolls:")
    for row in data[:10]:
        print(row)