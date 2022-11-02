#return all possible scores.
class lower_section:

    def __init__(self,given_dice):
        self.dice_actual = given_dice
        self.scores = [0,0,0,0,0,0,0] #needs to be 7 values.

    def dice_count(self):
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

    def score_scanner(self):
        print('Getting scores...')
        for i in self.dice_array: #checking for three of a kind -working
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
                        self.scores[2] = 25 #add checks for large/small straight below
        for i in self.dice_array: #checking for yahtzee
            if i == 5:
                self.scores[4] = 50
        print(f'Score scanner output: {self.scores}') #testing for output

if __name__ == '__main__':
    given_dice = [3,3,3,3,3]
    score = lower_section(given_dice)
    score.dice_count()
    score.score_scanner()

