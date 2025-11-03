import FarklePlayerFile as FarklePlayer

# Class to handle the game logic
class FarkleGame:
    def __init__(self, player_names):
        self.players = [FarklePlayer(name) for name in player_names]
        self.rules = FarkleRules()
        self.score_sheet = FarkleScoreSheet(self.players)
        self.current_player = 0

    def play_turn(self):
        player = self.players[self.current_player]
        print(f"\n{player.name}'s turn:")

        dice_left = 6
        farkle = False
        turn_over = False

        while not turn_over:
            roll = player.roll_dice(dice_left)
            print(f"Rolled: {roll}")
            score = FarkleScoring().calculate_score(roll)
            print(f"Score from roll: {score}")

            if score == 0:
                farkle = True
                print("Farkle! No points this turn.")
                player.turn_score = 0
                turn_over = True
            else:
                player.turn_score += score
                print(f"Turn score so far: {player.turn_score}")
                # Player decision-making goes here
                # For simplicity, we just bank points and end turn
                turn_over = True

        if not farkle:
            player.bank_points()
        self.score_sheet.update_score(player)
        self.current_player = (self.current_player + 1) % len(self.players)

    def print_score_sheet(self):
        print("\nScore Sheet:")
        self.score_sheet.print_scores()


if __name__ == '__main__':
    # Simulating a game
    player_names = ["Alice", "Bob", "Charlie", "Diana"]
    game = FarkleGame(player_names)

    for _ in range(10):  # Simulate 10 turns
        game.play_turn()
        game.print_score_sheet()