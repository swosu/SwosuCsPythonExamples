import random

# import the class Dice_game_player from the local folder Modules
from Modules.Dice_game_player import Dice_Game_Player

# create a class called Single_Roll_Dice_Game
# it has data members: player1, player2, current_player, current_scores, 
# current_roll, winning_score, game_over
# it has methods: roll, hold_dice, set_name, get_name,
# get_score, get_current_roll, print_options, print_score, print_current_roll
# pick_first_player, play_game, print_winner
# pick_player_order, print_player_order

class Single_Roll_Dice_Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.current_scores = [0,0]
        self.current_roll = 0
        self.game_over = False

    def get_name(self):
        return self.name

    def pick_first_player(self):
        print("We will now pick who goes first.")
        self.current_player = random.choice([self.player1, self.player2])
        print(self.current_player.get_name(), " will go first.")

    def play_game(self):
        print(self.current_player.get_name(), " it is your turn.")



if __name__ == "__main__":
    # make a player object from the Dice_Game_Player class and say hello
    user_name = input("Please enter your name: ")
    player1 = Dice_Game_Player(user_name)
    player1.greet_user()

    # make a computer player object from the Dice_Game_Player class and say hello
    player2 = Dice_Game_Player("Computer")
    player2.greet_user()

    # create a game object from the Single_Roll_Dice_Game class
    game1 = Single_Roll_Dice_Game(player1, player2)
    game1.pick_first_player()

    # play the game
    game1.play_game()