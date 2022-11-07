#return all possible scores.
import Faff_file
class lower_section:

    def __init__(self):
        self.dice_actual = []
        self.scores = [0,0,0,0,0,0,0] #needs to be 7 values.

    def dice_count(self,given_dice): #creates matching dice index and sorts dice 
        self.dice_actual = given_dice
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
        print(self.dice_actual)
        for i in self.dice_array: #checking for three of a kind 
            if i >= 3:
                score = 0
                for die in self.dice_actual:
                    score  += die
                self.scores[0] = score
        for i in self.dice_array: #checking for four of a kind
            if i >= 4:
                score = 0
                for die in self.dice_actual:
                    score += die
                self.scores[1] = score
        for i in self.dice_array: #checking for Fullhouse
            if i == 3:
                for i in self.dice_array:
                    if i == 2:
                        self.scores[2] = 25 
        count = 0
        index = 1
        for i in self.dice_actual: # checks for small straight()/large straight
            if index != 5:
                if (i + 1) == self.dice_actual[index]:
                    index += 1
                    count += 1
                    if count >= 3:
                        self.scores[3] = 30
                    if count >= 4:
                        self.scores[4] = 40  
        for i in self.dice_array: #checking for yahtzee
            if i == 5:
                self.scores[5] = 50
        score = 0
        for i in self.dice_actual: #Chance
            score += i
            self.scores[6] = score 
        return self.scores
    
    def Test_Straights(self):
        self.dice_count([3,5,4,1,2])
        self.score_scanner()
        print(self.scores)
        if self.scores != [0, 0, 0, 30, 40, 0, 15]:
            print('Straights test failed!')
        else:
            print('Straights test passed!')
        
if __name__ == '__main__':
    Possible_Scores = lower_section()
    Possible_Scores.Test_Straights()
