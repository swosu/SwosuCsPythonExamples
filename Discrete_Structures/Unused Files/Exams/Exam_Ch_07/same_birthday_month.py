import random
import time

def get_birthday_in_range(range_of_birthdays):
    my_birthday = random.randint(1,range_of_birthdays)
    return my_birthday

def do_we_have_a_match_for_a_single_room(number_of_people, range_of_birthdays):
    have_a_match = False
    our_birthdays = []
    for new_person_index in range(0, number_of_people):
        #print(f'new person index is: {new_person_index+1}.', end = '')
        new_birthday = get_birthday_in_range(range_of_birthdays)
        #print(f' Birthday is {new_birthday}.')
        if new_birthday in our_birthdays:
            have_a_match = True
            break
        else:
            our_birthdays.append(new_birthday)
    return have_a_match

def count_number_of_trials_resulting_in_matching_birthday(\
    number_of_trials, number_of_people, range_of_birthdays):
    had_a_match_count = 0
    for trial_index in range(0, number_of_trials):
        #print(f'on trial {trial_index+1}')
        have_a_match = do_we_have_a_match_for_a_single_room(number_of_people, range_of_birthdays)
        if have_a_match:
            had_a_match_count += 1
    return had_a_match_count

if __name__ == "__main__":
    start_time = time.time()
    range_of_birthdays = 366
    number_of_trials = 100000
    # range is 12 for matching months, 31 for day in a month, 366 for day in a year 
    
    for number_of_people in range (2, 32):
    
        number_of_matches = \
            count_number_of_trials_resulting_in_matching_birthday(\
                number_of_trials, number_of_people, range_of_birthdays)
        
        match_count_divided_by_trial_count = (number_of_matches / number_of_trials) 
        print(f'for {number_of_people} people and {range_of_birthdays} holes, ', end = '')
        print(f'had a match count was: {number_of_matches}. ', end = '')
        percentage = "{:.2%}".format(match_count_divided_by_trial_count)
        print(percentage)

    elapsed_time = time.time() - start_time
    print(f'time in seconds {elapsed_time}.')