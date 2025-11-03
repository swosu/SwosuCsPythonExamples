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