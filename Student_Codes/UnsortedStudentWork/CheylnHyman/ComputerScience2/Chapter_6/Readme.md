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

Starter Code

# Define your function here 

if __name__ == '__main__':
    # Type your code here. Your code must call the function. 

    #2)

    23.2 LAB: Max magnitude
    Write a function max_magnitude() with three integer parameters that returns the largest magnitude value. Use the function in the main program that takes three integer inputs and outputs the largest magnitude value.

    Ex: If the inputs are:

    5
    7
    9
    function max_magnitude() returns and the main program outputs:

    9
    Ex: If the inputs are:

    -17
    -8
    -2
    function max_magnitude() returns and the main program outputs:

    -17
    Note: The function does not just return the largest value, which for -17 -8 -2 would be -2. Though not necessary, you may use the built-in absolute value function to determine the max magnitude, but you must still output the input number (Ex: Output -17, not 17).

    Your program must define and call the following function:
    def max_magnitude(user_val1, user_val2, user_val3)

    Starter Code

    # Define your function here.

    if __name__ == '__main__':
        # Type your code here.

        #3)

        23.4 LAB: Leap year - functions
        A common year in the modern Gregorian Calendar consists of 365 days. In reality, Earth takes longer to rotate around the sun. To account for the difference in time, every 4 years, a leap year takes place. A leap year is when a year has 366 days: An extra day, February 29th. The requirements for a given year to be a leap year are:

        1) The year must be divisible by 4

        2) If the year is a century year (1700, 1800, etc.), the year must be evenly divisible by 400; therefore, both 1700 and 1800 are not leap years

        Some example leap years are 1600, 1712, and 2016.

        Write a program that takes in a year and determines the number of days in February for that year.

        Ex: If the input is:

        1712
        the output is:

        1712 has 29 days in February. 
        Ex: If the input is:

        1913
        the output is:

        1913 has 28 days in February.
        Your program must define and call the following function. The function should return the number of days in February for the input year.
        def days_in_feb(user_year)
