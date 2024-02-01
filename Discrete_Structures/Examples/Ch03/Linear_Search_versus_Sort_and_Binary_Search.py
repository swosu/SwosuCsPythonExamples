



if __name__ == "__main__":


    # Create a list of random numbers
    import random
    import time
    random.seed(time.time())

    minimum_number_of_numbers = 1000
    maximum_number_of_numbers = 10000000
    for number_of_numbers in range(minimum_number_of_numbers, maximum_number_of_numbers, 1000000):

        range_of_random_numbers = 10 * number_of_numbers

        # print the number of numbers
        print("Number of numbers: ", number_of_numbers)
        random_numbers = [random.randint(0, range_of_random_numbers) for i in range(number_of_numbers)]

        # make a copy of the random numbers list for the linear search
        linear_search_random_numbers = random_numbers.copy()

        # make a copy of the random numbers list for the binary search
        binary_search_random_numbers = random_numbers.copy()
        # time how long it takes to do a linear search for a random number
        # that is in the list

        # pick a random number from the list
        random_number_in_list = random.choice(linear_search_random_numbers)

        # start timer
        start_time = time.time()

        # do a linear search for the random number
        for i in range(len(linear_search_random_numbers)):
            if linear_search_random_numbers[i] == random_number_in_list:
                break

        # stop timer
        stop_time = time.time()
        elapsed_linear_search_time = stop_time - start_time
        # print the time it took to do the linear search
        print("Linear search when number is in list time: ", elapsed_linear_search_time)


        # make a copy of the numbers for linear search when number is not in list
        linear_search_random_numbers = random_numbers.copy()

        # pick a random number that is not in the list
        random_number_not_in_list = random.randint(range_of_random_numbers, 2 * range_of_random_numbers)

        # start timer
        start_time = time.time()

        # do a linear search for the random number
        for i in range(len(linear_search_random_numbers)):
            if linear_search_random_numbers[i] == random_number_not_in_list:
                break

        # stop timer
        stop_time = time.time()
        elapsed_linear_search_time_not_in_list = stop_time - start_time
        # print the time it took to do the linear search
        print("Linear search when number is not in list time: ", elapsed_linear_search_time_not_in_list)


        # time how long it takes to do a binary search for a random number
        # after sorting the list
        # for a number that is in the list.

        # use the same number as the first experiement.
        print('random_number_in_list', random_number_in_list)
        

        # start timer
        start_time = time.time()

        # sort the list
        binary_search_random_numbers.sort()

        # do a binary search for the random number
        low = 0
        high = len(binary_search_random_numbers) - 1
        while low <= high:
            mid = (low + high) // 2
            if binary_search_random_numbers[mid] == random_number_in_list:
                break
            elif binary_search_random_numbers[mid] < random_number_in_list:
                low = mid + 1
            else:
                high = mid - 1

        # stop timer
        stop_time = time.time()
        elapsed_binary_search_time_number_in_list = stop_time - start_time

        # print the time it took to do the binary search

        print("Binary search when number is in list time: ", elapsed_binary_search_time_number_in_list)


        # time how long it takes to do a binary search for a random number
        # after sorting the list
        # for a number that is not in the list.

        # use the same number as the second experiement.
        print('random_number_not_in_list', random_number_not_in_list)

        # make a copy of the data for the binary search with a number not in the list
        binary_search_random_numbers_not_in_list = random_numbers.copy()

        # start timer
        start_time = time.time()

        # sort the list
        binary_search_random_numbers_not_in_list.sort()

        # do a binary search for the random number
        low = 0
        high = len(binary_search_random_numbers_not_in_list) - 1
        while low <= high:
            mid = (low + high) // 2
            if binary_search_random_numbers_not_in_list[mid] == random_number_not_in_list:
                break
            elif binary_search_random_numbers_not_in_list[mid] < random_number_not_in_list:
                low = mid + 1
            else:
                high = mid - 1

        # stop timer
        stop_time = time.time()

        elapsed_binary_search_time_number_not_in_list = stop_time - start_time

        # print the time it took to do the binary search

        print("Binary search when number is not in list time: ", elapsed_binary_search_time_number_not_in_list)

    """

        # print the ratio of the linear search time to the binary search time
        print("Ratio of linear search time to binary search time when number is in list: ",
                elapsed_linear_search_time / elapsed_binary_search_time_number_in_list)
        
        # print the ratio of the linear search time to the binary search time
        print("Ratio of linear search time to binary search time when number is not in list: ",
                elapsed_linear_search_time_not_in_list / elapsed_binary_search_time_number_not_in_list)



    """







