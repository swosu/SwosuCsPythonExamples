import time
import csv
import matplotlib.pyplot as plt

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def count_primes(limit):
    """Count the number of primes less than the limit."""
    count = 0
    for num in range(2, limit):
        if is_prime(num):
            count += 1
    return count

def log_execution_time(limit):
    """Count primes and log execution time."""
    start_time = time.time()
    prime_count = count_primes(limit)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return prime_count, elapsed_time

def write_results_to_csv(results, filename="prime_counts.csv"):
    """Write results to a CSV file."""
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Limit", "Prime Count", "Time Taken (s)"])
        for limit, prime_count, elapsed_time in results:
            writer.writerow([limit, prime_count, elapsed_time])

# Example usage
limits = [10, 100, 1000, 10000, 100000, 1000000]
results = []
for limit in limits:
    prime_count, elapsed_time = log_execution_time(limit)
    results.append((limit, prime_count, elapsed_time))
    print(f"Limit: {limit}, Prime Count: {prime_count}, Time Taken: {elapsed_time:.4f} seconds")

# Write to CSV
write_results_to_csv(results)

# Plotting the results
limits = [x[0] for x in results]
prime_counts = [x[1] for x in results]

plt.plot(limits, prime_counts, marker='o')
plt.xscale('log')
plt.yscale('log')
plt.xlabel("Limit (log scale)")
plt.ylabel("Number of Primes (log scale)")
plt.title("Log Plot of Prime Counts")
plt.grid(True)
plt.show()
