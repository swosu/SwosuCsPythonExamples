# create a class called player
# it has data members: name, score, current_roll 
# it has methods: roll, hold_dice, set_name, get_name, 
# change_name, get_score, get_current_roll
# additional mentods: print_options, print_score, print_current_roll
class Dice_Game_Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.current_roll = []

    def roll(self):
        self.current_roll = random.randint(1,6)
        return self.current_roll

    def hold_dice(self):
        self.score += self.current_roll
        self.current_roll = 0

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def get_current_roll(self):
        return self.current_roll
    
    def greet_user(self):
        print("Hello, ", self.name, "! I am glad you are here.")
    

if __name__ == "__main__":
    print("This is where we test the Dice_Game_Player class")

    # create a player
    user_input = input("Please enter your name: ")
    player1 = Dice_Game_Player(user_input)
    print("Player 1's name is: ", player1.get_name())
    player1.greet_user()