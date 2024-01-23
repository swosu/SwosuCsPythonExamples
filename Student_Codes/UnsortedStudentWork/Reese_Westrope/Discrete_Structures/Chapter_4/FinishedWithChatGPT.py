import numpy as np
import matplotlib.pyplot as plt

def sieve_of_eratosthenes(n):
    # Create a boolean array "prime[0..n]" and
    # initialize all entries it as true.
    prime = [True for i in range(n+1)]
    p = 2
    while(p * p <= n):
         
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
             
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    
    # Count the number of prime numbers
    count = 0
    for p in range(2, n):
        if prime[p]:
            count += 1
    return count

# Plot the number of primes less than n for different values of n
n_values = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
primes = [sieve_of_eratosthenes(n) for n in n_values]

plt.xscale("log")
plt.yscale("log")
plt.scatter(n_values, primes)
plt.xlabel("n")
plt.ylabel("Number of primes less than n")
plt.show()

# Print the number of primes less than 10 million
print("Number of primes less than 10 million:", sieve_of_eratosthenes(10000000))
