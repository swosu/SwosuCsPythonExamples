import random

#---------------------------------------------------------------------------------------------------------------------------#
# This is how the code is organized in this file:

# Add enemies, lands, roads, and terrains in the dictionaries below
# - Classes:
#    - Character
#    - Enemy
#    - Companion
#    - Item
#    - Location
#    - Game

# - Dictionaries:
#    - Character Type
#    - Enemy Type
#    - Item Type
#    - Location Type
#    - Road Type
#    - Landmark Type

# Character Functions:
# - Character Stats

# Companion functions:
# - Companion Stats
# - Generate Companion Sequence
# - Maybe Companion
# - Generate Companion

# Basic Attack Functions:
# Change from a d20 to a d6
# - Roll Result
# - Char Roll
# - Enemy Roll

# Enemy functions:
# - Generate Enemy
# - Enemy Stats
# - Enemy Encounter
# - Fighting Sequence

# Generate Places Functions:
# - Random Road
# - Random Landmark
# - Random Terrain

# Functions that run when the user chooses to explore:
# - Explore Tavern
#    - Potential of finding a companion
# - Explore Keep
# - Explore Temple
# - Explore Witch

# User Stay Functions:
# - Character Stay
# - Character Rest
# - Character Explore

# Main round functions:
# - Character Go
# - New Round

# New Game Functions:
# These run once at the beginning of the game
# - Game Rules
# - Class Selection
# - Main
#---------------------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------------------------------------#
# Character class
class Character:
    def __init__(self, name, type, location , attack, health, gold, has_companion=False):
        self.name = name
        self.type = type
        self.location = location
        self.attack = attack
        self.health = health
        self.gold = gold
        self.has_companion = has_companion
    def modify_health(damage):
        Character.health += damage
    def modify_gold(gold_change):
        Character.gold += gold_change

# Enemy Class
class Enemy:
    def __init__(self, name, type, health, attack):
        self.name = name
        self.type = type
        self.health = health
        self.attack = attack
    def modify_health(self, health_change):
        self.health += health_change

# Companion Class
class Companion:
    def __init__(self, name, type, health, attack, with_player=False):
        self.name = name
        self.type = type
        self.health = health
        self.attack = attack
        self.with_player = with_player
    def modify_health(damage):
        Companion.health += damage

# Item Class, store means where the users stores the item (specific spot on their body, or in their bag)
class Item:
    def __init__(self, name, type, store, value):
        self.name = name
        self.type = type
        self.store = store
        self.value = value

# Location Class
class Location:
    def __init__ (self, name, outsideCity=False):
        self.name = name
        self.outside_city = outsideCity

#Game Class
class Game:
    def __init__ (self):
        self.player = None
        self.selected_road = None
        self.selected_land = None
        self.selected_terrain = None
        self.current_enemy = None
        self.companion = None
#---------------------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------------------------------------#
# Dictionary of Enemies, Roads, Landmarks, and Terrains
# Character Type dictionary
character_type_dict = {
    "Knight": Companion("Prince Arthur", "Knight", 3, 100),
    "Elf": Companion("Faedra", "Elf", 1, 80),
    "Viking": Companion("Sven", "Viking", 4, 100),
    "Dwarf": Companion("Gunnar", "Dwarf", 3, 100),
    "Assassin": Companion("Naelis", "Assassin", 2, 100),
    "Archer": Companion("Vaeril", "Archer", 2, 100),
}

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
    "More Road": Location("More Road", False),
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

item_dict = {
    "Sword": Item("Sword", "Weapon", "Belt", 10),
    "Bow": Item("Bow", "Weapon", "Back", 10),
    "Dagger": Item("Dagger", "Weapon", "Belt", 10),
    "Axe": Item("Axe", "Weapon", "Belt", 10),
    "Staff": Item("Staff", "Weapon", "Hand", 10),
    "Potion": Item("Potion", "Healing", "Bag", 10),
}
#---------------------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------------------------------------#
# Basic Attack Functions:
def roll_result():
    char_roll_result = char_roll()
    enemy_roll_result = enemy_roll()
    roll_difference = char_roll_result - enemy_roll_result
    if roll_difference > 0:
        print(f"\nYou dealt {roll_difference} damage!")
        Game.current_enemy.modify_health(-roll_difference)
    elif roll_difference < 0:
        print(f"\nThe enemy dealt {-roll_difference} damage!")
        Character.modify_health( roll_difference)
    else:
        print("\nYou both missed!")
