### This is the Yahtzee project. We are going to break it into multiple pieces. ###

# import statements
import random
import time
from Yahtzee_player import Yahtzee_player

# function definitions

def get_player_names(player_names):
    # get player names
    print('we need to know who is playing. Enter "done" when finished.')
    while True:
        player_name = input('Enter player name (or "done"): ')
        if player_name == 'done':
            break
        player_names.append(player_name)

    return player_names


# beginning of code

print('hello')

# set random seed
random.seed(5)

# set random seed based on the clock
# random.seed(time.time())

player_names = []

while True:
    player_names = get_player_names(player_names)
    print('here are the players we have: ')
    for player_name in player_names:
        print(player_name)

    answer = input('do you want to have any more players? If yes, enter y. Press anything else to continue.')
    if answer == 'y':
        player_names = get_player_names(player_names)
    else:
        break
# print('for this game we will haave the following players: ')

# create the player objects

player_object_list = []

for player_name in player_names:
    my_initial_roll = random.randint(1, 6)
    #print('player name: ', player_name, 'initial roll: ', my_initial_roll)
    player_object_list.append(Yahtzee_player(player_name, my_initial_roll))

# print out the player objects including the names and initial rolls
for player_object in player_object_list:
    print('player name: ', player_object.name, 'initial roll: ', player_object.initial_roll)

# decide who goes first by finding the highest initial roll. Whoever has the last highest role goes first incase of a tie.

highest_initial_roll = 0
player_index = 0
starting_player_index = 0
for player_object in player_object_list:
    player_index += 1
    # for testing, I let this be >, but for production it should be >=
    if player_object.initial_roll >= highest_initial_roll:
        highest_initial_roll = player_object.initial_roll
        initial_player = player_object.name
        starting_player_index = player_index

print('the player who goes first is: ', initial_player, 'with the highest initial roll of: ', highest_initial_roll, 'and they are player number: ', starting_player_index)



sorted_player_object_list = []
number_of_players = len(player_object_list)
for working_index in range(number_of_players):
    sorted_player_object_list.append(player_object_list[(starting_player_index + working_index - 1) % number_of_players])

# print off the player order
print('the player order is: ')
for player_object in sorted_player_object_list:
    print(player_object.name)


