import random
from collections import Counter

import FarkleRulesFile as FarkleRules

# Class for scoring calculations
class FarkleScoring:
    def __init__(self):
        self.scoring_rules = {
            '1': 100,  # 1's are worth 100 points
            '5': 50,   # 5's are worth 50 points
        }

    def calculate_score(self, dice):
        counts = Counter(dice)
        score = 0

        # Scoring for triplets or higher
        for num in range(1, 7):
            if counts[num] >= 3:
                if num == 1:
                    score += 1000 * (counts[num] // 3)  # Three 1's are 1000 points
                else:
                    score += num * 100 * (counts[num] // 3)  # Three of any other number
                counts[num] %= 3  # Reduce the count by the number used

        # Scoring for individual 1's and 5's
        score += counts[1] * self.scoring_rules.get('1', 0)
        score += counts[5] * self.scoring_rules.get('5', 0)

        return score

# Class for player interactions
class FarklePlayer:
    def __init__(self, name):
        self.name = name
        self.total_score = 0
        self.turn_score = 0

    def roll_dice(self, num_dice):
        return [random.randint(1, 6) for _ in range(num_dice)]

    def bank_points(self):
        self.total_score += self.turn_score
        self.turn_score = 0

# Class for score sheet
class FarkleScoreSheet:
    def __init__(self, players):
        self.scores = {player.name: 0 for player in players}

    def update_score(self, player):
        self.scores[player.name] = player.total_score

    def print_scores(self):
        for player, score in self.scores.items():
            print(f"{player}: {score} points")

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

# Simulating a game
player_names = ["Alice", "Bob", "Charlie", "Diana"]
game = FarkleGame(player_names)

for _ in range(10):  # Simulate 10 turns
    game.play_turn()
    game.print_score_sheet()
