from time import perf_counter

def fib_iter(n):
    if n < 2:
        return n, 0
    a, b = 0, 1
    steps = 0
    for _ in range(2, n + 1):
        a, b = b, a + b
        steps += 1
    return b, steps

def fib_rec(n):
    global CALLS
    CALLS += 1
    if n < 2:
        return n
    return fib_rec(n-1) + fib_rec(n-2)

def run(n):
    t0 = perf_counter()
    val_i, steps_i = fib_iter(n)
    t1 = perf_counter()

    global CALLS
    CALLS = 0
    t2 = perf_counter()
    val_r = fib_rec(n)
    t3 = perf_counter()
    return {
        "n": n,
        "value": val_i,
        "iter_steps": steps_i,
        "iter_time_s": t1 - t0,
        "rec_calls": CALLS,
        "rec_time_s": t3 - t2
    }

if __name__ == "__main__":
    for n in (5, 10, 20, 30):
        CALLS = 0
        print(run(n))
