import random

print('we can make an addition quiz.')

import random

number_one = random.randint(0,10)
number_two = random.randint(0,50)

correct_number = number_one + number_two


while True:
    user_guess = input(f'what is {number_two} + {number_one}? ')
    print(f'that was {user_guess}.')
    if user_guess.isnumeric():
        user_guess = int(user_guess)
        if user_guess < correct_number:
            print('that was too low')
        elif user_guess > correct_number:
            print('too high')
        elif user_guess == correct_number:
            print('that was correct!')
            break
    else:
        print('that was not a good guess.')