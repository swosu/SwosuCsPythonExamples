"""Helpers for collecting Fibonacci timing and call-count metrics."""


def fib_iterative(n):
    """Return the nth Fibonacci number using iteration."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fib_recursive(n, counter=None):
    """Return the nth Fibonacci number using naive recursion.

    counter: a single-item list used to count how many recursive calls occur.
    """
    if counter is None:
        counter = [0]
    counter[0] += 1
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib_recursive(n - 1, counter=counter) + fib_recursive(n - 2, counter=counter)


def collect_metrics(n_max_iter=40, n_max_rec=28):
    """Return timing and call-count data for iterative and recursive Fibonacci."""
    import time

    n_values_iter = list(range(0, min(n_max_iter, 40) + 1))
    n_values_rec = list(range(0, min(n_max_rec, 28) + 1))

    iter_times = []
    rec_times = []
    rec_calls = []

    for n in n_values_iter:
        start = time.perf_counter()
        fib_iterative(n)
        iter_times.append(time.perf_counter() - start)

    for n in n_values_rec:
        counter = [0]
        start = time.perf_counter()
        fib_recursive(n, counter=counter)
        rec_times.append(time.perf_counter() - start)
        rec_calls.append(counter[0])

    return n_values_iter, iter_times, n_values_rec, rec_times, rec_calls
