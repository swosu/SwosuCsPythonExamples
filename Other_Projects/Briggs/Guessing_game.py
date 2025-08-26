print('we can make a guess the number game.')

import random

correct_number = random.randint(0,100)
#print(f'the random number is: {correct_number}.')

while True:
    user_guess = input('what number would you like to guess?')
    print(f'that was {user_guess}.')
    if user_guess.isnumeric():
        user_guess = int(user_guess)
        if user_guess < correct_number:
            print('that was too low, guess again...')
        elif user_guess > correct_number:
            print('too high, guess again...')
        elif user_guess == correct_number:
            print('that was correct!')
            break
    else:
        print('that was not a good guess. Guess again.')