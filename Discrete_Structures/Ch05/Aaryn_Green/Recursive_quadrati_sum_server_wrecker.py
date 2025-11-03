import math
import time
import random

def recursive_quadratic_sum(n):
    """Recursively calculates the sum of squares from 1 to n."""
    if n == 1:
        return 1
    else:
        return n * n + recursive_quadratic_sum(n - 1)

def measure_performance(n):
    """Measures the performance of the recursive quadratic sum function."""
    start_time = time.time()
    result = recursive_quadratic_sum(n)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Sum of squares from 1 to {n} is {result}.")
    print(f"Execution time: {execution_time:.6f} seconds.")

if __name__ == "__main__":
    n = random.randint(10000, 1000000)  # You can change the range for different performance tests
    measure_performance(n)
