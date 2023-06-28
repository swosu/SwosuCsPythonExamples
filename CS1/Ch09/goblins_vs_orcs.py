import random

class Fighter:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.health = 100

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

goblins = []
for i in range(1, 10):
    name = f"Goblin {i}"
    attack = random.randint(1, 100)
    defense = random.randint(1, 100)
    goblin = Fighter(name, attack, defense)
    goblins.append(goblin)

orcs = []
for i in range(1, 10):
    name = f"Orc {i}"
    attack = random.randint(1, 1000)
    defense = random.randint(1, 1000)
    orc = Fighter(name, attack, defense)
    orcs.append(orc)

while len(goblins) > 0 and len(orcs) > 0:
    attacker = random.choice(goblins + orcs)
    defender = random.choice(goblins + orcs)
    while defender == attacker:
        defender = random.choice(goblins + orcs)
    damage = attacker.attack - defender.defense
    if damage < 0:
        damage = 0
    print(f"{attacker.name} attacks {defender.name} for {damage} damage.")
    defender.take_damage(damage)
    if defender.health == 0:
        print(f"{defender.name} has been defeated!")
        if defender in goblins:
            goblins.remove(defender)
        else:
            orcs.remove(defender)

if len(goblins) == 0:
    print("The orcs win!")
else:
    print("The goblins win!")