import random
from itertools import repeat

possible_score_list = []
winner = ''

possible_score_dict = {
    'straight' : 3000,
    'full_house' : 1500,
    'two_triplets' : 2500,
    'six_of_a_kind' : 3000,
    'five_of_a_kind' : 2000,
    'four_of_a_kind' : 1000,
    'three_ones' : 1000,
    'three_of_a_kind' : 500,
    'three_pairs' : 1500,
    'ones' : 100,
    'fives' : 50,
    'farkle' : 0
}

def list_to_string(num_list, str_list):
    for item in num_list:
        str_list.append(str(item))
    return str_list


def list_to_num(num_list, str_list):
    for item in str_list:
        num_list.append(item)
    return num_list


class Dice:
    def __init__(self):
        self.faces = [1, 2, 3, 4, 5, 6]

    def roll(self):
        result = random.choice(self.faces)
        return result

die1 = Dice()
die2 = Dice()
die3 = Dice()
die4 = Dice()
die5 = Dice()
die6 = Dice()
class Cup:
    def __init__(self):
        self.cup = []
        self.count = []
        self.add_dice()

    def add_dice(self):
        self.cup.append(die1)
        self.cup.append(die2)
        self.cup.append(die3)
        self.cup.append(die4)
        self.cup.append(die5)
        self.cup.append(die6)

    def roll(self):
        roll_result = []
        for die in self.cup:
            roll_result.append(die.roll())
        return roll_result

    #counts how many times each die occurs (for scoring purposes)
    def get_dice_count(self, roll):    
        global count

        count = [0, 0, 0, 0, 0, 0]
        for die in roll:
            if (die == 1):
                count[0] += 1
            elif (die == 2):
                count[1] += 1
            elif (die == 3):
                count[2] += 1
            elif (die == 4):
                count[3] += 1
            elif (die == 5):
                count[4] += 1
            elif (die == 6):
                count[5] += 1
        return count

    #tells the player which dice they can take in order to score    
    def print_score_check(self, count):
        global possible_score_list   

        #check for straight
        if count == [1, 1, 1, 1, 1, 1]:
            print(f"You can take all the dice for 3000 points.")
            possible_score_list.append('straight')

        #check for full house
        if count.count(2) == 1 and count.count(4) == 1:
            print(f"You can take the full house for 1500 points.")
            possible_score_list.append('full_house')

        #check for two triplets
        if count.count(3) == 2:
            print(f"You can take the two triplets for 2500 points.")
            possible_score_list.append('two_triplets')

        #check for six of a kind
        if 6 in count:
            print(f"You can take the 6 {str(count.index(6)+1)}'s for 3000 points.")
            possible_score_list.append('six_of_a_kind')

        #check for five of a kind
        if 5 in count:
            print(f"You can take the 5 {str(count.index(5)+1)}'s for 2000 points.")
            possible_score_list.append('five_of_a_kind')

        #check for four of a kind
        if 4 in count:
            print(f"You can take the 4 {str(count.index(4)+1)}'s for 1000 points")
            possible_score_list.append('four_of_a_kind')
        
        #check for three ones
        if count[0] == 3:
            print(f"You can take the 3 ones for 1000 points.")
            possible_score_list.append('three_ones')

        #check for three of a kind
        if count[1] == 3 or count[2] == 3 or count[3] == 3 or count[4] == 3 or count[5] == 3:
            print(f"You can take the 3 {str(count.index(3)+1)}'s for 500 points.")
            possible_score_list.append('three_of_a_kind')
            
        #check for three pairs
        if count.count(2) == 3:
            print(f"You can take the 3 pairs for 1500 points.")
            possible_score_list.append('three_pairs')
   
        #check for ones
        if count[0] <= 2 and count[0] != 0:
            print(f"You can take the {str(count[0])} 1's for {str(count[0]*100)} points.")
            value = 'ones'
            possible_score_list.extend([value for i in range(count[0])])

        #check for fives
        if count[4] <= 2 and count[4] != 0:
            print(f"You can take the {str(count[4])} fives for {str(count[4]*50)} points.")
            value = 'fives'
            possible_score_list.extend([value for i in range(count[4])])

        if possible_score_list == []:
            possible_score_list.append("Farkle")

        return possible_score_list



game_cup = Cup()


