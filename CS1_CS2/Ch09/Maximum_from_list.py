import random

class Numbers:
    def get_nums(self):
        return self.nums
    
    def __init__(self):
        self.nums = []
    
    def fill_randomly(self, seed, num):
        random.seed(seed)
        for index in range(num):
            self.nums.append(random.randint(0, 100))
    
    def print(self):
        print(self.nums)
    
    def sum(self):
        total = 0
        for i in self.nums:
            total += i
        return total
    
    def average(self):
        return self.sum() / len(self.nums)
    
    def min(self):
        return min(self.nums)
    
    def max(self):
        return max(self.nums)
    
    def count(self):
        return len(self.nums)
    
    def clear(self):
        self.nums = []


if __name__ == "__main__":
    my_numbers = Numbers()
    my_numbers.fill_randomly(7, 10) 
    # Fill nums with 10 pseudo-random numbers using seed value 7
    my_numbers.print() # Print the list of numbers
    print(my_numbers.get_nums()) # Print the list of numbers