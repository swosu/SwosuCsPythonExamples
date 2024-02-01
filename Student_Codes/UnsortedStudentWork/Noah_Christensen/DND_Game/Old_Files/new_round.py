import random
import fighting_sequence


game_variables = {
    "selected_road": "",
    "selected_land": "",
    "selected_terrain": "",
    "current_enemy": None
}


#---------------------------------------------------------------------------------------------------------------------------#
# Main Round Functions, loops everytime user ends the round. 
# How the user navigates through the game

def main():
    while True:
        print("What do you want to do?")
        print("1. Go")
        print("2. Stay")
        choice = int(input("Select Option (1/2): "))
        if choice == 1:
            char_go()
        elif choice == 2:
            char_stay()
        else:
            print("Really?  Follow the directions.")
        continue
if __name__ == "__main__":
    main()

#---------------------------------------------------------------------------------------------------------------------------#
# User chooses to go
def char_go():
    while True:
        print("Where would you like to go?")
        print("1. Follow the road.")
        print("2. Go to a nearby landmark.")
        print("3. Journey across the terrain.")
        go_choice = int(input("Select an option (1/2/3): "))
        if go_choice == 1:
            rand_road()
            print(f"You encounter: {game_variables['selected_road']}")
            fighting_sequence.main()
        elif go_choice == 2:
            rand_land()
            print(f"You encounter: {game_variables['selected_land']}")
            fighting_sequence.main()
        elif go_choice == 3:
            rand_terr()
            print(f"You encounter: {game_variables['selected_terrain']}")
            fighting_sequence.main()
        else:
            print("Really? Follow the rules.")
            continue
# Functions that generates places
def rand_road():
    road = ["Abandoned City", "Guarded City", "More Road"]
    game_variables["selected_road"] = random.choice(road)
def rand_land():
    land = ["Cave", "Village", "Temple"]
    game_variables["selected_land"] = random.choice(land)
def rand_terr():
    terrain = ["Woods", "Fields", "Desert"]
    game_variables["selected_terrain"] = random.choice(terrain)
#---------------------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------------------------------------#
# User decides to stay:

def char_stay():
    while True:
        print("Sorry, this still needs to be coded:")
        char_go()
        break