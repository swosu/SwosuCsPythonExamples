class User:
    def __init__(self, name):
        # Basic attributes
        self.name = name
        self.health = 100  # Default health
        self.damage = 10   # Base damage
        self.inventory = []  # Starts empty
        self.location = (0, 0)  # Default starting point (x, y)

    # ----- Core Behaviors -----
    def collect_item(self, item):
        """Add an item to the user’s inventory."""
        self.inventory.append(item)
        print(f"{self.name} collected {item}!")

    def attack(self, target):
        """Perform a basic attack on another user or enemy."""
        if not target:
            print("No target to attack!")
            return
        print(f"{self.name} attacks {target.name} for {self.damage} damage!")
        target.defend(self.damage)

    def defend(self, damage):
        """Reduce health based on incoming damage."""
        self.health -= damage
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")
        if self.health <= 0:
            print(f"{self.name} has been defeated!")

    def give_item(self, item, target):
        """Give an item to another user."""
        if item in self.inventory:
            self.inventory.remove(item)
            target.inventory.append(item)
            print(f"{self.name} gave {item} to {target.name}.")
        else:
            print(f"{self.name} doesn’t have {item}.")

    # ----- Special Abilities -----
    def ice_block(self, target):
        print(f"{self.name} casts Ice Block on {target.name}, freezing them in place!")

    def fireball(self, target):
        dmg = self.damage + 15
        print(f"{self.name} hurls a Fireball at {target.name} for {dmg} damage!")
        target.defend(dmg)

    def lightning(self, target):
        dmg = self.damage + 20
        print(f"{self.name} summons Lightning on {target.name} for {dmg} damage!")
        target.defend(dmg)

    def heal(self, amount=20):
        """Restore health."""
        self.health += amount
        print(f"{self.name} heals for {amount}. Health is now {self.health}.")

    def move(self, x, y):
        """Change player location."""
        self.location = (x, y)
        print(f"{self.name} moves to {self.location}.")
