import time




if __name__ == '__main__':
    # make a list of fibonacci numbers
    fibo = [0, 1]

    # spend 3 seconds making the list as long as possible
    start_time = time.time()
    time_difference = 0
    while time_difference < 0.0001:
        current_time = time.time()

        time_difference = current_time - start_time
        
        
        fibo.append(fibo[-1] + fibo[-2])

        if len(fibo) % 10 == 0:
            print('time difference:', time_difference, 'seconds', end = ' ')
            print(' fibo length:', len(fibo), end = ' ')
            # print last 10 numbers
            print(fibo[-10:])


    # what was the largest number we calculated in fibo?
    max_fibo = fibo[-1]
    print('max_fibo:', max_fibo)

    # use the Sieve of Eratosthenes to find all the prime numbers up to max_fibo
    # assume all numbers are prime to start
    primes = [True] * (max_fibo + 1)
    primes[0] = False
    primes[1] = False

    # for each number up to the square root of max_fibo
    for i in range(2, int(max_fibo ** 0.5) + 1):
        # if the number is prime
        if primes[i]:
            # for each multiple of the number
            for j in range(i * i, max_fibo + 1, i):
                # mark the multiple as not prime
                primes[j] = False

    # print the primes
    print('primes:', end = ' ')
    # print the length of the primes list
    print('length:', len(primes), end = ' ')

    # print off the number of numbers in primes that are prime
    print('number of primes:', sum(primes))

    """
    # print the first 100 primes, 10 numbers to a row.
    for i in range(100):
        if primes[i]:
            print(i, end = ' ')
            if i % 10 == 9:
                print()
    print()
    """

    # print how many numbers are prime and fibonacci numbers
    print('primes and fibo:', end = ' ')
    count = 0
    for i in range(len(primes)):
        if primes[i] and i in fibo:
            count += 1
    print('the number of numbers in both lists is: ', count)

    # print the numbers that are prime and fibonacci numbers
    print('primes and fibo:', end = ' ')
    for i in range(len(primes)):
        if primes[i] and i in fibo:
            print(i, end = ' ')
    print()

    




   

