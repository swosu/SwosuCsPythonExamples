import random

#---------------------------------------------------------------------------------------------------------------------------#
# Character class
class Char:
    def __init__(self, name, type, location , attack, health, gold):
        self.name = name
        self.type = type
        self.location = location
        self.attack = attack
        self.health = health
        self.gold = gold
    def modify_health(damage):
        Char.health += damage
    def modify_gold(gold_change):
        Char.gold += gold_change

# Enemy Class
class Enemy:
    def __init__(self, name, type, health, attack):
        self.name = name
        self.type = type
        self.health = health
        self.attack = attack
    def modify_health(self, health_change):
        self.health += health_change

# Location Class
class Location:
    def __init__ (self, name, outsideCity=False):
        self.name = name
        self.outside_city = outsideCity
#---------------------------------------------------------------------------------------------------------------------------#





#---------------------------------------------------------------------------------------------------------------------------#
# Dictionary of Enemies, Roads, Landmarks, and Terrains
# Add Enemies and Bosses here
enemy_dict={
    "Daegon": Enemy("Daegon", "Demon", 40, 4),
    "Centaurith": Enemy("Centaurith", "Beast", 40, 4),
    "Aacalith": Enemy("Aacalith", "Vampire", 30, 3),
    "Zrython": Enemy("Zrython", "Beast", 30, 2),
    "Thraspinox": Enemy("Thraspinox", "Beast", 30, 2),  
    "Umbrafiend": Enemy("Umbrafiend", "Ghoul", 20, 2),      
}

enemy_boss = {
    "Vziathar": Enemy("Vziathar", "God", 100, 8)
}

road_dict = {
    "Abandoned City": Location("Abandoned City", False),
    "Guarded City": Location("Guarded City", True),
    "Road": Location("Road", False),
}

land_dict = {
    "Cave": Location("Cave", False),
    "Village": Location("Village", True),
    "Temple": Location("Temple", False),
}

terrain_dict = {
    "Woods": Location("Woods", False),
    "Fields": Location("Fields", False),
    "Desert": Location("Desert", False),
}

game_variables = {
    "selected_road": None,
    "selected_land": None,
    "selected_terrain": None,
    "current_enemy": None,
}
#---------------------------------------------------------------------------------------------------------------------------#




#---------------------------------------------------------------------------------------------------------------------------#
def char_stats():
    print(f"\n{Char.name}'s Type = ",Char.type,)
    print(f"{Char.name}'s Attack = ",Char.attack,)
    print(f"{Char.name}'s Health = ",Char.health,)

def generate_enemy():
    random_enemy_key = random.choice(list(enemy_dict.keys()))
    game_variables["current_enemy"] = enemy_dict[random_enemy_key]


def current_enemy_check():
    if game_variables["current_enemy"] == None:
        print(" ")
    else:
        print(f"WARNING THERE'S NOT SUPPOSED TO BE AN ENEMY \nCurrent enemy: {game_variables['current_enemy'].name} \n{game_variables['current_enemy'].type} \n{game_variables['current_enemy'].health} \n{game_variables['current_enemy'].attack}")
#---------------------------------------------------------------------------------------------------------------------------#




#---------------------------------------------------------------------------------------------------------------------------#
# Should only run once at the beginning of the game
def game_rules():
    username = input("\nWhat is your name traveler? ")
    Char.name = username
    print(f"Welcome {Char.name} let me tell ya what ya gettin yerself into...\n \nYa'l journey throughout the land fighting monsters,\nFind your way to the Guarded City and explore the city!\nYa can access the city by choosing to stay and explore after defeating the creature that's at the gates of the city.\nYa'l have many adventures, ya'l meet many people, some who might come along, whatever you do,\nDon't work with Demons")
    print("---------------------------------------------------------------------------------------------------------------------------")

