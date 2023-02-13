import multiprocessing
import math
import time
import os


total_primes = 0
average_time = 0
lowest_time = 0
highest_time = 0
run_times_temp = []
test_times = []


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_number_of_primes(start, end):
    return sum(1 for i in range(int(start), int(end)) if is_prime(i))  # adds 1 to the sum for every prime number in the range

def pool_method(worker_count):  # i think this is working as intended
    global total_primes, counter
    counter = 0
    results = []

    chunk_size = counter_ceiling / worker_count
    chunks = [(i, i + chunk_size) for i in range(0, int(counter_ceiling), int(chunk_size))]

    with multiprocessing.Pool(processes=worker_count) as pool:
        for i in range(pool.__getattribute__('_processes')):
            results.append(pool.apply_async(find_number_of_primes,args=(chunks[i])))  # adds the result of the function to the list

            if counter == 0:
                for result in results:
                    total_primes += result.get()
                counter += 1
            else:  # you have to run result.get everytime
                for result in results:
                    result.get()
        pool.close()

def get_average(worker_count, run_count):
    global run_times_temp
    run_times_temp = [] # clear the list, as it is temporary
    total_time = 0

    for i in range(run_count):
        # os.system('cls' if os.name == 'nt' else 'clear')
        print("workers: ", worker_count, end='')
        print(f"Run {i} / {run_count}   ", end='')

        run_timer_start = time.time()
        pool_method(worker_count)
        run_timer_end = time.time()

        run_time = (run_timer_end - run_timer_start)
        temp_tuple = (i, run_time)
        run_times_temp.append(temp_tuple)
        total_time += run_time

        print(round(run_time, 3), 'seconds')

    average_run_time = total_time / run_count
    lowest_run_time = min(run_times_temp, key=lambda x: x[1])[1]
    highest_run_time = max(run_times_temp, key=lambda x: x[1])[1]
    test_times.append({'processes': worker_count, 'average_time': average_run_time, 'lowest_time': lowest_run_time, 'times': run_times_temp})



    print("numbers searched: ", counter_ceiling)
    print("primes found: ", total_primes)
    print("cpu count: ", os.cpu_count())
    print("processes: ", worker_count)
    print(f"Average time taken: {round(average_run_time, 3)} seconds")
    print(f"Lowest time taken: {round(lowest_run_time, 3)} seconds")
    print(f"Highest time taken: {round(highest_run_time, 3)} seconds")
    print("------------------------------------")
   # print('total elapsed time: ', round(end__global_time - start_global_time, 3), 'seconds')


def run_bench(worker_count, runs):
    for i in range(0, worker_count + 1, 2): # CORE COUNT PLUS ONE PROBALY NEEDS FIXING LATER
        if i == 0:
            get_average(1, runs)
        else: get_average(i, runs)


if __name__ == '__main__':
    counter_ceiling = 1000

    start_global_time = time.time()

    run_bench(runs=5, worker_count=2) # must be a multiple of 2
    #get_average(run_count=100, worker_count=1)

    end__global_time = time.time()

    input("Press enter to exit")
    # creates a list of tuples with the time taken for each run