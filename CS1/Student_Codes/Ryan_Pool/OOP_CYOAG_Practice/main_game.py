from UserClass import User

def main():
    # Create two users
    jeremy = User("Jeremy")
    ryan = User("Ryan")

    print("\n--- The Adventure Begins! ---\n")

    # Starting setup
    jeremy.collect_item("Wooden Sword")
    jeremy.collect_item("Healing Potion")
    ryan.collect_item("Magic Staff")

    # Ryan explores the world
    ryan.move(2, 3)
    ryan.collect_item("Mana Crystal")

    # Ryan encounters Jeremy
    print("\n--- Encounter! ---\n")
    ryan.fireball(jeremy)

    # Jeremy fights back
    jeremy.attack(ryan)

    # Ryan uses special powers
    ryan.lightning(jeremy)

    # Jeremy heals up
    jeremy.heal()

    # Ryan gives an item to Jeremy as a peace offering
    ryan.give_item("Mana Crystal", jeremy)

    print("\n--- Current Stats ---")
    print(f"{jeremy.name} → Health: {jeremy.health}, Inventory: {jeremy.inventory}, Location: {jeremy.location}")
    print(f"{ryan.name} → Health: {ryan.health}, Inventory: {ryan.inventory}, Location: {ryan.location}")

    print("\n--- End of Demo ---\n")

if __name__ == "__main__":
    main()
