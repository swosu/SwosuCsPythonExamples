# heads or tails game
print('Welcome to our heads or tails game!')

# Get user selection
user_selection = \
input('please press 1 for heads or 2 for tails and then press enter')

if str(1) == user_selection:
    print('you selected heads')
elif str(2) == user_selection:
    print('you selected tails')
else:
    print("you didn't follow instructions...")
    user_selection = \
    input('please press 1 for heads or 2 for tails and then press enter')

# get flip result
from random import random
random_number = random()
if 0.5 <= random_number:
    print(f'{random_number:.3f} is greater than or equal to 0.5.')
    flip_result = "1"
else:
    print(f'{random_number:.3f} is less than 0.5.')
    flip_result = "2"

if str(1) == flip_result:
    print('computer selected heads')
elif str(2) == flip_result:
    print('computer selected tails')


# if user selection matches flip result, user wins

if flip_result == user_selection:
    print("The user is the winner!")
else:
    print("The computer did not guess correctly.")

# else users does not win