def char_roll():
    input("Press enter to roll ")
    char_roll_result = random.randint(1, 20)
    print(f"\nYou roll a {char_roll_result}")
    char_attack = Character.attack + char_roll_result
    print(f"Your attack this round is {char_attack}")
    return char_attack
def enemy_roll():
    enemy_roll_result = random.randint(1, 20)
    print(f"\nThe enemy rolls a {enemy_roll_result}")
    enemy_attack = Game.current_enemy.attack + enemy_roll_result
    print(f"The enemy's attack this round is {enemy_attack}")
    return enemy_attack
#---------------------------------------------------------------------------------------------------------------------------#



#---------------------------------------------------------------------------------------------------------------------------#
# Character Functions:
def char_stats():
    print(f"\n{Character.name}'s Type = ",Character.type,)
    print(f"{Character.name}'s Attack = ",Character.attack,)
    print(f"{Character.name}'s Health = ",Character.health,)
    print(f"{Character.name}'s Gold = ",Character.gold,)


# Companion functions:
def companion_stats():
    print(f"\n{Companion.name}'s Type = ",Companion.type,)
    print(f"{Companion.name}'s Attack = ",Companion.attack,)
    print(f"{Companion.name}'s Health = ",Companion.health,)

def maybe_companion():
    rand_num = random.randint(1, 10)
    if rand_num == 5:
        generate_companion_sequence()
    else:
        print("\n They didn't want to talk to you.")

def generate_companion_sequence():
    print("\nYou found a companion!")
    
    print("Would you like to take this companion with you?")
    companion_choice = int(input("1. Yes\n2. No\n"))
    if companion_choice == 1:
        Companion.with_player = True
        print(f"\nYou have taken {Companion.name} with you.")
        companion_stats()
    elif companion_choice == 2:
        print("\nYou left the companion.")
    else:
        print("\nINVALID INPUT WE NOW HAVE YER BANK ACCOUNT INFO\n")
        generate_companion_sequence()

def generate_companion():
    random_companion_key = random.choice(list(character_type_dict.keys()))
    Game.companion = character_type_dict[random_companion_key]


#Enemy functions:
def generate_enemy():
    random_enemy_key = random.choice(list(enemy_dict.keys()))
    Game.current_enemy = enemy_dict[random_enemy_key]

def enemy_stats():
    print(f"\n{Game.current_enemy.name}'s Type = ",Game.current_enemy.type,)
    print(f"{Game.current_enemy.name}'s Attack = ",Game.current_enemy.attack,)
    print(f"{Game.current_enemy.name}'s Health = ",Game.current_enemy.health,)
    print("- - - - - - - - - - - - - - - -")


def enemy_encounter():
    generate_enemy()
    print(f"\nYou've encountered {Game.current_enemy.name}!")
    enemy_stats()
    fight_or_flee = int(input("1. Fight\n2. Flee\n"))
    if fight_or_flee == 1:
        fight_sequence()
    elif fight_or_flee == 2:
        print("You fled!")
        Game.current_enemy = None
    else:
        print("\nINVALID INPUT WE NOW HAVE YER BANK ACCOUNT INFO\n")
        fight_sequence()

# Fight sequence, triggers when the user chooses to fight
def fight_sequence():
    while Game.current_enemy.health > 0 and Character.health > 0:
        print(f"\n{Game.current_enemy.name}'s Health: {Game.current_enemy.health}\n{Game.current_enemy.name}'s Attack: {Game.current_enemy.attack}")
        print(f"\n{Character.name}'s Health: {Character.health}\n{Character.name}'s Attack: {Character.attack}")
        roll_result()
        print("---------------------------------------------------------------------------------------------------------------------------")
    if Game.current_enemy.health <= 0:
        print(f"\n\nYou have defeated {Game.current_enemy.name}!\n\n")
        Game.current_enemy = None
        if Character.location == "outside_City":
            Character.location = "in_City"
            print("\nYou are in a city.")
        else:
            print("\nYou are not in a city.")
    elif Character.health <= 0:
        print("\n\nYou have died!\n\n")
        Game.current_enemy = None
        main()
