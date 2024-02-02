is_leap_year = 'false'

year = int(input('What year would you like to check?'))

if year % 100 == 0:
    if year % 400 == 0:
        is_leap_year = 'true'

elif year % 100 == 0:
    if year % 400 != 0:
        is_leap_year = 'false'

elif year % 4 != 0:
    is_leap_year = 'false'

elif year % 4 == 0:
    is_leap_year = 'true'

if is_leap_year == 'true':
    print('The year you entered (',year,') is a leap year.')
else:
    print('The year you entered (',year,') is not a leap year.')