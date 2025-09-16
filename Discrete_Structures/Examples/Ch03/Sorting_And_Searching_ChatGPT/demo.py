import random
from linear_search import linear_search
from binary_search import binary_search
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from timer_and_repeated_trials_wrapper import run_trials
from memory_profiler_wrapper import run_with_memory
from results_logger import write_results_csv

if __name__ == "__main__":
    sizes = [100, 1_000, 5_000]  # keep manageable at first for bubble
    trials = 5
    csv_file = "benchmark_results.csv"
    all_rows = []

    for n in sizes:
        print(f"\n=== Array size: {n} ===")
        data = [random.randint(0, 1_000_000) for _ in range(n)]

        # --- Bubble sort ---
        timing_bub = run_trials(lambda arr: bubble_sort(arr), data, trials=trials)
        memory_bub = run_with_memory(lambda arr: bubble_sort(arr), data, trials=trials)
        all_rows.append({
            "algorithm": "bubble_sort",
            "size": n,
            "best_time": timing_bub["best"],
            "worst_time": timing_bub["worst"],
            "average_time": timing_bub["average"],
            "best_mem": memory_bub["best_mem"],
            "worst_mem": memory_bub["worst_mem"],
            "average_mem": memory_bub["average_mem"]
        })

        # --- Merge sort ---
        timing_mer = run_trials(lambda arr: merge_sort(arr), data, trials=trials)
        memory_mer = run_with_memory(lambda arr: merge_sort(arr), data, trials=trials)
        all_rows.append({
            "algorithm": "merge_sort",
            "size": n,
            "best_time": timing_mer["best"],
            "worst_time": timing_mer["worst"],
            "average_time": timing_mer["average"],
            "best_mem": memory_mer["best_mem"],
            "worst_mem": memory_mer["worst_mem"],
            "average_mem": memory_mer["average_mem"]
        })

    write_results_csv(csv_file, all_rows)
    print(f"\n✅ Results written to {csv_file}")
