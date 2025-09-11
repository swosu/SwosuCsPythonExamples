import csv, time, math, datetime, os, sys
from pathlib import Path
from multiprocessing import Process, Queue
import matplotlib.pyplot as plt

from fib_recursive import fib_recursive
from fib_iterative import fib_iterative
from fib_instrumented import (
    fib_recursive_instrumented, fib_iterative_instrumented,
    RecMetrics, IterMetrics
)

def _timed_call_in_process(func, args=(), kwargs=None, timeout_s=6.0):
    if kwargs is None:
        kwargs = {}
    q = Queue()

    def target(q):
        try:
            start_wall = time.perf_counter()
            start_cpu = time.process_time()
            val = func(*args, **kwargs)
            wall = time.perf_counter() - start_wall
            cpu = time.process_time() - start_cpu
            q.put(("ok", val, wall, cpu, ""))
        except Exception as e:
            q.put(("error", None, None, None, repr(e)))

    p = Process(target=target, args=(q,))
    p.start()
    p.join(timeout_s)
    if p.is_alive():
        p.terminate()
        p.join()
        return ("timeout", None, None, None, "timeout")
    if q.empty():
        return ("error", None, None, None, "no result")
    return q.get()

def run_benchmark(
    out_csv_path: str,
    wall_plot_path: str,
    cpu_plot_path: str,
    start_ns=(1, 5),
    step=5,
    timeout_s=6.0,
    stop_on_first_failure=True,
    instrument_each_n=True
):
    rows = []
    ns = [start_ns[0]] + list(range(start_ns[1], 100000, step))

    xs = []
    y_wall_recursive, y_wall_iterative = [], []
    y_cpu_recursive, y_cpu_iterative = [], []

    broke = False
    for n in ns:
        status_r, value_r, wall_r, cpu_r, err_r = _timed_call_in_process(fib_recursive, args=(n,), timeout_s=timeout_s)
        status_i, value_i, wall_i, cpu_i, err_i = _timed_call_in_process(fib_iterative, args=(n,), timeout_s=timeout_s)

        rec_calls = rec_adds = rec_depth = rec_assign = None
        it_iters = it_adds = it_assign = None

        if instrument_each_n:
            def rec_inst():
                val, m = fib_recursive_instrumented(n)
                return (val, m.calls, m.additions, m.max_depth, m.assignments)
            s_rec_m, rec_out, wall_rec_m, cpu_rec_m, err_rec_m = _timed_call_in_process(rec_inst, timeout_s=timeout_s)
            if s_rec_m == "ok":
                (val_m, rec_calls, rec_adds, rec_depth, rec_assign) = rec_out

            def it_inst():
                val, m = fib_iterative_instrumented(n)
                return (val, m.iterations, m.additions, m.assignments)
            s_it_m, it_out, wall_it_m, cpu_it_m, err_it_m = _timed_call_in_process(it_inst, timeout_s=timeout_s)
            if s_it_m == "ok":
                (val_im, it_iters, it_adds, it_assign) = it_out

        note = ""
        if status_r == "ok" and status_i == "ok" and value_r != value_i:
            note = "mismatch!"

        ts = datetime.datetime.now().isoformat(timespec="seconds")
        rows.append({
            "timestamp": ts, "algorithm": "recursive_bare", "n": n,
            "status": status_r, "value": value_r,
            "wall_time_sec": wall_r, "cpu_time_sec": cpu_r,
            "calls": rec_calls, "additions": rec_adds, "max_depth": rec_depth,
            "iterations": None, "assignments": rec_assign, "note": note or err_r
        })
        rows.append({
            "timestamp": ts, "algorithm": "iterative_bare", "n": n,
            "status": status_i, "value": value_i,
            "wall_time_sec": wall_i, "cpu_time_sec": cpu_i,
            "calls": None, "additions": it_adds, "max_depth": None,
            "iterations": it_iters, "assignments": it_assign, "note": note or err_i
        })

        if status_r == "ok" and status_i == "ok":
            xs.append(n)
            y_wall_recursive.append(wall_r); y_wall_iterative.append(wall_i)
            y_cpu_recursive.append(cpu_r);   y_cpu_iterative.append(cpu_i)
        else:
            broke = True

        if broke and stop_on_first_failure:
            break

    # Write CSV
    fieldnames = ["timestamp","algorithm","n","status","value","wall_time_sec","cpu_time_sec",
                  "calls","additions","max_depth","iterations","assignments","note"]
    Path(out_csv_path).parent.mkdir(parents=True, exist_ok=True)
    with open(out_csv_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader(); w.writerows(rows)

    # Plot wall-clock
    plt.figure()
    plt.plot(xs, y_wall_recursive, label="recursive (wall)")
    plt.plot(xs, y_wall_iterative, label="iterative (wall)")
    plt.xlabel("n (Fibonacci index)")
    plt.ylabel("time (seconds, wall)")
    plt.title("Fibonacci timing — wall clock")
    plt.legend(); plt.tight_layout(); plt.savefig(wall_plot_path); plt.close()

    # Plot CPU time
    plt.figure()
    plt.plot(xs, y_cpu_recursive, label="recursive (cpu)")
    plt.plot(xs, y_cpu_iterative, label="iterative (cpu)")
    plt.xlabel("n (Fibonacci index)")
    plt.ylabel("time (seconds, CPU)")
    plt.title("Fibonacci timing — CPU time")
    plt.legend(); plt.tight_layout(); plt.savefig(cpu_plot_path); plt.close()

    return {
        "points_evaluated": len(xs),
        "last_n": xs[-1] if xs else None,
        "csv_path": out_csv_path,
        "wall_plot": wall_plot_path,
        "cpu_plot": cpu_plot_path
    }

if __name__ == "__main__":
    out_dir = Path(__file__).parent
    res = run_benchmark(
        out_csv_path=str(out_dir / "fib_benchmark.csv"),
        wall_plot_path=str(out_dir / "fib_wall.png"),
        cpu_plot_path=str(out_dir / "fib_cpu.png"),
        start_ns=(1, 5),
        step=5,
        timeout_s=6.0,
        stop_on_first_failure=True,
        instrument_each_n=True
    )
    print(res)