class Player:
    def __init__(self, number, name):
        self.name = name
        self.number = number
        self.score = 0
        self.possible_scores = []
        self.kept_score = []
        self.kept_dice = []

    def get_score_as_str(self):
        return str(self.score)

    def get_name(self):
        return self.name

    #this function removes dice that repeat so socring validity can be checked
    def remove_repeating_dice(self, master_list):
        temp_list = []
        seen = set()
        for die in master_list:
            if die in seen:
                temp_list.append(die)
                seen.add(die)
            else:
                seen.add(die)
        for die in master_list:
            if die in temp_list:
                master_list.remove(die)

    #defining a function to check the dice a player kept and then returning the score based on the dice
    def dice_to_kept_score(self):
        global correct_dice, kind
        correct_dice = False

        

        if 'full_house' in self.possible_scores:
            for die in self.kept_dice:
                if self.kept_dice.count(die) == 4:
                    temp_list = [*set(self.kept_dice)]
                    if len(temp_list) == 2:
                        correct_dice = True
            if correct_dice:
                self.kept_score.append('full_house')
                self.kept_dice.clear()
                correct_dice = False
            

        if 'two_triplets' in self.possible_scores:
            for die in self.kept_dice:
                if self.kept_dice.count(die) == 3:
                    temp_list = [*set(self.kept_dice)]
                    if len(temp_list) == 2:
                        correct_dice = True
            if correct_dice:
                self.kept_score.append('two_triplets')
                self.kept_dice.clear()
                correct_dice = False

        if 'six_of_a_kind' in self.possible_scores:
            for die in self.kept_dice:
                if self.kept_dice.count(die) == 6:
                    correct_dice = True
            if correct_dice:
                self.kept_score.append('six_of_a_kind')
                self.kept_dice.clear()
                correct_dice = False

        if 'five_of_a_kind' in self.possible_scores:
            for die in self.kept_dice:
                if self.kept_dice.count(die) == 5:
                    correct_dice = True
            if correct_dice:
                self.kept_score.append('five_of_a_kind')
                self.remove_repeating_dice(self.kept_dice)
                correct_dice = False

        if 'four_of_a_kind' in self.possible_scores:
            for die in self.kept_dice:
                if self.kept_dice.count(die) == 4:
                    correct_dice = True
            if correct_dice:
                self.kept_score.append('four_of_a_kind')
                self.remove_repeating_dice(self.kept_dice)
                correct_dice = False

        if 'three_of_a_kind' in self.possible_scores:
            for die in self.kept_dice:
                if self.kept_dice.count(die) == 3:
                    correct_dice = True
            if correct_dice:
                self.kept_score.append('three_of_a_kind')
                self.remove_repeating_dice(self.kept_dice)
                correct_dice = False

        if 'three_ones' in self.possible_scores:
            ones_list = []
            for die in self.kept_dice:
                if die == '1':
                    ones_list.append(die)
            if len(ones_list) == 3:
                correct_dice = True
            if correct_dice:
                self.kept_score.append('three_ones')
                correct_dice = False


        if 'three_pairs' in self.possible_scores:
            for die in self.kept_dice:
                if self.kept_dice.count(die) == 2:
                    temp_list = [*set(self.kept_dice)]
                    if len(temp_list) == 3:
                        correct_dice = True
            if correct_dice:
                self.kept_score.append('three_pairs')
                self.kept_dice.clear()
                correct_dice = False

        if 'ones' in self.possible_scores:
            for die in self.kept_dice:
                if die == '1':
                    self.kept_score.append('ones')

        if 'fives' in self.possible_scores:
            for die in self.kept_dice:
                if die == '5':
                    self.kept_score.append('fives')

        if [1, 2, 3, 4, 5, 6] in self.kept_dice and 'straight' in self.possible_scores:
            self.kept_score += 'straight'
            self.kept_dice.clear()

        if 'Farkle' in self.possible_scores:
            self.kept_dice.clear()
            self.kept_score.append('Farkle')

        return self.kept_score




    #this is the master function for running a player's turn
    def turn(self):
        global possible_score_dict, possible_score_list, kind
        print(f"{self.name}, it is your turn")
        print(f"Your score is {self.score}")
        decision = input("Would you like to roll or pass?\n:")
        if decision == "roll":

            #printing the dice for this turn's roll
            print("You rolled the following numbers:")
            turn_roll = game_cup.roll()
            str_turn_roll = []
            str_turn_roll = list_to_string(turn_roll, str_turn_roll)
            for die in str_turn_roll:
                print(die)

            #checking how many of each dice there are in the roll
            dice_count = game_cup.get_dice_count(turn_roll)

            #checking and printing combinations of dice that can score

            if game_cup.print_score_check(dice_count) != "Farkle":
                print("Which dice would you like to take?")
                kept_dice_str = input(":")
                kept_dice_list = list(kept_dice_str)
                self.kept_dice = list_to_num(self.kept_dice, kept_dice_list)
                print(kept_dice_list)

                #adding global possible scores to player possible scores
                self.possible_scores = possible_score_list
                print(self.possible_scores)

                #adding only the scores to kept score based on the dice the player took
                self.dice_to_kept_score()
                print(self.kept_score)

                #adding the kept score to the player's total score
                for score in self.kept_score:
                    if score in possible_score_dict:
                        self.score += possible_score_dict[score]
                    else: self.score += 0

                #reseting player scoring lists for next roll
                self.kept_dice.clear()
                self.kept_score.clear()
                self.possible_scores.clear()
                kind = 0
                print(f"Your new score is {self.score}.")

                #reseting global score list for next roll
                possible_score_list.clear()
                
   




def start_game():
    global winner
    play = True

    winning_points = int(input("How many points do you want to play to?"))
    num_of_players = int(input("How many players are playing today?\n:"))
    player_list = []

    #creates player object for each player requested by user and adds to player list
    for num in range(1,num_of_players +1):
        name = input(f"What is player {num}'s name?\n:")
        player = Player(num, name)
        player_list.append(player)

    while play:
        top_players = []
        for player in player_list:
            player.turn()

        #check if any score has exceeded winning points
        for player in player_list:
            #check for highest score greater than winning points, end game if winning score has been reached
            if player.score > winning_points:
                highest_score = 0
                top_players.append(player)
                for player in top_players:
                    if player.score > highest_score:
                        highest_score = player.score
                        winner = player.name
                        play = False

            else:
                break


    

if __name__ == "__main__":

    start_game()
    print(f"Congratulation {winner}! You win!")