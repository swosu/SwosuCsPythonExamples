import numpy as np
import matplotlib.pyplot as plt
import math

def is_prime(n):
    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def count_primes(n):
    count = 0
    for i in range(1, n):
        if is_prime(i):
            count += 1
    return count

n = [10, 100, 1000, 10000, 100000, 1000000]
primes = [count_primes(i) for i in n]

plt.plot(n, primes, 'o-')
plt.yscale('log')
plt.xlabel('n')
plt.ylabel('Number of primes less than n')
plt.title('Number of primes less than n')
plt.show()
