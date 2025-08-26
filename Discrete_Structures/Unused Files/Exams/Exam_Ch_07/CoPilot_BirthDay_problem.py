import random
from datetime import datetime

def generate_birthdays(number_of_people):
    random.seed(datetime.now().timestamp())

    birthdays = []

    for i in range(number_of_people):

        birthdays.append(random.randint(1, 366))

    return birthdays

def check_for_366_in_birthdays ():

    had_a_366_birthday = False

    while not had_a_366_birthday:
            
        birthdays_for_people_in_the_room = generate_birthdays(people_in_room)
    
        for birthday in birthdays_for_people_in_the_room:
    
            if birthday == 366:
    
                had_a_366_birthday = True
    
                break

if __name__ == '__main__':
    starting_time = datetime.now()
    number_of_rooms_to_check = 20000
    #check_for_366_in_birthdays ()
    list_of_people_in_room = []
    odds_of_two_people_with_same_birthday = []

    for people_in_room in range(2, 60):

        repeats = 0
        no_repeats = 0

        for room_index in range(number_of_rooms_to_check):
            birthdays_for_people_in_the_room = generate_birthdays(people_in_room)
    
            #birthdays_for_people_in_the_room.sort()
    
            #print(birthdays_for_people_in_the_room)

            birthdays_for_people_in_the_room_without_repeats = \
                set(birthdays_for_people_in_the_room)

            if len(birthdays_for_people_in_the_room) == \
                len(birthdays_for_people_in_the_room_without_repeats):

                #print('no repeats')
                no_repeats += 1
            else:
                #print('repeats')
                repeats += 1

        #print('repeats:', repeats)
        #print('no repeats:', no_repeats)
        #print('repeats / no repeats:', repeats / no_repeats)
        #print('repeats / number_of_rooms_to_check:', repeats / number_of_rooms_to_check)
        odds_of_two_people_with_same_birthday_as_percentage =100 * (repeats / number_of_rooms_to_check)
        print(f'for {people_in_room} people in a room,', end = '')
        print(f' {odds_of_two_people_with_same_birthday_as_percentage:.4f}% odds of two people with the same birthday.')

        list_of_people_in_room.append(people_in_room)
        odds_of_two_people_with_same_birthday.append(odds_of_two_people_with_same_birthday_as_percentage)

    ending_time = datetime.now()
    print(f'elapsed time: {ending_time - starting_time}')
    # plot the results
    #import matplotlib.pyplot as plt
    #plt.plot(list_of_people_in_room, odds_of_two_people_with_same_birthday)
    #plt.xlabel('number of people in room')
    #plt.ylabel('odds of two people with same birthday')
    #plt.show()

    # plot the results as a bar chart
    import matplotlib.pyplot as plt
    plt.bar(list_of_people_in_room, odds_of_two_people_with_same_birthday)
    plt.xlabel('number of people in room')
    plt.ylabel('odds of two people with same birthday')
    plt.show()


