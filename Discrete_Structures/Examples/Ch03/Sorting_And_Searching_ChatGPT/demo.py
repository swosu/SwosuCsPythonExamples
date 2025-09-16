import random
from linear_search import linear_search
from timer_and_repeated_trials_wrapper import run_trials
from memory_profiler_wrapper import run_with_memory

if __name__ == "__main__":
    # generate a random list
    data = [random.randint(0, 1000000) for _ in range(10000)]
    
    # run timing tests
    timing_results = run_trials(lambda arr: linear_search(arr, 42), data, trials=20)
    print("Timing results:", timing_results)
    
    # run timing + memory tests
    memory_results = run_with_memory(lambda arr: linear_search(arr, 42), data, trials=20)
    print("Timing + Memory results:", memory_results)