def class_selection():
    print(f"\nWell hello, {Char.name}, what kind of traveler are ya??")
    
    print("\n1. Knight\n    As a guardian of the land, ya must be on a quest from the king.\nSuch a noble life, ya'l most likely have cheaper rates through ya journey\nAlthough watch out for those who don't want you up in their business.")
    print("Here are the statistics for the Knight:")
    print("- Health: 100\n- Attack: +3")
    
    print("\n2. Elf\n    As an elf ya grew up on the outskirts of civilization.  Outcasted by society, set on revenge.\nElves aren't respected in cities, watch yer back.")
    print("    Elves are naturally gifted in the spiritual world.  They're the only class to be able to wield magic and enchanted weapons.")
    print("Here are the statistics for the Elf:")
    print("- Health: 80\n- Attack: +1")
    
    print("\n3. Viking\n    As pillagers of the sea, yer known to use anything to take what they please.")
    print("Here are the statistics for the Viking:")
    print("-- Health: 100\n- Attack: +4")
    
    print("\n4. Dwarf\n    Ya'v spend most of ya life underground, were ya working or hiding from the world?")
    print("Here are the statistics for the Dwarf:")
    print("- Health: 100\n- Attack: +3")
    
    print("\n5. Assassin\n    Hired by some rich fella, ya must be on a journey across the land, fulfilling a contract.")
    print("Here are the statistics for the Assassin:")
    print("- Health: 100\n- Attack: +2")
    
    print("\n6. Archer\n    Are ya hunting a monster or your next meal?")
    print("Here are the statistics for the Archer:")
    print("- Health: 100\n- Attack: +2")

    class_selection_num = int(input("\nPlease select your class (1-6): "))

    if class_selection_num == 1:
        Char.type = "Knight"
        Char.attack = 3
        Char.health = 100
        Char.gold = 20
    
    elif class_selection_num == 2:
        Char.type = "Elf"
        Char.attack = 1
        Char.health = 80
        Char.gold = 20
    
    elif class_selection_num == 3:
        Char.type = "Viking"
        Char.attack = 4
        Char.health = 100
        Char.gold = 20

    elif class_selection_num == 4:
        Char.type = "Dwarf"
        Char.attack = 3
        Char.health = 100
        Char.gold = 20

    elif class_selection_num == 5:
        Char.type = "Assassin"
        Char.attack = 2
        Char.health = 100
        Char.gold = 20
    
    elif class_selection_num == 6:
        Char.type = "Archer"
        Char.attack = 2
        Char.health = 100
        Char.gold = 20

    else:
        print("\nINVALID INPUT WE NOW HAVE YER MEDICAL RECORDS\n")
        class_selection()
#---------------------------------------------------------------------------------------------------------------------------#

  


#---------------------------------------------------------------------------------------------------------------------------#
# User decides to go
def char_go():
    Char.location = "onJourney"
    print("\nWhere would you like to go?")
    print("1. Follow the road.")
    print("2. Go to a nearby landmark.")
    print("3. Journey across the terrain.")
    go_choice = int(input("Select an option (1/2/3): "))
    if go_choice == 1:
        rand_road()
        print(f"\nYer at {game_variables['selected_road']}")
        if game_variables["selected_road"] == "Guarded City":
            Char.location = "outsideCity"
            enemy_encounter()
        else:
            enemy_encounter()
    elif go_choice == 2:
        rand_land()
        print(f"\nYer at {game_variables['selected_land']}")
        enemy_encounter()
    elif go_choice == 3:
        rand_terr()
        print(f"\nYer in the {game_variables['selected_terrain']}")
        enemy_encounter()
    else:
        print("\nINVALID INPUT WE NOW HAVE YER SSN\n")
        char_go()     
#---------------------------------------------------------------------------------------------------------------------------#




#---------------------------------------------------------------------------------------------------------------------------#
# Functions that generates places
# Add roads, landmarks, and terrains here:
def rand_road():
    road = random.choice(list(road_dict.keys()))
    game_variables["selected_road"] = road

def rand_land():
    land = random.choice(list(land_dict.keys()))
    game_variables["selected_land"] = land

def rand_terr():
    terrain = random.choice(list(terrain_dict.keys()))
    game_variables["selected_terrain"] = terrain
#---------------------------------------------------------------------------------------------------------------------------#




#---------------------------------------------------------------------------------------------------------------------------#
# User Chooses to Stay
def char_stay():
    print("\nWhat would you like to do?")
    print("1. Rest")
    print("2. Explore")
    stay_choice = int(input("Select an option (1/2): "))

    if stay_choice == 1:
        char_rest()
    elif stay_choice == 2:
        char_explore()
    else:
        print("\nINVALID INPUT WE NOW HAVE YER ADDRESS\n")
        char_stay()

def char_rest():
    Char.health += 10
    print(f"\nYou have rested. Your health is now {Char.health}.")

