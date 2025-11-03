import random

class GVDie_Class:  
   def __init__(self):      
      # set default values
      print('this is when our object is created.')
      self.my_value = random.randint(1, 6)
      self.rand = random.Random()
      # add a number of sides attribute that is hidden
      self.__number_of_sides = 6
      self.rolls = 0


   def roll(self):
        minimum_roll = 1
        self.my_value = self.rand.randint(minimum_roll, self.__number_of_sides)  
      
   # set the random number generator seed for testing
   def set_seed(self, seed):
        print('we are setting the seed to: ', seed)
        self.rand.seed(seed)
   
   # allows dice to be compared if necessary
   def compare_to(self, other):
       return self.my_value - d.my_value
       

def roll_total(die, total):
    print('this is our function')
    print('our total is: ', total)

    sub_total = 0
    rolls = 0
    while sub_total < total:
        die.roll()
        sub_total += die.my_value
        rolls += 1
        print(f'Rolled: {die.my_value}, subtotal: {sub_total}')
    return rolls


if __name__ == "__main__":
    print('hello and welcome to the main function' )
    die_object = GVDie_Class()   # Create a GVDie object
    other_object = GVDie_Class()

    dillon_die = GVDie_Class()
    jaydon_die = GVDie_Class()
    caspar_die = GVDie_Class()
    jeremy_die = GVDie_Class()
    breyden_die = GVDie_Class()

    our_seed = random.randint(1, 100)
    print('our seed is: ', our_seed)
    dillon_die.set_seed(our_seed)
    jaydon_die.set_seed(our_seed)
    caspar_die.set_seed(our_seed)
    jeremy_die.set_seed(our_seed)
    breyden_die.set_seed(our_seed)

    dillon_die.__number_of_sides = 4
    jaydon_die.__number_of_sides = 11
    caspar_die.__number_of_sides = 17
    jeremy_die.__number_of_sides = 8
    breyden_die.__number_of_sides = 9
    print('dillons dice has side count of : ', dillon_die.__number_of_sides)
    
    die_object.set_seed(15)   # Set the GVDie object with seed value 15
          
    total = random.randint(1, 100)
    print('the total you are rolling for is: ', total)
    dillon_die.rolls = roll_total(dillon_die, total) # Should return the number of rolls to reach total.
    caspar_die.rolls = roll_total(caspar_die, total) # Should return the number of rolls to reach total.
    jeremy_die.rolls = roll_total(jeremy_die, total) # Should return the number of rolls to reach total.
    breyden_die.rolls = roll_total(breyden_die, total) # Should return the number of rolls to reach total.
    jaydon_die.rolls = roll_total(jaydon_die, total) # Should return the number of rolls to reach total.
    #rolls = roll_total(die_object, total) # Should return the number of rolls to reach total.
    print(f'Dillon Number of rolls to reach at least {total}: {dillon_die.rolls}')
    print(f'Caspar Number of rolls to reach at least {total}: {caspar_die.rolls}')
    print(f'Jeremy Number of rolls to reach at least {total}: {jeremy_die.rolls}')
    print(f'Breyden Number of rolls to reach at least {total}: {breyden_die.rolls}')
    print(f'Jaydon Number of rolls to reach at least {total}: {jaydon_die.rolls}')