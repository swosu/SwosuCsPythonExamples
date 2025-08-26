import random
from new_game import Character

#---------------------------------------------------------------------------------------------------------------------------#
# Exploring the City Functions:
# Tavern: Talk to bartender for a drink, or talk to the drunk (I need to add that the drunk can give you a quest)
def explore_tavern():
    print("\nYou enter the Tavern.\nWhat would you like to do?\n1. Talk to the Bartender\n2. Talk to the Drunk\n3. Leave")
    tavern_choice = int(input("Select an option (1/2/3/4): "))
    if tavern_choice == 1:
        print("\nYou talk to the Bartender.\nBartender: Welcome to the Tavern! What can I get you?\n1. Ale (5 Gold)\n2. Water (2 Gold)\n3. Leave")
        bartender_choice = int(input("Select an option (1/2/3): "))
        if bartender_choice == 1:
            print("\nYou order an ale.\nBartender: That'll be 5 gold.")
            Character.modify_gold(-5)
            print("You have: ", Character.gold, "gold.")
            print("Bartender: Here you go.\nYou feel refreshed.")
            if Character.health <= 90:
                Character.modify_health(10)
                print(f"Your health is now {Character.health}.")
            elif Character.health > 90:
                Character.health = 100
                print(f"Your health is now {Character.health}.")
        elif bartender_choice == 2:
            print("\nYou order some water.\nBartender: That'll be 2 gold.")
            Character.modify_gold(-2)
            print("You have: ", Character.gold, "gold.")
            print("Bartender: Here you go.\nYou feel refreshed.")
            if Character.health <= 90:
                Character.modify_health(10)
                print(f"Your health is now {Character.health}.")
            elif Character.health > 90:
                Character.health = 100
                print(f"Your health is now {Character.health}.")
        elif bartender_choice == 3:
            print("\nYou leave the Tavern.")
        else:
            print("\nINVALID INPUT WE NOW HAVE YER BANK ACCOUNT INFO\n")
            explore_tavern()
    elif tavern_choice == 2:
        print("\nYou talk to the Drunk.")
        print("Drunk: GET OUT OF MY FACE!")
        print("He punches you in the face and you lose 10 health.")
        Character.modify_health(-10)
    elif tavern_choice == 3:
        print("\nYou leave the Tavern.")

# Keep: Talk to the King for a quest
def explore_keep():
    if Character.type == "Knight":
        print("\nYou enter the Keep.")
        print("King: Welcome Knight!  Stay a while.")
        maybe_gold()
    elif Character.type == "Elf":
        print("\nYou enter the Keep.")
        print("King: GET THAT CREATURE OUT OF HERE!")
    elif Character.type == "Viking":
        print("\nYou enter the Keep.")
        print("King: What do you want?")
        maybe_gold()
    elif Character.type == "Dwarf":
        print("\nYou Enter the Keep.")
        print("King: Welcome.")
        maybe_gold()
    elif Character.type == "Assassin":
        print("\nYou enter the Keep.")
        print("King: What do you want?")
        maybe_gold()
    elif Character.type == "Archer":
        print("\nYou enter the Keep.")
        print("King: Welcome, what can we do for you?")
        maybe_gold()
def maybe_gold():
    rand_num = random.randint(1, 10)
    if rand_num == 1 or rand_num == 3 or rand_num == 7:
        gold_amount = random.randint(1, 20)
        print(f"\nKing: Thank you for your service.  Here is {gold_amount} gold.")
        Character.modify_gold(gold_amount)
        print("You have: ", Character.gold, "gold.")
    else:
        print("\nKing: Thank you for your service.")

# Temple: Talk to the Priest to pray or repent
def explore_temple():
    print("\nYou enter the Temple.\nPriest: What would you like to do?\n1. Pray\n2. Repent\n3. Leave")
    temple_choice = int(input("Select an option (1/2/3): "))
    if temple_choice == 1:
        print("\nYou pray.")
        if Character.health <= 96:
            holy_heal = random.randint(1, 4)
            print(f"You feel refreshed.  Your health is now {Character.health + holy_heal}.")
        else:
            print("Priest: May the Gods be with you.")

    elif temple_choice == 2:
        print("\nYou repent.")
        print("Priest: May the Gods be with you.")
    elif temple_choice == 3:
        print("\nYou leave the Temple.")
    else:
        print("\nINVALID INPUT WE NOW HAVE YER BANK ACCOUNT INFO\n")
        explore_temple()

# Witch: Talk to the Witch for a fortune or a curse
def explore_witch():
    print("\nYou enter the Witch's Hut.\nWitch: Don't be scared.")
    input("Press enter to continue.")
    gift_or_curse = random.randint(1, 2)
    if gift_or_curse == 1:
        if Character.health <= 85:
            print("\nWitch: The Gods smile upon you.")
            gift_amount = random.randint(1, 15)
            Character.modify_health(gift_amount)
            print(f"Your health is now {Character.health}.")
        else:
            print("\nWitch: The Gods smile upon you.")
            Character.health = 100
            print(f"Your health is now {Character.health}.")
    elif gift_or_curse == 2:
        print("\nWitch: The Gods don't favor you.")
        print("You feel cursed.")
        Character.modify_health(-10)
        print(f"Your health is now {Character.health}.")
    else:
        print("\nINVALID INPUT WE NOW HAVE YER BANK ACCOUNT INFO\n")
        explore_witch()
#---------------------------------------------------------------------------------------------------------------------------#



#---------------------------------------------------------------------------------------------------------------------------#
# User Chooses to Stay
def main():
    print("\nWhat would you like to do?")
    print("1. Rest")
    print("2. Explore")
    stay_choice = int(input("Select an option (1/2): "))

    if stay_choice == 1:
        char_rest()
    elif stay_choice == 2:
        char_explore()
    else:
        print("\nINVALID INPUT WE NOW HAVE YER ADDRESS\n")
        main()

def char_rest():
    Character.health += 10
    print(f"\nYou have rested. Your health is now {Character.health}.")

def char_explore():
    if Character.location == "in_City":
        print("\nWhat would you like to do?")
        print("1. Go to the Tavern")
        print("2. Go to the Keep")
        print("3. Go to the Temple")
        print("4. Go to the Witch")
        explore_choice = int(input("Select an option (1/2/3/4): "))
        if explore_choice == 1:
            print("\nYou go to the Tavern.")
            explore_tavern()
            Character.location = "onJourney"
        elif explore_choice == 2:
            print("\nYou go to the Keep.")
            explore_keep()
            Character.location = "onJourney"
        elif explore_choice == 3:
            print("\nYou go to the Temple.")
            explore_temple()
            Character.location = "onJourney"
        elif explore_choice == 4:
            print("\nYou go to the Witch.")
            explore_witch()
            Character.location = "onJourney"
        else:
            print("\nINVALID INPUT WE NOW HAVE YER MEDICAL RECORDS\n")
            Character.location = "onJourney"
            char_explore()
    else:
        print("\nYou are not in a city.")
#---------------------------------------------------------------------------------------------------------------------------#

if __name__ == "__main__":
    main()
