class Scorepad_class:
    def __init__(self):
        self.data = []
    
    def ask_user_which_index_to_keep(self,upper_scorecard_object):
        while True:
            upper_scorecard_object.print_upper_scorecard_options()
            keep_index = int(input('which score input would you like to keep?'))
            print(f'you entered {keep_index}')
            print(f'this is {upper_scorecard_object.score_vector[(keep_index - 1)]}')
            #print(f'type of score vector is {type(upper_scorecard_object.score_vector)}')
            user_selection = input('press 1 if correct, else enter something else.')
            if '1' == user_selection:
                print('got it.')
                break
    def make_clean_scorecard(self, our_object):
        print('making a clean score card')



if __name__ == '__main__':
    print('running scorepad to load a score')
    scorecard_object = Scorepad_class()
    import Faff_file
    our_object = Faff_file.User_interactions()
    our_object.player_count = 2
    our_object.player_names = ['Brian', 'Stewie']
    scorecard_object.make_clean_scorecard(our_object)
    print('what are the dice on the table?')
    import dice_file
    dice_object = dice_file.dice_class()
    dice_object.roll_new_five()

    print('what is the score options?')
    import upperscore_scorepad
    upper_scorecard_object = upperscore_scorepad.singles_possible_scores()
    upper_scorecard_object.load_input_dice(dice_object.dice_on_table)
    upper_scorecard_object.calculate_scores()
    upper_scorecard_object.print_upper_scorecard_options()

    
    scorecard_object.ask_user_which_index_to_keep(upper_scorecard_object)