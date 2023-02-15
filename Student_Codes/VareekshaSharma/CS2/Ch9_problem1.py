"""26.7 LAB: How many dice rolls?
Given a GVDie object and an integer that represents the total 
sum desired as parameters, complete function roll_total() that 
returns the number of rolls needed to achieve at least the total sum.

Note: For testing purposes, the GVDie object is created in the 
main() function using a pseudo-random number generator with a 
fixed seed value. The program uses a seed value of 15 during 
development, but when submitted, a different seed value will 
be used for each test case.

Ex: If the GVDie object is created with a seed value of 15 and
 the input of the program is:

20
the output is:

Number of rolls to reach at least 20: 8


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
       

def roll_total(die, total):
    # Type your code here

if __name__ == "__main__":
    die = GVDie()   # Create a GVDie object
    die.set_seed(15)   # Set the GVDie object with seed value 15
          
    total = int(input())
    rolls = roll_total(die, total) # Should return the number of rolls to reach total.
    print(f'Number of rolls to reach at least {total}: {rolls}')




