from random import randint

class RandomNumbers:
    # Type your code here.
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.num3 = 0

    def set_rand_nums(self, low, high):
        self.num1 = randint(0, high-low)
        self.num2 = randint(0, high-low)
        self.num3 = randint(0, high-low)
    
    def get_rand_nums(self):
        print(f'The three random values from the range {high} to {low} are: {self.num1}, {self.num2}, and {self.num3}')
    

if __name__ == "__main__":
    low = int(input("Enter the minimum value: "))
    high = int(input("Enter the maximum value: "))

    numbers = RandomNumbers()
    numbers.set_rand_nums(low, high)
    numbers.get_rand_nums()

