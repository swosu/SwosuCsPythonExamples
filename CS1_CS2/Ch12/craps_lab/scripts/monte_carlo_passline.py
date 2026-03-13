from src.craps_rules import play_pass_line_round


def monte_carlo(num_games):

    wins = 0
    losses = 0
    profit = 0

    for _ in range(num_games):

        outcome, rolls = play_pass_line_round()

        if outcome == "win":
            wins += 1
            profit += 1

        else:
            losses += 1
            profit -= 1

    ev = profit / num_games
    house_edge = -ev

    print("\nMonte Carlo Results")
    print("-------------------")
    print("Games simulated:", num_games)
    print("Wins:", wins)
    print("Losses:", losses)
    print("Win rate:", wins / num_games)
    print("Expected value:", ev)
    print("House edge:", house_edge)


if __name__ == "__main__":

    monte_carlo(1_000_000)