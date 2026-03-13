import csv
from collections import Counter


def analyze_rolls(filename):

    totals = []

    with open(filename) as file:

        reader = csv.DictReader(file)

        for row in reader:

            totals.append(int(row["total"]))

    counts = Counter(totals)

    return counts


if __name__ == "__main__":

    counts = analyze_rolls("data/dice_rolls.csv")

    print("Frequency of dice totals:")

    for total in sorted(counts):

        print(total, ":", counts[total])