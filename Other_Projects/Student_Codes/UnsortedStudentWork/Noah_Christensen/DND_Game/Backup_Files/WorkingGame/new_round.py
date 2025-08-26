import random
import fighting_sequence

game_variables = {
    "selected_road": "",
    "selected_land": "",
    "selected_terrain": "",
}


#---------------------------------------------------------------------------------------------------------------------------#
# Main Round Functions, loops everytime user ends the round. 
# How the user navigates through the game
# Loops until user dies
def main():
    while True:
        print("\nWhat do you want to do?")
        print("1. Go")
        print("2. Stay")
        choice = int(input("Select Option (1/2): "))
        if choice == 1:
            char_go()
        elif choice == 2:
            char_stay()
        else:
            print("\nINVALID INPUT WE NOW HAVE YER CREDIT CARD NUMBER\n")
        continue
#---------------------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------------------------------------#
# User chooses to go
def char_go():
    print("\nWhere would you like to go?")
    print("1. Follow the road.")
    print("2. Go to a nearby landmark.")
    print("3. Journey across the terrain.")
    go_choice = int(input("Select an option (1/2/3): "))
    if go_choice == 1:
        rand_road()
        print(f"\nYer at {game_variables['selected_road']}")
        fighting_sequence.main()
    elif go_choice == 2:
        rand_land()
        print(f"\nYer at {game_variables['selected_land']}")
        fighting_sequence.main()
    elif go_choice == 3:
        rand_terr()
        print(f"\nYer in the {game_variables['selected_terrain']}")
        fighting_sequence.main()
    else:
        print("\nINVALID INPUT WE NOW HAVE YER SSN\n")
        char_go()     
#---------------------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------------------------------------#
# Functions that generates places
# Add roads, landmarks, and terrains here:
def rand_road():
    road = ["an Abandoned City", "the Guarded City", "more Road"]
    game_variables["selected_road"] = random.choice(road)
def rand_land():
    land = ["a Cave", "a Village", "a Temple"]
    game_variables["selected_land"] = random.choice(land)
def rand_terr():
    terrain = ["Woods", "Fields", "Desert"]
    game_variables["selected_terrain"] = random.choice(terrain)
#---------------------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------------------------------------#
# User chooses to stay
def char_stay():
    print("You decide to stay.")
    print("You rest for the night.")
    print("You wake up.")
    print("You decide to go.")
    char_go()
#---------------------------------------------------------------------------------------------------------------------------#

if __name__ == "__main__":
    main()