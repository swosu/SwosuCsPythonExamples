"""
Birthday Problem Monte Carlo with a variance/CI-based stopping rule.

Key idea:
Each Monte Carlo trial is Bernoulli:
    success = at least one shared birthday in a room of size n
So after T trials:
    p_hat = S / T
    Var(p_hat) ≈ p_hat*(1-p_hat)/T
We stop when our uncertainty (CI half-width) is small AND the estimate is stable.

Outputs:
- One plot per room size n showing variance vs trials with a vertical stop line.
- A summary plot of estimated p(n) vs the theoretical value.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

import math
import numpy as np
import matplotlib.pyplot as plt


# -----------------------------
# Statistics helpers
# -----------------------------

def z_value_for_two_sided(confidence: float) -> float:
    """
    Convert confidence level (e.g., 0.99) to a two-sided z critical value.

    For 99% CI: alpha = 0.01, z = Phi^{-1}(1 - alpha/2) = Phi^{-1}(0.995).
    We avoid scipy to keep this script lightweight.
    We'll use an accurate approximation via math.erfcinv-like approach is not in stdlib,
    so instead we provide a small lookup for common values and a fallback approximation.
    """
    common = {
        0.90: 1.6448536269514722,
        0.95: 1.959963984540054,
        0.98: 2.3263478740408408,
        0.99: 2.5758293035489004,
        0.995: 2.807033768343811,
        0.999: 3.2905267314919255,
    }
    if confidence in common:
        return common[confidence]

    # Fallback: inverse normal approx (Peter John Acklam's approximation style)
    # Good enough for stopping criteria when confidence isn't one of the common constants.
    # Reference: https://web.archive.org/web/20150910044729/http://home.online.no/~pjacklam/notes/invnorm/
    p = 0.5 + confidence / 2.0  # convert two-sided CI to one-sided tail prob
    if not (0.5 < p < 1.0):
        raise ValueError("confidence must be in (0,1)")

    # Coefficients for approximation
    a = [-3.969683028665376e+01, 2.209460984245205e+02, -2.759285104469687e+02,
         1.383577518672690e+02, -3.066479806614716e+01, 2.506628277459239e+00]
    b = [-5.447609879822406e+01, 1.615858368580409e+02, -1.556989798598866e+02,
         6.680131188771972e+01, -1.328068155288572e+01]
    c = [-7.784894002430293e-03, -3.223964580411365e-01, -2.400758277161838e+00,
         -2.549732539343734e+00, 4.374664141464968e+00, 2.938163982698783e+00]
    d = [7.784695709041462e-03, 3.224671290700398e-01, 2.445134137142996e+00,
         3.754408661907416e+00]

    plow = 0.02425
    phigh = 1 - plow

    if p < plow:
        q = math.sqrt(-2 * math.log(p))
        return (((((c[0]*q + c[1])*q + c[2])*q + c[3])*q + c[4])*q + c[5]) / \
               ((((d[0]*q + d[1])*q + d[2])*q + d[3])*q + 1)
    elif p > phigh:
        q = math.sqrt(-2 * math.log(1 - p))
        return -(((((c[0]*q + c[1])*q + c[2])*q + c[3])*q + c[4])*q + c[5]) / \
                 ((((d[0]*q + d[1])*q + d[2])*q + d[3])*q + 1)
    else:
        q = p - 0.5
        r = q*q
        return (((((a[0]*r + a[1])*r + a[2])*r + a[3])*r + a[4])*r + a[5]) * q / \
               (((((b[0]*r + b[1])*r + b[2])*r + b[3])*r + b[4])*r + 1)


def wilson_interval_half_width(successes: int, trials: int, z: float) -> float:
    """
    Wilson score confidence interval half-width for a binomial proportion.

    If p_hat = successes / trials, then the Wilson interval center and half-width are:
        denom = 1 + z^2 / trials
        center = (p_hat + z^2/(2*trials)) / denom
        half = z * sqrt( p_hat(1-p_hat)/trials + z^2/(4*trials^2) ) / denom

    We return the half-width 'half' as a direct uncertainty measure.
    """
    if trials <= 0:
        return float("inf")
    p_hat = successes / trials
    z2 = z * z
    denom = 1.0 + z2 / trials
    radicand = (p_hat * (1.0 - p_hat) / trials) + (z2 / (4.0 * trials * trials))
    return (z * math.sqrt(radicand)) / denom


def estimated_variance_of_phat(p_hat: float, trials: int) -> float:
    """Plug-in estimate of Var(p_hat) = p(1-p)/T using p_hat."""
    if trials <= 0:
        return float("inf")
    return (p_hat * (1.0 - p_hat)) / trials


# -----------------------------
# Simulation helpers
# -----------------------------

def count_collisions_in_batch(rng: np.random.Generator, people: int, batch_size: int) -> int:
    """
    Simulate 'batch_size' rooms of size 'people' and count how many have a shared birthday.

    Efficient trick:
    - Generate birthdays as integers 0..364 into a (batch_size, people) array
    - Sort each row
    - A duplicate exists in a row if any adjacent entries are equal after sorting
    """
    birthdays = rng.integers(0, 365, size=(batch_size, people), endpoint=False)
    birthdays.sort(axis=1)
    has_duplicate = np.any(birthdays[:, 1:] == birthdays[:, :-1], axis=1)
    return int(np.sum(has_duplicate))


@dataclass
class ConvergenceHistory:
    trials: List[int]
    p_hat: List[float]
    var_hat: List[float]
    ci_half_width: List[float]
    stop_trials: int
    stop_p_hat: float
    stop_var_hat: float
    stop_ci_half_width: float
    stopped_reason: str


def run_until_converged(
    rng: np.random.Generator,
    people: int,
    *,
    confidence: float = 0.99,
    epsilon: float = 0.005,
    drift_tol: float = 0.0005,
    window: int = 6,
    batch_size: int = 5000,
    min_trials: int = 20000,
    max_trials: int = 2_000_000,
    checkpoint_every_batches: int = 1,
) -> ConvergenceHistory:
    """
    Run Monte Carlo for a fixed room size 'people' until the estimate converges.

    Convergence definition:
    1) Uncertainty small: Wilson CI half-width <= epsilon
    2) Estimate stable: last 'window' checkpoints have small max step-to-step drift
    3) Guardrails: trials >= min_trials and trials <= max_trials

    Why both CI and drift?
    - CI ensures statistical precision.
    - Drift check prevents stopping during a rare lucky streak where CI appears tight early.
    """
    z = z_value_for_two_sided(confidence)

    successes = 0
    trials = 0

    trials_hist: List[int] = []
    p_hist: List[float] = []
    var_hist: List[float] = []
    ci_hist: List[float] = []

    stopped_reason = f"Reached max_trials={max_trials} without satisfying convergence."

    batches_run = 0
    while trials < max_trials:
        successes += count_collisions_in_batch(rng, people, batch_size)
        trials += batch_size
        batches_run += 1

        if batches_run % checkpoint_every_batches != 0:
            continue

        p_hat = successes / trials
        var_hat = estimated_variance_of_phat(p_hat, trials)
        half_width = wilson_interval_half_width(successes, trials, z)

        trials_hist.append(trials)
        p_hist.append(p_hat)
        var_hist.append(var_hat)
        ci_hist.append(half_width)

        # Need enough data to judge stability
        if trials < min_trials or len(p_hist) < window + 1:
            continue

        # Stability: look at the last 'window' step-to-step changes in p_hat
        recent = p_hist[-(window + 1):]
        step_changes = [abs(recent[i] - recent[i - 1]) for i in range(1, len(recent))]
        max_step_change = max(step_changes)

        # Our “steady state” rule:
        if half_width <= epsilon and max_step_change <= drift_tol:
            stopped_reason = (
                f"Converged: CI half-width <= {epsilon} and drift <= {drift_tol} "
                f"over last {window} checkpoints."
            )
            break

    stop_trials = trials_hist[-1] if trials_hist else trials
    stop_p_hat = p_hist[-1] if p_hist else (successes / trials if trials else 0.0)
    stop_var_hat = var_hist[-1] if var_hist else estimated_variance_of_phat(stop_p_hat, trials)
    stop_ci_half_width = ci_hist[-1] if ci_hist else wilson_interval_half_width(successes, trials, z)

    return ConvergenceHistory(
        trials=trials_hist,
        p_hat=p_hist,
        var_hat=var_hist,
        ci_half_width=ci_hist,
        stop_trials=stop_trials,
        stop_p_hat=stop_p_hat,
        stop_var_hat=stop_var_hat,
        stop_ci_half_width=stop_ci_half_width,
        stopped_reason=stopped_reason,
    )


def theoretical_birthday_probability(people: int) -> float:
    """
    Exact probability of at least one shared birthday (ignoring leap day), i.e.
      1 - P(all birthdays distinct)
      = 1 - product_{k=0 to people-1} (365-k)/365
    """
    if people <= 1:
        return 0.0
    prob_distinct = 1.0
    for k in range(people):
        prob_distinct *= (365 - k) / 365
    return 1.0 - prob_distinct


# -----------------------------
# Plotting
# -----------------------------

def plot_variance_history(n: int, hist: ConvergenceHistory, out_dir: Path) -> None:
    """
    Plot Var(p_hat) vs trials for a single room size n.
    Mark the stopping point with a vertical line.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    plt.figure()
    plt.plot(hist.trials, hist.var_hat, label="Estimated Var(p̂) = p̂(1-p̂)/T")
    plt.axvline(hist.stop_trials, linestyle="--", label=f"Stop @ T={hist.stop_trials}")
    plt.xlabel("Trials (T)")
    plt.ylabel("Estimated variance of p̂")
    plt.title(f"Birthday problem Monte Carlo convergence (n={n})")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_dir / f"variance_convergence_n_{n:02d}.png", dpi=160)
    plt.close()

    # Optional extra plot: CI half-width (often more interpretable than variance)
    plt.figure()
    plt.plot(hist.trials, hist.ci_half_width, label="Wilson CI half-width")
    plt.axhline(y=hist.stop_ci_half_width, linestyle=":", label=f"Stop half-width={hist.stop_ci_half_width:.4g}")
    plt.axvline(hist.stop_trials, linestyle="--", label=f"Stop @ T={hist.stop_trials}")
    plt.xlabel("Trials (T)")
    plt.ylabel("CI half-width")
    plt.title(f"CI half-width over time (n={n})")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_dir / f"ci_halfwidth_n_{n:02d}.png", dpi=160)
    plt.close()


