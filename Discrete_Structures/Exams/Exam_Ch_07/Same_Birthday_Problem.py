import random

def assign_a_birthday():
    my_birthday = random.randint(1,366)
    return my_birthday
    #print(f'the random birthday was {my_birthday}.')

def check_our_birthday_guesser():
    for checkvalue in range (1, 367):
        #print(f'hunting {checkvalue}')
        keep_checking = True
        while keep_checking:
            my_birthday = assign_a_birthday()
            if my_birthday == checkvalue:
                keep_checking = False
                #print(f'match {checkvalue}.')
        print(f'{checkvalue}, ', end ='')
        if 0 == checkvalue % 12:
            print()


if __name__ == '__main__':
    print('hello.')

    #check_our_birthday_guesser()

    number_of_people_in_the_room = 22
    number_of_trials = 100000
    number_of_rooms_with_matching_birthdays = 0


    for trial_count in range (1,number_of_trials + 1):
        birthday_with_possible_repeats = []
        birthdays_without_repeats = set()
        #print(f'trial count {trial_count}.')
        for people in range(1,number_of_people_in_the_room + 1):
            #print(f'number of people in the room {people}.')
            birthday_with_possible_repeats.append(assign_a_birthday())
        #print(f'our list of birthdays.\n {birthday_with_possible_repeats}')
        birthdays_without_repeats = set(birthday_with_possible_repeats)
        if len(birthdays_without_repeats) < len(birthday_with_possible_repeats):
            #print('We had a repeat!')
            number_of_rooms_with_matching_birthdays += 1

    percent_trials_with_matching_birthdays = \
    number_of_rooms_with_matching_birthdays / number_of_trials

    print(f'percent of trials with matching birthdays {percent_trials_with_matching_birthdays}.')
