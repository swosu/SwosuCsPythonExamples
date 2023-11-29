import random

# generate 4 random player names
player_names = ['player1', 'player2', 'player3', 'player4']

# have all players roll a six sided die.
# the player with the lowest score goes first
# if there is a tie, the players with the lowest score roll again
# if there is a tie again, the players with the lowest score roll again
player_roll = [random.randint(1,6) for i in range(4)]
print(player_roll)
