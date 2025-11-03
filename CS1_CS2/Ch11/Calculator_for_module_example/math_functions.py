

# math_functions.py

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Cannot divide by zero.'
    

if __name__ == '__main__':
    print('hello from math_functions.py')
    print('Welcome to the math functions program!')

    # Test the functions
    assert add(1, 2) == 3
    assert subtract(5, 3) == 2
    assert multiply(2, 3) == 6
    assert divide(10, 2) == 5
    assert divide(10, 0) == 'Cannot divide by zero.'
    print('All tests passed!')
    
