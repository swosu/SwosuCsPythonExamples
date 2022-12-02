#return all possible scores.
import Faff_file


class lower_section:

    def __init__(self):
        self.dice_actual = []
        self.scores = [0,0,0,0,0,0,0] #need 7 values.
        self.score_label_vector = ['Three of a kind:', 'Four of a kind:', 'Full House:', 'Small Straight:', 'Large Straight:', 'Yahtzee:', 'Chance:']
    
    def take_dice(self, given_dice):
         self.dice_actual = given_dice
    
    def print_lower_scorecard_options(self):
        print('here are your scores')
        print('\nSCORE LABEL:', end = '')
        for label in self.score_label_vector:
            print(f'\t{label}', end = '')
        print()
        print(f'SCORE VALUE:\t{self.scores[0]}\t\t\t\t', end = '')
        for score in self.scores[1:7]:
            print(f'{score}\t\t\t', end = '')
        print()
        print('SCORE INDEX:\t1\t\t\t\t2\t\t\t3\t\t\t4\t\t\t5\t\t\t6\t\t\t7')

    def dice_count(self): #creates matching dice index and sorts dice 
        self.dice_actual.sort()
        ones = []
        twoes = []
        threes = []
        fours = []
        fives = []
        sixes = []
        for die in self.dice_actual:
            if die == 1:
                ones.append(1)
            if die == 2:
                twoes.append(2)
            if die == 3:
                threes.append(3)
            if die == 4:
                fours.append(4)
            if die == 5:
                fives.append(5)
            if die == 6:
                sixes.append(6)
        self.dice_array = [len(ones),len(twoes),len(threes),len(fours),len(fives),len(sixes)]
        #print(f'Your dice value index looks like: {self.dice_array}')

    def score_scanner(self):
        #print(self.dice_actual)
        for i in self.dice_array: #checking three of a kind 
            if i >= 3:
                score = 0
                for die in self.dice_actual:
                    score  += die
                self.scores[0] = score
        for i in self.dice_array: #checking four of a kind
            if i >= 4:
                score = 0
                for die in self.dice_actual:
                    score += die
                self.scores[1] = score
        for i in self.dice_array: #checking Fullhouse
            if i == 3:
                for i in self.dice_array:
                    if i == 2:
                        self.scores[2] = 25 
        count = 0
        index = 1
        for i in self.dice_actual: # checking small straight and large straight
            if index != 5:
                if (i + 1) == self.dice_actual[index]:
                    index += 1
                    count += 1
                    if count >= 3:
                        self.scores[3] = 30
                    if count >= 4:
                        self.scores[4] = 40  
        for i in self.dice_array: #checking yahtzee
            if i == 5:
                self.scores[5] = 50
        score = 0
        for i in self.dice_actual: #Calculating Chance
            score += i
            self.scores[6] = score 
        return self.scores
    
    def test(self):
        ans = str(input("Run tests: Yes/No? \n"))
        if ans in ["YES","Yes","yes","Y","y"]:
            test = lower_section
            test.test_matching()
            test.test_straights(self)
            test.test_yahtzee(self)
        elif ans in ["NO","No","no","N","n"]:
            pass

    def test_matching():
        test_of_kinds = lower_section()
        test_of_kinds.take_dice([1,1,1,1,4])
        test_of_kinds.dice_count()
        test_of_kinds.score_scanner()
        if test_of_kinds.scores == [8,8,0,0,0,0,8]:
            test_fullhouse = lower_section()
            test_fullhouse.take_dice([1,1,1,4,4])
            test_fullhouse.dice_count()
            test_fullhouse.score_scanner()
            if test_fullhouse.scores == [11, 0, 25, 0, 0, 0, 11]:
                print("Matching test passed!")
            else:
                print('Matching test failed! Full_House Error!')
        else:
            print("Matching test failed! Of_Kinds error!")

    def test_straights(self):
        test_straights = lower_section()
        test_straights.take_dice([3,5,4,1,2])
        test_straights.dice_count()
        test_straights.score_scanner()
        if test_straights.scores == [0, 0, 0, 30, 40, 0, 15]:
            print('Straights test passed!') 
        else:
            print('Straights test failed!')

    def test_yahtzee(self):
        test_yahtzee = lower_section()
        test_yahtzee.take_dice([4,4,4,4,4])
        test_yahtzee.dice_count()
        test_yahtzee.score_scanner()
        if test_yahtzee.scores[5] != 50:
            print('Yahtzee test failed!')
        else:
            print('Yahtzee test passed!')
        
if __name__ == '__main__':
    possible_scores = lower_section()
    #possible_scores.test()
    possible_scores.take_dice([4,4,4,4,4])
    possible_scores.dice_count()
    possible_scores.score_scanner()
    possible_scores.print_lower_scorecard_options()
    
