import random
class Character:
    def __init__(self, name, type, location , attack, health, gold):
        self.name = name
        self.type = type
        self.location = location
        self.attack = attack
        self.health = health
        self.gold = gold
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
    def __init__(self, name, type, health, attack,with_player=False):
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






#---------------------------------------------------------------------------------------------------------------------------#
# Basic Companion Functions
def companion_stats():
    print(f"\n{Game.companion.name}'s Type = ",Game.companion.type,)
    print(f"{Game.companion.name}'s Attack = ",Game.companion.attack,)
    print(f"{Game.companion.name}'s Health = ",Game.companion.health,)

def maybe_companion():
    rand_num = random.randint(1, 30)
    if rand_num == 24:
        generate_companion_sequence()
    else:
        print("\n They didn't want to talk to you.")

def generate_companion_sequence():
    print("\nYou found a companion!")
    generate_companion()
    print("Would you like to take this companion with you?")
    companion_choice = int(input("1. Yes\n2. No\n"))
    if companion_choice == 1:
        Companion.with_player = True
        print(f"\nYou have taken {Game.companion.name} with you.")
        companion_stats()
    elif companion_choice == 2:
        print("\nYou left the companion.")
    else:
        print("\nINVALID INPUT WE NOW HAVE YER BANK ACCOUNT INFO\n")
        generate_companion_sequence()

def generate_companion():
    random_companion_key = random.choice(list(character_type_dict.keys()))
    Game.companion = character_type_dict[random_companion_key]
    companion_stats()
#---------------------------------------------------------------------------------------------------------------------------#

def test():
    while Game.companion == None:
        maybe_companion()
        print("Trying again...")
    else:
        print("You have a companion!")


test()
