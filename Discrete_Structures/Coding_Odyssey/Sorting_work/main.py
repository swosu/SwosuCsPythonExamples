import time
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    print('starting bubble sort algorithm')
    # make a copy of the array passed in
    orig_arr = arr.copy()
    n = len(arr)
    print('our array starts as:', arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print('after bubble sort, our array looks like this:', arr)

    # sort the original array
    orig_arr.sort()

    # check if arr is equal to the original array after sorting
    if arr != orig_arr:
        print("Bubble Sort failed to sort the array correctly.")

    
    

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def generate_random_array(size):
    return [random.randint(1, (100 * size)) for _ in range(size)]

def measure_sorting_time(sort_function, data):
    start_time = time.time()
    sort_function(data.copy())
    end_time = time.time()
    return end_time - start_time

def run_experiment(array_sizes):
    sorting_algorithms = [bubble_sort, merge_sort]  # Add more sorting algorithms as needed
    results = {algorithm.__name__: [] for algorithm in sorting_algorithms}

    for size in array_sizes:
        for _ in range(5):  # Run each size 5 times
            data = generate_random_array(size)

            for algorithm in sorting_algorithms:
                sorted_data = data.copy()
                print('running', algorithm.__name__)
                time_taken = measure_sorting_time(algorithm, sorted_data)
                print('after sorting, our sorted data looks like this:', sorted_data)
                if sorted_data != sorted(data):
                    print(f"{algorithm.__name__} failed to sort the array correctly.")

                results[algorithm.__name__].append(time_taken)

    return results

def print_results(results):
    print("Array Size\tAlgorithm\tTime Taken (seconds)")
    for algorithm, times in results.items():
        for i, time_taken in enumerate(times, start=1):
            print(f"{i}\t\t{algorithm}\t{time_taken:.6f}")

def plot_results(results):
    for algorithm, times in results.items():
        plt.plot(range(1, len(times) + 1), times, label=algorithm)

    plt.xlabel('Experiment Number')
    plt.ylabel('Time Taken (seconds)')
    plt.legend()
    plt.title('Sorting Algorithm Performance')
    plt.show()

if __name__ == "__main__":
    array_sizes = [10]  # Add more sizes as needed
    experiment_results = run_experiment(array_sizes)
    
    print_results(experiment_results)
    plot_results(experiment_results)
