# Recursive Fibonacci with step counting
def fibonacci_recursive(n, steps=[0]):
    steps[0] += 1
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1, steps) + fibonacci_recursive(n-2, steps)

# Iterative Fibonacci with step counting
def fibonacci_iterative(n):
    steps = 0
    if n <= 0:
        return 0, steps
    elif n == 1:
        return 1, steps
    a, b = 0, 1
    for _ in range(2, n + 1):
        steps += 1
        a, b = b, a + b
    return b, steps

n = 10

# Recursive
steps_recursive = [0]
fib_recursive = fibonacci_recursive(n, steps_recursive)
print(f"Recursive: Fibonacci number at position {n} is {fib_recursive} and took {steps_recursive[0]} steps")

# Iterative
fib_iterative, steps_iterative = fibonacci_iterative(n)
print(f"Iterative: Fibonacci number at position {n} is {fib_iterative} and took {steps_iterative} steps")
