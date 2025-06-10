import numpy as np
import matplotlib.pyplot as plt

def sieve_of_eratosthenes(limit):
    """ Returns a list of primes up to 'limit' """
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            sieve[i*i:limit+1:i] = False
    return np.where(sieve)[0]

def count_primes(limit):
    """ Returns the number of primes less than 'limit' """
    primes = sieve_of_eratosthenes(limit)
    return len(primes)

# Values to check: 10, 100, 1000, 10000, 100000, 1000000
limits = [10, 100, 1000, 10000, 100000, 1000000]
prime_counts = [count_primes(limit) for limit in limits]

# Plotting the log plot
plt.figure(figsize=(8, 6))
plt.plot(limits, prime_counts, 'bo-', label="Prime counts")
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Limit (log scale)')
plt.ylabel('Number of Primes (log scale)')
plt.title('Log Plot of Number of Primes Less Than Given Numbers')
plt.grid(True)
plt.legend()

# Display the plot
plt.show()

# Predicting the number of primes less than 10 million using the trend
predicted_primes_10_million = count_primes(10000000)
print(f"Number of primes less than 10 million: {predicted_primes_10_million}")
