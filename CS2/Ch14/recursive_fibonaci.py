def fibo (number):
    if number < 0:
        print(f'we have hit the first base case and can return 0 because our number is negative')
        return 0
    elif number == 0:
        print(f'we have hit the first base case and can return 0 because our number is 0')
        return 0
    elif number == 1:
        print(f'we have hit the second base case and can return 1 because our number is 1')
        return 1
    else:
        print(f'to find fibo({number}), we need to find fibo({number-1}) + fibo({number-2})')
        return fibo(number - 1) + fibo(number - 2)
    
def run_tests():
    assert fibo(-5) == 0, 'Test case 1 failed because we mishandled negative numbers'
    assert fibo(0) == 0, 'Test case 2 failed because we mishandled 0'
    assert fibo(1) == 1, 'Test case 3 failed because we mishandled 1'
    assert fibo(2) == 1, 'Test case 4 failed because we mishandled 2'
    assert fibo(3) == 2, 'Test case 5 failed because we mishandled 3'
    assert fibo(4) == 3, 'Test case 6 failed because we mishandled 4'
    assert fibo(5) == 5, 'Test case 7 failed because we mishandled 5'
    assert fibo(6) == 8, 'Test case 8 failed because we mishandled 6'
    assert fibo(7) == 13, 'Test case 9 failed because we mishandled 7'
    assert fibo(8) == 21, 'Test case 10 failed because we mishandled 8'
    assert fibo(9) == 34, 'Test case 11 failed because we mishandled 9'
    assert fibo(10) == 55, 'Test case 12 failed because we mishandled 10'
    print('All tests pass')
    
if __name__ == "__main__":

    run_tests()
    number = int(input("Enter a number: "))
    print(fibo(number))