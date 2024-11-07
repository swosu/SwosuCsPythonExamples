# Python program to display the Fibonacci sequence
import time
def recur_fibo(n):
    #print('n is: ', n)
    if n <= 1:
       return n
    else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 40
print('n terms is: ', nterms, end=' ')

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
        start_time = time.time()
        print('i is: ', i, ': ', end=' ')
        print('your fibo is: ', recur_fibo(i))
        stop_time = time.time()
        elapsed_time = stop_time - start_time
        print('elapsed time is: ', elapsed_time)