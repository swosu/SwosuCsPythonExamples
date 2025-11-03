def fibo(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return a

# Test case for -7 term
result = fibo(-7)
assert result == -1, "Incorrect value for -7 term"