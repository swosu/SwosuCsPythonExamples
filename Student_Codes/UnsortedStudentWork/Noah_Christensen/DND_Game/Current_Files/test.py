import random
game_variables = {
    "current_enemy": None,
}

class Enemy:
    def __init__(self, name, type, health, attack):
        self.name = name
        self.type = type
        self.health = health
        self.attack = attack
    def modify_health(self, health_change):
        self.health += health_change

class Location:
    def __init__ (self, name, outside_city):
        self.name = name
        self.outside_city = outside_city


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


def rand_road():
    road = random.choice(list(road_dict.keys()))
    game_variables["selected_road"] = road
    print(f"\nYou are on the {road}.")

def generate_enemy():
    random_enemy_key = random.choice(list(enemy_dict.keys()))
    game_variables["current_enemy"] = enemy_dict[random_enemy_key]
    print(f"\nYou've encountered a {game_variables['current_enemy'].name}!")

def clear_current_enemy():
    game_variables["current_enemy"] = None

def main():
    rand_road()
    generate_enemy()
    clear_current_enemy()
    generate_enemy()
    rand_road()

if __name__ == "__main__":
    main()