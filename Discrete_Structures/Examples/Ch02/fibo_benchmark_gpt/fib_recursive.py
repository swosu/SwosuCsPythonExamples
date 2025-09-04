def fib_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)
