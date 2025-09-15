"""
Walmart Bonfire Adventure
A simple choose-your-own-adventure game to demonstrate Python's if, elif, else.
Theme: Shopping for a bonfire party at Walmart while avoiding trouble!
Author: Jeremy's Monday Morning Buddy
"""

def get_choice(prompt, options):
    """
    Utility function that forces user to pick a valid numeric option.
    Loops until the user types something valid.
    Args:
        prompt (str): The input prompt to display.
        options (list): List of valid numeric options.
    Returns:
        int: The valid choice the user made.
    Easter egg: if user types 42, print a special message but don't accept it as valid input.
    """
    while True:
        user_input = input(prompt).strip()  # keep raw text for better error reporting
        try:
            # First try to convert nicely (handles "3." or "2.0")
            choice = int(float(user_input))
            
            if choice in options:
                return choice
            elif choice == 42:
                print("✨ You've discovered the secret option 42! But alas, it won't help you here. Try again.")
            else:
                print(f"'{choice}' isn’t one of the choices. Please try again.")
        except ValueError:
            print(f"Invalid input: '{user_input}'. Numbers only, please!")



def walmart_adventure():
    print("🔥 Welcome to Walmart Bonfire Adventure! 🔥")
    print("Your goal: Gather supplies for a festive bonfire.")
    print("But beware... not everyone in Walmart is cheering for your flames.\n")

    print("You enter the store and grab a shopping cart.")
    print("Do you head first to:")
    print("1. Outdoor section (hammocks, firewood)")
    print("2. Grocery aisle (marshmallows, chocolate, jalapeño hot dogs)")
    print("3. Automotive (gas cans, lighter fluid)")

    choice1 = get_choice("Choose 1, 2, or 3: ", [1, 2, 3])

    if choice1 == 1:
        print("\nYou stroll to the Outdoor section. 🌲")
        print("You see hammocks AND bundles of firewood. Jackpot!")
        print("But... a disgruntled Walmart employee is blocking the firewood.")
        print("Do you:")
        print("1. Try to sneak around them.")
        print("2. Politely ask for help.")
        print("3. Abandon wood and grab a hammock instead.")

        choice2 = get_choice("Choose 1, 2, or 3: ", [1, 2, 3])

        if choice2 == 1:
            print("\nYou ninja your way past and snag the firewood. Success!")
        elif choice2 == 2:
            print("\nThe employee grumbles but lets you have the firewood. You win them over with kindness.")
        else:
            print("\nYou pick a hammock. Not great fuel, but comfy if the bonfire fails.")

    elif choice1 == 2:
        print("\nYou head into the Grocery aisle. 🍫🌭")
        print("Marshmallows, chocolate, and jalapeño hot dogs await!")
        print("But someone is hoarding all the marshmallows.")
        print("Do you:")
        print("1. Ask them to share.")
        print("2. Distract them with a shiny candy bar.")
        print("3. Forget marshmallows and double down on hot dogs.")

        choice2 = get_choice("Choose 1, 2, or 3: ", [1, 2, 3])

        if choice2 == 1:
            print("\nThey reluctantly give you a bag. S’mores are back on the menu!")
        elif choice2 == 2:
            print("\nClassic misdirection! You score marshmallows AND hot dogs.")
        else:
            print("\nYou’re now running a jalapeño hot dog–only bonfire. Bold move.")

    else:  # choice1 == 3
        print("\nYou walk into Automotive. 🚗⛽")
        print("Gas cans gleam in the fluorescent light.")
        print("But uh oh... A manager catches you eyeing the lighter fluid.")
        print("Do you:")
        print("1. Tell them you’re just preparing for a safe camping trip.")
        print("2. Run with the gas can!")
        print("3. Ditch the plan and look for something else.")

        choice2 = get_choice("Choose 1, 2, or 3: ", [1, 2, 3])

        if choice2 == 1:
            print("\nThey nod suspiciously but let you buy it. Camping story for the win!")
        elif choice2 == 2:
            print("\nYou sprint through self-checkout with the gas can. Risky but effective.")
        else:
            print("\nNo fire starter? That’s going to be a pretty sad bonfire.")

    # Ending
    print("\nYou check out and roll your cart into the night.")
    print("The bonfire awaits. Whatever you collected will decide the party’s fate.")
    print("🔥 The End 🔥")


# Run the game
if __name__ == "__main__":
    walmart_adventure()
