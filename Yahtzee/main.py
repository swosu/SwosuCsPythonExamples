### This is the Yahtzee project. We are going to break it into multiple pieces. ###

# import statements
import random
import time
from Player import Player

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
print('for this game we will haave the following players: ')

# create the player objects

player_object_list = []

for player_name in player_names:
    my_initial_roll = random.randint(1, 6)
    print('player name: ', player_name, 'initial roll: ', my_initial_roll)
    player_object_list.append(Player(player_name, my_initial_roll))