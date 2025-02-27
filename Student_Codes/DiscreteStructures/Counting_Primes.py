def sieve_of_eratosthenes(limit):
    """Return a list of all prime numbers up to the given limit."""
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    for num in range(2, int(limit**0.5) + 1):
        if is_prime[num]:
            for multiple in range(num*num, limit + 1, num):
                is_prime[multiple] = False

    primes = [num for num in range(limit + 1) if is_prime[num]]
    return primes

def find_primes_until_limit(limit):
    """Find all prime numbers until the prime number hits above or equal to the limit."""
    primes = sieve_of_eratosthenes(limit)
    count = 0
    for prime in primes:
        if prime >= limit:
            break
        count += 1
    return primes[:count], count

# Find all prime numbers until the prime number hits above or equal to 10,000
limit = 10000
primes, count = find_primes_until_limit(limit)
print(f"Prime numbers until {limit} are: {primes}")
print(f"Total number of primes until {limit}: {count}")
