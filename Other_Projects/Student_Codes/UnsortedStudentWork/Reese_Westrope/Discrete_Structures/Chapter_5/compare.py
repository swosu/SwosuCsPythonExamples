import time
from iterative import fibonacci_iterative
from recursive import fibonacci_recursive


def compare_times(iterative_time, recursive_time):
    if iterative_time > recursive_time:
        print(f"The recursive function was faster by {str(iterative_time - recursive_time)} seconds.")
    elif iterative_time < recursive_time:
        print(f"The iterative function was faster by {str(recursive_time - iterative_time)} seconds.")
    else:
        print("There was an error calculating the faster funtion.")


if __name__ == '__main__':

    recursive_num = int(input("Choose a number of years to test recursively."))
    iterative_num = int(input("Choose a number of years to test iteratively."))
    
    

    recursive_start = time.time()
    print(f"After {recursive_num} years, there will be {fibonacci_recursive(recursive_num)} rabbits on the island.")
    recursive_end = time.time()
    recursive_total = (recursive_end - recursive_start)
    print(f"It took {recursive_total} seconds to test {recursive_num} years.")

    iterative_start = time.time()
    print(f"After {iterative_num} years, there will be {fibonacci_iterative(iterative_num)} rabbits on the island.")
    iterative_end = time.time()
    iterative_total = (iterative_end - iterative_start)
    print(f"It took {iterative_total} seconds to test {iterative_num} years.")

    compare_times(iterative_total, recursive_total)
