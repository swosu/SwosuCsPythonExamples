import time
def fibo(term_index):
    if 0 == term_index:
        return 0
    elif 1 == term_index:
        return 1
    elif 1 < term_index:
        fibs = [0, 1, 1]                                                                                           
        for f in range(2, term_index):                                                                                      
            fibs.append(fibs[-1] + fibs[-2])                                                                         
        return fibs[term_index]
    else:
        return -1
    
def run_tests():
    #start a timer
    start = time.time()
    print('start of tests')
    assert -1 == fibo(-7), "Incorrect value for -7 term"
    assert 0 == fibo(0), f"{fibo(0)} Incorrect value for 0 term"
    assert 1 == fibo(1), f"{fibo(1)} Incorrect value for 1 term"
    assert 1 == fibo(2), f"{fibo(2)} Incorrect value for 2 term"
    assert 2 == fibo(3), f"{fibo(3)} Incorrect value for 3 term"
    assert fibo(4) == 3, f"{fibo(4)} Incorrect value for 4 term"
    assert fibo(8) == 21, f"{fibo(8)} Incorrect value for 8 term"
    assert fibo(16) == 987, f"{fibo(16)} Incorrect value for 16 term"
    assert fibo(32) == 2178309, f"{fibo(32)} Incorrect value for 32 term"
    assert fibo(64) == 10610209857723, f"{fibo(64)} Incorrect value for 64 term"
    #stop the timer
    end = time.time()
    print('all tests passed')
    print('elapsed time: ', end - start)

if __name__ == '__main__':
    run_tests()