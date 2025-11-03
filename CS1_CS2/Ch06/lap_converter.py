
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
'''
#1)

23.1 LAB: Track laps to miles
One lap around a standard high-school running track is exactly 0.25 miles. Define a function named laps_to_miles that takes a number of laps as a parameter, and returns the number of miles. Then, write a main program that takes a number of laps as an input, calls function laps_to_miles() to calculate the number of miles, and outputs the number of miles.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'{your_value:.2f}')

Ex: If the input is:

7.6
the output is:

1.90
Ex: If the input is:

2.2
the output is:

0.55
The program must define and call the following function:
def laps_to_miles(user_laps)
'''
#Starter Code

# Define your function here 
def laps_to_miles(number_of_laps):
    number_of_miles = number_of_laps / 4
    return number_of_miles
    

if __name__ == '__main__':
    # Type your code here. Your code must call the function. 
    
    number_of_laps = float(input())
    number_of_miles = laps_to_miles(number_of_laps)
    #print(f'We had {number_of_laps} laps which is {number_of_miles:.2f} miles.')
    print(f'{number_of_miles:.2f}')