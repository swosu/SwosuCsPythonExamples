#!/usr/bin/env python3
"""
Coin Toss Confidence Interval Demo
- Simulate Bernoulli trials (Heads=1, Tails=0)
- Plot running estimate p-hat vs n with 0.5 reference line
- Plot whisker-style confidence intervals at selected n values

This uses the same normal-approx (Wald) halfwidth you use in Chapter 3:
    halfwidth = z * sqrt(p_hat * (1-p_hat) / n)

Note: for very small n, Wald intervals can be goofy. We clip to [0, 1] for display.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


@dataclass(frozen=True)
class CI:
    lower: np.ndarray
    upper: np.ndarray
    halfwidth: np.ndarray


def z_value(confidence: float) -> float:
    """Common two-sided z critical values. Keeps dependencies light."""
    table = {
        0.90: 1.645,
        0.95: 1.960,
        0.99: 2.576,
    }
    # If it's not a common one, default to 1.96 as a sane teaching default.
    return table.get(round(confidence, 2), 1.960)


def wald_ci(p_hat: np.ndarray, n: np.ndarray, z: float) -> CI:
    half = z * np.sqrt((p_hat * (1.0 - p_hat)) / n)
    lower = np.clip(p_hat - half, 0.0, 1.0)
    upper = np.clip(p_hat + half, 0.0, 1.0)
    return CI(lower=lower, upper=upper, halfwidth=half)


def select_whisker_points(total_n: int, k: int = 35) -> np.ndarray:
    """
    Pick roughly log-spaced n-values for whiskers so the plot isn't a porcupine.
    Includes 1 and total_n.
    """
    if total_n <= 1:
        return np.array([1], dtype=int)

    xs = np.unique(np.round(np.logspace(0, np.log10(total_n), num=k)).astype(int))
    xs[0] = 1
    xs[-1] = total_n
    return xs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--trials", type=int, default=5000, help="Number of coin tosses (n).")
    ap.add_argument("--seed", type=int, default=42, help="RNG seed for reproducibility.")
    ap.add_argument("--confidence", type=float, default=0.95, help="Confidence level (e.g., 0.95).")
    ap.add_argument("--out", type=Path, default=Path("diagrams/coin_toss_ci_demo.pdf"),
                    help="Output PDF path for the figure.")
    args = ap.parse_args()

    n = args.trials
    if n < 1:
        raise SystemExit("trials must be >= 1")

    rng = np.random.default_rng(args.seed)
    tosses = rng.integers(0, 2, size=n)          # 0=Tails, 1=Heads
    cum_heads = np.cumsum(tosses)
    ns = np.arange(1, n + 1)
    p_hat = cum_heads / ns

    z = z_value(args.confidence)
    ci = wald_ci(p_hat=p_hat, n=ns, z=z)

    whisk_n = select_whisker_points(n, k=35)
    whisk_p = p_hat[whisk_n - 1]
    whisk_low = ci.lower[whisk_n - 1]
    whisk_high = ci.upper[whisk_n - 1]
    whisk_err = np.vstack([whisk_p - whisk_low, whisk_high - whisk_p])

    args.out.parent.mkdir(parents=True, exist_ok=True)

    # One figure, two stacked panels (keeps inclusion simple).
    fig = plt.figure(figsize=(10.5, 7.5))

    ax1 = fig.add_subplot(2, 1, 1)
    ax1.plot(ns, p_hat, linewidth=1.2, label=r"running $\hat{p}$ (Heads rate)")
    ax1.plot(ns, np.full_like(ns, 0.5, dtype=float), linestyle="--", linewidth=1.0, label="true p = 0.5")
    ax1.fill_between(ns, ci.lower, ci.upper, alpha=0.18, label=f"{int(args.confidence*100)}% CI band (Wald)")
    ax1.set_title("Coin tosses: estimate stabilizes, uncertainty shrinks")
    ax1.set_xlabel("n (number of tosses)")
    ax1.set_ylabel(r"$\hat{p}$")
    ax1.set_ylim(-0.02, 1.02)
    ax1.legend(loc="best")

    ax2 = fig.add_subplot(2, 1, 2)
    ax2.errorbar(whisk_n, whisk_p, yerr=whisk_err, fmt="o", markersize=3.5, capsize=2)
    ax2.plot(whisk_n, np.full_like(whisk_n, 0.5, dtype=float), linestyle="--", linewidth=1.0)
    ax2.set_title("Whisker view: confidence intervals tighten as n grows")
    ax2.set_xlabel("n (selected points)")
    ax2.set_ylabel(r"$\hat{p}$ with CI")
    ax2.set_ylim(-0.02, 1.02)

    fig.tight_layout()
    fig.savefig(args.out, bbox_inches="tight")
    print(f"Wrote: {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

