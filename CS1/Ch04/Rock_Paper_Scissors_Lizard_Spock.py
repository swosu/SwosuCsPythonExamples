"""
This is a twist on the classic Rock Paper Scissors game. This version is called Rock Paper Scissors Lizard Spock.
I am going to implement this using a dictionary of dictionaries.
The outer dictionary will contain the choices, 
and the inner dictionaries will contain the choices that the outer choice can beat.

The rules are:
Scissors cuts Paper
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporizes Rock
(and as it always has) Rock crushes Scissors


The program will:
- Prompt the user to select a choice
- Randomly select a choice for the computer
- Determine the winner
- Display the winner

The program will continue to run until the user decides to quit.
"""

import random

def print_choices(user_choice, computer_choice):
    choices = {1: 'Rock', 2: 'Paper', 3: 'Scissors', 4: 'Lizard', 5: 'Spock'}
    print('You chose:', choices[user_choice])
    print('The computer chose:', choices[computer_choice])

def dictionary_of_user_choices(user_choice, computer_choice):
    #print('made it to dictionary_of_user_choices')
    user_selection_dictionary = { 
        1: user_picked_rock_computer_dictionary(computer_choice),
        2: user_picked_paper_computer_dictionary(computer_choice),
        3: user_picked_scissors_computer_dictionary(computer_choice),
        4: user_picked_lizard_computer_dictionary(computer_choice),
        5: user_picked_spock_computer_dictionary(computer_choice)
    }
    return user_selection_dictionary[user_choice]

def user_picked_rock_computer_dictionary(computer_choice):
    #print('made it to user_picked_rock_computer_dictionary')    
    rock_dictionary = {
        1: 'It\'s a tie!',
        2: 'Paper covers Rock. You lose!',
        3: 'Rock crushes Scissors. You win!',
        4: 'Rock crushes Lizard. You win!',
        5: 'Spock vaporizes Rock. You lose!'
    }
    return rock_dictionary[computer_choice]

def user_picked_paper_computer_dictionary(computer_choice):
    paper_dictionary = {
        1: 'Paper covers Rock. You win!',
        2: 'It\'s a tie!',
        3: 'Scissors cuts Paper. You lose!',
        4: 'Lizard eats Paper. You lose!',
        5: 'Paper disproves Spock. You win!'
    }
    return paper_dictionary[computer_choice]

def user_picked_scissors_computer_dictionary(computer_choice):
    scissors_dictionary = {
        1: 'Rock crushes Scissors. You lose!',
        2: 'Scissors cuts Paper. You win!',
        3: 'It\'s a tie!',
        4: 'Scissors decapitates Lizard. You win!',
        5: 'Spock smashes Scissors. You lose!'
    }
    return scissors_dictionary[computer_choice]

def user_picked_lizard_computer_dictionary(computer_choice):
    lizard_dictionary = {
        1: 'Rock crushes Lizard. You lose!',
        2: 'Lizard eats Paper. You win!',
        3: 'Scissors decapitates Lizard. You lose!',
        4: 'It\'s a tie!',
        5: 'Lizard poisons Spock. You win!'
    }
    return lizard_dictionary[computer_choice]

def user_picked_spock_computer_dictionary(computer_choice):
    spock_dictionary = {
        1: 'Spock vaporizes Rock. You win!',
        2: 'Paper disproves Spock. You lose!',
        3: 'Spock smashes Scissors. You win!',
        4: 'Lizard poisons Spock. You lose!',
        5: 'It\'s a tie!'
    }
    return spock_dictionary[computer_choice]
    
if __name__ == "__main__":
    print('Welcome to Rock Paper Scissors Lizard Spock!')

    print('Here are your options to choose from:')
    print('1. Rock\t2. Paper\t3. Scissors\t4. Lizard\t5. Spock\t6. Quit')
    
    user_choice = input('Please select your choice: ')
    try:
        user_choice = int(user_choice)
    except ValueError:
        print('Invalid choice. Please select a number from 1 to 6.')
        user_choice = 0

    while user_choice != 6:
        computer_choice = random.randint(1, 5)
        print_choices(user_choice, computer_choice)
        print(dictionary_of_user_choices(user_choice, computer_choice))

        user_choice = input('Please select your choice: ')
        try:
            user_choice = int(user_choice)
        except ValueError:
            print('Invalid choice. Please select a number from 1 to 6.')
            user_choice = 0

