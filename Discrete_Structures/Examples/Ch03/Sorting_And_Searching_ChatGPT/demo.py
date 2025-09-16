import random
from linear_search import linear_search
from binary_search import binary_search
from timer_and_repeated_trials_wrapper import run_trials
from memory_profiler_wrapper import run_with_memory
from results_logger import write_results_csv

if __name__ == "__main__":
    sizes = [100, 1_000, 10_000, 100_000]
    trials = 10
    csv_file = "benchmark_results.csv"

    all_rows = []

    for n in sizes:
        print(f"\n=== Array size: {n} ===")

        data = [random.randint(0, 1_000_000) for _ in range(n)]

        # --- Linear search ---
        timing_lin = run_trials(lambda arr: linear_search(arr, 42), data, trials=trials)
        memory_lin = run_with_memory(lambda arr: linear_search(arr, 42), data, trials=trials)

        all_rows.append({
            "algorithm": "linear_search",
            "size": n,
            "best_time": timing_lin["best"],
            "worst_time": timing_lin["worst"],
            "average_time": timing_lin["average"],
            "best_mem": memory_lin["best_mem"],
            "worst_mem": memory_lin["worst_mem"],
            "average_mem": memory_lin["average_mem"]
        })

        # --- Binary search ---
        sorted_data = sorted(data)
        timing_bin = run_trials(lambda arr: binary_search(arr, 42), sorted_data, trials=trials)
        memory_bin = run_with_memory(lambda arr: binary_search(arr, 42), sorted_data, trials=trials)

        all_rows.append({
            "algorithm": "binary_search",
            "size": n,
            "best_time": timing_bin["best"],
            "worst_time": timing_bin["worst"],
            "average_time": timing_bin["average"],
            "best_mem": memory_bin["best_mem"],
            "worst_mem": memory_bin["worst_mem"],
            "average_mem": memory_bin["average_mem"]
        })

    # Write results to CSV
    write_results_csv(csv_file, all_rows)
    print(f"\n✅ Results written to {csv_file}")
