import random
from Upper_scorecard_file import Upper_scorecard

class Player():
    def __init__(self, name, roll):
        self.name = name
        self.initial_roll = roll
        self.upper_scorecard = Upper_scorecard()



if __name__ == '__main__':
    print('hello')