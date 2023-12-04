import random
from welcome_message import Char, char_stats
from new_round import game_variables
import new_game

#---------------------------------------------------------------------------------------------------------------------------#
# Enemy Object:
class Enemy:
    def __init__(self, type, health, attack):
        self.type = type
        self.health = health
        self.attack = attack

# Add enemies and bosses here:
def generate_enemy():
    enemy_list={
        "Daegon": Enemy("Demon", 40, 4),
        "Centaurith": Enemy("Beast", 40, 4),
        "Aacalith": Enemy("Vampire", 30, 3),
        "Zrython": Enemy("Beast", 30, 2)
    }
    enemy_boss = {
        "Vziathar": Enemy("God", 100, 8)
    }
    random_enemy_key = random.choice(list(enemy_list.keys()))
    return enemy_list[random_enemy_key]
#---------------------------------------------------------------------------------------------------------------------------#



#---------------------------------------------------------------------------------------------------------------------------#
# Treasure sequence
def treasure_sequence():
    print("still needs to be coded...")
#---------------------------------------------------------------------------------------------------------------------------#



#---------------------------------------------------------------------------------------------------------------------------#
# Basic Fighting Mechanisms:

# Main fighting function, is only looped everytime user enters new location:
# Generates Enemy then user can Fight or Flee
def main():
    while True:
        char_stats()
        game_variables["current_enemy"] = generate_enemy()
        current_enemy = game_variables["current_enemy"]
        print(f"\nYou encounter {current_enemy}\nThe mighty {current_enemy.type}:\nHealth: {current_enemy.health}\nAttack: {current_enemy.attack}")
        print("\nWhat do you want to do? Fight or flight?")
        fight_or_flee = int(input("\nPlease type:\n'1' to attack\n'2' to attempt to flee"))
        if fight_or_flee == 1:
            fight_enemy()
        elif fight_or_flee == 2:
            flee_enemy()
        else:
            print(f"The {current_enemy} charges at ya, get ready to fight!")
            fight_enemy()
if __name__ == "__main__":
    main()

#---------------------------------------------------------------------------------------------------------------------------#
# Loops until current_enemy.health <= 0
def fight_enemy():
    while True:
        char_stats()
        print("Roll to attack.")
        roll_trigger = int(input("Type any whole number to roll: "))
        if roll_trigger == int:
            fighting_sequence()
        else:
            print("Follow the directions.")
            
def fighting_sequence():
    while True:
        char_roll()
        enemy_roll()
        roll_result()
        char_stats()
        if Char.health <= 0:
            new_game.main()
        elif Enemy.health <= 0:
            treasure_sequence()
        else:
            fight_enemy()
#---------------------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------------------------------------#
# Fighting_sequence() Functions:
def char_roll():
    char_roll_result = random.randint(1, 20)
    Char.attack += char_roll_result
    return char_roll_result
def enemy_roll():
    enemy_roll_result = random.randint(1, 20)
    Enemy.attack += enemy_roll_result
    return enemy_roll_result
def roll_result():
    char_roll_result = char_roll()
    enemy_roll_result = enemy_roll()
    roll_difference = char_roll_result - enemy_roll_result
    if roll_difference > 0:
        Enemy.modify_health(-roll_difference)
    else:
        Char.modify_health(-roll_difference)
#---------------------------------------------------------------------------------------------------------------------------#


def flee_enemy():
    print("Still needs to be coded, sorry LOL")
    fight_enemy()




