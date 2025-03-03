# Iterative approach
def iterative_factorial(n):
    steps = 0
    result = 1
    for i in range(1, n+1):
        result *= i
        steps += 1
    return result, steps

# Recursive approach
def recursive_factorial(n, steps=0):
    if n == 0 or n == 1:
        return 1, steps + 1
    else:
        result, step_count = recursive_factorial(n-1, steps + 1)
        return result * n, step_count

# Test with an example number (e.g., n = 5)
n = 5

# Iterative factorial
iter_result, iter_steps = iterative_factorial(n)

# Recursive factorial
rec_result, rec_steps = recursive_factorial(n)

# Display results
print(f"Iterative Factorial of {n}: {iter_result}, Steps: {iter_steps}")
print(f"Recursive Factorial of {n}: {rec_result}, Steps: {rec_steps}")
