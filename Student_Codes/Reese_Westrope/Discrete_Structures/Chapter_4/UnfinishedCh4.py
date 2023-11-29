#Write a program to count the number of primes less than some number. 
#Make a log plot of the number of primes less than ten, one hundred, a thousand, ten thousand, a hundred thousand and a million. 
#Predict the number of primes less than 10 million



import math
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


given_numbers = []
num_of_primes = []

def count_primes(number):
    count = 0
        
    for num in range(number):
        if num <= 1:
            continue
        for integer in range(2, num):
            if (num % integer) == 0:
                break
        else:
            count += 1
    
    return count

def add_to_lists():
    global given_numbers, num_of_primes
    num = int(input("Enter a number: "))
    given_numbers.append(num)
    
    num_of_primes.append(count_primes(num))
    return given_numbers, num_of_primes
    
    
def create_log_plot():
    log_plot = pd.DataFrame({'x': given_numbers, 'y': num_of_primes})
    xlog = np.log(log_plot.x)
    ylog = np.log(log_plot.y)
    plt.scatter(xlog, ylog)

    plt.show()



if __name__ == '__main__':


    while len(given_numbers) < 4:
        add_to_lists()

    print(given_numbers)
    print(num_of_primes)
    
    create_log_plot()
    
    

    