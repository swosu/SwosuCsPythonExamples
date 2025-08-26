import time
import csv
def seive_of_eratosthenes(upper_limit_for_primes):
    #print('type for upper_limit_for_primes: ', type(upper_limit_for_primes))
    # create a list of numbers from 2 to upper_limit_for_primes
    #list_of_numbers = list(range(2, upper_limit_for_primes + 1))
    list_of_numbers = []
    for number in range(2, upper_limit_for_primes + 1):
        #print('inside for loop, number: ', number)
        list_of_numbers.append(number)
    #list_of_numbers = [i for number in range(2, upper_limit_for_primes + 1)]
    #print('list of numbers: ', list_of_numbers)

    # create an empty list where we can store our primes
    list_of_primes = []

    # loop through the list of numbers
    for number in list_of_numbers:
        #print('number: ', number)
        # if the number is not in the list of primes
        if number not in list_of_primes:
            #print('number not in list of primes')
            # add the number to the list of primes
            list_of_primes.append(number)
            #print('list of primes is now: ', list_of_primes)

            # remove all multiples of the number from the list of numbers
            for multiple in range(number * number, upper_limit_for_primes + 1, number):
                #print('multiple: ', multiple)
                if multiple in list_of_numbers:
                    list_of_numbers.remove(multiple)

            #print('after removing multiples, list of numbers: ', list_of_numbers)

    return list_of_primes

if __name__ == "__main__":
    print('hello')
    csv_file_name = 'primes.csv'
    list_of_upper_limits = [10, 100, 1000, 10000, 100000, 1000000, 10000000]

    for our_number in list_of_upper_limits:
        upper_limit_for_primes = our_number
    

        print('pass upper limit to a funciton: ', upper_limit_for_primes)
        start_time = time.time()
        list_of_primes = seive_of_eratosthenes(upper_limit_for_primes)
        stop_time = time.time()
        elapsed_time = stop_time - start_time

        print('list of primes: ', list_of_primes)

        
        # data row should be
        # upper_limit_for_primes, number_of_primes, elapsed_time
        data_row = [upper_limit_for_primes, len(list_of_primes), elapsed_time]
        print('data row: ', data_row)
        print('store results into a csv file')
        # open the csv file
        with open(csv_file_name, 'a') as csv_file:
            # create a csv writer object
            csv_writer = csv.writer(csv_file)
            # write the data row to the csv file
            csv_writer.writerow(data_row)
        print('done')

        # close csv file
        csv_file.close()
        print('csv file closed')

    print('goodbye')

