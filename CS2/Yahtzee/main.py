# we are going to make some of our own modules.
# here are two good sites to skim
# https://docs.python.org/3/tutorial/modules.html
# https://docs.python.org/3/tutorial/classes.html
# https://www.pythonpool.com/python-class-vs-module/


import kendell_file
import jeremy_file
import kylar_file
import Josh_file
import jessie_file
import Dalton_File
import jarett_file
import spencer_file
import ryan_file

import Faff_file
import dice_file
import upperscore_scorepad
our_object = Faff_file.User_interactions()
dice_object = dice_file.dice_class()
upper_scorecard_object = upperscore_scorepad.singles_possible_scores()
our_object.say_hello()

our_object.testing_or_playing()

our_object.ask_player_count()

our_object.ask_player_names()

while True:
    for player_number in range(0, our_object.get_player_count()):
        print(f'ready player {player_number + 1}, aka {our_object.get_player_name(player_number)}')

        dice_object.roll_new_five()
        upper_scorecard_object.get_possible_scores(dice_object)
        while 3 >= dice_object.roll_count:
            dice_object.ask_player_what_to_keep(our_object)
            print('done asking what to save')
            print('now we roll the ones not saved.')
            dice_object.roll_unsaved_dice()
            if 4 == dice_object.roll_count:
                print('this turn is over.')
    print('good round everyone!')
    break
