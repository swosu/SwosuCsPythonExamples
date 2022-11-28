class whats_left:
    def __init__(self):
        self.scorepad_input = 0
        self.player_index = 0
        self.singles_array = []

    def load_input(self, scorepad, player_index):
        self.scorepad_input = scorepad
        self.player_index = player_index

    def possible_player_inputs(self):
<<<<<<< HEAD
        
        for x in range (1, (len(self.scorepad_input))):
            if self.scorepad_input[x][self.player_index + 1] == "none":
             self.singles_array.append(self.scorepad_input[x][0])
        
        print(f'Possible Singles for {self.scorepad_input[0][self.player_index + 1]}: {self.singles_array}')

            


example_score =[['', 'Brian', 'Link', 'Carol'], ['Aces', 'none', 1, 'none'], ['Twos', 'none', 2, 'none'], ['Threes', 'none', 3, 'none'], ['Fours', 'none', 4, 'none'], ['Fives', 'none', 'none', 'none'], ['Sixes', 'none', 'none', 'none']]

if __name__ == '__main__':
    """
    whats_left = whats_left()
    whats_left.load_input(example_score, 1)
    whats_left.possible_player_inputs()
    """
import Faff_file
import dice_file
import upperscore_scorepad
import Scorepad_file
our_object = Faff_file.User_interactions()
dice_object = dice_file.dice_class()
upper_scorecard_object = upperscore_scorepad.singles_possible_scores()

our_object.say_hello()

our_object.testing_or_playing()

=======

        for x in range (1, (len(self.scorepad_input))):
            if self.scorepad_input[x][self.player_index + 1] == "none":
             self.singles_array.append(self.scorepad_input[x][0])

        print(f'Possible Singles for {self.scorepad_input[0][self.player_index + 1]}: {self.singles_array}')




example_score =[['', 'Brian', 'Link', 'Carol'], ['Aces', 'none', 1, 'none'], ['Twos', 'none', 2, 'none'], ['Threes', 'none', 3, 'none'], ['Fours', 'none', 4, 'none'], ['Fives', 'none', 'none', 'none'], ['Sixes', 'none', 'none', 'none']]

if __name__ == '__main__':
    """
    whats_left = whats_left()
    whats_left.load_input(example_score, 1)
    whats_left.possible_player_inputs()
    """
import Faff_file
import dice_file
import upperscore_scorepad
import Scorepad_file
our_object = Faff_file.User_interactions()
dice_object = dice_file.dice_class()
upper_scorecard_object = upperscore_scorepad.singles_possible_scores()

our_object.say_hello()

our_object.testing_or_playing()

>>>>>>> trevor
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
        print('------------------------marker')
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

<<<<<<< HEAD
    print('good round everyone!')
=======
    print('good round everyone!')
>>>>>>> trevor
