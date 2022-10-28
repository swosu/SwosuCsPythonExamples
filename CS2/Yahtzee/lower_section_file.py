#return all possible scores.
given_dice = [3,3,3,3,3]

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
dice_index = [len(ones),len(twoes),len(threes),len(fours),len(fives),len(sixes)]
print(given_dice)
print(dice_index)

class lower_section:
    def __init__(self,dice_index,given_dice): # score system needs to be updated: return independant scores for each method.
        self.dice_array = dice_index
        self.dice_actual = given_dice
        self.score = 0
 
    def three_kind(self): 
        for d in self.dice_array:
            if d >= 3:
                for i in self.dice_actual:
                    self.score += i
                return self.score
    
    def four_kind(self): 
        for d in self.dice_array:
            if d >= 4:
                for i in self.dice_actual:
                    self.score += i
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

dice_array = lower_section(dice_index,given_dice)
print(f'Three of a kind score: {dice_array.three_kind()}')
print(f'Four of a kind score: {dice_array.four_kind()}')
print(f'Full house score: {dice_array.full_house()}')
print(f'Yahtzee score: {dice_array.yahtzee()}')

