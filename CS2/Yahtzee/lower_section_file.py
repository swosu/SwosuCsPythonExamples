#return all possible scores.
given_dice = [2,2,2,2,2]

ones = []
twoes = []
threes = []
fours = []
fives = []
sixes = []
for i in given_dice:
    if i == 1:
        ones.append(1)
    if i == 2:
        twoes.append(2)
    if i == 3:
        threes.append(3)
    if i == 4:
        fours.append(4)
    if i == 5:
        fives.append(5)
    if i == 6:
        sixes.append(6)
        
dice_array = [2,2,2,2,2]
print(given_dice)
print(dice_array)

class lower_section:

    def __init__(self,given_dice): # score system needs to be updated: return independant scores for each method.
        self.dice_actual = given_dice
        self.dice_array = given_dice
        self.score = 0

    #def dice_count(self):
        

    def three_kind(self):
        score = 0 
        for d in self.dice_array:
            if d >= 3:
                for i in self.dice_actual:
                    score += i
                self.score = score
                return self.score
    
    def four_kind(self):
        score = 0 
        for d in self.dice_array:
            if d >= 4:
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
        print(f'{lower_section.three_kind(given_dice)}')

lower_section.get_possible_score(given_dice)

if __name__ == 'main':
    lower_section.get_possible_score(given_dice)
