import csv
from generate_data import generate_dice_rolls


def write_rolls_to_csv(filename, num_rolls):

    rolls = generate_dice_rolls(num_rolls)

    with open(filename, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["die1", "die2", "total"])

        for row in rolls:
            writer.writerow(row)

    print("CSV file created:", filename)


if __name__ == "__main__":

    write_rolls_to_csv("data/dice_rolls.csv", 10000)