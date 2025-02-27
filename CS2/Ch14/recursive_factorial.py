def factorial(n):
    print(f'we got passed in an n of {n}')
    if n == 0:
        print('we hit the base case')
        return 1
    else:
        print(f'we are going to return {n} * factorial({n-1})')
        our_result  = n * factorial(n-1)
        print(f'we got {n} * factorial({n-1}) = {our_result}')
        return our_result
    
def run_tests():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120
    assert factorial(6) == 720
    assert factorial(7) == 5040
    print('all tests pass')
if __name__ == '__main__':
    run_tests()
    print(factorial(5))

    

