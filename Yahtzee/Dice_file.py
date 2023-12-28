# import statements
import random

# set random seed
random.seed(5)

import time

# set random seed based on the clock
# random.seed(time.time())

class Dice_class():
    def __init__(self):
        self.number_of_dice = 5
        self.dice_on_the_table = []
        for dice_index in range(self.number_of_dice):
            self.dice_on_the_table.append(0)
        self.keepers = []
        self.roll_number = 0
        self.single_die = 0

    def roll_single_die(self):
        self.single_die = random.randint(1, 6)
        return self.single_die
    
    def first_roll(self):
        self.roll_number = 1
        self.dice_on_the_table = []
        for dice_index in range(self.number_of_dice):
            self.dice_on_the_table.append(0)

        for dice_index in range(len(self.dice_on_the_table)):
            self.dice_on_the_table[dice_index] = self.roll_single_die()
        # sort the list in ascending order
        self.print_dice_on_the_table()
        self.dice_on_the_table.sort()
        print(" after sorting: ")
        self.print_dice_on_the_table()
        
    def print_dice_on_the_table(self):
        print("Dice on the table: ", self.dice_on_the_table)

    def keep_dice(self):
        self.keepers = []
        print("time to pick what to keep")

        # print the dice on the table next to the letters A, B, C, D, E
        for dice_index in range(len(self.dice_on_the_table)):
            print(chr(dice_index + 65), ": ", self.dice_on_the_table[dice_index])

        # get input from the user
        user_input = input("Enter the letters for the dice you would like to keep, seperated by a space: ")
        
        user_input = user_input.upper()
        user_tokens = user_input.split()

        # add the dice to the keepers list
        for letter in user_tokens:
            print('keeping: ', letter, ' which is ', self.dice_on_the_table[ord(letter) - 65])  
            self.keepers.append(self.dice_on_the_table[ord(letter) - 65])

        # print the keepers list
        print("Keepers: ", self.keepers)

        # remove the keepers from the dice_on_the_table list
        for keeper in self.keepers:
            self.dice_on_the_table.remove(keeper)

        print(" so you want to keep these: ", self.keepers)
        print(' and re-roll these: ', self.dice_on_the_table)
        user_input = input('enter y if this is correct, or any other key to reselect keepers: ')
        if user_input == 'y':
            return
        else:
            self.keep_dice()

    def second_roll(self):

        # increment the roll number
        self.roll_number += 1

        # clear the dice on the table list
        self.dice_on_the_table = []

        # how many keepers did we have?
        number_of_keepers = len(self.keepers)
        print("number of keepers: ", number_of_keepers)

        # how many dice do we need to roll?
        number_of_dice_to_roll = 5 - number_of_keepers

        # load the keepers into the dice_on_the_table list
        for keeper in self.keepers:
            self.dice_on_the_table.append(keeper)

        # roll the remaining dice
        for dice_index in range(number_of_dice_to_roll):
            self.dice_on_the_table.append(self.roll_single_die())

        # sort the list in ascending order
        self.print_dice_on_the_table()
        self.dice_on_the_table.sort()
        print(" after sorting: ")
        self.print_dice_on_the_table()

    def third_roll(self):

        # increment the roll number
        self.roll_number += 1

        # clear the dice on the table list
        self.dice_on_the_table = []

        # how many keepers did we have?
        number_of_keepers = len(self.keepers)
        print("number of keepers: ", number_of_keepers)

        # how many dice do we need to roll?
        number_of_dice_to_roll = 5 - number_of_keepers

        # load the keepers into the dice_on_the_table list
        for keeper in self.keepers:
            self.dice_on_the_table.append(keeper)

        # roll the remaining dice
        for dice_index in range(number_of_dice_to_roll):
            self.dice_on_the_table.append(self.roll_single_die())

        # sort the list in ascending order
        self.print_dice_on_the_table()
        self.dice_on_the_table.sort()
        print(" after sorting: ")
        self.print_dice_on_the_table()
