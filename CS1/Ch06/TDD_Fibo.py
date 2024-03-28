import time

def fibonacci(number):
    if not isinstance(number, int):
        return "Invalid input!"
    elif 0 == number:
        return 0
    elif 1 == number:
        return 1
    elif 1 < number:
        fibs = [0, 1]
        for i in range(2, number+1):
            fibs.append(fibs[-1] + fibs[-2])
        return fibs[-1]
    else:
        return -1
    
def run_tests():
    print('start testing...')
    # start a timer
    start = time.time()
    assert fibonacci(-7) == -1
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(8) == 21
    assert fibonacci(9) == 34
    assert fibonacci(10) == 55
    assert fibonacci(20) == 6765 
    assert fibonacci(30) == 832040
    assert fibonacci(40) == 102334155
    assert fibonacci('Robert') == "Invalid input!"
    # stop the timer
    end = time.time()
    print('tests completed successfully!')
    print('time elapsed: ', end - start, 'seconds')


if __name__ == '__main__':
    #run_tests()
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')