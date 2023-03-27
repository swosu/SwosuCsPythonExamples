import time

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
    primeList = SieveOfEratosthenes(100000)
    fibList = [0,1]
    primeFiblist = []
    for i in range(amountReturn):
        num = fibList[-2]
        numTwo = fibList[-1]
        nextNum = num + numTwo
        fibList.append(nextNum)
    for f in fibList:
        if f in primeList:
            primeFiblist.append(f)
    return primeFiblist

print(fib(10000))
