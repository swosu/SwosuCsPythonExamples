import matplotlib.pyplot as plt

def count_primes(n):
    if n <= 2:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers
    p = 2
    while p * p < n:
        if primes[p]:
            for i in range(p * p, n, p):
                primes[i] = False
        p += 1
    number_of_primes = sum(primes)
    return number_of_primes

# Generate data for the plot
max_n = 100
x_values = list(range(2, max_n + 1))
y_values = [count_primes(x) for x in x_values]

# Create a log plot
plt.figure()
plt.semilogy(x_values, y_values)
plt.title('Number of Primes Less Than N')
plt.xlabel('N')
plt.ylabel('Number of Primes (log scale)')
plt.grid(True)
plt.show()
