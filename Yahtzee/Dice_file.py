# import statements
import random

# set random seed
random.seed(5)

import time

# set random seed based on the clock
# random.seed(time.time())

class Dice_class():
    def __init__(self):
        self.dice_on_the_table = [0, 0, 0, 0, 0, 0]
        self.keepers = []
        self.roll_number = 0
        self.single_die = 0

    def roll_single_die(self):
        self.single_die = random.randint(1, 6)
        return self.single_die
    
    def first_roll(self):
        self.roll_number = 1
        for dice_index in range(6):
            self.dice_on_the_table[dice_index] = self.roll_single_die()
        return self.dice_on_the_table