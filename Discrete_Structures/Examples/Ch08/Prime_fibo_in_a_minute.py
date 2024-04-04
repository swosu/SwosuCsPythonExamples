import time


def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def check_if_number_is_prime(number):
    is_prime = True
    if number < 2:
        is_prime = False
    elif number % 2 == 0:
        is_prime = False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            is_prime = False
    return is_prime

if __name__ == '__main__':
    assert fibonacci_iterative(-1) == 0, f'Test for negative number failed. Expected 0, got {fibonacci_iterative(0)}'
    assert fibonacci_iterative(0) == 0, f'Test for 0 failed. Expected 0, got {fibonacci_iterative(0)}'
    assert fibonacci_iterative(1) == 1, f'Test for 1 failed. Expected 1, got {fibonacci_iterative(1)}'
    assert fibonacci_iterative(2) == 1, f'Test for 2 failed. Expected 1, got {fibonacci_iterative(2)}'

    start = time.time()
    n = 2
    list_of_prime_fibonacci = []

    run_time = 60
    time_difference = 0
    while(time_difference < run_time):
        test_number = fibonacci_iterative(n)
        # if the test_number is prime, add it to the list. Use isprime from the math library
        if check_if_number_is_prime(test_number):
            list_of_prime_fibonacci.append(test_number)
        n += 1
        time_difference = time.time() - start
        print(f'n is {n}, test_number_was {test_number}, time_difference is {time_difference}')

    print(f'after {run_time} seconds, we had {len(list_of_prime_fibonacci)} prime fibonacci numbers.')
    print(f'The prime fibonacci numbers were: {list_of_prime_fibonacci}')