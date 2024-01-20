# common year, 365 days
# every 4 years, leap year
# leap year 366 days
#y divisible by 4, if year is century must be divisible by 400

def is_leap_year(year):
    if year % 100 == 0 :
        #century year
        if year % 400 == 0:
            return True
        else:return False
    elif year % 4 == 0:
        return True
    else:return False

input_year = int(input("Please enter a year: "))
result = is_leap_year(input_year)

print(result)