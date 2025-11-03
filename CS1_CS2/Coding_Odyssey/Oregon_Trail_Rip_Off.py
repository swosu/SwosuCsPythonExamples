import random
import time

# -------------------------------
# Player Class
# -------------------------------
class Player:
    def __init__(self, name, wealth_level, luck_level, party_size):
        self.name = name
        self.wealth = wealth_level
        self.luck = luck_level
        self.party_size = party_size
        self.supplies = {"food": 0, "water": 0, "ammo": 0, "medicine": 0}
        self.is_alive = True

    def adjust_supplies(self, item, amount):
        """Increase or decrease the player's supply of a specific item."""
        if item in self.supplies:
            self.supplies[item] += amount
            if self.supplies[item] < 0:
                self.supplies[item] = 0

    def lose_party_member(self):
        """Reduce party size when bad things happen."""
        if self.party_size > 1:
            self.party_size -= 1
            print(f"😢 A member of your party didn't make it. Remaining: {self.party_size}")
        else:
            self.is_alive = False
            print("💀 You're the last one standing... and even you didn’t stand long.")


# -------------------------------
# Game Class
# -------------------------------
class Game:
    def __init__(self):
        self.player = None
        self.current_day = 1
        self.starting_point = None
        self.starting_month = None

    def start(self):
        """Main game start sequence."""
        self._intro()
        self._create_player()
        self._choose_starting_point()
        self._choose_starting_month()
        self._buy_supplies()
        self._begin_journey()

    def _intro(self):
        print("🌄 Welcome to the *Oregon-ish Trail!*")
        print("Can you survive dysentery, bandits, and bad decisions?")
        input("Press Enter to begin your journey...\n")

    def _create_player(self):
        """Gather player info and create Player object."""
        username = input("Enter your traveler's name: ")
        party_size = int(input("How many are in your party (1–6)? "))

        print("\nChoose your fate:")
        print("1. Poor but Lucky (less money, more good fortune)")
        print("2. Rich and Dumb (more money, but awful luck)")
        print("3. Average (balanced everything)")
        choice = input("> ")

        if choice == "1":
            wealth, luck = 50, 80
        elif choice == "2":
            wealth, luck = 150, 30
        else:
            wealth, luck = 100, 50

        self.player = Player(username, wealth, luck, party_size)

    def _choose_starting_point(self):
        """Let player choose starting point."""
        options = ["Independence", "St. Joseph", "Springfield"]
        print("\nChoose your starting point:")
        for i, town in enumerate(options, start=1):
            print(f"{i}. {town}")
        choice = int(input("> ")) - 1
        self.starting_point = options[choice]
        print(f"You begin your journey in {self.starting_point}.\n")

    def _choose_starting_month(self):
        """Set the starting month."""
        options = ["March", "April", "May", "June"]
        print("Choose your starting month:")
        for i, month in enumerate(options, start=1):
            print(f"{i}. {month}")
        choice = int(input("> ")) - 1
        self.starting_month = options[choice]
        print(f"You set off in {self.starting_month}.\n")

    def _buy_supplies(self):
        """Simulate buying supplies with available wealth."""
        print("Welcome to Ye Olde General Store!")
        prices = {"food": 10, "water": 5, "ammo": 20, "medicine": 15}

        while self.player.wealth > 0:
            print(f"\nYou have ${self.player.wealth} left.")
            print("Supplies: ", self.player.supplies)
            print("Available items:")
            for item, price in prices.items():
                print(f"{item.title()} - ${price} per unit")
            choice = input("What would you like to buy (or 'done')? ").lower()

            if choice == "done":
                break
            if choice in prices:
                quantity = int(input(f"How many {choice} do you want to buy? "))
                cost = prices[choice] * quantity
                if cost <= self.player.wealth:
                    self.player.wealth -= cost
                    self.player.adjust_supplies(choice, quantity)
                    print(f"Added {quantity} {choice}. Remaining money: ${self.player.wealth}")
                else:
                    print("Not enough funds for that purchase!")
            else:
                print("Invalid choice!")

    def _begin_journey(self):
        """Main event loop of the game."""
        print("\n🚙 Your wagon creaks westward...")
        time.sleep(1)

        while self.player.is_alive:
            self.current_day += 1
            event = random.choice([
                self._find_water, self._cross_river, self._set_up_camp,
                self._find_town, self._go_hunting
            ])
            event()

            if random.randint(0, 100) < 5:
                print("🎉 You reached Oregon alive and dusty! You win!")
                break

    # -------------------------------
    # Event Functions
    # -------------------------------
    def _find_water(self):
        print("\n💧 You find a stream of fresh water.")
        if random.randint(0, 100) < self.player.luck:
            print("You fill your barrels and feel refreshed.")
            self.player.adjust_supplies("water", 3)
        else:
            print("The water was dirty! Everyone gets sick.")
            self.player.lose_party_member()

    def _cross_river(self):
        print("\n🌊 You attempt to cross a river.")
        if random.randint(0, 100) < self.player.luck:
            print("You crossed safely. Ducks salute you.")
        else:
            print("You lose supplies to the current!")
            self.player.adjust_supplies("food", -3)
            if random.randint(0, 1):
                self.player.lose_party_member()

    def _set_up_camp(self):
        print("\n🏕️ You set up camp for the night.")
        event = random.choice(["robbed", "animals", "food"])
        if event == "robbed":
            print("Bandits raid your camp! You lose supplies.")
            self.player.adjust_supplies("ammo", -2)
            self.player.adjust_supplies("food", -2)
        elif event == "animals":
            print("Your oxen run away! You lose time chasing them.")
            self.current_day += 2
        else:
            print("You find edible berries nearby!")
            self.player.adjust_supplies("food", 3)

    def _find_town(self):
        print("\n🏘️ You stumble into a small frontier town.")
        outcome = random.choice(["trade", "robbed", "gift"])
        if outcome == "trade":
            print("You trade trinkets for supplies.")
            self.player.adjust_supplies("food", 2)
        elif outcome == "robbed":
            print("The mayor's cousin robs you blind.")
            self.player.adjust_supplies("food", -2)
        else:
            print("A kind stranger gives you medicine!")
            self.player.adjust_supplies("medicine", 1)

    def _go_hunting(self):
        print("\n🎯 You go hunting.")
        if self.player.supplies["ammo"] > 0:
            self.player.adjust_supplies("ammo", -1)
            if random.randint(0, 100) < self.player.luck:
                print("You bag a buffalo! Food +5.")
                self.player.adjust_supplies("food", 5)
            else:
                print("You miss everything. Even your pride.")
        else:
            print("No ammo left. You eat sadness tonight.")


# -------------------------------
# Run the Game
# -------------------------------
if __name__ == "__main__":
    game = Game()
    game.start()
