from src.craps_rules import play_pass_line_round
import csv
import os


def monte_carlo(num_games, report_interval=10000):

    wins = 0
    losses = 0
    profit = 0

    convergence_data = []

    for i in range(1, num_games + 1):

        outcome, rolls = play_pass_line_round()

        if outcome == "win":
            wins += 1
            profit += 1
        else:
            losses += 1
            profit -= 1

        ev = profit / i
        house_edge = -ev

        # Save convergence snapshot
        if i % report_interval == 0:
            convergence_data.append((i, ev, house_edge))
            print(f"Games simulated: {i:,}  EV: {ev:.5f}  House Edge: {house_edge:.5f}")

    print("\nFinal Results")
    print("-------------------")
    print("Games simulated:", num_games)
    print("Wins:", wins)
    print("Losses:", losses)
    print("Win rate:", wins / num_games)
    print("Expected value:", ev)
    print("House edge:", house_edge)

    os.makedirs("data", exist_ok=True)

    with open("data/convergence.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["games", "ev", "house_edge"])

        for row in convergence_data:
            writer.writerow(row)

    print("\nConvergence data written to data/convergence.csv")


if __name__ == "__main__":

    monte_carlo(1_000_000)