#---------------------------------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------------------------------#
# Functions that generates places
# Add roads, landmarks, and terrains here:
def rand_road():
    road = random.choice(list(road_dict.keys()))
    Game.selected_road = road
def rand_land():
    land = random.choice(list(land_dict.keys()))
    Game.selected_land = land
def rand_terr():
    terrain = random.choice(list(terrain_dict.keys()))
    Game.selected_terrain = terrain
#---------------------------------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------------------------------#
# User Stay -> Explore Functions:
# Exploring the City Functions:
# Tavern: Talk to bartender for a drink, or talk to the drunk (I need to add that the drunk can give you a quest)
def explore_tavern():
    print("\nYou enter the Tavern.\nWhat would you like to do?\n1. Talk to the Bartender\n2. Talk to the Drunk\n3. Talk to a stranger\n4. Leave")
    tavern_choice = int(input("Select an option (1/2/3/4): "))
    if tavern_choice == 1:
        print("\nYou talk to the Bartender.\nBartender: Welcome to the Tavern! What can I get you?\n1. Ale (5 Gold)\n2. Water (2 Gold)\n3. Leave")
        bartender_choice = int(input("Select an option (1/2/3): "))
        if bartender_choice == 1:
            print("\nYou order an ale.\nBartender: That'll be 5 gold.")
            Character.modify_gold(-5)
            print("You have: ", Character.gold, "gold.")
            print("Bartender: Here you go.\nYou feel refreshed.")
            if Character.health <= 90:
                Character.modify_health(10)
                print(f"Your health is now {Character.health}.")
            elif Character.health > 90:
                Character.health = 100
                print(f"Your health is now {Character.health}.")
        elif bartender_choice == 2:
            print("\nYou order some water.\nBartender: That'll be 2 gold.")
            Character.modify_gold(-2)
            print("You have: ", Character.gold, "gold.")
            print("Bartender: Here you go.\nYou feel refreshed.")
            if Character.health <= 90:
                Character.modify_health(10)
                print(f"Your health is now {Character.health}.")
            elif Character.health > 90:
                Character.health = 100
                print(f"Your health is now {Character.health}.")
        elif bartender_choice == 3:
            print("\nYou leave the Tavern.")
        else:
            print("\nINVALID INPUT WE NOW HAVE YER BANK ACCOUNT INFO\n")
            explore_tavern()
    elif tavern_choice == 2:
        print("\nYou talk to the Drunk.")
        print("Drunk: GET OUT OF MY FACE!")
        print("He punches you in the face and you lose 10 health.")
        Character.modify_health(-10)
    elif tavern_choice == 3:
        maybe_companion()
    elif tavern_choice == 4:
        print("\nYou leave the Tavern.")

# Keep: Talk to the King for a quest
def explore_keep():
    if Character.type == "Knight":
        print("\nYou enter the Keep.")
        print("King: Welcome Knight!  Stay a while.")
        maybe_gold()
    elif Character.type == "Elf":
        print("\nYou enter the Keep.")
        print("King: GET THAT CREATURE OUT OF HERE!")
    elif Character.type == "Viking":
        print("\nYou enter the Keep.")
        print("King: What do you want?")
        maybe_gold()
    elif Character.type == "Dwarf":
        print("\nYou Enter the Keep.")
        print("King: Welcome.")
        maybe_gold()
    elif Character.type == "Assassin":
        print("\nYou enter the Keep.")
        print("King: What do you want?")
        maybe_gold()
    elif Character.type == "Archer":
        print("\nYou enter the Keep.")
        print("King: Welcome, what can we do for you?")
        maybe_gold()
