import random

class Dice_class():
    def __init__(self):
        self.dice_values = [0, 0, 0, 0, 0, 0]
        self.keepers = []
        self.roll_number = 0
        self.single_die = 0

    def roll_single_die(self):
        self.single_die = random.randint(1, 6)
        return self.single_die