import random

#---------------------------------------------------------------------------------------------------------------------------#
class Char:
    def __init__(self, health, attack):
        self.health = health
        self.attack = attack
    def modify_health(self, health_change):
        self.health += health_change
char = Char(100, 4)
def char_stats():
    print(f"\nYour stats:\nHealth: {char.health}\nAttack: {char.attack}")
#---------------------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------------------------------------#
# Enemy Object:
class Enemy:
    def __init__(self, name, type, health, attack):
        self.name = name
        self.type = type
        self.health = health
        self.attack = attack
    def modify_health(self, health_change):
        self.health += health_change
#---------------------------------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------------------------------#
game_variables = {
    "current_enemy": None
}
#---------------------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------------------------------------#
# Add enemies and bosses here:
def generate_enemy():
    enemy_dict={
        "Daegon": Enemy("Daegon", "Demon", 40, 4),
        "Centaurith": Enemy("Centaurith", "Beast", 40, 4),
        "Aacalith": Enemy("Aacalith", "Vampire", 30, 3),
        "Zrython": Enemy("Zrython", "Beast", 30, 2)
    }
    enemy_boss = {
        "Vziathar": Enemy("Vziathar", "God", 100, 8)
    }
    random_enemy_key = random.choice(list(enemy_dict.keys()))
    game_variables["current_enemy"] = enemy_dict[random_enemy_key]
#---------------------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------------------------------------#
def clear_current_enemy():
    game_variables["current_enemy"] = None
def current_enemy_check():
    if game_variables["current_enemy"] == None:
        print("No enemy")
    else:
        print(f"Current enemy: {game_variables['current_enemy'].name} \n{game_variables['current_enemy'].type} \n{game_variables['current_enemy'].health} \n{game_variables['current_enemy'].attack}")
#---------------------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------------------------------------#
# Basic Fighting Sequence:
# Main fighting Function, triggers when the user enters a new location
def enemy_encounter():
    generate_enemy()
    print(f"You've encountered {game_variables['current_enemy'].name}!")
    fight_or_flee = int(input("1. Fight\n2. Flee\n"))
    if fight_or_flee == 1:
        fight_sequence()
    elif fight_or_flee == 2:
        print("You fled!")
        clear_current_enemy()
    else:
        print("Invalid input")
        fight_sequence()
# Fight sequence, triggers when the user chooses to fight
def fight_sequence():
    while game_variables["current_enemy"].health > 0 and char.health > 0:
        print(f"\n{game_variables['current_enemy'].name} stats:\nHealth: {game_variables['current_enemy'].health}\nAttack: {game_variables['current_enemy'].attack}")
        print(f"\nYour stats:\nHealth: {char.health}\nAttack: {char.attack}")
        roll_result()
        print(f"Your health is {char.health}")
        print(f"The enemy's health is {game_variables['current_enemy'].health}")
    if game_variables["current_enemy"].health <= 0:
        print(f"You have defeated {game_variables['current_enemy'].name}!")
        clear_current_enemy()
        current_enemy_check()
    elif char.health <= 0:
        print("You have died!")
        exit()
#---------------------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------------------------------------#
# Roll Result is the result of two functions: char_roll, enemy_roll
# Both Char and Enemy roll a d20, then add their attack stat to the roll, then establishes the difference between the two rolls
def roll_result():
    char_roll_result = char_roll()
    enemy_roll_result = enemy_roll()
    roll_difference = char_roll_result - enemy_roll_result
    if roll_difference > 0:
        print(f"You dealt {roll_difference} damage!")
        game_variables["current_enemy"].modify_health(-roll_difference)
    elif roll_difference < 0:
        print(f"The enemy dealt {-roll_difference} damage!")
        char.modify_health(roll_difference)
    else:
        print("You both missed!")
def char_roll():
    useless_var = input("Press enter to roll")
    char_roll_result = random.randint(1, 20)
    print(f"You roll a {char_roll_result}")
    char_attack = char.attack + char_roll_result
    print(f"Your attack this round is {char_attack}")
    return char_attack
def enemy_roll():
    enemy_roll_result = random.randint(1, 20)
    print(f"The enemy rolls a {enemy_roll_result}")
    enemy_attack = game_variables["current_enemy"].attack + enemy_roll_result
    print(f"The enemy's attack this round is {enemy_attack}")
    return enemy_attack
#---------------------------------------------------------------------------------------------------------------------------#



















#---------------------------------------------------------------------------------------------------------------------------#
# Testing Functions:
'''def generate_enemy_test():
    while True:
        print(game_variables["current_enemy"])
        generate_enemy()
        print(game_variables["current_enemy"].name + "\n" + game_variables["current_enemy"].type + "\n" + str(game_variables["current_enemy"].health) + "\n" + str(game_variables["current_enemy"].attack))
        clear_current_enemy()
        user_again = input("Again? (y/n): ")
        if user_again == "n":
            break'''
#---------------------------------------------------------------------------------------------------------------------------#

def main():
    enemy_encounter()

if __name__ == "__main__":
    main()