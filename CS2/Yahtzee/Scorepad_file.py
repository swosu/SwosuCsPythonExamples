class Scorepad_class:
    def __init__(self, our_object, all_scores):
        self.default_score_vector = []
        self.data = []
        #print(f'how many players do we have? {len(our_object.player_names)}')
        self.score_card = [['none' for column_index in range(1 + len(our_object.player_names))] \
            for row_index in range(1 + (len(all_scores.score_label_vector) )) ] #integrate to have lower_section_scores print with scorepad, look at upper_scorepad for refrence
        self.player_index = 0
    
    def ask_user_which_index_to_keep(self,all_scores, our_object):
        import random
        if our_object.testing:
            print('in testing mode.')
            while True:
                keep_index = random.randint(1, (len(self.score_card) - 1))
                print(f'keep index was: {keep_index}')
                print(f'player index is: {self.player_index}.')
                #self.print_score_card()
                if 'none' == self.score_card[keep_index][self.player_index + 1] :
                    self.score_card[keep_index][self.player_index + 1] = upper_scorecard_object.score_vector[(keep_index - 1)]
                    self.score_card[keep_index][self.player_index + 1] = lower_section_scores.scores[(keep_index - 1)]
                    break
        else:
            while True:
                upper_scorecard_object.print_upper_scorecard_options()
                lower_section_scores.print_lower_scorecard_options()
                print('please select only 1 score.')
                keep_index = int(input('which score input would you like to keep?'))
                print(f'you entered {keep_index}')
                print(f'this is {upper_scorecard_object.score_vector[(keep_index - 1)]}')
                print(f'this is {lower_section_scores.scores[(keep_index - 1)]}')
                #print(f'type of score vector is {type(upper_scorecard_object.score_vector)}')
                user_selection = input('press 1 if correct, else enter something else.')
                if '1' == user_selection:
                    print('got it.')
                    if 'none' == self.score_card[keep_index][self.player_index + 1] :
                        self.score_card[keep_index][self.player_index + 1] = upper_scorecard_object.score_vector[(keep_index - 1)]
                        self.score_card[keep_index][self.player_index + 1] = lower_section_scores.scores[(keep_index - 1)]
                        break
                    else:
                        print('that score is not availible, please try again.')

    def initilize_score_card(self, our_object, upper_scorecard_object,lower_section_scores):
        #print('going to put in names')
        self.score_card[0][0] = ''
        for column_index in range(0, len(our_object.player_names)):
            self.score_card[0][column_index + 1] = our_object.player_names[column_index]
        
        #print('adding score labels for upper scorecard')
        #print(f'length {len(self.score_card)}.')
        for row_index in range (0, (len(upper_scorecard_object.score_label_vector) )):
            #print(f'row index: {row_index}.')
            #print(self.score_card)
            self.score_card[row_index + 1][0] = \
                upper_scorecard_object.score_label_vector[row_index]
            #self.score_card[row_index + 1][1] = \
            #    lower_section_scores.score_label_vector[row_index]

        #print('adding score labels for lower scorecard')
        #print(f'length {len(self.score_card)}.')
        for row_index in range (len(upper_scorecard_object.score_label_vector) ,\
             (len(self.score_card) - 1 )):
            #print(f'row index: {row_index}.')
            #print(self.score_card)
            #self.score_card[row_index + 1][0] = \
            #    upper_scorecard_object.score_label_vector[row_index]
            self.score_card[row_index + 1][0] = \
                lower_section_scores.score_label_vector[row_index- len(upper_scorecard_object.score_label_vector)]

    def print_score_card(self):
        #from prettytable import PrettyTable
        #t = PrettyTable(['Ya', 'htz','ee'])
        
        print('Here are the current scores.')
        
        #print(self.score_card)
        for row_index in range (0, len(self.score_card)):
            #our_additional_row = []
            for column_index in range (0, len(self.score_card[0])):
                #our_additional_row.append(self.score_card[row_index][column_index])
                #print(f'({row_index}, {column_index}), ', end = '')
                #good print(f'\t{self.score_card[row_index][column_index]}', end = '')
                #print('{0:{width}}'.format(self.score_card[row_index][column_index], {width=16}), end = '')
                if 0 == column_index:
                    print(f'{self.score_card[row_index][column_index]:.<20}', end = '')
                else:
                    print(f'{self.score_card[row_index][column_index]:.>7}', end = '')

            print()
            #t.add_row(our_additional_row)
        #print('Here are the other current scores.')
        #print(t)
        

if __name__ == '__main__':
    #print('running scorepad to load a score')
    
    import Faff_file
    import dice_file
    import upperscore_scorepad
    import lower_section_file
    upper_scorecard_object = upperscore_scorepad.singles_possible_scores()
    lower_section_scores = lower_section_file.lower_section()
    our_object = Faff_file.User_interactions()
    dice_object = dice_file.dice_class()

    #our_object.player_count = 3
    our_object.player_names = ['Brian', 'Link', 'Carol']
    scorecard_object = Scorepad_class(our_object, upper_scorecard_object,lower_section_scores)
    scorecard_object.initilize_score_card(our_object, upper_scorecard_object,lower_section_scores)
    #scorecard_object.print_score_card()

    our_object.testing = True

    for round_index in range(1, (len(scorecard_object.score_card))):
        for player_index in range (0, len(our_object.player_names)):
            scorecard_object.player_index = player_index
            print(f'Player number {player_index + 1}, aka {our_object.player_names[player_index]}, you are up!')
        
            #print('what are the dice on the table?')
            dice_object.roll_new_five()
            dice_object.print_dice_on_table()

            print('what are the score options?')
        
            upper_scorecard_object.load_input_dice(dice_object.dice_on_table)
            upper_scorecard_object.calculate_scores()
            lower_section_scores.take_dice(dice_object.dice_on_table)
            lower_section_scores.score_scanner()
            #upper_scorecard_object.print_upper_scorecard_options()
            scorecard_object.ask_user_which_index_to_keep(upper_scorecard_object,lower_section_scores, our_object)
            #scorecard_object.print_score_card()

