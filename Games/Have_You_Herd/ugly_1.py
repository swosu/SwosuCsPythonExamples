print('good morning and welcome to the first version of this game.')
print('this is called have you herd.')

# link to the game on wikipedia:
# https://en.wikipedia.org/wiki/Animal_Husbandry_(game)

# and here is the github page:
# https://github.com/masak/farm


if __name__ == '__main__':
    print('let us get started.')

    print('we create a dictionary called players')

    # empty dictionary
    player_roster = {}
    player_count = 0;
    more_players_to_add = True
    while(more_players_to_add):
        player_count += 1
        player_name = input('next player, what is your name?: ')
        player_roster[str(player_count)] = player_name
        player_selection = \
        input('Please press 1 if would you like to add more players?: ')
        if(str(1) != player_selection):
            more_players_to_add = False

    # Iterate over key/value pairs in dict and print them
    for key, value in player_roster.items():
        print(key, ' : ', value)
