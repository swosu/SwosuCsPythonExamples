
import FarkleGameFile as FarkleGame

if __name__ == "__main__":
    # Simulating a game
    player_names = ["Alice", "Bob", "Charlie", "Diana"]
    game = FarkleGame(player_names)

    for _ in range(10):  # Simulate 10 turns
        game.play_turn()
        game.print_score_sheet()