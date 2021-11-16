import random
random.seed()

# have a person have a birthday from 1 to 366
"""
for i in range(100000):
    my_birthday = random.randint(1,367)
    if(my_birthday == 366):
        print(my_birthday)
"""

my_birthday = random.randint(1,367)

# make a room full of birthdays
#print(my_birthday)
birthdays_in_room_list = []

number_of_people_in_the_room = 23

for index in range(number_of_people_in_the_room):
    my_birthday = random.randint(1,367)
    birthdays_in_room_list.append(my_birthday)

print(birthdays_in_room_list)

# see if two people have the same birthday.
birthdays_in_room_set = set(birthdays_in_room_list)

if (len(birthdays_in_room_set) != len(birthdays_in_room_list)):
    print('We had at least one pair of people with the same birthday')
