from math import sqrt, log
from pathlib import Path
import csv
import matplotlib.pyplot as plt

def count_primes_upto(n: int) -> int:
    if n < 2:
        return 0
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    limit = int(sqrt(n))
    for p in range(2, limit + 1):
        if sieve[p]:
            start = p * p
            step = p
            span = ((n - start) // step) + 1
            sieve[start:n+1:step] = b"\x00" * span
    return int(sum(sieve))

def pnt_estimate(x: int) -> float:
    return x / log(x)

def li_series_estimate(x: int, terms: int = 4) -> float:
    L = log(x)
    coeffs = [1, 1, 2, 6]
    s = sum(coeffs[k] / (L ** k) for k in range(terms))
    return (x / L) * s

def main() -> None:
    milestones = [10, 100, 1_000, 10_000, 100_000, 1_000_000]
    rows = [(n, count_primes_upto(n)) for n in milestones]

    out = Path(".")
    with (out / "prime_counts.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["N", "pi(N)"])
        w.writerows(rows)

    xs = [n for n, _ in rows]; ys = [c for _, c in rows]
    plt.figure(figsize=(7,5))
    plt.plot(xs, ys, marker="o")
    plt.xscale("log"); plt.yscale("log")
    plt.title("Number of primes ≤ N (log-log plot)")
    plt.xlabel("N (log)"); plt.ylabel("pi(N) (log)")
    plt.tight_layout(); plt.savefig(out / "prime_counts_log_plot.png"); plt.close()

    x = 10_000_000
    pnt = pnt_estimate(x); li = li_series_estimate(x)
    actual = count_primes_upto(x)
    with (out / "prime_prediction.txt").open("w", encoding="utf-8") as f:
        for n, c in rows: f.write(f"pi({n}) = {c}\n")
        f.write(f"\nPNT estimate x/log x: {pnt:.0f}\n")
        f.write(f"Li-series estimate  : {li:.0f}\n")
        f.write(f"Actual pi(10,000,000) from sieve: {actual}\n")

if __name__ == "__main__":
    main()
