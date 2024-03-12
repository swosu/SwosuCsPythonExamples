def fibo(number):
    if number <= 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibo(number - 1) + fibo(number - 2)



def run_tests():
    assert 0 == fibo(-2), "fib(-2) should be 0, but got " + str(fibo(-2))
    assert 0 == fibo(0), "fib(0) should be 0, but got " + str(fibo(0))
    assert 1 == fibo(1), "fib(1) should be 1, but got " + str(fibo(1))
    assert 1 == fibo(2), "fib(2) should be 1, but got " + str(fibo(2))
    assert 2 == fibo(3), "fib(3) should be 2, but got " + str(fibo(3))
    assert 3 == fibo(4), "fib(4) should be 3, but got " + str(fibo(4))
    assert 5 == fibo(5), "fib(5) should be 5, but got " + str(fibo(5))

    print('all tests passed')

if __name__ == "__main__":
    run_tests()