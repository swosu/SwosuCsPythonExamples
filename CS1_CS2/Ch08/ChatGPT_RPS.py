import random


def build_game_rules():
    """
    Create and return the full dictionary-of-dictionaries structure
    for Rock, Paper, Scissors.

    How it works:
    - The outer dictionary uses the USER'S choice as the key.
    - Each value in the outer dictionary is another dictionary.
    - That inner dictionary uses the COMPUTER'S choice as the key.
    - The final value is the game result:
        "Tie", "You win", or "You lose"

    This is a dictionary-of-dictionaries approach because one dictionary
    stores other dictionaries as its values.

    Example:
        rules["R"]["P"] -> "You lose"

    Meaning:
    - User chose Rock
    - Computer chose Paper
    - Result is "You lose"
    """
    rock_choice_dictionary = {
        "R": "Tie",
        "P": "You lose",
        "S": "You win"
    }

    paper_choice_dictionary = {
        "R": "You win",
        "P": "Tie",
        "S": "You lose"
    }

    scissors_choice_dictionary = {
        "R": "You lose",
        "P": "You win",
        "S": "Tie"
    }

    user_choice_dictionary = {
        "R": rock_choice_dictionary,
        "P": paper_choice_dictionary,
        "S": scissors_choice_dictionary
    }

    return user_choice_dictionary


def build_choice_name_dictionary():
    """
    Create and return a dictionary that translates short letter codes
    into full words.

    This is useful because the game uses short keys like:
        R, P, S

    But when we print results for humans, we want:
        Rock, Paper, Scissors

    Example:
        choice_names["R"] -> "Rock"
    """
    return {
        "R": "Rock",
        "P": "Paper",
        "S": "Scissors"
    }


def get_computer_choice():
    """
    Randomly select and return one of the valid computer choices.

    We use random.choice() on a list of the valid keys:
        ["R", "P", "S"]

    Returns:
        str: One of "R", "P", or "S"
    """
    valid_choices = ["R", "P", "S"]
    return random.choice(valid_choices)


def get_user_choice():
    """
    Ask the user to enter Rock, Paper, or Scissors using
    the letters R, P, or S.

    This function keeps asking until the user enters a valid choice.

    Returns:
        str: The validated user choice as "R", "P", or "S"
    """
    while True:
        user_choice = input("Enter R for Rock, P for Paper, or S for Scissors: ").upper().strip()

        if user_choice in ["R", "P", "S"]:
            return user_choice

        print("Invalid choice. Please enter only R, P, or S.")


def look_up_game_result(user_choice, computer_choice, game_rules):
    """
    Use the dictionary-of-dictionaries to determine the game result.

    Dictionary behavior being used:
    1. We access the OUTER dictionary with the user's choice.
       Example:
           game_rules[user_choice]

       This returns the inner dictionary for that user's move.

    2. We then access the INNER dictionary with the computer's choice.
       Example:
           game_rules[user_choice][computer_choice]

       This returns the final result string.

    Example:
        game_rules["R"]["S"] -> "You win"

    Parameters:
        user_choice (str): "R", "P", or "S"
        computer_choice (str): "R", "P", or "S"
        game_rules (dict): The dictionary-of-dictionaries containing all rules

    Returns:
        str: "Tie", "You win", or "You lose"
    """
    return game_rules[user_choice][computer_choice]


def display_round_result(user_choice, computer_choice, result, choice_names):
    """
    Display the choices and the result in a readable format.

    We use the choice_names dictionary to translate letter codes
    into full words.

    Example:
        choice_names["R"] -> "Rock"
    """
    print()
    print(f"You chose: {choice_names[user_choice]}")
    print(f"Computer chose: {choice_names[computer_choice]}")
    print(f"Result: {result}")
    print()


def ask_if_user_wants_to_play_again():
    """
    Ask the user if they want to play another round.

    Returns:
        bool:
            True if the user wants to continue
            False if the user wants to stop
    """
    while True:
        answer = input("Would you like to play again? (Y/N): ").upper().strip()

        if answer == "Y":
            return True
        if answer == "N":
            return False

        print("Invalid choice. Please enter Y or N.")


def play_one_round(game_rules, choice_names):
    """
    Play one complete round of Rock, Paper, Scissors.

    This function coordinates several smaller functions:
    - get the user's choice
    - get the computer's choice
    - look up the result in the dictionary-of-dictionaries
    - display the result
    """
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = look_up_game_result(user_choice, computer_choice, game_rules)
    display_round_result(user_choice, computer_choice, result, choice_names)


def run_rock_paper_scissors_game():
    """
    Run the full Rock, Paper, Scissors game loop.

    This function sets up the needed dictionaries once, then keeps
    playing rounds until the user decides to stop.

    Why this design is nice:
    - Each function has one job
    - The program is easier to read
    - The program is easier to test
    - The dictionary-of-dictionaries keeps the game logic organized
    """
    game_rules = build_game_rules()
    choice_names = build_choice_name_dictionary()

    print("Welcome to Rock, Paper, Scissors!")
    print("We are using a dictionary-of-dictionaries to determine the result.")
    print()

    while True:
        play_one_round(game_rules, choice_names)

        if not ask_if_user_wants_to_play_again():
            print("\nThanks for playing!")
            break


# This line starts the program.
run_rock_paper_scissors_game()