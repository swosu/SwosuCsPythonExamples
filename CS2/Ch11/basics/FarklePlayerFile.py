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
