### This is the Yahtzee project. We are going to break it into multiple pieces. ###

# import statements

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

player_names = []

player_names = get_player_names(player_names)



print('here are the players we have: ')
for player_name in player_names:
    print(player_name)

answer = input('do you want to have any more players? If yes, enter y. Press anything else to continue.')
if answer == 'y':
    player_names = get_player_names(player_names)