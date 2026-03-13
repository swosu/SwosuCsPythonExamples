from src.craps_rules import play_pass_line_round


def monte_carlo(num_games, report_interval=10000):

    wins = 0
    losses = 0

    for i in range(1, num_games + 1):

        outcome, _ = play_pass_line_round()

        if outcome == "win":
            wins += 1
        else:
            losses += 1

        if i % report_interval == 0:

            win_rate = wins / i
            loss_rate = losses / i

            ev = win_rate - loss_rate
            house_edge = -ev

            print(
                f"Games simulated: {i:,}  "
                f"WinRate: {win_rate:.6f}  "
                f"HouseEdge: {house_edge:.6f}"
            )

    win_rate = wins / num_games
    loss_rate = losses / num_games

    ev = win_rate - loss_rate
    house_edge = -ev

    print("\nFinal Results")
    print("-------------------")
    print("Games simulated:", num_games)
    print("Wins:", wins)
    print("Losses:", losses)
    print("Win rate:", win_rate)
    print("Expected value:", ev)
    print("House edge:", house_edge)


if __name__ == "__main__":
    monte_carlo(1_000_000)