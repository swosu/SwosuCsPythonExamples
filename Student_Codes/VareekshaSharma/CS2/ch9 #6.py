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


def roll_specific_number(die, num, goal):
    target = 0
    total_rolls = 0
    while target < goal:
        die.roll()
        if num == die.my_value:
            target += 1
        total_rolls += 1
    return total_rolls

if __name__ == "__main__":
    die = GVDie()   # Create a GVDie object
    die.set_seed(15)   # Set the GVDie object with seed value 15
          
    num = int(input("enter a number you would like to roll (1-6): "))
    goal = int(input(f"how many times would you like to roll {num}? "))
    rolls = roll_specific_number(die, num, goal) # Call roll_specific_number() and return number of rolls.
    print(f'It took {rolls} rolls to get a \"{num}\" {goal} times.')