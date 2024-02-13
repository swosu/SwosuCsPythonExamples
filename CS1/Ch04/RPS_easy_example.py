# start

# list of choices
possible_choices = ["r", "p", "s"]

# tell the user what the choices are and what to enter for each choice
print('Welcome to the game of rock, paper, scissors!')
print('Enter "r" for rock') 
print('Enter "p" for paper')
print('Enter "s" for scissors')

# get user input
user_choice = input('Enter your choice: ')

if "r" == user_choice:
    print('You chose rock!')
elif "p" == user_choice:
    print('You chose paper!')
elif "s" == user_choice:
    print('You chose scissors!')
else:
    print('Invalid choice')

# get computer choice
# import the random module
import random
# get a random number between 0 and 2
computer_choice = random.choice(possible_choices)

# print the computer's choice
if "r" == computer_choice:
    print('The computer chose rock!')
elif "p" == computer_choice:
    print('The computer chose paper!')
elif "s" == computer_choice:
    print('The computer chose scissors!')
else:
    print('Invalid computer choice')

# if user selects rock

if "r" == user_choice:
    if "r" == computer_choice:
        print("It's a tie!")
    elif "p" == computer_choice:
        print("You lose!")
    elif "s" == computer_choice:
        print("You win!")
    else:
        print("Invalid computer choice")

elif "p" == user_choice:
    if "r" == computer_choice:
        print("You win!")
    elif "p" == computer_choice:
        print("It's a tie!")
    elif "s" == computer_choice:
        print("You lose!")
    else:
        print("Invalid computer choice")

elif "s" == user_choice:
    if "r" == computer_choice:
        print("You lose!")
    elif "p" == computer_choice:
        print("You win!")
    elif "s" == computer_choice:
        print("It's a tie!")
    else:
        print("Invalid computer choice")
else:
    print("Invalid user choice")