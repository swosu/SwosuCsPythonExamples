# Character class 
from enemy_class_file import Enemy


class Character(Enemy):
    def __init__(self, location, attack, health, gold, has_companion=False):
        self.location = location
        self.gold = gold
        self.has_companion = has_companion
    def modify_health(damage):
        Character.health += damage
    def modify_gold(gold_change):
        Character.gold += gold_change