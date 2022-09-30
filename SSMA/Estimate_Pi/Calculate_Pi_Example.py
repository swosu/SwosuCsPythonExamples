from random import *
from math import sqrt  
import math
import time

print('trials, \tpi est. \t abs err, \t time (sec)')
for zero_count in range (0,8):
    tic = time.perf_counter()
    inside=0  
    n= 10 ** zero_count
    for i in range(0,n):  
        x = random()  
        y = random()  
        if sqrt(x*x+y*y)<=1:  
            inside+=1  
    pi=4*inside/n  
    toc = time.perf_counter()
    #print (f'For {n} trials, pi is estimated at {pi}, which has an error of {abs(math.pi - pi):e} in {toc - tic:0.4f} seconds.')
    print (f'{n}\t{pi} \t {abs(math.pi - pi):e} \t {toc - tic:0.4f} ')