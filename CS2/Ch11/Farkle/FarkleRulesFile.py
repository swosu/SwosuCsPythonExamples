import FarkleScoreingFile as FarkleScoring

# Class for the rules of the game
class FarkleRules:
    def __init__(self):
        self.dice_count = 6  # Number of dice rolled per turn

    def check_farkle(self, dice):
        # Check if any scoring combination is possible with the current roll
        score = FarkleScoring().calculate_score(dice)
        return score == 0  # If no points can be scored, it's a Farkle
    
