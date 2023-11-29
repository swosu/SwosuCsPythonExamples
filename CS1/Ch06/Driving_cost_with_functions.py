"""
6.19 LAB: Driving costs - functions
Write a function driving_cost() with input parameters 
miles_per_gallon, dollars_per_gallon, and miles_driven, 
that returns the dollar cost to drive those miles. 

All items are of type float. 

The function called with arguments (20.0, 3.1599, 50.0) returns 7.89975.

Define that function in a program whose inputs are the car's miles per gallon 

and the price of gas in dollars per gallon (both float). 

Output the gas cost for 10 miles, 50 miles, and 400 miles, 

by calling your driving_cost() function three times.

Output each floating-point value with two digits 
after the decimal point, which can be achieved as follows:
print(f'{your_value:.2f}')

Ex: If the input is:

20.0
3.1599
the output is:

1.58
7.90
63.20
Your program must define and call a function:
def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven)
"""

# Define your function here.
def greet_user():
    print('hello and welcome to driving costs')
    
def get_miles_per_gallon_from_user():
    mpg = float(input('how many miles per gallon does the vehicle get? \n') )
    return mpg

def print_miles_per_gallon(mpg):
    print(f'you said your vehicle gets {mpg:.2f} miles per gallon.')


    
def get_dollars_per_gallon_from_user():
    dollars_per_gallon = float(input('how many dollars does a gallon of gas cost? \n') )
    return dollars_per_gallon

def print_dollars_per_gallon(dollars_per_gallon):
    print(f'you said a gallon of gas costs ${dollars_per_gallon:.2f}.')




    
    
def get_miles_driven():
    miles_driven = float(input('how many miles are you going to drive?\n'))
    return miles_driven

def print_miles_driven(miles_driven):
    print(f'you said you would drive {miles_driven:.2f} miles.')
    
    
def calculate_driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    gallons_used = miles_driven / miles_per_gallon 
    driving_cost = gallons_used * dollars_per_gallon
    return driving_cost
    

if __name__ == '__main__':
    # Type your code here.
    
    greet_user()
    
    miles_per_gallon = get_miles_per_gallon_from_user()
    print_miles_per_gallon(miles_per_gallon)
    
    dollars_per_gallon = get_dollars_per_gallon_from_user()
    print_dollars_per_gallon(dollars_per_gallon)
    
    
    #miles_driven = get_miles_driven()
    #print_miles_driven(miles_driven)
    
    for miles_driven in [10, 50, 400]:
        driving_cost = calculate_driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven)
        print('you driving costs were', end ='')
        print(f' ${driving_cost:.2f}')
    
   