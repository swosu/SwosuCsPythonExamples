import random
random.seed()

def did_anyone_have_a_birthday_match(people_in_room):
    birthdays_in_room_list = []
    for index in range(people_in_room):
        my_birthday = random.randint(1,367)
        birthdays_in_room_list.append(my_birthday)
    # see if two people have the same birthday.
    birthdays_in_room_set = set(birthdays_in_room_list)
    if (len(birthdays_in_room_set) != len(birthdays_in_room_list)):
        return True
    else:
        return False

if __name__ == '__main__':
    people_in_room = 27

    match_count = 0
    sample_size = 10000
    for index in range(sample_size):
        we_had_a_match = did_anyone_have_a_birthday_match(people_in_room)
        if(we_had_a_match):
            #print('we had a match')
            match_count += 1
        #else:
            #print('no match')
    percent_match = (match_count / sample_size) * 100.0
    print('Out of a sample size of {0}, we had {1} matches, or {2}%. {3} people in the room.'.format(sample_size, match_count, percent_match, people_in_room))
