import tracemalloc

def run_with_memory(algorithm, data, trials=10):
    times = []
    memories = []
    result = None
    
    for _ in range(trials):
        data_copy = data[:]
        tracemalloc.start()
        start = time.perf_counter()
        result = algorithm(data_copy)
        end = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        times.append(end - start)
        memories.append(peak)
    
    return {
        "best_time": min(times),
        "worst_time": max(times),
        "average_time": statistics.mean(times),
        "best_mem": min(memories),
        "worst_mem": max(memories),
        "average_mem": statistics.mean(memories),
        "result": result
    }
