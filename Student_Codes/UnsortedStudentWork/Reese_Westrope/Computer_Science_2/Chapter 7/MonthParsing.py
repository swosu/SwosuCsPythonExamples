import re

user_string = input("Please input a date in the following format: Month X, XXXX\n:")

months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
    }

def string_to_list(string):
    global DateInfo
    DateInfo = string.split()
    return DateInfo
    
def get_month_string():
    global DateInfo
    month_string = DateInfo[0]
    return month_string
    
def get_day_int():
    global DateInfo
    day_string = int(DateInfo[1])
    return day_string
    
def get_year_int():
    global DateInfo
    year_string = int(DateInfo[2])
    return year_string
    


def get_month_as_int():
    global month_string

    if month_string == 'January':
        month_int = 1
    elif month_string == 'February':
        month_int = 2
    elif month_string == 'March':
        month_int = 3
    elif month_string == 'April':
        month_int = 4
    elif month_string == 'May':
        month_int = 5
    elif month_string == 'June':
        month_int = 6
    elif month_string == 'July':
        month_int = 7
    elif month_string == 'August':
        month_int = 8
    elif month_string == 'September':
        month_int = 9
    elif month_string == 'October':
        month_int = 10
    elif month_string == 'November':
        month_int = 11
    elif month_string == 'December':
        month_int = 12
    else:
        month_int = 0

    return month_int
    

def CheckFormat():
    global DateInfo
    for data in DateInfo:
        if data == -1:
            break
        if re.match(r'(\w+) (\d{1,2}), (\d{4})', data) == None:
            continue
        output = data.split(" ")
        output[0] = str(months[output[0]])
        output[1] = output[1].replace(",", "")
        print("/".join(output))


# TODO: Read dates from input, parse the dates to find the one
#       in the correct format, and output in m/d/yyyy format


if __name__ == "__main__":
    string_to_list(user_string)
    CheckFormat()




    