from datetime import date, timedelta, datetime
import calendar


def list_to_num(num_list, str_list):
    for item in str_list:
        item = int(item)
        num_list.append(item)
    return num_list

def read_date():
    date_list = []
    
    for num in range(4):
        user_date = input("input a date in the format 2121-04-12\n:")

        temp_list = user_date.split("-")
        num_temp_list = []

        list_to_num(num_temp_list, temp_list)

        actual_date = date(num_temp_list[0], num_temp_list[1], num_temp_list[2])
        date_list.append(actual_date)

    return date_list

def sort_dates(date_list):

    date_list.sort()
    return date_list

def print_dates(sorted_dates):
    for date in sorted_dates:
        print(date.strftime("%m/%d/%Y"))


def get_difference_in_days(date_list):
    date_1 = date_list[3]
    date_2 = date_list[2]

    difference = date_1 - date_2
    print(f"The difference in days between the last two dates is {difference.days} days.")


def three_weeks_from_recent(date_list):
    today = datetime.now()
    today_date_obj = today.date()
    most_recent_index = 0
    most_recent_date = date_list[most_recent_index]
    counter = 0
    index = 0
    if today_date_obj >= date_list[index]:
        og_difference = today_date_obj - date_list[index]
    elif today_date_obj <= date_list[index]:
        og_difference = date_list[index] - today_date_obj

    while counter < len(date_list) - 1:
        if today_date_obj >= date_list[index]:
            og_difference = today_date_obj - date_list[index]
        elif today_date_obj <= date_list[index]:
            og_difference = date_list[index] - today_date_obj
        new_difference = abs(today_date_obj - date_list[index + 1])
        if  og_difference > new_difference:
            og_difference = new_difference
            most_recent_index = index + 1
            most_recent_date = date_list[most_recent_index]
        counter += 1
        index += 1
        
    three_weeks = timedelta(days=21)
    three_weeks_from_recent = most_recent_date + three_weeks
    return three_weeks_from_recent

        
def earliest_day_of_the_week(date_list):
    earliest_date = min(date_list)
    name = calendar.day_name[earliest_date.weekday()]
    return name


if __name__ == '__main__':

    date_list = read_date()
    print_dates(sort_dates(date_list))
    get_difference_in_days(date_list)
    print(f"The date that is three weeks from the most recent date is {three_weeks_from_recent(date_list)}")
    print(f"The earliest date falls on a {earliest_day_of_the_week(date_list)}.")