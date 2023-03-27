import time

def fib(amountReturn):
    fibList = [0,1]
    primeFiblist = []
    for i in range(amountReturn):
        num = fibList[-2]
        numTwo = fibList[-1]
        nextNum = num + numTwo
        fibList.append(nextNum)
    return fibList

def SieveOfEratosthenes(num):
    fibList = fib(100000)
    #print(fibList)
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
    for f in primes:
        if f in fibList:
            print(f)
    print("Done")
    #return primes

SieveOfEratosthenes(1000000)
#print(SieveOfEratosthenes(100))