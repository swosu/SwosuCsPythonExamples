def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci_primes(limit):
    """Generate Fibonacci numbers and yield prime numbers."""
    a, b = 0, 1
    while a <= limit:
        if is_prime(a):
            yield a
        a, b = b, a + b

# Set the upper limit for Fibonacci numbers
limit = 1000

# Generate and print prime Fibonacci numbers up to the limit
for prime_fib in fibonacci_primes(limit):
    print(prime_fib)
