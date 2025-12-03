# data_collector.py
from __future__ import annotations

from dataclasses import dataclass, asdict
from statistics import NormalDist
from typing import Dict, List, Optional, Tuple


@dataclass(frozen=True)
class TrialRecord:
    """One trial worth of data (exactly what you said you want to capture)."""
    trial_id: int
    winning_door: int
    initial_pick: int
    revealed_losing_door: int
    switched: bool
    final_pick: int
    won: bool


@dataclass(frozen=True)
class BucketStats:
    """Stats for one outcome bucket: count, proportion, and 99% CI."""
    count: int
    proportion: float
    ci_low: float
    ci_high: float
    half_width: float


class DataCollector:
    """
    Collects Monty Hall trial records and decides when to stop based on 99% confidence intervals
    for these 4 buckets (each bucket is a Bernoulli over ALL trials):
      1) stay & win
      2) stay & lose
      3) switch & win
      4) switch & lose

    Stop rule (default):
      - at least min_trials AND
      - each bucket has at least min_bucket_count AND
      - max half-width across all 4 buckets <= target_half_width
    """

    BUCKETS = ("stay_win", "stay_lose", "switch_win", "switch_lose")

    def __init__(
        self,
        confidence: float = 0.99,
        target_half_width: float = 0.01,
        min_trials: int = 1000,
        min_bucket_count: int = 30,
        keep_records: bool = True,
    ) -> None:
        if not (0.5 < confidence < 1.0):
            raise ValueError("confidence must be between 0.5 and 1.0 (exclusive).")
        if target_half_width <= 0:
            raise ValueError("target_half_width must be > 0.")
        if min_trials < 1:
            raise ValueError("min_trials must be >= 1.")
        if min_bucket_count < 0:
            raise ValueError("min_bucket_count must be >= 0.")

        self.confidence = confidence
        self.target_half_width = target_half_width
        self.min_trials = min_trials
        self.min_bucket_count = min_bucket_count
        self.keep_records = keep_records

        self._z = NormalDist().inv_cdf(0.5 + confidence / 2.0)

        self.n_trials: int = 0
        self._counts: Dict[str, int] = {b: 0 for b in self.BUCKETS}
        self.records: List[TrialRecord] = []

    # ---------- Recording ----------

    def record_trial(
        self,
        trial_id: int,
        winning_door: int,
        initial_pick: int,
        revealed_losing_door: int,
        switched: bool,
        final_pick: int,
        won: bool,
    ) -> None:
        rec = TrialRecord(
            trial_id=trial_id,
            winning_door=winning_door,
            initial_pick=initial_pick,
            revealed_losing_door=revealed_losing_door,
            switched=switched,
            final_pick=final_pick,
            won=won,
        )
        self.n_trials += 1
        self._counts[self._bucket_name(switched=switched, won=won)] += 1
        if self.keep_records:
            self.records.append(rec)

    def record_from_result(self, trial_id: int, result: object) -> None:
        """
        Convenience: accept a GameResult-like object that has matching attributes:
          winning_door, initial_pick, revealed_losing_door, final_pick, switched, won
        """
        self.record_trial(
            trial_id=trial_id,
            winning_door=int(getattr(result, "winning_door")),
            initial_pick=int(getattr(result, "initial_pick")),
            revealed_losing_door=int(getattr(result, "revealed_losing_door")),
            switched=bool(getattr(result, "switched")),
            final_pick=int(getattr(result, "final_pick")),
            won=bool(getattr(result, "won")),
        )

    # ---------- Stats + stop rule ----------

    def bucket_counts(self) -> Dict[str, int]:
        return dict(self._counts)

    def bucket_stats(self) -> Dict[str, BucketStats]:
        """
        Compute proportion and Wilson CI for each bucket using n = total trials.
        Each bucket is: count(bucket)/n_trials.
        """
        n = self.n_trials
        stats: Dict[str, BucketStats] = {}
        for b in self.BUCKETS:
            k = self._counts[b]
            p = (k / n) if n > 0 else 0.0
            lo, hi = self._wilson_interval(k=k, n=n, z=self._z)
            stats[b] = BucketStats(
                count=k,
                proportion=p,
                ci_low=lo,
                ci_high=hi,
                half_width=(hi - lo) / 2.0,
            )
        return stats

    def stop_rule_met(self) -> Tuple[bool, str]:
        """
        Returns (should_stop, explanation).
        """
        n = self.n_trials
        if n < self.min_trials:
            return False, f"need min_trials: {n}/{self.min_trials}"

        # Ensure each bucket has some minimum representation so the CI isn't "accidentally" tight early.
        for b, c in self._counts.items():
            if c < self.min_bucket_count:
                return False, f"bucket '{b}' needs >= {self.min_bucket_count} (has {c})"

        stats = self.bucket_stats()
        worst_bucket = max(stats.items(), key=lambda kv: kv[1].half_width)
        worst_name, worst_stats = worst_bucket

        if worst_stats.half_width > self.target_half_width:
            return (
                False,
                f"worst half-width {worst_stats.half_width:.5f} in '{worst_name}' "
                f"> target {self.target_half_width:.5f}",
            )

        return True, (
            f"all buckets meet target half-width <= {self.target_half_width:.5f} "
            f"at {self.confidence:.0%} CI (n={n})"
        )

    # ---------- Internals ----------

    @staticmethod
    def _bucket_name(switched: bool, won: bool) -> str:
        if not switched and won:
            return "stay_win"
        if not switched and not won:
            return "stay_lose"
        if switched and won:
            return "switch_win"
        return "switch_lose"

    @staticmethod
    def _wilson_interval(k: int, n: int, z: float) -> Tuple[float, float]:
        """
        Wilson score interval for a proportion.
        Stable even when k=0 or k=n.
        """
        if n <= 0:
            return 0.0, 1.0

        p_hat = k / n
        z2 = z * z
        denom = 1.0 + z2 / n
        center = (p_hat + z2 / (2.0 * n)) / denom
        radius = (z * ((p_hat * (1.0 - p_hat) / n + z2 / (4.0 * n * n)) ** 0.5)) / denom
        lo = max(0.0, center - radius)
        hi = min(1.0, center + radius)
        return lo, hi


if __name__ == "__main__":
    # Quick demo to prove the stop logic works (without needing the other classes yet).
    dc = DataCollector(target_half_width=0.02, min_trials=200, min_bucket_count=10)

    # Fake some data: evenly spread buckets
    trial_id = 0
    for _ in range(400):
        trial_id += 1
        # cycle buckets just for demo
        bucket = DataCollector.BUCKETS[trial_id % 4]
        switched = bucket.startswith("switch")
        won = bucket.endswith("win")
        dc.record_trial(
            trial_id=trial_id,
            winning_door=1,
            initial_pick=2,
            revealed_losing_door=3,
            switched=switched,
            final_pick=1,
            won=won,
        )

    should_stop, why = dc.stop_rule_met()
    print("stop?", should_stop, "-", why)
    for name, st in dc.bucket_stats().items():
        print(name, st)
