import random
import multiprocessing
import time
import csv
import psutil
import os
from itertools import product

class FindXandY:
    def __init__(self, seed, range_magnitude):
        random.seed(seed)
        self.range_magnitude = range_magnitude
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
    
    def search_worker(self, x_value, y_range, found, result_queue):
        for y_guess in y_range:
            if found.value:
                return
            if self.a * x_value + self.b * y_guess == self.c and self.d * x_value + self.e * y_guess == self.f:
                with found.get_lock():
                    found.value = 1
                result_queue.put((x_value, y_guess))
                return
    
    def find_x_and_y_parallel(self):
        manager = multiprocessing.Manager()
        result_queue = manager.Queue()
        found = self.found
        
        start_time = time.time()
        start_cpu = psutil.cpu_percent(interval=None)
        
        while True:
            x_values = range(-self.search_magnitude, self.search_magnitude)
            y_values = list(range(-self.search_magnitude, self.search_magnitude))
            
            processes = []
            for x in x_values:
                p = multiprocessing.Process(target=self.search_worker, args=(x, y_values, found, result_queue))
                processes.append(p)
                p.start()
            
            for p in processes:
                p.join()
            
            if not result_queue.empty():
                x, y = result_queue.get()
                end_time = time.time()
                end_cpu = psutil.cpu_percent(interval=None)
                return x, y, end_time - start_time, end_cpu
            
            self.search_magnitude *= 2
    
    def find_x_and_y_sequential(self):
        start_time = time.time()
        start_cpu = psutil.cpu_percent(interval=None)
        
        self.search_magnitude = 1
        while True:
            for x_guess in range(-self.search_magnitude, self.search_magnitude):
                for y_guess in range(-self.search_magnitude, self.search_magnitude):
                    if self.a * x_guess + self.b * y_guess == self.c and self.d * x_guess + self.e * y_guess == self.f:
                        end_time = time.time()
                        end_cpu = psutil.cpu_percent(interval=None)
                        return x_guess, y_guess, end_time - start_time, end_cpu
            self.search_magnitude *= 2

if __name__ == "__main__":
    seeds = [5, 14, 24, 42]
    range_magnitudes = [10, 100, 200, 300, 500, 1000]
    results_file = os.path.join(os.path.dirname(__file__), "results.csv")

    
    if os.path.exists(results_file):
        with open(results_file, "r") as f:
            existing_results = set(tuple(row[:2]) for row in csv.reader(f))
    else:
        existing_results = set()
    
    with open(results_file, "a", newline="") as f:
        writer = csv.writer(f)
        if not existing_results:
            writer.writerow(["Seed", "Range Magnitude", "X_parallel", "Y_parallel", "Time_parallel", "CPU_parallel", "X_sequential", "Y_sequential", "Time_sequential", "CPU_sequential"])
        
        for seed in seeds:
            for magnitude in range_magnitudes:
                if (str(seed), str(magnitude)) in existing_results:
                    print(f"Skipping Seed={seed}, Magnitude={magnitude} (Already Computed)")
                    continue
                
                print(f"Running Seed={seed}, Magnitude={magnitude}")
                parallel_solver = FindXandY(seed, magnitude)
                x_p, y_p, time_p, cpu_p = parallel_solver.find_x_and_y_parallel()
                
                sequential_solver = FindXandY(seed, magnitude)
                x_s, y_s, time_s, cpu_s = sequential_solver.find_x_and_y_sequential()
                
                writer.writerow([seed, magnitude, x_p, y_p, time_p, cpu_p, x_s, y_s, time_s, cpu_s])
                f.flush()
    
    print("Results saved to results.csv")
