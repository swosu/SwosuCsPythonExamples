import time

def fibo_recursive(nth_term, memo={}):
    if nth_term < 0:
        print('Invalid input')
        return None
    elif nth_term == 0:
        return 0
    elif nth_term == 1:
        return 1
    elif 1 < nth_term:
        return fibo_recursive(nth_term - 1) + fibo_recursive(nth_term - 2)
    else:
        print('Invalid input')
        return None
    

def fibo_iterative(nth_term):
    first_of_two = 0
    second_of_two = 1
    if 0 == nth_term:
        return first_of_two
    elif 1 == nth_term:
        return second_of_two
    elif 1 < nth_term:
        for iterative_index in range(nth_term - 1):
            next_term = first_of_two + second_of_two
            first_of_two = second_of_two
            second_of_two = next_term
        return next_term
    else:
        print('Invalid input')
        return None
    
if __name__ == '__main__':
    recursive_times = []
    iterative_times = []

    for i in range(5, 105, 5):

        start_time = time.time()
        fibo_recursive(i)
        end_time = time.time()
        recursive_times.append(end_time - start_time)
        
        start_time = time.time()
        fibo_iterative(i)
        end_time = time.time()
        iterative_times.append(end_time - start_time)

        # print of the time for the current run
        print(f"Time for {i}th term:")
        print("Recursive time:", recursive_times[-1])
        print("Iterative time:", iterative_times[-1])

    print("Recursive times:", recursive_times)
    print("Iterative times:", iterative_times)