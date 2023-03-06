"""11.12 LAB: Dates
Complete the code to implement the following operations:

Complete read_date():
Read an input string representing a date in the format yyyy-mm-dd.
Create a date object from the input string.
Return the date object.
Call read_date() to read four (unique) date objects and store the 
date objects in a list.
Call sorted() to sort the list of date objects, earliest first. 
Store the sorted dates in a new list.
Output the sorted_dates, in the format mm/dd/yy.
Hint: Use strftime() to format the date outputs. (See resource below.)
Output the number of days between the last two dates in the sorted 
list as a positive number.
Output the date that is 3 weeks from the most recent date in the 
format "July 4, 1776".
Hint: Use timedelta() to set a duration of time for the arithmetic on 
date objects. (See resources below.)
Ex: timedelta(days=50, seconds=27, hours=8, weeks=2) will define a 
duration of 50 days + 27 seconds + 8 hours + 2 weeks.
Output the full name of the day of the week of the earliest day.
Ex: If the input is:

2022-01-27
2022-07-04
2020-12-31
2022-07-29
the output is:

12/31/2020
01/27/2022
07/04/2022
07/29/2022
25
August 19, 2022
Thursday
Resources on datetime module can be found here:
Examples of using date objects
Format output of date objects with strftime()
Examples of using timedelta()


Starter Code"""

from datetime import date, timedelta, time

# 1 Complete read_date()
def read_date():
    """Read a string representing a date in the format 2121-04-12, create a
    date object from the input string, and return the date object
    """

# 2. Use read_date() to read four (unique) date objects, putting the date objects in a list

# 3. Use sorted() to sort the dates, earliest first

# 4. Output the sorted_dates in order, earliest first, in the format mm/dd/yy

# 5. Output the number of days between the last two dates in the sorted list
#    as a positive number

# 6. Output the date that is 3 weeks from the most recent date in the list

# 7. Output the full name of the day of the week of the earliest day