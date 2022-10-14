class dice_class:
    def __init__(self):
        self.dice_on_table = [1, 2, 3, 4, 5]
        self.roll_count = 0

    def roll_new_five(self):
        import random
        self.roll_count = 1
        print('New roll.')
        for die in range(0, len(self.dice_on_table)):
            self.dice_on_table[die] = random.randint(1,6)
        print('here are the dice on the table.')
        print('\nDICE NUMBER\t1\t2\t3\t4\t5')
        print('DICE VALUE,', end = '')
        for die in self.dice_on_table:
            print(f'\t{die}', end = '')
        print()

    def ask_player_what_to_keep(self, our_object):
        print('which dice do you want to keep?')
        print('enter the dice number or numbers to keep')
        print('just press enter to reroll all dice.')
        if our_object.testing:
            print('This code needs to be completed still.')
        else:
            user_selection = input('enter which dice do you want to keep seperated by spaces?')
            print(f'you selected to keep: {user_selection}.')

if __name__ == '__main__':

    import Faff_file
    our_object = Faff_file.User_interactions()
    our_object.set_testing_false()
    dice_object = dice_class()

    dice_object.roll_new_five()
    dice_object.ask_player_what_to_keep(our_object)
