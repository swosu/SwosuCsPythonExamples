import re

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

UserData = []

def GetUserData():
    global user_input
    while '-1' not in UserData:
        user_input = input("Please enter a date in the format Month XX, YYYY\nIf you are done entering dates, type '-1'\n: ")
        UserData.append(user_input)

def FormatCheck():
    for data in UserData:
        if data == -1:
            break
        if re.match(r'(\w+) (\d{1,2}), (\d{4})', data) == None:
            continue
        Output = data.split(" ")
        Output[0] = str(months[Output[0]])
        Output[1] = Output[1].replace(",", "")
        print("/".join(Output))


if __name__ == "__main__":
    
    GetUserData()
    FormatCheck()