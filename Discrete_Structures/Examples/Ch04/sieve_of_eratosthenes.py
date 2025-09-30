def sieve(n: int) -> list[int]:
    """
    Return a list of all prime numbers <= n using the Sieve of Eratosthenes.
    """
    if n < 2:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False

    return [i for i, prime in enumerate(is_prime) if prime]


def prime_gaps(primes: list[int]) -> list[int]:
    """
    Given a list of primes, return the list of differences between consecutive primes.
    """
    return [primes[i + 1] - primes[i] for i in range(len(primes) - 1)]


def predict_next(primes: list[int], gaps: list[int], lookback: int = 5) -> int:
    """
    Predict the next prime based on the average of the last `lookback` prime gaps.
    """
    if len(gaps) < lookback:
        lookback = len(gaps)
    avg_gap = sum(gaps[-lookback:]) / lookback
    last_prime = primes[-1]
    return last_prime + round(avg_gap)


def main():
    # Step 1: Generate primes up to 1000
    primes = sieve(1000)
    print(f"Number of primes up to 1000: {len(primes)}")
    print(f"Last few primes: {primes[-10:]}")

    # Step 2: Calculate prime gaps
    gaps = prime_gaps(primes)
    print(f"Last 10 gaps: {gaps[-10:]}")

    # Step 3: Predict the next prime after 1000
    prediction = predict_next(primes, gaps, lookback=5)
    print(f"Predicted next prime around: {prediction}")

    # Step 4: Verify by extending the sieve
    extended_primes = sieve(1200)
    actual_next = [p for p in extended_primes if p > primes[-1]][0]
    print(f"Actual next prime: {actual_next}")
    print(f"Prediction error: {abs(actual_next - prediction)}")


if __name__ == "__main__":
    main()
