#return all possible scores.
class lower_section:

    def __init__(self,given_dice):
        self.dice_actual = given_dice
        self.score = 0

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
        print(f'Dice count {self.dice_array}')

    def three_kind(self):
        for a in self.dice_array:
            if a >= 3:
                self.score = 3
            return self.score
    
    def four_kind(self):
        score = 0 
        for die in self.dice_array:
            if die >= 4:
                for i in self.dice_actual:
                    score += i
        self.score == score
        return self.score
        

    def full_house(self): 
        for i in self.dice_array:
            if i >= 3:
                for i in self.dice_array:
                    if i == 2:
                        self.score = 25
                return self.score
    
    def small_straight(self):
        
        pass                    #define
    
    def large_straight(self):
        pass                    #define

    def yahtzee(self):
        for i in self.dice_array:
            if i == 5:
                self.score = 50
        return self.score    

    
    def chance(self): 
        pass

    def get_possible_score(self):
        print('Getting possible scores...')
        print('Three of a kind: Four of a kind: Full House: Small Straight: Large Straight: Yahtzee:')


if __name__ == '__main__':
    given_dice = [2,2,3,3,3]
    dice = lower_section(given_dice)
    dice.dice_count()
    dice.get_possible_score()
