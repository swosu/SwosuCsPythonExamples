import time
#write Fibonacci sequence infinitely and return only prime
def fib():
    #start time
    fabPrime = []
    Count = time.time()
    a, b = 0, 1
    #print('Check')
    while time.time() - Count < 5:
        #print('Check 2')
        #yield a
        a, b = b, a + b
        #check time
        fabPrime.append(a)
    return fabPrime
        
def primes():
    for i in fib():
        if i > 1:
            for j in range(2, i): 
                if (i % j) == 0:
                    break
            else:
                yield i 

#call the function and print result

