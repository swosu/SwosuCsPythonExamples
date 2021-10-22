"""
Given the code that reads a list of integers,
complete the number_guess() function,
which should choose a random number
between 1 and 100 by calling
random.randint() and then output if the guessed number is too low,
too high, or correct.

Import the random module to use the random.seed()
and random.randint() functions.

random.seed(seed_value) seeds the random number generator
using the given seed_value.
random.randint(a, b) returns a random number between a and b (inclusive).
For testing purposes, use the seed value 900,
which will cause the computer to choose the same random
number every time the program runs.

Ex: If the input is:

32 45 48 80
the output is:

32 is too low. Random number was 80.
45 is too high. Random number was 30.
48 is correct!
80 is too low. Random number was 97.
"""
import guess_number_utilities

guess_number_utilities.greetUser()

our_random_number = guess_number_utilities.generate_random_number()
print('our randome number is ', str(our_random_number))

user_was_wrong = True

while(user_was_wrong):
    user_guess = guess_number_utilities.get_user_guess()
    print('your guess was: ', str(user_guess))
    user_was_wrong = \
        guess_number_utilities.was_answer_correct(our_random_number,user_guess)
    if user_was_wrong:
        guess_number_utilities.give_user_a_hint(our_random_number,user_guess)
