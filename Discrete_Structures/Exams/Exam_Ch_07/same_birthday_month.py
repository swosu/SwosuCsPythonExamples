
import random

def get_birthday():
    my_birthday = random.randint(1,12) # for same month in year
    return my_birthday



if __name__ == "__main__":
    print('hello')
    print(f'test my birthday {get_birthday()}.')

    number_of_trials = 100000
    number_of_people = 7
    # 7 people should have a 50% chance of having two people born in the same month.
    had_a_match_count = 0
    for trial_index in range(0, number_of_trials):
        #print(f'on trial {trial_index+1}')
        our_birthdays = []
        have_a_match = False
        for new_person_index in range(0, number_of_people):
            #print(f'new person index is: {new_person_index+1}.', end = '')
            new_birthday = get_birthday()
            #print(f' Birthday is {new_birthday}.')
            if new_birthday in our_birthdays:
                have_a_match = True
            else:
                our_birthdays.append(new_birthday)
        #print(f'had a match was: {have_a_match}.')
        #print(our_birthdays)
        our_birthdays.sort()
        #print(our_birthdays)
        if have_a_match:
            had_a_match_count += 1
    print(f'had a match count was: {had_a_match_count}.')
    match_count_divided_by_trial_count = (had_a_match_count / number_of_trials) 
    print(f'for {number_of_people} people,', end = '')
    percentage = "{:.2%}".format(match_count_divided_by_trial_count)
    print(percentage)
    
