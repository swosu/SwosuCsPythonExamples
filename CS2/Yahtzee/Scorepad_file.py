class Scorepad_class:
    def __init__(self, our_object, upper_scorecard_object):
        self.default_score_vector = []
        self.data = []
        self.score_card = [['none' for column_index in range(1 + len(our_object.player_names))] for row_index in range(1 + len(upper_scorecard_object.score_label_vector))]
        self.player_index = 0
    
    def ask_user_which_index_to_keep(self,upper_scorecard_object):
        while True:
            upper_scorecard_object.print_upper_scorecard_options()
            print('please select only 1 score.')
            keep_index = int(input('which score input would you like to keep?'))
            print(f'you entered {keep_index}')
            print(f'this is {upper_scorecard_object.score_vector[(keep_index - 1)]}')
            #print(f'type of score vector is {type(upper_scorecard_object.score_vector)}')
            user_selection = input('press 1 if correct, else enter something else.')
            if '1' == user_selection:
                print('got it.')
                self.score_card[keep_index][self.player_index + 1] = upper_scorecard_object.score_vector[(keep_index - 1)]
                break

    def initilize_score_card(self, upper_scorecard_object):
        #print('going to put in names')
        self.score_card[0][0] = ''
        for column_index in range(0, len(our_object.player_names)):
            self.score_card[0][column_index + 1] = our_object.player_names[column_index]
        
        #print('adding score labels')
        #print(f'length {len(self.score_card)}.')
        for row_index in range (0, (len(self.score_card) -1)):
            #print(f'row index: {row_index}.')
            #print(self.score_card)
            self.score_card[row_index + 1][0] = upper_scorecard_object.score_label_vector[row_index]

    def print_score_card(self):
        print('Here are the current scores.')
        #print(self.score_card)
        for row_index in range (0, len(self.score_card)):
            for column_index in range (0, len(self.score_card[0])):
                #print(f'({row_index}, {column_index}), ', end = '')
                print(f'\t{self.score_card[row_index][column_index]}', end = '')
            print()
        

if __name__ == '__main__':
    #print('running scorepad to load a score')
    
    import Faff_file
    import dice_file
    import upperscore_scorepad
    import My_Score_File
    upper_scorecard_object = upperscore_scorepad.singles_possible_scores()
    our_object = Faff_file.User_interactions()
    dice_object = dice_file.dice_class()

    our_object.player_count = 2
    our_object.player_names = ['Brian', '1234567', 'Carol']
    scorecard_object = Scorepad_class(our_object, upper_scorecard_object)
    scorecard_object.initilize_score_card(upper_scorecard_object)
    scorecard_object.print_score_card()

    for player_index in range (0, len(our_object.player_names)):
        scorecard_object.player_index = player_index
        print(f'Player number {player_index + 1}, aka {our_object.player_names[player_index]}, you are up!')

    
        #print('what are the dice on the table?')
        dice_object.roll_new_five()
        dice_object.print_dice_on_table()

        print('what are the score options?')
    
        upper_scorecard_object.load_input_dice(dice_object.dice_on_table)
        upper_scorecard_object.calculate_scores()
        #upper_scorecard_object.print_upper_scorecard_options()
        scorecard_object.ask_user_which_index_to_keep(upper_scorecard_object)
        scorecard_object.print_score_card()