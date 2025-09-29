from multiprocessing import Pool
import time, math

def inside(n):
    import random
    count = 0
    for _ in range(n):
        x, y = random.random(), random.random()
        if x*x + y*y <= 1.0:
            count += 1
    return count

if __name__ == "__main__":
    N = 10_000_000   # increase to show big speedup
    workers = 8      # try 1, 2, 4, … up to your CPU count
    with Pool(workers) as p:
        start = time.time()
        counts = p.map(inside, [N//workers]*workers)
        pi = 4 * sum(counts) / N
        print(f"π ≈ {pi}, time: {time.time()-start:.2f}s with {workers} workers")

