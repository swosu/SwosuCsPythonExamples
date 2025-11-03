from game_engine import GameEngine

def get_player_names():
    """Prompt the user for player names."""
    player_names = []
    num_players = 0

    # Ask for number of players (limit to 1–4 for fairness)
    while True:
        try:
            num_players = int(input("Enter number of players (1–4): "))
            if 1 <= num_players <= 4:
                break
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Get each player's name
    for i in range(num_players):
        name = input(f"Enter name for Player {i + 1}: ").strip()
        if not name:
            name = f"Player{i + 1}"  # fallback name
        player_names.append(name)

    return player_names


def get_round_count():
    """Ask how many rounds to play."""
    while True:
        try:
            rounds = int(input("Enter number of rounds to play (default 5): ") or 5)
            if rounds > 0:
                return rounds
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    print("🎲 Welcome to the Modular Dice Game! 🎲\n")
    players = get_player_names()
    rounds = get_round_count()

    # Create and start the game
    game = GameEngine(players, rounds)
    game.play_game()

    print("\nThanks for playing! Come back soon!\n")


if __name__ == "__main__":
    main()
