import random

def print_greeting(player_name):
    print(f'Hello, {player_name}.')

def get_initial_player_health():
    player_health = 20
    return player_health

def attack_player(player_health, \
    player_name):
    damage = random.randrange(0,7)
    player_health -= damage
    print(f'{player_name} took {damage} damage and has {player_health} health.')
    return player_health


def print_player_health(player_name, player_health):
    print(f'{player_name} has {player_health} health.')

if __name__ == '__main__':
    #print('Hello, World.')

    # create 2 players
    player_One_Name = 'Zoe'
    player_Two_Name = 'Matt'
    print_greeting(player_One_Name)
    print_greeting(player_Two_Name)

    # give each player some health
    player_One_Health = get_initial_player_health()
    player_Two_Health = get_initial_player_health()

    print_player_health(player_One_Name, player_One_Health)
    print_player_health(player_Two_Name, player_Two_Health)

    keep_playing = True
    round_count = 0
    while(keep_playing):
        round_count += 1
        print(f'Round: {round_count}.')
        # have each player get attacked

        player_One_Health = attack_player(player_One_Health, player_One_Name)
        player_Two_Health = attack_player(player_Two_Health, player_Two_Name)

        if 10 <= round_count:
            keep_playing = False
        elif 0 >= player_One_Health or 0 >= player_Two_Health:
            keep_playing = False
            if player_One_Health > player_Two_Health :
                print(f'{player_One_Name} has won.')
            else:
                print(f'{player_Two_Name} has won.')

    # player with the least health
    #  when one player is defeated loses
