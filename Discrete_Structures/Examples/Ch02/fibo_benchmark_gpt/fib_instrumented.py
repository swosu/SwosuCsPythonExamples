from dataclasses import dataclass

@dataclass
class RecMetrics:
    n: int = 0
    calls: int = 0
    additions: int = 0
    max_depth: int = 0
    assignments: int = 0  # rough proxy; recursion has fewer explicit assignments

def fib_recursive_instrumented(n: int, metrics: RecMetrics | None = None, depth: int = 0):
    if n < 0:
        raise ValueError("n must be non-negative")
    if metrics is None:
        metrics = RecMetrics(n=n)
    # entering the function
    metrics.calls += 1
    if depth > metrics.max_depth:
        metrics.max_depth = depth

    if n < 2:
        return n, metrics

    v1, metrics = fib_recursive_instrumented(n - 1, metrics, depth + 1)
    v2, metrics = fib_recursive_instrumented(n - 2, metrics, depth + 1)
    # one addition to combine the two results
    metrics.additions += 1
    # local rebindings (count as assignments)
    metrics.assignments += 2
    return v1 + v2, metrics


@dataclass
class IterMetrics:
    n: int = 0
    iterations: int = 0
    additions: int = 0
    assignments: int = 0

def fib_iterative_instrumented(n: int, metrics: IterMetrics | None = None):
    if n < 0:
        raise ValueError("n must be non-negative")
    if metrics is None:
        metrics = IterMetrics(n=n)

    a = 0
    b = 1
    metrics.assignments += 2  # a=0, b=1

    for _ in range(n):
        tmp = a + b
        metrics.additions += 1
        metrics.assignments += 1  # tmp=...
        a, b = b, tmp
        metrics.assignments += 2
        metrics.iterations += 1

    return a, metrics
