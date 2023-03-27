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
	prime = [True for i in range(num+1)]
	p = 2
	primes  = []
	while (p * p <= num):

		if (prime[p] == True):

			# Updating all multiples of p
			for i in range(p * p, num+1, p):
				prime[i] = False
		p += 1

	for p in range(2, num+1):
		if prime[p]:
			primes.append(p)
	
	return primes

fiblist = fib(10000000)
primeslist = SieveOfEratosthenes(100000)
#print(fiblist)
#print(primeslist)

for i in primeslist:
	if i in fiblist:
		print(i)

