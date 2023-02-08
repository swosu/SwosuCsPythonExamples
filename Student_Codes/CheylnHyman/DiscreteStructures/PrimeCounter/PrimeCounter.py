import multiprocessing
import math
import time
import os

# multiprocessing is used to create multiple processes to speed up the program, MUST HAVE IF NAME == MAIN
# you have to play with the numbers to get the best results, more cores is better for high er numbers but less cores is better for lower numbers,
# i think

counter_ceiling = 1000000
process_nummber = 12

test_length = 3
chunk_count = process_nummber
chunk_size = counter_ceiling / chunk_count
chunks = [(i, i + chunk_size) for i in range(0, int(counter_ceiling), int(chunk_size))]
total_primes = 0
counter = 0
average_time = 0

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def find_number_of_primes(start, end):
    return sum(1 for i in range(int(start), int(end)) if is_prime(i)) # adds 1 to the sum for every prime number in the range
def pool_method(): # i think this is working as intended
    global total_primes, counter

    results = []

    with multiprocessing.Pool(processes=process_nummber) as pool:
        for i in range(process_nummber):
            results.append(pool.apply_async(find_number_of_primes, args=(chunks[i]))) # adds the result of the function to the list
            if counter == 0:
                for result in results:
                    total_primes += result.get()
                counter += 1
            else: # you have to run result.get everytime
                for result in results:
                    result.get()
def get_average(number_of_times=test_length):
    global average_time
    total_time = 0

    for i in range(number_of_times):
        # clear screen
        #os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Run {i+1} / {number_of_times}   ", end='')

        # run the program and time it
        start_time = time.time()
        pool_method()
        end_time = time.time()

        total_time += end_time - start_time
        print(round(end_time - start_time,3), 'seconds')
    average_time = total_time / number_of_times





if __name__ == '__main__':
    # timer
    start_time = time.time()


    get_average()


    #timer
    end_time = time.time()



    print("numbers searched: ", counter_ceiling)
    print("primes found: ", total_primes)
    print("cpu count: ", os.cpu_count())
    print("processes: ", process_nummber)
    print(f"Average time taken: {round(average_time, 3)} seconds")
    print('total elapsed time: ',round(end_time - start_time, 3), 'seconds')



