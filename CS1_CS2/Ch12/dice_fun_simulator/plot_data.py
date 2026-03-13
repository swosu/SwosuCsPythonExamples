import matplotlib.pyplot as plt
from read_csv import analyze_rolls


def plot_rolls(filename):

    counts = analyze_rolls(filename)

    totals = sorted(counts.keys())
    frequencies = [counts[t] for t in totals]

    plt.bar(totals, frequencies)

    plt.title("Dice Roll Distribution")
    plt.xlabel("Dice Total")
    plt.ylabel("Frequency")

    plt.show()


if __name__ == "__main__":

    plot_rolls("data/dice_rolls.csv")