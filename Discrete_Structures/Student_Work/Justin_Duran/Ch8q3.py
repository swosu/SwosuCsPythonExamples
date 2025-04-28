def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False  # 0 and 1 are not prime numbers

    for num in range(2, int(limit**0.5) + 1):
        if is_prime[num]:
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False

    prime_count = sum(is_prime)
    return prime_count

# Get user input
num = int(input("Enter a number: "))
print(f"Number of primes not exceeding {num}: {sieve_of_eratosthenes(num)}")