def char_explore():
    if Char.location == "inCity":
        print("\nWhat would you like to do?")
        print("1. Go to the Tavern")
        print("2. Go to the Keep")
        print("3. Go to the Temple")
        print("4. Go to the Witch")
        explore_choice = int(input("Select an option (1/2/3/4): "))
        if explore_choice == 1:
            print("\nYou go to the Tavern.")
            explore_tavern()
            Char.location = "onJourney"
        elif explore_choice == 2:
            print("\nYou go to the Keep.")
            explore_keep()
            Char.location = "onJourney"
        elif explore_choice == 3:
            print("\nYou go to the Temple.")
            explore_temple()
            Char.location = "onJourney"
        elif explore_choice == 4:
            print("\nYou go to the Witch.")
            explore_witch()
            Char.location = "onJourney"
        else:
            print("\nINVALID INPUT WE NOW HAVE YER MEDICAL RECORDS\n")
            Char.location = "onJourney"
            char_explore()
    else:
        print("\nYou are not in a city.")
#---------------------------------------------------------------------------------------------------------------------------#




#---------------------------------------------------------------------------------------------------------------------------#
# Exploring the City Functions:
# Tavern: Talk to bartender for a drink, or talk to the drunk (I need to add that the drunk can give you a quest)
def explore_tavern():
    print("\nYou enter the Tavern.")
    print("What would you like to do?")
    print("1. Talk to the Bartender")
    print("2. Talk to the Drunk")
    print("3. Leave")
    tavern_choice = int(input("Select an option (1/2/3/4): "))
    if tavern_choice == 1:
        print("\nYou talk to the Bartender.")
        print("Bartender: Welcome to the Tavern! What can I get you?")
        print("1. Ale")
        print("2. Water")
        print("3. Leave")
        bartender_choice = int(input("Select an option (1/2/3): "))
        if bartender_choice == 1:
            print("\nYou order an ale.")
            print("Bartender: That'll be 5 gold.")
            print("You pay the Bartender 5 gold.")
            Char.modify_gold(-5)
            print("You have: ", Char.gold, "gold.")
            print("Bartender: Here you go.")
            print("You drink the ale.")
            print("You feel refreshed.")
            Char.modify_health(10)
            print(f"Your health is now {Char.health}.")
        elif bartender_choice == 2:
            print("\nYou order some water.")
            print("Bartender: That'll be 2 gold.")
            print("You pay the Bartender 2 gold.")
            Char.modify_gold(-2)
            print("You have: ", Char.gold, "gold.")
            print("Bartender: Here you go.")
            print("You drink the water.")
            print("You feel refreshed.")
            Char.modify_health(10)
            print(f"Your health is now {Char.health}.")
        elif bartender_choice == 3:
            print("\nYou leave the Tavern.")
        else:
            print("\nINVALID INPUT WE NOW HAVE YER BANK ACCOUNT INFO\n")
            explore_tavern()
    elif tavern_choice == 2:
        print("\nYou talk to the Drunk.")
        print("Drunk: Hic! I'm drunk!")
        print("You leave the Drunk.")
    elif tavern_choice == 3:
        print("\nYou leave the Tavern.")




# Keep: Talk to the King for a quest
def explore_keep():
    if Char.type == "Knight":
        print("\nYou enter the Keep.")
        print("King: Welcome Knight!  Stay a while.")
        maybe_gold()
    elif Char.type == "Elf":
        print("\nYou enter the Keep.")
        print("King: GET THAT CREATURE OUT OF HERE!")
    elif Char.type == "Viking":
        print("\nYou enter the Keep.")
        print("King: What do you want?")
        maybe_gold()
    elif Char.type == "Dwarf":
        print("\nYou Enter the Keep.")
        print("King: Welcome.")
        maybe_gold()
    elif Char.type == "Assassin":
        print("\nYou enter the Keep.")
        print("King: What do you want?")
        maybe_gold()
    elif Char.type == "Archer":
        print("\nYou enter the Keep.")
        print("King: Welcome, what can we do for you?")
        maybe_gold()


def maybe_gold():
    rand_num = random.randint(1, 10)
    if rand_num == 1 or rand_num == 3 or rand_num == 7:
        print("\nKing: Thank you for your service.  Here is some gold.")
        Char.modify_gold(10)
        print("You have: ", Char.gold, "gold.")
    else:
        print("\nKing: Thank you for your service.")




# Temple: Talk to the Priest to pray or repent
def explore_temple():
    print("\nYou enter the Temple.")
    print("Priest: What would you like to do?")
    print("1. Pray")
    print("2. Repent")
    print("3. Leave")
    temple_choice = int(input("Select an option (1/2/3): "))
    if temple_choice == 1:
        print("\nYou pray.")
        print("Priest: May the Gods be with you.")
        print("You feel refreshed.")
        Char.modify_health(10)
        print(f"Your health is now {Char.health}.")
    elif temple_choice == 2:
        print("\nYou repent.")
        print("Priest: May the Gods be with you.")
        print("You feel refreshed.")
        Char.modify_health(10)
        print(f"Your health is now {Char.health}.")
    elif temple_choice == 3:
        print("\nYou leave the Temple.")
    else:
        print("\nINVALID INPUT WE NOW HAVE YER BANK ACCOUNT INFO\n")
        explore_temple()




