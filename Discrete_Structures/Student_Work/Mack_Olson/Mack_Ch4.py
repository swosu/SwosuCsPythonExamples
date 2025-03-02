import math
import time
import matplotlib.pyplot as plt

def count_primes(limit_value):
    """Returns the number of prime numbers less than limit_value using the Sieve of Eratosthenes."""
    if limit_value < 2:
        return 0
    sieve = [True] * limit_value
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for number in range(2, int(limit_value**0.5) + 1):
        if sieve[number]:
            for multiple in range(number * number, limit_value, number):
                sieve[multiple] = False
    return sum(sieve)

# Values to check
limit_values = [10, 100, 1000, 10000, 100000, 1000000]
prime_counts = []
execution_times = []

for limit_value in limit_values:
    start_time = time.time()
    prime_count = count_primes(limit_value)
    elapsed_time = time.time() - start_time
    prime_counts.append(prime_count)
    execution_times.append(elapsed_time)
    print(f"Number of primes less than {limit_value}: {prime_count} (Calculated in {elapsed_time:.6f} seconds)")

# Predict primes less than 10 million using the Prime Number Theorem
prediction_limit = 10_000_000
predicted_prime_count = prediction_limit / math.log(prediction_limit)
prediction_time_start = time.time()
print(f"Predicted number of primes less than {prediction_limit}: {int(predicted_prime_count)}")
prediction_time_elapsed = time.time() - prediction_time_start
print(f"Time taken to predict: {prediction_time_elapsed:.6f} seconds")

# Plot execution time
plt.figure(figsize=(8, 5))
plt.plot(limit_values, execution_times, marker='o', linestyle='-', label='Execution Time')
plt.xlabel('Limit Value')
plt.ylabel('Time (seconds)')
plt.title('Execution Time for Counting Primes')
plt.grid(True, linestyle="--", linewidth=0.5)
plt.legend()
plt.show()
