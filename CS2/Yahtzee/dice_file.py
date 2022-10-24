import random


class dice_class:

    def __init__(self):
        self.dice_on_table = [1, 2, 3, 4, 5]
        self.roll_count = 0
        self.dice_index_to_save = []
        self.saved_dice = []

    def print_dice_on_table(self):
        print('here are the dice on the table.')
        #print(self.dice_on_table)
        print('\nDICE NUMBER\t1\t2\t3\t4\t5')
        print('DICE VALUE,', end = '')
        for die in self.dice_on_table:
            print(f'\t{die}', end = '')
        print()

    def roll_new_five(self):

        self.roll_count = 1
        #print('New roll.')
        for die in range(0, len(self.dice_on_table)):
            self.dice_on_table[die] = random.randint(1,6)



    def ask_player_what_to_keep(self, our_object):
        self.saved_dice = []
        self.print_dice_on_table()
        print('which dice do you want to keep?')
        print('enter the dice number or numbers to keep')
        print('just press enter to reroll all dice.')
        if our_object.testing:
            print('This code needs to be completed still.')
        else:
            user_selection = input('enter which dice do you want to keep seperated by spaces?')
            self.dice_index_to_save = user_selection
            self.update_saved_dice()
            print(f'you selected to keep: {self.dice_index_to_save}.')
            print(f'this would be dice {self.saved_dice}.')
            save_and_continue = input('press 1 if correct, anything else to try again.')
            if "1" == save_and_continue:

                print('moving on.')
                self.roll_count += 1
                print(f'you are on roll {self.roll_count}.')
            else:
                self.dice_index_to_save = []
                self.ask_player_what_to_keep(our_object)

    def update_saved_dice(self):
        print(f'trying to save: {self.dice_index_to_save}.')
        print(f'length of dice index to save is {len(self.dice_index_to_save)} ')
        for item in self.dice_index_to_save:
            if item.isnumeric():
                print(f'going to save dice index {item} with type: {(type(item))}.')
                self.saved_dice.append(int(self.dice_on_table[int(item)-1]))
        print(f'saved dice are: {self.saved_dice}.')

    def roll_unsaved_dice(self):
        print(f'we have {len(self.saved_dice)} saved dice')
        number_of_dice_to_reroll = 5 - len(self.saved_dice)
        self.dice_on_table=[]
        for item in self.saved_dice:
            print('loading saved dice.')
            self.dice_on_table.append(int(item))
            print(f'dice on the table: {self.dice_on_table}.')
        for index in range (0, number_of_dice_to_reroll):
            print('rolling new dice.')
            self.dice_on_table.append(random.randint(1,6))
            print(f'dice on the table: {self.dice_on_table}.')
        print('done rolling new dice for the table')
        self.print_dice_on_table()

if __name__ == '__main__':

    import Faff_file
    print('getting started testing dice file.')
    our_object = Faff_file.User_interactions()
    our_object.set_testing_false()
    dice_object = dice_class()

    dice_object.roll_new_five()
    while 3 >= dice_object.roll_count:
        dice_object.ask_player_what_to_keep(our_object)
        print('done asking what to save')
        print('now we roll the ones not saved.')
        dice_object.roll_unsaved_dice()

else:
    print('you imported dice_file')
