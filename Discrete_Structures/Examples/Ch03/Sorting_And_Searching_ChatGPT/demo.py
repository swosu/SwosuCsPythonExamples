import random
from linear_search import linear_search
from binary_search import binary_search
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from timer_and_repeated_trials_wrapper import run_trials
from memory_profiler_wrapper import run_with_memory
from results_logger import write_results_csv
from jump_search import jump_search   # NEW

if __name__ == "__main__":
    sizes = [100, 1_000, 5_000]  # keep manageable at first for bubble
    trials = 5
    csv_file = "benchmark_results.csv"
    all_rows = []

    for n in sizes:
        print(f"\n=== Array size: {n} ===")
        data = [random.randint(0, 1_000_000) for _ in range(n)]

        # --- Sorting Algorithms --- #
        # Bubble sort
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

        # Merge sort
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

        # --- Searching Algorithms --- #
        sorted_data = sorted(data)  # searching needs sorted input

        # Linear search
        timing_lin = run_trials(lambda arr: linear_search(arr, target_value=42), sorted_data, trials=trials)
        memory_lin = run_with_memory(lambda arr: linear_search(arr, target_value=42), sorted_data, trials=trials)
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

        # Binary search
        timing_bin = run_trials(lambda arr: binary_search(arr, target=42), sorted_data, trials=trials)
        memory_bin = run_with_memory(lambda arr: binary_search(arr, target=42), sorted_data, trials=trials)
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

        # Jump search (NEW)
        timing_jump = run_trials(lambda arr: jump_search(arr, target_value=42), sorted_data, trials=trials)
        memory_jump = run_with_memory(lambda arr: jump_search(arr, target_value=42), sorted_data, trials=trials)
        all_rows.append({
            "algorithm": "jump_search",
            "size": n,
            "best_time": timing_jump["best"],
            "worst_time": timing_jump["worst"],
            "average_time": timing_jump["average"],
            "best_mem": memory_jump["best_mem"],
            "worst_mem": memory_jump["worst_mem"],
            "average_mem": memory_jump["average_mem"]
        })

    # --- Write all results to CSV --- #
    write_results_csv(csv_file, all_rows)
    print(f"\n✅ Results written to {csv_file}")
import random
from linear_search import linear_search
from binary_search import binary_search
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from timer_and_repeated_trials_wrapper import run_trials
from memory_profiler_wrapper import run_with_memory
from results_logger import write_results_csv
from jump_search import jump_search   # NEW

if __name__ == "__main__":
    sizes = [100, 1_000, 5_000]  # keep manageable at first for bubble
    trials = 5
    csv_file = "benchmark_results.csv"
    all_rows = []

    for n in sizes:
        print(f"\n=== Array size: {n} ===")
        data = [random.randint(0, 1_000_000) for _ in range(n)]

        # --- Sorting Algorithms --- #
        # Bubble sort
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

        # Merge sort
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

        # --- Searching Algorithms --- #
        sorted_data = sorted(data)  # searching needs sorted input

        # Linear search
        timing_lin = run_trials(lambda arr: linear_search(arr, target_value=42), sorted_data, trials=trials)
        memory_lin = run_with_memory(lambda arr: linear_search(arr, target_value=42), sorted_data, trials=trials)
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

        # Binary search
        timing_bin = run_trials(lambda arr: binary_search(arr, target=42), sorted_data, trials=trials)
        memory_bin = run_with_memory(lambda arr: binary_search(arr, target=42), sorted_data, trials=trials)
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

        # Jump search (NEW)
        timing_jump = run_trials(lambda arr: jump_search(arr, target_value=42), sorted_data, trials=trials)
        memory_jump = run_with_memory(lambda arr: jump_search(arr, target_value=42), sorted_data, trials=trials)
        all_rows.append({
            "algorithm": "jump_search",
            "size": n,
            "best_time": timing_jump["best"],
            "worst_time": timing_jump["worst"],
            "average_time": timing_jump["average"],
            "best_mem": memory_jump["best_mem"],
            "worst_mem": memory_jump["worst_mem"],
            "average_mem": memory_jump["average_mem"]
        })

    # --- Write all results to CSV --- #
    write_results_csv(csv_file, all_rows)
    print(f"\n✅ Results written to {csv_file}")
