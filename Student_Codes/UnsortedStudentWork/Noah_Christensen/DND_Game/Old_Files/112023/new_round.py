import random 
from fighting_sequence import main as fighting_sequence
from character_stay import main as character_stay  

game_variables = {
    "selected_road": "",
    "selected_land": "",
    "selected_terrain": "",
}

class Char:
    def __init__(self, name, type, attack, health, gold, in_city=False):
        self.type = type
        self.name = name
        self.attack = attack
        self.health = health
        self.gold = gold
        self.in_city = in_city
    def modify_health(damage):
        Char.health += damage
    def modify_gold(gold_change):
        Char.gold += gold_change

def char_stats():
    print(f"\n{Char.name}'s Type = ",Char.type,)
    print(f"{Char.name}'s Attack = ",Char.attack,)
    print(f"{Char.name}'s Health = ",Char.health,)

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
            character_stay.main()
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
    if game_variables["selected_road"] == "the Guarded City":
        Char.in_city = True
    else:
        Char.in_city = False
def rand_land():
    land = ["a Cave", "a Village", "a Temple"]
    game_variables["selected_land"] = random.choice(land)
    Char.in_city = False
def rand_terr():
    terrain = ["Woods", "Fields", "Desert"]
    game_variables["selected_terrain"] = random.choice(terrain)
    Char.in_city = False
#---------------------------------------------------------------------------------------------------------------------------#






#---------------------------------------------------------------------------------------------------------------------------#


if __name__ == "__main__":
    main()