def maybe_gold():
    rand_num = random.randint(1, 10)
    if rand_num == 1 or rand_num == 3 or rand_num == 7:
        gold_amount = random.randint(1, 20)
        print(f"\nKing: Thank you for your service.  Here is {gold_amount} gold.")
        Character.modify_gold(gold_amount)
        print("You have: ", Character.gold, "gold.")
    else:
        print("\nKing: Get lost.")

# Temple: Talk to the Priest to pray or repent
def explore_temple():
    print("\nYou enter the Temple.\nPriest: What would you like to do?\n1. Pray\n2. Repent\n3. Leave")
    temple_choice = int(input("Select an option (1/2/3): "))
    if temple_choice == 1:
        print("\nYou pray.")
        if Character.health <= 96:
            holy_heal = random.randint(1, 4)
            print(f"You feel refreshed.  Your health is now {Character.health + holy_heal}.")
        else:
            print("Priest: May the Gods be with you.")

    elif temple_choice == 2:
        print("\nYou repent.")
        print("Priest: May the Gods be with you.")
    elif temple_choice == 3:
        print("\nYou leave the Temple.")
    else:
        print("\nINVALID INPUT WE NOW HAVE YER BANK ACCOUNT INFO\n")
        explore_temple()

# Witch: Talk to the Witch for a fortune or a curse
def explore_witch():
    print("\nYou enter the Witch's Hut.\nWitch: Don't be scared.")
    input("Press enter to continue.")
    gift_or_curse = random.randint(1, 2)
    if gift_or_curse == 1:
        if Character.health <= 85:
            print("\nWitch: The Gods smile upon you.")
            gift_amount = random.randint(1, 15)
            Character.modify_health(gift_amount)
            print(f"Your health is now {Character.health}.")
        else:
            print("\nWitch: The Gods smile upon you.")
            Character.health = 100
            print(f"Your health is now {Character.health}.")
    elif gift_or_curse == 2:
        print("\nWitch: The Gods don't favor you.")
        print("You feel cursed.")
        Character.modify_health(-10)
        print(f"Your health is now {Character.health}.")
    else:
        print("\nINVALID INPUT WE NOW HAVE YER BANK ACCOUNT INFO\n")
        explore_witch()
#---------------------------------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------------------------------#
# User Stay Functions:
def char_stay():
    print("\nWhat would you like to do?")
    print("1. Rest")
    print("2. Explore City")
    stay_choice = int(input("Select an option (1/2): "))

    if stay_choice == 1:
        char_rest()
    elif stay_choice == 2:
        char_explore()
    else:
        print("\nINVALID INPUT WE NOW HAVE YER ADDRESS\n")
        char_stay()

def char_rest():
    Character.health += 10
    print(f"\nYou have rested. Your health is now {Character.health}.")

def char_explore():
    if Character.location == "in_City":
        print("\nWhat would you like to do?")
        print("1. Go to the Tavern")
        print("2. Go to the Keep")
        print("3. Go to the Temple")
        print("4. Go to the Witch")
        explore_choice = int(input("Select an option (1/2/3/4): "))
        if explore_choice == 1:
            print("\nYou go to the Tavern.")
            explore_tavern()
            Character.location = "onJourney"
        elif explore_choice == 2:
            print("\nYou go to the Keep.")
            explore_keep()
            Character.location = "onJourney"
        elif explore_choice == 3:
            print("\nYou go to the Temple.")
            explore_temple()
            Character.location = "onJourney"
        elif explore_choice == 4:
            print("\nYou go to the Witch.")
            explore_witch()
            Character.location = "onJourney"
        else:
            print("\nINVALID INPUT WE NOW HAVE YER MEDICAL RECORDS\n")
            Character.location = "onJourney"
            char_explore()
    else:
        print("\nYou are not in a city.")
