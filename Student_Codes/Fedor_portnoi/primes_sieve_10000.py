n = 10000
sieve = [True] * (n + 1)
sieve[0] = sieve[1] = False

import math
for p in range(2, int(math.isqrt(n)) + 1):
    if sieve[p]:
        start = p * p
        sieve[start:n+1:p] = [False] * (((n - start) // p) + 1)

primes = [i for i, is_prime in enumerate(sieve) if is_prime]
print(len(primes))          # count of primes ≤ 10,000
print(primes[:10])          # first few
print(primes[-10:])         # last few
