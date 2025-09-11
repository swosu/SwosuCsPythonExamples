# Fibonacci Lab

This folder contains four Python modules plus a benchmark runner:

1. **fib_recursive.py** — Bare recursive Fibonacci (no logging, no printing).
2. **fib_iterative.py** — Bare iterative Fibonacci (no logging, no printing).
3. **fib_instrumented.py** — Instrumented recursive + iterative implementations:
   - Recursive: counts function calls, additions, and tracks max recursion depth.
   - Iterative: counts iterations, additions, and rough assignment counts.
4. **fib_benchmark.py** — Runs both bare versions across `n = 1, 5, 10, 15, ...`
   until one fails (timeout or error). At each `n`, it *also* runs the instrumented
   versions (with the same timeout) and logs micro-metrics.

## Outputs
- `fib_benchmark.csv` — All data points (timestamps, statuses, times, metrics).
- `fib_wall.png` — Timing plot (wall-clock time).
- `fib_cpu.png` — Timing plot (CPU time).

## Run locally
```bash
python fib_benchmark.py
```
