import random
random.seed()

# imports for plotting
# try to install matplotlib with
# pip install matplotlib
import matplotlib.pyplot as plt

def did_anyone_have_a_birthday_match(people_in_room):
    birthdays_in_room_maybe_repeats = []
    for index in range(people_in_room):
        my_birthday = random.randint(1,367)
        birthdays_in_room_maybe_repeats.append(my_birthday)
    # see if two people have the same birthday.
    birthdays_in_room_no_repeats = set(birthdays_in_room_maybe_repeats)
    if (len(birthdays_in_room_no_repeats) != len(birthdays_in_room_maybe_repeats)):
        return True
    else:
        return False

def percent_chance_of_a_match_for_one_number_of_people_in_room(people_in_room, sample_size):
    match_count = 0
    for index in range(sample_size):
        we_had_a_match = did_anyone_have_a_birthday_match(people_in_room)
        if(we_had_a_match):
            #print('we had a match')
            match_count += 1
        #else:
            #print('no match')
    percent_match = (match_count / sample_size) * 100.0
    #print('Out of a sample size of {0}, we had {1} matches, or {2}%, with {3} people in the room.'.format(sample_size, match_count, percent_match, people_in_room))
    return percent_match

if __name__ == '__main__':
    """
    # testing our function.
    # 23 people should give us just over 50%.
    people_count = 23
    sample_size = 10000
    percent_match = percent_chance_of_a_match_for_one_number_of_people_in_room(people_count, sample_size )
    #print('Out of a sample size of {0}, {1}% had a room with at least 2 people with matching birthdays when {2} people are in the room.'.format(sample_size, percent_match, people_in_room))
    """

    sample_size = 1000
    print('sample size', sample_size)

    data = {}

    for people_count in range (1,55+1):
        percent_match = percent_chance_of_a_match_for_one_number_of_people_in_room(people_count, sample_size )
        print('People in room {0}, {1}% chance'.format(people_count, percent_match))
        #print('sample size of {0}, {1}% had a room with at least 2 people with matching birthdays when {2} people are in the room.'.format(sample_size, percent_match, people_count))
        data[people_count] = percent_match

    #print('our percentage by people count dictionary', birthday_percentage_by_people_count)
    names = list(data.keys())
    values = list(data.values())
    plt.bar(range(len(data)), values, tick_label=names)
    plt.ylabel('Percent likelyhood ')
    plt.xlabel('Number of people per room')
    plt.title('sample size: '+ str(sample_size))
    plt.suptitle('Percent likelyhood at least 2 people in a room have the same birthday')
    plt.show()
