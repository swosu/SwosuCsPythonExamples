"""26.16 LAB: Rolling for a pair
Given two GVDie objects that represent 2 six-sided dice and an
integer that represents a desired value as parameters, complete 
the function rolling_for_pair(). The function rolling_for_pair() 
rolls the dice until a pair with the desired value is rolled and 
then returns the number of rolls thrown to achieve the result. 
Assume the desired value received from input is within the 
appropriate range, 1-6.

Note: For testing purposes, the GVDie objects are created in 
the main() function using a pseudo-random number generator 
with a fixed seed value. The program uses a seed value of 15 
during development, but when submitted, a different seed 
value will be used for each test case.

Ex: If the GVDie objects are created with a seed value of 15 
and the input of the program is:

3
the output is:

It took 13 rolls to get a pair of 3's.


Starter Code"""

import random

class GVDie:  
   def __init__(self):      
      # set default values
      self.my_value = random.randint(1, 6)
      self.rand = random.Random()

   def roll(self):
       self.my_value = self.rand.randint(1, 6)  
      
   # set the random number generator seed for testing
   def set_seed(self, seed):
       self.rand.seed(seed)
   
   # allows dice to be compared if necessary
   def compare_to(self, other):
       return self.my_value - d.my_value
       

def rolling_for_pair(d1, d2, val):
    # Type your code here

if __name__ == "__main__":
    die1 = GVDie()   # Create a GVDie object
    die2 = GVDie()   # Create a second GVDie object
    die1.set_seed(15)   # Set the first GVDie object with seed value 15
    die2.set_seed(15)   # Set the second GVDie object with seed value 15
          
    val = int(input())
    rolls = rolling_for_pair(die1, die2, val) # Should return the number of rolls to reach total.
    print(f'It took {rolls} rolls to get a pair of {val}\'s.')
