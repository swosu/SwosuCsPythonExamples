"""
A year in the modern Gregorian Calendar consists of 365 days. 
In reality, the earth takes longer to rotate around the sun. 
To account for the difference in time, every 4 years, a
 leap year takes place. 
 A leap year is when a year has 366 days: An extra day, February 29th. 
 The requirements for a given year to be a leap year are:

1) The year must be divisible by 4

2) If the year is a century year (1700, 1800, etc.), the year must be evenly divisible by 400

Some example leap years are 1600, 1712, and 2016.

Write a program that takes in a year and determines whether that year is a leap year.

Ex: If the input is:

1712
the output is:

1712 - leap year
Ex: If the input is:

1913
the output is:

1913 - not a leap year

Table
1600 - Leap year (working)
1712 - leap year (working)
2016 - Leap year (working)

1601 - not a leap year
1700 - not a leap year (working)
1713 - not a leap year
2017  - not a leap year (working)
"""

input_year = int(input())

is_a_leap_year = False

if 0 == input_year % 4:
    if 0 == input_year % 100:
        if 0 == input_year % 400:
            is_a_leap_year = True
    else:
        is_a_leap_year = True
        
    
    
    
if is_a_leap_year:
    print(f'{input_year} - leap year')
else:
    print(f'{input_year} - not a leap year')