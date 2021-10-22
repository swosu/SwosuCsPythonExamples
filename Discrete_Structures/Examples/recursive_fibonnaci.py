def fibonacci(n):
    print('start of fibbo call with:', n)
    if n < 0:
        print('n was less than 0, and is now', n)
        print('this should be the bottom of the call.')
        return -1
    elif n <= 1:
        print('n was less than or equal to 1, and is now', n)
        print('this is close to the end.')
        return n
    print('now we look for n-1 which is', n-1)
    print('now we look for n-2 which is', n-2)
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    print('which fibonacci number would you like?\n')
    the_fibonacci_number_you_want = int(input())
    fibonacci_result = fibonacci(the_fibonacci_number_you_want)
    print('fibonacci({}) is {}'.format(\
    the_fibonacci_number_you_want, fibonacci_result))
