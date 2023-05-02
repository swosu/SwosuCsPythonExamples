import time

# Recursive implementation of Fibonacci sequence
def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

# Iterative implementation of Fibonacci sequence
def fib_iterative(n):
    if n <= 1:
        return n+1
    else:
        a, b = 0, 1
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return b

# Compare the two implementations
n = 35 # The nth Fibonacci number to compute
start_time = time.time()
result_recursive = fib_recursive(n)
end_time_recursive = time.time()
result_iterative = fib_iterative(n)
end_time_iterative = time.time()

print("Recursive result:", result_recursive)
print("Iterative result:", result_iterative)
print("Recursive time:", end_time_recursive - start_time)
print("Iterative time:", end_time_iterative - end_time_recursive)
