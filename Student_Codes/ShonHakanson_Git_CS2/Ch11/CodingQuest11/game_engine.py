from player import Player
from game_rules import calculate_points


class GameEngine:
    """Manages the flow and logic of the dice game."""

    def __init__(self, player_names, rounds=5):
        """Initialize the game with a list of player names and round count."""
        if not player_names:
            raise ValueError("At least one player name is required.")
        
        self.players = [Player(name) for name in player_names]
        self.rounds = rounds

    def play_round(self):
        """Each player rolls their dice and earns points for the round."""
        print("\nRolling dice...")
        for player in self.players:
            rolls = player.roll_dice()
            points = calculate_points(rolls)
            player.add_score(points)
            print(f"{player.name} earned {points:+} points. "
                  f"Total score: {player.score}")
        print("-" * 40)

    def play_game(self):
        """Run the game for the specified number of rounds."""
        print(f"\n🎲 Starting a {self.rounds}-round dice game!\n")
        for round_num in range(1, self.rounds + 1):
            print(f"===== Round {round_num} =====")
            self.play_round()
        self.show_winner()

    def show_winner(self):
        """Determine and display the player(s) with the highest score."""
        print("\n📊 Final Scores:")
        for player in self.players:
            print(f"{player.name}: {player.score} points")

        # Find the highest score
        highest = max(player.score for player in self.players)
        winners = [p.name for p in self.players if p.score == highest]

        # Print winner(s)
        if len(winners) == 1:
            print(f"\n🏆 Winner: {winners[0]} with {highest} points!")
        else:
            print(f"\n🤝 It's a tie between: {', '.join(winners)} with {highest} points each!")


if __name__ == "__main__":
    game = GameEngine(["Alex", "Jamie", "Riley"], rounds=3)
    game.play_game()
