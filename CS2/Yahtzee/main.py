 # we are going to make some of our own modules.
# here are two good sites to skim
# https://docs.python.org/3/tutorial/modules.html
# https://docs.python.org/3/tutorial/classes.html
# https://www.pythonpool.com/python-class-vs-module/


<<<<<<< HEAD
import kendell_file
import jeremy_file
import kylar_file
import Josh_file
import jessie_file
import Dalton_File
import jarett_file
import spencer_file
import ryan_file
import trevor_file
=======
#import kendell_file
#import jeremy_file
#import kylar_file
#import Josh_file
#import jessie_file
#import Dalton_File
#import jarett_file
#import spencer_file
#import ryan_file

>>>>>>> c7de0f8bcb6d1284c130038bf273184f050ead7e
import Faff_file
import dice_file
import upperscore_scorepad
import Scorepad_file
import lower_section_file

our_object = Faff_file.User_interactions()
dice_object = dice_file.dice_class()
upper_scorecard_object = upperscore_scorepad.singles_possible_scores()

our_object.say_hello()

our_object.testing_or_playing()

our_object.ask_player_count()

our_object.ask_player_names()
scorecard_object = Scorepad_file.Scorepad_class(our_object, upper_scorecard_object)
scorecard_object.initilize_score_card(our_object, upper_scorecard_object)
scorecard_object.print_score_card()

for round_index in range (0, (len(scorecard_object.score_card) - 1)):
    for player_number in range(0, our_object.get_player_count()):
        scorecard_object.player_index = player_number
        print(f'ready player {player_number + 1}, aka {our_object.get_player_name(player_number)}')

        dice_object.roll_new_five()
        upper_scorecard_object.load_input_dice(dice_object.dice_on_table)
        upper_scorecard_object.calculate_scores()
        upper_scorecard_object.print_upper_scorecard_options()
        while 3 >= dice_object.roll_count:
            dice_object.ask_player_what_to_keep(our_object)
            print('done asking what to save')
            print('now we roll the ones not saved.')
            dice_object.roll_unsaved_dice()
            upper_scorecard_object.load_input_dice(dice_object.dice_on_table)
            upper_scorecard_object.calculate_scores()
            upper_scorecard_object.print_upper_scorecard_options()
            if 4 == dice_object.roll_count:
                print('you are out of rolls..')
                dice_object.print_dice_on_table()
        scorecard_object.ask_user_which_index_to_keep(upper_scorecard_object, our_object)
        scorecard_object.print_score_card()

    print('good round everyone!')
    #break
