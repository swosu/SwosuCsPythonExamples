import time

def fib_iter(n):
    steps = 0
    a, b = 0, 1
    if n == 0:
        return 0, steps
    for _ in range(1, n):
        steps += 1
        a, b = b, a + b
    return b, steps

def fib_rec(n, counter):
    counter[0] += 1
    if n <= 1:
        return n
    return fib_rec(n - 1, counter) + fib_rec(n - 2, counter)

def measure(n_values):
    rows = []
    for n in n_values:
        t0 = time.perf_counter()
        rc = [0]
        rv = fib_rec(n, rc)
        rt = time.perf_counter() - t0

        t0 = time.perf_counter()
        iv, isteps = fib_iter(n)
        it = time.perf_counter() - t0

        rows.append((n, rv, rc[0], rt, iv, isteps, it))
    return rows

if __name__ == "__main__":
    ns = [5, 10, 20, 30]
    results = measure(ns)
    print(" n | value | rec_steps | rec_time(s) | iter_steps | iter_time(s)")
    for n, rv, rsteps, rtime, iv, isteps, itime in results:
        print(f"{n:2d} | {rv:6d} | {rsteps:9d} | {rtime:10.6f} | {isteps:10d} | {itime:11.6f}")
