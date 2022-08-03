print('hello.')

# imports
from random import randint

# importing the module
import numpy as np

#  select distribution to simulate rolling a six sided die that is fair
# here is an example code:
# https://discuss.python.org/t/how-to-use-randit-with-the-random-module-to-create-a-six-sided-dice/9724
number_of_sides = 6
roll = randint(1, number_of_sides   )
print(f'our roll was {roll}.')

# set the bounds


#  Save the output
#we are going to save this to an array.
# creating the list
roll_result_25 = [0, 0, 0, 0, 0, 0]

# creating 1-d array
n = np.array(roll_result_25)
print(n)


# make a table for 25, 100, and 100,000 trials

# make a chart that shows the probability of each number
# occuring for each of these three scenarios
