import random

def get_user_choice():
    while True:
        choice = input("Choose between tounge, eye, and hand: ").lower()
        if choice in ['tounge', 'eye', 'hand']:
            return choice
        else:
            print("Invalid choice. Please try again.")

def get_opponent_choice():
    choices = ['tounge', 'eye', 'hand']
    return random.choice(choices)

def determine_winner(user_choice, opponent_choice):
    if user_choice == opponent_choice:
        return "It's a tie!"
    elif (user_choice == 'tounge' and opponent_choice == 'hand') or \
         (user_choice == 'hand' and opponent_choice == 'eye') or \
         (user_choice == 'eye' and opponent_choice == 'tounge'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_name = input("Enter your name: ")
    opponent_name = "AI Opponent"
    user_score = 0
    opponent_score = 0

    while user_score < 3 and opponent_score < 3:
        print(f"\n{user_name}: {user_score} | {opponent_name}: {opponent_score}")
        user_choice = get_user_choice()
        opponent_choice = get_opponent_choice()
        print(f"{user_name} chose {user_choice}")
        print(f"{opponent_name} chose {opponent_choice}")
        result = determine_winner(user_choice, opponent_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            opponent_score += 1

    if user_score > opponent_score:
        print(f"\nCongratulations, {user_name}! You won the game!")
    else:
        print(f"\nSorry, {user_name}. You lost the game.")

play_game()
