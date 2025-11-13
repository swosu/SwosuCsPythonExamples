#!/usr/bin/env python3
from itertools import permutations, combinations
import csv, json
from pathlib import Path
import matplotlib.pyplot as plt

PEEPS = ["Amina","Lin","Zahra","Jake","Buzz","Tink"]

def valid(seating):
    # A: Amina on an end
    if seating[0] != "Amina" and seating[-1] != "Amina":
        return False
    # B: Lin & Zahra adjacent (either order)
    adj = any({seating[i], seating[i+1]} == {"Lin","Zahra"} for i in range(len(seating)-1))
    if not adj:
        return False
    # C: Bots not adjacent
    for i in range(len(seating)-1):
        if seating[i] in {"Buzz","Tink"} and seating[i+1] in {"Buzz","Tink"}:
            return False
    return True

def main():
    files = Path("../files"); figs = Path("../figures")
    files.mkdir(parents=True, exist_ok=True); figs.mkdir(parents=True, exist_ok=True)

    all_seatings = list(permutations(PEEPS))
    raw = len(all_seatings)
    valid_seats = [s for s in all_seatings if valid(s)]
    good = len(valid_seats)

    # CSV of valid seatings
    with open(files/"ch01_valid_seatings.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["idx"] + [f"seat{i+1}" for i in range(6)])
        for i, s in enumerate(valid_seats, 1):
            w.writerow([i, *s])

    # Small bar chart
    plt.figure()
    plt.bar(["all (6!)","valid"], [raw, good])
    plt.title("Nebula Diner: Seating Counts")
    plt.savefig(figs/"ch01_seating_counts.png", dpi=160, bbox_inches="tight")

    # Console is boring on purpose
    print(f"RAW={raw} VALID={good}")

if __name__ == "__main__":
    main()

