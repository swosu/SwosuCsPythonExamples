import matplotlib.pyplot as plt
#A function to find all primes up to a given number
#The code is from geekforgeeks.org and was modified to return an array of primes instead of printing them individually
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

#A function that takes a array and makes a plot
def plot_primes(primes):
    x = []
    y = []
    for i in range(len(primes)):
        x.append(i)
        y.append(primes[i])
    plt.plot(x,y)
    plt.show()

if __name__ == '__main__':
	answer = input("Would you like to plot the primes? (y/n): ")
	if answer == "y":
		plot_primes(SieveOfEratosthenes(100))
		plot_primes(SieveOfEratosthenes(1000))
		plot_primes(SieveOfEratosthenes(10000))
		plot_primes(SieveOfEratosthenes(100000))
		plot_primes(SieveOfEratosthenes(1000000))
		plot_primes(SieveOfEratosthenes(10000000))
	print("Starting One Hundred...")
	print(SieveOfEratosthenes(100))
	print("Starting One Thousand...")
	print(SieveOfEratosthenes(1000))
	print("Starting Ten Thousand...")
	print(SieveOfEratosthenes(10000))
	print("Starting One Hundred Thousand...")
	print(SieveOfEratosthenes(100000))
	print("Starting One Million...")
	print(SieveOfEratosthenes(1000000))
	print("Starting Ten Million...")
	print(SieveOfEratosthenes(10000000))
	print("Done...")
    
#Sources: https://www.geeksforgeeks.org/sieve-of-eratosthenes/
#https://www.geeksforgeeks.org/plotting-graphs-in-python-set-1/
#https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
