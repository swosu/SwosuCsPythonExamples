import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FuncFormatter

def checkPrime():
 global lower
 global upper
 lower=int(input("enter the minimum value of the range: "))
 upper=int(input("enter the maximum value of the range: "))
 primeList = []
 for num in range (lower, upper+1):
  if num > 1:
   for i in range (2, num):
    if num % i == 0:
     break
   else: 
     primeList.append(num)
 numPrimes = print (f'the number of primes in the range {lower} to {upper} are:',
         len(primeList))
 return numPrimes

def logPlot():
 x = [4, 25, 168, 1229, 9592]
 y = [10, 100, 1000, 10000, 100000]
 plt.scatter(x, y, color = "green")
 plt.xlabel("# primes")
 plt.ylabel("# range up to 1 million")
 plt.title("# primes < 10 to 100,000")
 y_ticks = np.arange(0, 100000, 100)
 x_ticks = np.logspace(0, 10000)
 plt.show()

if __name__ == "__main__":
 checkPrime()
 logPlot()