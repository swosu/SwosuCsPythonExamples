import cupy as cp
import time

N = 8000
A = cp.random.rand(N, N)
B = cp.random.rand(N, N)

cp.cuda.Stream.null.synchronize()
start = time.time()
C = A @ B
cp.cuda.Stream.null.synchronize()
print(f"GPU {N}x{N} multiply: {time.time()-start:.2f} seconds")

