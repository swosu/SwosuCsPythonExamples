"""trying out sieve of eratosthenes and finding primes less than 10000
and use the fibbonacci sequence as well


"""

import math
import time

def is_prime(number):
    """Return True if number is prime, False otherwise."""
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for divisor in range(3, int(math.sqrt(number)) + 1, 2):
        if number % divisor == 0:
            return False
    return True

# def fibonacci_primes(limit):
    """Return list of prime numbers in the Fibonacci sequence up to limit."""
    fibonacci_sequence = [0, 1]
    fibonacci_primes_list = []
    for count in range(2, limit):
        fibonacci_number = fibonacci_sequence[count-1] + fibonacci_sequence[count-2]
        if fibonacci_number > limit:
            break
        fibonacci_sequence.append(fibonacci_number)
        # if is_prime(fibonacci_number):
            # fibonacci_primes_list.append(fibonacci_number)
    return fibonacci_sequence

def sieve_of_eratosthenes(limit):
    """Return list of prime numbers up to limit using segmented sieve of Eratosthenes algorithm."""
    segment_size = int(limit) + 1
    primes = [True] * segment_size
    primes[0] = primes[1] = False
    print(primes)

    for number in range(1, int(segment_size), 1):
        print(f'number before if: {number}')
        if primes[number]:
            print(f'number is {number} which is true in primes list')
            for multiple in range(number, segment_size, number):
                print(f'mults are {multiple}')
                primes[multiple] = False
                primes[number] = True
    print(primes)
    print("after for loop")

    results = []

    for number in range(1, int(segment_size), 1):
        if primes[number]:
            results.append(number)
    print(results)

    for low in range(segment_size, limit + 1, segment_size):
        high = min(low + segment_size, limit + 1)
        segment_primes = [True] * segment_size

        for number in range(3, int(math.sqrt(high)) + 1, 2):
            if primes[number]:
                start = (low // number) * number
                if start < low:
                    start += number
                for multiple in range(start, high, number):
                    segment_primes[multiple - low] = False

        results.extend([number for number in range(low + 1, high, 2) if segment_primes[number - low]])

    return results

if __name__ == '__main__':
    start_time = time.time()

    #fibonacci_primes_list = fibonacci_primes(10000)
    #filtered_fibonacci_primes_list = [prime for prime in fibonacci_primes_list if prime < 10000]
    sieve_of_eratosthenes_list = sieve_of_eratosthenes(100)

    end_time = time.time()

    # prime_fib_intersect = list(set(fibonacci_primes_list) & set(sieve_of_eratosthenes_list))

    # print(f"Prime numbers in Fibonacci sequence up to 10000 are: {filtered_fibonacci_primes_list}")
    print(f"Prime numbers less than 100 using Sieve of Eratosthenes algorithm are: {sieve_of_eratosthenes_list}")
    # print(prime_fib_intersect)
    print(f"Time taken: {end_time - start_time:.5f} seconds")

