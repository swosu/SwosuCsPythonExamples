#!/usr/bin/env python3
# ASCII-only. Samples process memory/CPU while naive recursion runs.
# This will not be as precise as Valgrind, but it is classroom-friendly.

import os, time, threading
try:
    import psutil
except ImportError:
    psutil = None

from fib_variants import DataTracker, fib_recursive

SAMPLE_INTERVAL = 0.05  # seconds

def sampler(stop_flag, pid, out_path):
    if psutil is None:
        return
    proc = psutil.Process(pid)
    with open(out_path, "w") as f:
        f.write("t_sec,rss_bytes,cpu_percent\n")
        t0 = time.time()
        while not stop_flag["stop"]:
            t = time.time() - t0
            try:
                rss = proc.memory_info().rss
                cpu = proc.cpu_percent(interval=None)
            except psutil.Error:
                break
            f.write(f"{t:.3f},{rss},{cpu:.1f}\n")
            time.sleep(SAMPLE_INTERVAL)

def main(n=38):
    # WARNING: pick n that is slow enough to show growth, but not so large it hangs.
    trk = DataTracker()
    stop_flag = {"stop": False}
    out_csv = "fib_memtrace.csv"

    th = None
    if psutil is not None:
        th = threading.Thread(target=sampler, args=(stop_flag, os.getpid(), out_csv))
        th.daemon = True
        th.start()

    t0 = time.time()
    val = fib_recursive(n, trk)
    t1 = time.time()

    stop_flag["stop"] = True
    if th is not None:
        th.join()

    with open("fib_memprobe_summary.txt", "w") as f:
        f.write("n,value,time_sec,calls,adds,assigns\n")
        f.write(f"{n},{val},{t1-t0:.6f},{trk.calls},{trk.adds},{trk.assigns}\n")

    print("[OK] Wrote fib_memtrace.csv and fib_memprobe_summary.txt")

if __name__ == "__main__":
    main(38)

