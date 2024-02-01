# Enemy Class
class Enemy:
    def __init__(self, name, type, health, attack):
        self.name = name
        self.type = type
        self.health = health
        self.attack = attack
    def modify_health(self, damage):
        self.health += damage