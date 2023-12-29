import random
from Upper_scorecard_file import Upper_Scorecard_class

class Player():
    def __init__(self, name, roll):
        self.name = name
        self.initial_roll = roll
        self.upper_scorecard = Upper_Scorecard_class()



if __name__ == '__main__':
    print('hello')
    test_player = Player('test', 5)
    unfilled_categories = test_player.upper_scorecard.get_unfilled_categories()
    print(unfilled_categories)
    from Dice_file import Dice_class
    test_dice = Dice_class()
    # first roll
    print('first roll')
    test_dice.first_roll()
    test_dice.print_dice_on_the_table()