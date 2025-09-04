import random

choices = ['rock', 'paper', 'scissors']

# Player selection
player_choice = input("Choose rock, paper, or scissors: ").lower()
if player_choice not in choices:
    print("Invalid choice.")
else:
    # Computer selection
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("You lose!")