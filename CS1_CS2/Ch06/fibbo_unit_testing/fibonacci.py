# fibonacci.py

def fibonacci(n):
    """
    Calculate the nth Fibonacci number iteratively.
    :param n: Non-negative integer, the position in the Fibonacci sequence.
    :return: The nth Fibonacci number.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Iteratively calculate Fibonacci
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
