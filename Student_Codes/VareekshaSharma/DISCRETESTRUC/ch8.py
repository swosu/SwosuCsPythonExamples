"""trying out sieve of eratosthenes and finding primes less than 10000
and use the fibbonacci sequece as well"""



"""
def SoEin(number):

if __name__ == '__main__':
"""

def is_prime(number):
    """Return True if number is prime, False otherwise."""
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True

def fibonacci_primes(limit):
    """Return a list of prime numbers in the Fibonacci sequence up to limit."""
    fibonacci_sequence = [0, 1]
    fibonacci_primes_list = []
    for count in range(2, limit):
        fibonacci_sequence.append(fibonacci_sequence[count-1] + fibonacci_sequence[count-2])
        if is_prime(fibonacci_sequence[count]):
            fibonacci_primes_list.append(fibonacci_sequence[count])
    return fibonacci_primes_list

def sieve_of_eratosthenes(limit):
    """Return a list of prime numbers up to limit using Sieve of Eratosthenes algorithm."""
    primes = [True] * (limit+1)
    primes[0] = primes[1] = False
    for number in range(2, int(limit ** 0.5)+1):
        if primes[number]:
            for multiple in range(number**2, limit+1, number):
                primes[multiple] = False
    return [number for number in range(limit+1) if primes[number]]

fibonacci_primes_list = fibonacci_primes(10000)
filtered_fibonacci_primes_list = [prime for prime in fibonacci_primes_list if prime < 10000]
sieve_of_eratosthenes_list = sieve_of_eratosthenes(10000)

print(f"Prime numbers in Fibonacci sequence up to 10000 are: {filtered_fibonacci_primes_list}")
print(f"Prime numbers less than 10000 using Sieve of Eratosthenes algorithm are: {sieve_of_eratosthenes_list}")

