print('we can make a guess the number game.')

import random
import time
score = 0
print('starting the clock.')
start_time = time.time()
questions = 10

for round in range(0, questions):

    number_one = random.randint(0,10)
    number_two = random.randint(0,50)

    correct_number = number_one + number_two

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
            score = score + 1
    else:
        print('that was not a good guess.')

print('stop the clock.')
print(f'Time was: {time.time() - start_time} seconds.')
print(f'your score was: {score}.')
if questions == score:
    print('that was a perfect score')
elif (questions/2) < score:
    print('that was pretty good.')
elif (questions/4) < score:
    print('maybe you need a snack.')
else:
    print('maybe you should try a different computer...')