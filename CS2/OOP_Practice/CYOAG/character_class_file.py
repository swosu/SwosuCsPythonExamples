class character:

    def __init__(self):
        self.data = []
        self.health = 100
        self.inventory_dictionary = {}

    def get_health(self):
        return self.health

    def take_damage(self, damage):
        print(f'we took {damage} damage.')
        self.health = self.health - damage

    def set_health(self, health):
        print(f'we add {health} health.')
        self.health = self.health + health