# Witch: Talk to the Witch for a fortune or a curse
def explore_witch():
    print("\nYou enter the Witch's Hut.")
    print("Witch: Take a seat.")
    input("Press enter to continue.")
    gift_or_curse = random.randint(1, 2)
    if gift_or_curse == 1:
        print("\nWitch: I will give you a gift.")
        print("You feel refreshed.")
        Char.modify_health(10)
        print(f"Your health is now {Char.health}.")
    elif gift_or_curse == 2:
        print("\nWitch: I will curse you.")
        print("You feel cursed.")
        Char.modify_health(-10)
        print(f"Your health is now {Char.health}.")
    else:
        print("\nINVALID INPUT WE NOW HAVE YER BANK ACCOUNT INFO\n")
        explore_witch()
#---------------------------------------------------------------------------------------------------------------------------#



#---------------------------------------------------------------------------------------------------------------------------#
# Basic Fighting Sequence:
# Main fighting Function, triggers when the user enters a new location
def enemy_encounter():
    generate_enemy()
    print(f"\nYou've encountered {game_variables['current_enemy'].name}!")
    fight_or_flee = int(input("1. Fight\n2. Flee\n"))
    if fight_or_flee == 1:
        fight_sequence()
    elif fight_or_flee == 2:
        print("You fled!")
        game_variables["current_enemy"] = None
    else:
        print("\nINVALID INPUT WE NOW HAVE YER BANK ACCOUNT INFO\n")
        fight_sequence()

# Fight sequence, triggers when the user chooses to fight
def fight_sequence():
    while game_variables["current_enemy"].health > 0 and Char.health > 0:
        print(f"\n{game_variables['current_enemy'].name}'s stats:\nHealth: {game_variables['current_enemy'].health}\nAttack: {game_variables['current_enemy'].attack}")
        print(f"\n{Char.type}'s stats:\nHealth: {Char.health}\nAttack: {Char.attack}")
        roll_result()
        print(f"\nYour health is {Char.health}")
        print(f"The enemy's health is {game_variables['current_enemy'].health}\n")
        print("---------------------------------------------------------------------------------------------------------------------------")
    if game_variables["current_enemy"].health <= 0:
        print(f"\n\nYou have defeated {game_variables['current_enemy'].name}!\n\n")
        game_variables["current_enemy"] = None
        if Char.location == "outsideCity":
            Char.location = "inCity"
            print("\nYou are in a city.")
        else:
            print("\nYou are not in a city.")
    elif Char.health <= 0:
        print("\n\nYou have died!\n\n")
        game_variables["current_enemy"] = None
        main()
#---------------------------------------------------------------------------------------------------------------------------#




#---------------------------------------------------------------------------------------------------------------------------#
# Roll Result is the result of two functions: char_roll, enemy_roll
# Both Char and Enemy roll a d20, then add their attack stat to the roll, then establishes the difference between the two rolls
def roll_result():
    char_roll_result = char_roll()
    enemy_roll_result = enemy_roll()
    roll_difference = char_roll_result - enemy_roll_result
    if roll_difference > 0:
        print(f"\nYou dealt {roll_difference} damage!")
        game_variables["current_enemy"].modify_health(-roll_difference)
    elif roll_difference < 0:
        print(f"\nThe enemy dealt {-roll_difference} damage!")
        Char.modify_health( roll_difference)
    else:
        print("\nYou both missed!")
def char_roll():
    input("Press enter to roll ")
    char_roll_result = random.randint(1, 20)
    print(f"\nYou roll a {char_roll_result}")
    char_attack = Char.attack + char_roll_result
    print(f"Your attack this round is {char_attack}")
    return char_attack
def enemy_roll():
    enemy_roll_result = random.randint(1, 20)
    print(f"\nThe enemy rolls a {enemy_roll_result}")
    enemy_attack = game_variables["current_enemy"].attack + enemy_roll_result
    print(f"The enemy's attack this round is {enemy_attack}")
    return enemy_attack
#---------------------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------------------------------------#
# Main Round Functions, loops everytime user ends the round. 
# How the user navigates through the game
# Loops until user dies
def new_round():
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
# Loops everytime a user dies
def main():
    game_rules()
    class_selection()
    char_stats()
    new_round()

if __name__ == "__main__":
    main()
#---------------------------------------------------------------------------------------------------------------------------#
