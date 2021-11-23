import pandas as pd

# importing the module
import json

def greet_player():
    player_data = {}
    # Opening JSON file
    with open('player_file.json') as json_file:
        player_data = json.load(json_file)
    #print(player_data)
    print('it is nice to meet you,', player_data['name'])


def no_connection(coin):
    print("\nNo connection found. Go explore the shuttle.")
    answer1 = input("\nYou are currently in the control room. Would you like to explore:\n"
                    "a.The room you are in.\n"
                    "b.The break room.\n"
                    "c.The engine room.\n"
                    "d.Put on space suit and explore the moon.\n")
    return answer1

def wake_up(coin):
    with open('player_file.json') as json_file:
        player_data = json.load(json_file)
    print("You wake up in a space shuttle on the moon with a month's worth oxygen and no fuel to go home.")
    print('Here are your options,', player_data['name'])
    print("a.Check coms to see if theres connection.\nb. Explore shuttle")
    answer = input("What would you like to do?")
    return answer

def say_my_name_and_car():
    player_data = {}
    # Opening JSON file
    with open('player_file.json') as json_file:
        player_data = json.load(json_file)

    print('Hello', player_data['name'])
    print('You drive a', player_data['car'])

if __name__ == '__main__':
    say_my_name_and_car()
