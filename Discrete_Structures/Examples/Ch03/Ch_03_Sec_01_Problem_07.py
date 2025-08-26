
import random

def fill_list_of_integers(number_of_integers):
    list_of_integers = []
    for number in range(0, number_of_integers):
        new_number = random.randint(0,22)
        list_of_integers.append(new_number)
    return list_of_integers

def find_last_even_integer(list_of_integers):
    #finds the location of the last even integer in the
    #list or returns 0 if there are no even integers in the list.
    last_location = 0

    """
    Reverse the list because we only need to find the last last_location
    Start looking at the beginning of the list and stop
    when we find the first even number
    """
    list_of_integers.reverse()
    print(f'reversed list of integers {list_of_integers}.')

    """
    Check each number, starting at the beginning, to
    see if it is even.
    """
    location = 0
    check_location = 0
    for check_number in list_of_integers:
        if 0 == check_number % 2:
            print(f'you found an even! {check_number}')
            print(f'check location was {check_location}.')
            location = len(list_of_integers) - check_location -1
            print(f'our actual location was {location}.')
            break
        else:
            check_location += 1

    return location


if __name__ == '__main__':
    """ . Describe an algorithm that takes as input a list of n
    integers and finds the location of the last even integer in the
    list or returns 0 if there are no even integers in the list.
    """

    number_of_integers = 5 # pick a number of integers for our list
    list_of_integers = [] # create an empty list to fill

    # go fill the list of integers in a function
    list_of_integers = fill_list_of_integers(number_of_integers)

    # verify the list got filled
    print(f'your list of integers was: {list_of_integers}.')

    #finds the location of the last even integer in the
    #list or returns 0 if there are no even integers in the list.
    last_even_integer_address = find_last_even_integer(list_of_integers)

    # print the result so we can check it against the list
    print(f'The location of the last even was {last_even_integer_address}.')