def plot_summary(results: Dict[int, ConvergenceHistory], out_dir: Path) -> None:
    """Plot estimated probability vs n alongside the theoretical curve."""
    out_dir.mkdir(parents=True, exist_ok=True)

    ns = sorted(results.keys())
    p_est = [results[n].stop_p_hat for n in ns]
    p_theory = [theoretical_birthday_probability(n) for n in ns]

    plt.figure()
    plt.plot(ns, p_est, marker="o", label="Monte Carlo (stopped when converged)")
    plt.plot(ns, p_theory, label="Theoretical")
    plt.xlabel("People in room (n)")
    plt.ylabel("P(at least one shared birthday)")
    plt.title("Birthday problem: Monte Carlo vs theory (n=2..50)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_dir / "summary_probability_vs_n.png", dpi=180)
    plt.close()


# -----------------------------
# Main
# -----------------------------

def main() -> None:
    # You can tweak these dials depending on how “tight” you want the final estimates.
    # epsilon = absolute error tolerance on p (e.g., 0.005 => about half a percentage point)
    config = {
        "confidence": 0.99,
        "epsilon": 0.005,
        "drift_tol": 0.0005,
        "window": 6,
        "batch_size": 5000,
        "min_trials": 20000,
        "max_trials": 2_000_000,
        "checkpoint_every_batches": 1,
    }

    rng = np.random.default_rng(seed=12345)  # reproducible chaos 🎲
    output_dir = Path("birthday_outputs")

    results: Dict[int, ConvergenceHistory] = {}

    for n in range(2, 51):
        hist = run_until_converged(rng, n, **config)
        results[n] = hist
        plot_variance_history(n, hist, output_dir)

        print(
            f"n={n:02d}  p̂={hist.stop_p_hat:.6f}  "
            f"Var(p̂)≈{hist.stop_var_hat:.3e}  "
            f"CI_half≈{hist.stop_ci_half_width:.4g}  "
            f"T={hist.stop_trials:,}  "
            f"Reason: {hist.stopped_reason}"
        )

    plot_summary(results, output_dir)
    print(f"\nSaved plots to: {output_dir.resolve()}")


if __name__ == "__main__":
    main()
