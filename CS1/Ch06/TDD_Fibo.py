import time

def fibo(number):
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

if __name__ == '__main__':
    print('start testing...')
    # start a timer
    start = time.time()
    assert fibo(-7) == -1
    assert fibo(0) == 0
    assert fibo(1) == 1
    assert fibo(2) == 1
    assert fibo(3) == 2
    assert fibo(4) == 3
    assert fibo(5) == 5
    assert fibo(6) == 8
    assert fibo(7) == 13
    assert fibo(8) == 21
    assert fibo(9) == 34
    assert fibo(10) == 55
    assert fibo(20) == 6765 
    assert fibo(30) == 832040
    assert fibo(40) == 102334155
    assert fibo('Robert') == "Invalid input!"
    # stop the timer
    end = time.time()
    print('tests completed successfully!')
    print('time elapsed: ', end - start, 'seconds')