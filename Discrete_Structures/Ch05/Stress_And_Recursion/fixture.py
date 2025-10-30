import random, csv
from tracker import Tracker
from bubble_sort_alg import bubble_sort
from merge_sort_alg import merge_sort
from parallel_merge_sort_alg import parallel_merge_sort
from builtin_sorts import builtin_sort, parallel_builtin_sort

def run_experiment(sizes, runs_per_size=2, outfile="results.csv"):
    with open(outfile, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["algorithm","batch_size","run",
                         "adds","subs","comps","reads","writes",
                         "func_calls","time"])

        algorithms = [bubble_sort, merge_sort, parallel_merge_sort,
                      builtin_sort, parallel_builtin_sort]

        for size in sizes:
            for run in range(runs_per_size):
                data = [random.randint(0, 10**6) for _ in range(size)]
                print(f"\n🧪 Size {size} | Run {run+1}")

                for alg in algorithms:
                    t = Tracker()
                    t.start()
                    alg(data) if 'builtin' in alg.__name__ else alg(data, t)
                    t.stop()
                    row = [alg.__name__, size, run+1, *t.summary().values()]
                    writer.writerow(row)
                    print(f"{alg.__name__:25s}  {t.elapsed():.4f}s")
