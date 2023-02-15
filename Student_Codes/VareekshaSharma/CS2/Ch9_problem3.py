"""26.22 LAB: Find the maximum in a list

Clone
Edit lab

Note
Complete the find_max() instance method in the Numbers class 
that returns the largest value in list nums.

Ex: If the list is:

[331, 970, 154, 404, 666, 49, 74, 840, 548, 96]
the output is:

[331, 970, 154, 404, 666, 49, 74, 840, 548, 96]
970
Note: During development, list nums is filled with 10 pseudo-random 
integers in main() using the fill_randomly() instance method from 
the Numbers class with a seed value of 7. When submitted, different 
seed values will be used to generate lists of different size for 
the test cases. Refer to the textbook section on Random numbers 
to learn more about pseudo-random numbers.


Starter Code"""

import random

class Numbers:
    def __init__(self):
        self.nums = []
    
    def get_nums(self):
        return self.nums
        
    def set_nums(self, nums):
        self.nums = []
        self.nums = nums[:]
        
    def find_max(self):
        # Type your code here
        
    def fill_randomly(self, seed, size):
        self.nums = []
        random.seed(seed)
        for index in range(size):
            self.nums.append(random.randint(0, 1000))
    
if __name__ == "__main__":
    my_numbers = Numbers()
    my_numbers.fill_randomly(7, 10) # Fill nums with 10 pseudo-random numbers using seed value 7
    print(my_numbers.get_nums())
    print(my_numbers.find_max())