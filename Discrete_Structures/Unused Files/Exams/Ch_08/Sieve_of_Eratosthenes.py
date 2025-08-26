import time

if __name__ == '__main__':
    print('hello world')

    # start a timer
    start = time.time()

    # 1. Create a list of all numbers from 2 to n
    n = 1_000_000 
    numbers = list(range(2, n+1))

    # 2. Create a list of primes
    primes = []

    # 3. While the list of numbers is not empty

    while len(numbers) > 0:
        # 4. Remove the first number from the list of numbers, and append it to the list of primes
        primes.append(numbers[0])
        # 5. Remove all multiples of the number from the list of numbers
        numbers = [x for x in numbers if x % numbers[0] != 0]

    # stop the timer
    end = time.time()
    print(primes)

    # how many primes are there?
    print(len(primes))

    # how long did it take?
    print(end - start)