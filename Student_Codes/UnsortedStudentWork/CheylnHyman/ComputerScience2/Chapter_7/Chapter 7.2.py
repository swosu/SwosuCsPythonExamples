import datetime

date_string = input('please enter date, as Month Day, Year')

while date_string != '-1':

        try:
            date = datetime.datetime.strptime(date_string, '%B %d, %Y')
            print('The date is:', date)
            break

        except ValueError:
            print('The date you entered is not valid')
            date_string = input('please enter date, as Month Day, Year')
            continue
