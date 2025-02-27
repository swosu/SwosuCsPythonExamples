import random
import time

class Find_x_and_y():
    def __init__(self):

        self.range_magnitude = 10000
        self.x = random.randint(-1 * self.range_magnitude, self.range_magnitude)
        self.y = random.randint(-1 * self.range_magnitude, self.range_magnitude)
        self.a = random.randint(0, 100)
        self.b = random.randint(0, 100)
        self.c = self.a * self.x + self.b * self.y
        self.d = random.randint(0, 100)
        self.e = random.randint(0, 100)
        self.f = self.d * self.x + self.e * self.y
        self.search_magnitude = 1

    def print_question(self):
        print(f"Given the following equations:\n{self.a}x + {self.b}y = {self.c}\n{self.d}x + {self.e}y = {self.f}\nFind x and y")
        print(f"Hint: You can use the substitution method or the elimination method")
        print(f"Note: x and y are integers, and x, y >= 0")
        print(f"hint hint hint x = {self.x}, y = {self.y}")

    def find_x_and_y(self):
        self.search_magnitude = 1
        while True:
            for x_guess in range(-1 * self.search_magnitude, self.search_magnitude):
                for y_guess in range(-1 * self.search_magnitude, self.search_magnitude):
                    if self.a * x_guess + self.b * y_guess == self.c and self.d * x_guess + self.e * y_guess == self.f:
                        print(f"x = {x_guess}, y = {y_guess}")
                        return
            self.search_magnitude = self.search_magnitude * 2
            print('doubled the search magnitude')








if __name__ == "__main__":
    print("hello")
    random.seed(42)
    our_object = Find_x_and_y()
    our_object.print_question()
    start_time = time.time()
    our_object.find_x_and_y()
    elapsed_time = time.time() - start_time
    


