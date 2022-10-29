class singles_possible_scores:
    def __init__(self):
        self.dice_input = []
        self.score_vector = [0, 0, 0, 0, 0, 0]
        self.score_label_vector = ['Ace', 'Duce', 'Tre', 'Quad', 'Fives', 'Sixes']

    def load_input_dice(self,incoming_dice):
        self.dice_input = incoming_dice
        print(f'our incoming dice are: {self.dice_input}.')

    def print_upper_scorecard_options(self):
        print('here are your scores')
        print('\nSCORE LABEL:', end = '')
        for label in self.score_label_vector:
            print(f'\t{score}', end = '')
        print()
        print('SCORE VALUE:', end = '')
        for score in self.score_vector:
            print(f'\t{label}', end = '')
        print()
        print('SCORE INDEX:\t1\t2\t3\t4\t5\t6')
    
    def calculate_scores(self):
        #self.dice_input = [1, 2, 2, 5, 5]
        self.score_vector = [0, 0, 0, 0, 0, 0]
        ones = 1
        twos = 2
        threes = 3
        fours = 4
        fives = 5
        sixes = 6
        count=0
        for ele in self.dice_input:
            if ele == ones:
                count=count+1
                self.score_vector[0] = count*1
        count=0
        for ele in self.dice_input:
            if ele == twos:
                count=count+1
                self.score_vector[1] = count*2
        count=0
        for ele in self.dice_input:
            if ele == threes:
                count=count+1
                self.score_vector[2] = count*3
        count=0
        for ele in self.dice_input:
            if ele == fours:
                count=count+1
                self.score_vector[3] = count*4
        count=0
        for ele in self.dice_input:
            if ele == fives:
                count=count+1
                self.score_vector[4] = count*5
        count=0
        for ele in self.dice_input:
            if ele == sixes:
                count=count+1
                self.score_vector[5] = count*6
                
    def test_ones(self):
        self.load_input_dice([2, 1, 1, 1, 1])
        self.calculate_scores()
        print(self.score_vector)
        if[4, 2, 0, 0, 0, 0] == self.score_vector:
            print('ones test passed.')
        else:
            print('ones test failed.')



    def test_twos(self):
        self.load_input_dice([2, 1, 2, 2, 2])
        self.calculate_scores()
        print(self.score_vector)
        if[1, 8, 0, 0, 0, 0] == self.score_vector:
            print('twos test passed.')
        else:
            print('twos test failed.')

    def test_threes(self):
        self.load_input_dice([3, 3, 2, 3, 3])
        self.calculate_scores()
        print(self.score_vector)
        if[0, 2, 12, 0, 0, 0] == self.score_vector:
            print('threes test passed.')
        else:
            print('threes test failed.')

if __name__ == '__main__':
    our_object = singles_possible_scores()
    our_object.test_ones()
    our_object.test_twos()
    our_object.test_threes()

