import random
import multiprocessing
from itertools import product
import time

class FindXandY:
    def __init__(self):
        random.seed(42)
        self.range_magnitude = 10000
        self.x = random.randint(0, self.range_magnitude)
        self.y = random.randint(0, self.range_magnitude)
        self.a = random.randint(0, 100)
        self.b = random.randint(0, 100)
        self.c = self.a * self.x + self.b * self.y
        self.d = random.randint(0, 100)
        self.e = random.randint(0, 100)
        self.f = self.d * self.x + self.e * self.y
        self.search_magnitude = 1
        self.found = multiprocessing.Value('i', 0)
    
    def print_question(self):
        print(f"Given the following equations:\n{self.a}x + {self.b}y = {self.c}\n{self.d}x + {self.e}y = {self.f}\nFind x and y")
        print(f"Hint: x and y are integers, and x, y >= 0")
        print(f"hint hint hint x = {self.x}, y = {self.y}")

    def search_worker(self, x_value, y_range, found, result_queue):
        for y_guess in y_range:
            if found.value:
                return  # Stop if another process already found the solution
            if self.a * x_value + self.b * y_guess == self.c and self.d * x_value + self.e * y_guess == self.f:
                with found.get_lock():
                    found.value = 1
                result_queue.put((x_value, y_guess))
                return
    
    def find_x_and_y_parallel(self):
        num_workers = multiprocessing.cpu_count()
        manager = multiprocessing.Manager()
        result_queue = manager.Queue()
        found = self.found
        
        while True:
            x_values = range(-self.search_magnitude, self.search_magnitude)
            y_range = range(-self.search_magnitude, self.search_magnitude)
            
            processes = [multiprocessing.Process(target=self.search_worker, args=(x, y_range, found, result_queue))
                         for x in x_values]
            
            for p in processes:
                p.start()
            for p in processes:
                p.join()
            
            if not result_queue.empty():
                x, y = result_queue.get()
                print(f"x = {x}, y = {y}")
                return
            
            self.search_magnitude *= 2
            print('Doubled the search magnitude')

if __name__ == "__main__":
    print("hello")
    our_object = FindXandY()
    our_object.print_question()
    stat_time = time.time()
    our_object.find_x_and_y_parallel()
    elapsed_time = time.time() - stat_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")