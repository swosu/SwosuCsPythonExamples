def SieveOfEratosthenes(num):
    prime = [True for i in range(num+1)]
    p = 2
    primes = []
    while (p * p <= num):
        if (prime[p] == True):
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
    for p in range(2, num+1):
        if prime[p]:
            primes.append(p)
    return primes

def fib(amountReturn):
    primes = SieveOfEratosthenes(100000)
    #print(f"primes{primes}")
    fibList = [0,1]
    primeFiblist = []
    for i in range(amountReturn):
        num = fibList[-2]
        numTwo = fibList[-1]
        nextNum = num + numTwo
        if nextNum in primes:
            primeFiblist.append(nextNum)
        fibList.append(nextNum)
    #print(f"fibList{fibList}")
    return primeFiblist

#check if numbers in prime list and fib list are actually matching
print(f'Prime numbers in the Fibonacci sequence up to 100 thousand, {fib(10000)}')

