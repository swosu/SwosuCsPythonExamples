import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def is_prime(n):
    """
    Returns True if n is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def count_primes_less_than_x(x):
    """
    Counts the number of primes less than x.
    """
    print (x)
    count = 0
    for i in range(2, x):
        if is_prime(i):
            count += 1
    return count

# Generate a list of values of x
xs = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]
# Count the number of primes less than each value of x
counts = [count_primes_less_than_x(x) for x in xs]

# Fit a curve to the data
def func(x, a, b):
    return a * np.log(x) + b

popt, pcov = curve_fit(func, xs, counts)

# Plot the data and the fitted curve
plt.plot(xs, counts, 'o', label='data')
plt.plot(xs, func(xs, *popt), 'r-', label='fit')
plt.xlabel('x')
plt.ylabel('Number of primes less than x')
plt.legend()
plt.show()

# Estimate the number of primes less than a given value of x
x = 1000000000
estimated_count = func(x, *popt)
print(f"The estimated number of primes less than {x} is {int(estimated_count)}")
