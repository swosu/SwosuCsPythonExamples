import random

def generate_birthdays(number_of_people):

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

    people_in_room = 41
    number_of_rooms_to_check = 512000

    #check_for_366_in_birthdays ()
    #print('entering while loop...')

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

    print('repeats:', repeats)
    print('no repeats:', no_repeats)
    #print('repeats / no repeats:', repeats / no_repeats)
    #print('repeats / number_of_rooms_to_check:', repeats / number_of_rooms_to_check)
    print(f'repeats / number_of_rooms_to_check: {100 * (repeats / number_of_rooms_to_check):.4f}%')