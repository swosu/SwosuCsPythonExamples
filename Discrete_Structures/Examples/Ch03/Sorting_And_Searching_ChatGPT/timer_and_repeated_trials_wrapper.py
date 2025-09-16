import time
import statistics

def run_trials(algorithm, data, trials=10):
    """Run algorithm multiple times and measure execution time."""
    times = []
    result = None  # To hold the algorithm output for correctness checks
    
    for _ in range(trials):
        data_copy = data[:]  # avoid in-place mutations affecting other runs
        start = time.perf_counter()
        result = algorithm(data_copy)
        end = time.perf_counter()
        times.append(end - start)
    
    return {
        "best": min(times),
        "worst": max(times),
        "average": statistics.mean(times),
        "times": times,
        "result": result
    }
