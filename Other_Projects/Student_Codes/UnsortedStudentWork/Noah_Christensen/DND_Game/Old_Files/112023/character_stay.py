import random
from new_round import Char, char_go 

#---------------------------------------------------------------------------------------------------------------------------#
# User chooses to stay
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
    Char.health += 10
    print(f"\nYou have rested. Your health is now {Char.health}.")
    char_go()

def char_explore():
    if Char == True:
        print("\nWhat would you like to do?")
        print("1. Go to the Tavern")
        print("2. Go to the Keep")
        print("3. Go to the Temple")
        print("4. Go to the Witch")
        explore_choice = int(input("Select an option (1/2/3/4): "))
        if explore_choice == 1:
            print("\nYou go to the Tavern.")
            explore_tavern()
            Char.modify_location(None)
            char_go()
        elif explore_choice == 2:
            print("\nYou go to the Keep.")
            explore_keep()
            Char.modify_location(None)
            char_go()
        elif explore_choice == 3:
            print("\nYou go to the Temple.")
            explore_temple()
            Char.modify_location(None)
            char_go()
        elif explore_choice == 4:
            print("\nYou go to the Witch.")
            explore_witch()
            Char.modify_location(None)
            char_go()
        else:
            print("\nINVALID INPUT WE NOW HAVE YER MEDICAL RECORDS\n")
        Char.modify_location(None)
        char_go()
    else:
        char_go
#---------------------------------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------------------------------#
# Exploring the City Functions:
# Tavern: Talk to bartender for a drink, or talk to the drunk (I need to add that the drunk can give you a quest)
def explore_tavern():
    print("\nYou enter the Tavern.")
    print("\nYou enter the Tavern.")
    print("What would you like to do?")
    print("1. Talk to the Bartender")
    print("2. Talk to the Drunk")
    print("3. Leave")
    tavern_choice = int(input("Select an option (1/2/3/4): "))
    if tavern_choice == 1:
        print("\nYou talk to the Bartender.")
        print("Bartender: Welcome to the Tavern! What can I get you?")
        print("1. Ale")
        print("2. Water")
        print("3. Leave")
        bartender_choice = int(input("Select an option (1/2/3): "))
        if bartender_choice == 1:
            print("\nYou order an ale.")
            print("Bartender: That'll be 5 gold.")
            print("You pay the Bartender 5 gold.")
            Char.modify_gold(-5)
            print("You have: ", Char.gold, "gold.")
            print("Bartender: Here you go.")
            print("You drink the ale.")
            print("You feel refreshed.")
            Char.modify_health(10)
            print(f"Your health is now {Char.health}.")
            explore_tavern()
        elif bartender_choice == 2:
            print("\nYou order some water.")
            print("Bartender: That'll be 2 gold.")
            print("You pay the Bartender 2 gold.")
            Char.modify_gold(-2)
            print("You have: ", Char.gold, "gold.")
            print("Bartender: Here you go.")
            print("You drink the water.")
            print("You feel refreshed.")
            Char.modify_health(10)
            print(f"Your health is now {Char.health}.")
            explore_tavern()
        elif bartender_choice == 3:
            print("\nYou leave the Tavern.")
            char_go()
        else:
            print("\nINVALID INPUT WE NOW HAVE YER BANK ACCOUNT INFO\n")
            explore_tavern()
    elif tavern_choice == 2:
        print("\nYou talk to the Drunk.")
        print("Drunk: Hic! I'm drunk!")
        print("You leave the Drunk.")
        char_go()
    elif tavern_choice == 3:
        print("\nYou leave the Tavern.")
        char_go()

# Keep: Talk to the King for a quest
def explore_keep():
    if Char.type == "Knight":
        print("\nYou enter the Keep.")
        print("King: Welcome Knight!  Stay a while.")
        maybe_gold()
        char_explore()
    elif Char.type == "Elf":
        print("\nYou enter the Keep.")
        print("King: GET THAT CREATURE OUT OF HERE!")
        char_go()
    elif Char.type == "Viking":
        print("\nYou enter the Keep.")
        print("King: What do you want?")
        maybe_gold()
        char_go()
    elif Char.type == "Dwarf":
        print("\nYou Enter the Keep.")
        print("King: Welcome.")
        maybe_gold()
        char_explore()
    elif Char.type == "Assassin":
        print("\nYou enter the Keep.")
        print("King: What do you want?")
        maybe_gold()
        char_go()
    elif Char.type == "Archer":
        print("\nYou enter the Keep.")
        print("King: Welcome, what can we do for you?")
        maybe_gold()
        char_explore()

def maybe_gold():
    rand_num = random.randint(1, 10)
    if rand_num == 1 or rand_num == 3 or rand_num == 7:
        print("\nKing: Thank you for your service.  Here is some gold.")
        Char.modify_gold(10)
        print("You have: ", Char.gold, "gold.")
    else:
        print("\nKing: Thank you for your service.")


# Temple: Talk to the Priest to pray or repent

def explore_temple():
    print("\nYou enter the Temple.")
    print("Priest: What would you like to do?")
    print("1. Pray")
    print("2. Repent")
    print("3. Leave")
    temple_choice = int(input("Select an option (1/2/3): "))
    if temple_choice == 1:
        print("\nYou pray.")
        print("Priest: May the Gods be with you.")
        print("You feel refreshed.")
        Char.modify_health(10)
        print(f"Your health is now {Char.health}.")
        char_go()
    elif temple_choice == 2:
        print("\nYou repent.")
        print("Priest: May the Gods be with you.")
        print("You feel refreshed.")
        Char.modify_health(10)
        print(f"Your health is now {Char.health}.")
        char_go()
    elif temple_choice == 3:
        print("\nYou leave the Temple.")
        char_go()
    else:
        print("\nINVALID INPUT WE NOW HAVE YER BANK ACCOUNT INFO\n")
        explore_temple()

# Witch: Talk to the Witch for a fortune or a curse
def explore_witch():
    print("\nYou enter the Witch's Hut.")
    print("Witch: Take a seat.")
    input("Press enter to continue.")
    gift_or_curse = random.randint(1, 2)
    if gift_or_curse == 1:
        print("\nWitch: I will give you a gift.")
        print("You feel refreshed.")
        Char.modify_health(10)
        print(f"Your health is now {Char.health}.")
        char_go()
    elif gift_or_curse == 2:
        print("\nWitch: I will curse you.")
        print("You feel cursed.")
        Char.modify_health(-10)
        print(f"Your health is now {Char.health}.")
        char_go()
    else:
        print("\nINVALID INPUT WE NOW HAVE YER BANK ACCOUNT INFO\n")
        explore_witch()
#---------------------------------------------------------------------------------------------------------------------------#

if __name__ == "__main__":
    main()