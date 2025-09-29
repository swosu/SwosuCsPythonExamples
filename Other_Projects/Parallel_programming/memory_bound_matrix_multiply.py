import numpy as np
import time

N = 4000  # adjust size
A = np.random.rand(N, N)
B = np.random.rand(N, N)

start = time.time()
C = A @ B
print(f"{N}x{N} matrix multiply took {time.time()-start:.2f} seconds")