#---------------------------------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------------------------------#
# Main round functions:
def char_go():
    Character.location = "on_Journey"
    print("\nWhere would you like to go?")
    print("1. Follow the road.")
    print("2. Go to a nearby landmark.")
    print("3. Journey across the terrain.")
    go_choice = int(input("Select an option (1/2/3): "))
    if go_choice == 1:
        rand_road()
        print(f"\nYer at {Game.selected_road}")
        if Game.selected_road == "Guarded City":
            Character.location = "outside_City"
            enemy_encounter()
        else:
            enemy_encounter()
    elif go_choice == 2:
        rand_land()
        print(f"\nYer at {Game.selected_land}")
        enemy_encounter()
    elif go_choice == 3:
        rand_terr()
        print(f"\nYer in the {Game.selected_terrain}")
        enemy_encounter()
    else:
        print("\nINVALID INPUT WE NOW HAVE YER SSN\n")
        char_go() 

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
# New Game Functions:
def game_rules():
    username = input("\nWhat is yer name traveler? ")
    Character.name = username
    print(f"Welcome {Character.name} let me tell ya what ya gettin yerself into...\n \nYa'l journey throughout the land fighting monsters,\nFind your way to the Guarded City and explore the city!\nYa can access the city by choosing to stay and explore after defeating the creature that's at the gates of the city.\nYa'l have many adventures, ya'l meet many people, some who might come along, whatever you do,\nDon't work with Demons")
    print("---------------------------------------------------------------------------------------------------------------------------")

def class_selection():
    print(f"\nWell hello, {Character.name}, what kind of traveler are ya??")
    
    print("\n1. Knight\n    As a guardian of the land, ya must be on a quest from the king.\nSuch a noble life, ya'l most likely have cheaper rates through ya journey\nAlthough watch out for those who don't want you up in their business.")
    print("Here are the statistics for the Knight:")
    print("- Health: 100\n- Attack: +3\nGold: +20")
    
    print("\n2. Elf\n    As an elf ya grew up on the outskirts of civilization.  Outcasted by society, set on revenge.\nElves aren't respected in cities, watch yer back.")
    print("    Elves are naturally gifted in the spiritual world.  They're the only class to be able to wield magic and enchanted weapons.")
    print("Here are the statistics for the Elf:")
    print("- Health: 80\n- Attack: +1\nGold: +10")
    
    print("\n3. Viking\n    As pillagers of the sea, yer known to use anything to take what they please.")
    print("Here are the statistics for the Viking:")
    print("-- Health: 100\n- Attack: +4\nGold: +30")
    
    print("\n4. Dwarf\n    Ya'v spend most of ya life underground, were ya working or hiding from the world?")
    print("Here are the statistics for the Dwarf:")
    print("- Health: 100\n- Attack: +3\nGold: +40")
    
    print("\n5. Assassin\n    Hired by some rich fella, ya must be on a journey across the land, fulfilling a contract.")
    print("Here are the statistics for the Assassin:")
    print("- Health: 100\n- Attack: +2\nGold: +30")
    
    print("\n6. Archer\n    Are ya hunting a monster or your next meal?")
    print("Here are the statistics for the Archer:")
    print("- Health: 100\n- Attack: +2\nGold: +20")

    class_selection_num = int(input("\nPlease select your class (1-6): "))

    if class_selection_num == 1:
        Character.type = "Knight"
        Character.attack = 3
        Character.health = 100
        Character.gold = 20   
    elif class_selection_num == 2:
        Character.type = "Elf"
        Character.attack = 1
        Character.health = 80
        Character.gold = 10   
    elif class_selection_num == 3:
        Character.type = "Viking"
        Character.attack = 4
        Character.health = 100
        Character.gold = 30
    elif class_selection_num == 4:
        Character.type = "Dwarf"
        Character.attack = 3
        Character.health = 100
        Character.gold = 40
    elif class_selection_num == 5:
        Character.type = "Assassin"
        Character.attack = 2
        Character.health = 100
        Character.gold = 30
    elif class_selection_num == 6:
        Character.type = "Archer"
        Character.attack = 2
        Character.health = 100
        Character.gold = 20
    else:
        print("\nINVALID INPUT WE NOW HAVE YER MEDICAL RECORDS\n")
        class_selection()

# Loops everytime a user dies
def main():
    game_rules()
    class_selection()
    char_stats()
    new_round()

if __name__ == "__main__":
    main()
#---------------------------------------------------------------------------------------------------------------------------#
