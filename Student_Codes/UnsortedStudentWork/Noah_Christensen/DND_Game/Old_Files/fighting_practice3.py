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
# Add enemies and bosses here:
def generate_enemy():
    enemy_dict={
        Enemy("Daegon", "Demon", 40, 4),
        Enemy("Centaurith", "Beast", 40, 4),
        Enemy("Aacalith", "Vampire", 30, 3),
        Enemy("Zrython", "Beast", 30, 2)
    }
    enemy_boss = {
        "Vziathar": Enemy("Vziathar", "God", 100, 8)
    }
    random_enemy_key = random.choice(list(enemy_dict.keys()))
    enemy_instance = enemy_dict[random_enemy_key]
    return enemy_instance


#---------------------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------------------------------------#
# testing enemy object functions:
def current_enemy_check():
    print(f"Current enemy: {Enemy.name} \nEnemy Type: {Enemy.type} \nEnemy Health: {Enemy.health} \nEnemy Attack: {Enemy.attack}")

#---------------------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------------------------------------#
'''
def clear_current_enemy():
    game_variables["current_enemy"] = None

def assigning_enemy():
    game_variables["current_enemy"] = Enemy(game_variables["current_enemy"].name, game_variables["current_enemy"].type, game_variables["current_enemy"].health, game_variables["current_enemy"].attack)

def enemy_stats():
    #print(f"\nEnemy stats:\nHealth: {game_variables['current_enemy'].health}\nAttack: {game_variables['current_enemy'].attack}")

def assigning_enemy_to_class():
    print("Assigning enemy to class...")
    Enemy(game_variables["current_enemy"].name, game_variables["current_enemy"].type, game_variables["current_enemy"].health, game_variables["current_enemy"].attack)
    print("Enemy assigned to class.")
'''
#---------------------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------------------------------------#
# Fighting Functions:
# Both Char and Enemy roll a d20, then add their attack stat to the roll, then establishes the difference between the two rolls
def char_roll():
    useless_var = input("Press enter to roll")
    char_roll_result = random.randint(1, 20)
    print(f"You roll a {char_roll_result}")
    char_attack = Char.attack + char_roll_result
    print(f"Your attack this round is {char_attack}")
    return char_attack
def enemy_roll():
    enemy_roll_result = random.randint(1, 20)
    print(f"The enemy rolls a {enemy_roll_result}")
    enemy_attack = E .attack + enemy_roll_result
    print(f"The enemy's attack this round is {enemy_attack}")
    return enemy_attack
def roll_result():
    char_roll_result = char_roll()
    enemy_roll_result = enemy_roll()
    roll_difference = char_roll_result - enemy_roll_result
    if roll_difference > 0:
        Enemy.modify_health(-roll_difference)
        print(f"You hit the enemy for {roll_difference} damage!")
    elif roll_difference < 0:
        Char.modify_health(roll_difference)
        print(f"The enemy hits you for {-roll_difference} damage!")
    else:
        print("You both missed!")
#---------------------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------------------------------------#
# Basic Fighting Mechanisms:
# Main fighting function, is only looped everytime user enters new location:
def enemy_encounter(): 
    current_enemy = Enemy
    print(f"\nYou encounter {current_enemy.name}\nThe mighty {current_enemy.type}:\nHealth: {current_enemy.health}\nAttack: {current_enemy.attack}")
    fight_or_flee = int(input("\nPlease type:\n'1' to attack \n'2' to attempt to flee:\n"))
    if fight_or_flee == 1:
        fight_sequence()
    elif fight_or_flee == 2:
          flee_enemy()
    else:
        print(f"The {current_enemy} charges at ya, get ready to fight!")
        fight_sequence()

def fight_sequence(): 
    while char.health > 0 and Enemy.health > 0:
        roll_result()
        print(f"Your health is {Char.health}")
        print(f"The enemy's health is {Enemy.health}")
    if Char.health <= 0:
        print("You died. Game over.")
        exit()
    elif Enemy.health <= 0:
        print("You defeated the enemy!")
        exit()

def flee_enemy():
    print("fleeing enemy")
#---------------------------------------------------------------------------------------------------------------------------#

def test_main():
    char_stats()
    current_enemy = generate_enemy()
    current_enemy_check()
    enemy_encounter()



if __name__ == "__main__":
    test_main()