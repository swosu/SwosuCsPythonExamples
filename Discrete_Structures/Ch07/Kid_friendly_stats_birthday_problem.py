"""
Birthday Problem (Monte Carlo) with a mathematically-based stopping rule.

Super-simple viewpoint:
- One simulation is a YES/NO question:
    "In a room with N people, is there at least one shared birthday?"
  YES -> success (1), NO -> failure (0)
- That YES/NO result is a Bernoulli trial (like a coin flip).
- Repeating trials many times is a Bernoulli process.

What we estimate:
- After number_of_trials trials, if yes_count is how many YES outcomes we saw:
    estimated_probability = yes_count / number_of_trials

How we decide "enough trials":
- We compute a (kid-friendly) normal-approximation confidence interval half-width:
    half_width ≈ z_value * sqrt( estimated_probability * (1 - estimated_probability) / number_of_trials )

Stop when:
1) half_width <= absolute_tolerance
2) number_of_trials >= minimum_trials  (guardrail)
3) the estimate has stopped wobbling across recent checkpoints (stability check)
4) safety cap: number_of_trials <= maximum_trials

Outputs:
- For each room size 2..50:
  - variance-over-trials plot (with stop marked)
- After all room sizes:
  - trials-needed-vs-room-size plot
  - estimated probability vs theoretical probability plot
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict

import math
import numpy as np
import matplotlib.pyplot as plt


# -----------------------------
# Data structure for one room size
# -----------------------------

@dataclass
class ConvergenceRecord:
    number_of_people: int
    checkpoint_trial_counts: List[int]
    checkpoint_estimated_probabilities: List[float]
    checkpoint_estimated_variances: List[float]
    checkpoint_confidence_half_widths: List[float]
    stop_trial_count: int
    stop_estimated_probability: float
    stop_confidence_half_width: float
    stopped_because: str


# -----------------------------
# "Kid-friendly" statistics helpers
# -----------------------------

def z_value_for_two_sided_confidence(confidence_level: float) -> float:
    """
    Return the z-critical value for a two-sided confidence interval.

    Think of z like a "safety bubble multiplier".
    Bigger confidence -> bigger z -> bigger bubble.

    Common values:
    - 90%  -> 1.645
    - 95%  -> 1.960
    - 99%  -> 2.576
    """
    common_values = {
        0.90: 1.6448536269514722,
        0.95: 1.959963984540054,
        0.99: 2.5758293035489004,
    }
    if confidence_level not in common_values:
        raise ValueError(
            f"Please use one of these confidence levels: {sorted(common_values.keys())}. "
            f"You asked for {confidence_level}."
        )
    return common_values[confidence_level]


def estimated_variance_of_estimated_probability(estimated_probability: float, number_of_trials: int) -> float:
    """
    Approximate variance of the estimator:
        Var(estimated_probability) ≈ p(1-p) / trials
    We plug in estimated_probability for p.
    """
    if number_of_trials <= 0:
        return float("inf")
    return estimated_probability * (1.0 - estimated_probability) / number_of_trials


def normal_approx_confidence_half_width(
    estimated_probability: float,
    number_of_trials: int,
    z_value: float
) -> float:
    """
    Kid-friendly normal-approximation confidence half-width:
        half_width ≈ z * sqrt( p(1-p) / trials )
    We plug in estimated_probability for p.
    """
    variance = estimated_variance_of_estimated_probability(estimated_probability, number_of_trials)
    return z_value * math.sqrt(variance)


# -----------------------------
# Birthday simulation helpers
# -----------------------------

def room_has_shared_birthday(birthdays_for_one_room: np.ndarray) -> bool:
    """
    Returns True if any value repeats in the array.
    """
    # Sorting makes duplicates adjacent.
    sorted_birthdays = np.sort(birthdays_for_one_room)
    return bool(np.any(sorted_birthdays[1:] == sorted_birthdays[:-1]))


def count_rooms_with_shared_birthday(
    random_generator: np.random.Generator,
    number_of_people: int,
    number_of_rooms_in_batch: int
) -> int:
    """
    Simulate many rooms in one batch and count how many have at least one shared birthday.
    This is much faster than simulating rooms one-by-one in Python loops.
    """
    birthdays = random_generator.integers(
        low=0, high=365, size=(number_of_rooms_in_batch, number_of_people), endpoint=False
    )
    birthdays.sort(axis=1)
    room_has_duplicate = np.any(birthdays[:, 1:] == birthdays[:, :-1], axis=1)
    return int(np.sum(room_has_duplicate))


def theoretical_probability_of_shared_birthday(number_of_people: int) -> float:
    """
    Exact formula (ignoring leap day):
        P(shared) = 1 - P(all distinct)
                 = 1 - Π_{k=0..n-1} (365-k)/365
    """
    if number_of_people <= 1:
        return 0.0

    probability_all_distinct = 1.0
    for k in range(number_of_people):
        probability_all_distinct *= (365 - k) / 365

    return 1.0 - probability_all_distinct


# -----------------------------
# Stopping rule helper
# -----------------------------

def estimate_is_stable(
    recent_estimated_probabilities: List[float],
    maximum_allowed_change_between_checkpoints: float
) -> bool:
    """
    The estimate is stable if the biggest step-to-step change is small enough.
    """
    if len(recent_estimated_probabilities) < 2:
        return False

    changes = []
    for index in range(1, len(recent_estimated_probabilities)):
        changes.append(abs(recent_estimated_probabilities[index] - recent_estimated_probabilities[index - 1]))

    return max(changes) <= maximum_allowed_change_between_checkpoints


# -----------------------------
# Run for one room size until convergence
# -----------------------------

def run_until_converged_for_one_room_size(
    random_generator: np.random.Generator,
    number_of_people: int,
    *,
    confidence_level: float,
    absolute_tolerance: float,
    minimum_trials: int,
    maximum_trials: int,
    rooms_per_batch: int,
    batches_per_checkpoint: int,
    stability_window_checkpoints: int,
    maximum_allowed_change_between_checkpoints: float
) -> ConvergenceRecord:
    """
    Run Monte Carlo for one room size and stop when "confident enough".
    """

    z_value = z_value_for_two_sided_confidence(confidence_level)

    yes_count = 0
    number_of_trials = 0
    batches_completed = 0

    checkpoint_trial_counts: List[int] = []
    checkpoint_estimated_probabilities: List[float] = []
    checkpoint_estimated_variances: List[float] = []
    checkpoint_confidence_half_widths: List[float] = []

    stopped_because = f"Reached maximum_trials={maximum_trials} without meeting stopping rule."

    while number_of_trials < maximum_trials:
        yes_count += count_rooms_with_shared_birthday(random_generator, number_of_people, rooms_per_batch)
        number_of_trials += rooms_per_batch
        batches_completed += 1

        # Only record and evaluate convergence every so often, to reduce overhead.
        if batches_completed % batches_per_checkpoint != 0:
            continue

        estimated_probability = yes_count / number_of_trials
        estimated_variance = estimated_variance_of_estimated_probability(estimated_probability, number_of_trials)
        confidence_half_width = normal_approx_confidence_half_width(estimated_probability, number_of_trials, z_value)

        checkpoint_trial_counts.append(number_of_trials)
        checkpoint_estimated_probabilities.append(estimated_probability)
        checkpoint_estimated_variances.append(estimated_variance)
        checkpoint_confidence_half_widths.append(confidence_half_width)

        # Guardrails: don't stop too early.
        if number_of_trials < minimum_trials:
            continue
        if len(checkpoint_estimated_probabilities) < stability_window_checkpoints + 1:
            continue

        recent = checkpoint_estimated_probabilities[-(stability_window_checkpoints + 1):]
        stable = estimate_is_stable(recent, maximum_allowed_change_between_checkpoints)

        if confidence_half_width <= absolute_tolerance and stable:
            stopped_because = (
                "Stopped because:\n"
                f"- confidence half-width ({confidence_half_width:.6f}) <= tolerance ({absolute_tolerance})\n"
                f"- estimate stabilized over the last {stability_window_checkpoints} checkpoints\n"
                f"- trials ({number_of_trials}) >= minimum_trials ({minimum_trials})"
            )
            break

    final_estimated_probability = checkpoint_estimated_probabilities[-1]
    final_confidence_half_width = checkpoint_confidence_half_widths[-1]

    return ConvergenceRecord(
        number_of_people=number_of_people,
        checkpoint_trial_counts=checkpoint_trial_counts,
        checkpoint_estimated_probabilities=checkpoint_estimated_probabilities,
        checkpoint_estimated_variances=checkpoint_estimated_variances,
        checkpoint_confidence_half_widths=checkpoint_confidence_half_widths,
        stop_trial_count=checkpoint_trial_counts[-1],
        stop_estimated_probability=final_estimated_probability,
        stop_confidence_half_width=final_confidence_half_width,
        stopped_because=stopped_because
    )


# -----------------------------
# Plotting helpers
# -----------------------------

def plot_variance_over_trials(record: ConvergenceRecord, output_folder: Path) -> None:
    output_folder.mkdir(parents=True, exist_ok=True)

    plt.figure()
    plt.plot(record.checkpoint_trial_counts, record.checkpoint_estimated_variances, label="Estimated variance")
    plt.axvline(record.stop_trial_count, linestyle="--", label=f"Stopped at {record.stop_trial_count:,} trials")
    plt.xlabel("Number of trials")
    plt.ylabel("Estimated variance of the probability estimate")
    plt.title(f"Variance shrinking over trials (room size = {record.number_of_people})")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_folder / f"variance_room_{record.number_of_people:02d}.png", dpi=160)
    plt.close()


def plot_trials_needed_by_room_size(records: List[ConvergenceRecord], output_folder: Path) -> None:
    output_folder.mkdir(parents=True, exist_ok=True)

    room_sizes = [r.number_of_people for r in records]
    trials_needed = [r.stop_trial_count for r in records]

    plt.figure()
    plt.plot(room_sizes, trials_needed, marker="o")
    plt.xlabel("Number of people in room")
    plt.ylabel("Number of trials needed to stop")
    plt.title("How many Monte Carlo trials were needed to become confident?")
    plt.tight_layout()
    plt.savefig(output_folder / "trials_needed_by_room_size.png", dpi=180)
    plt.close()


def plot_estimated_probability_vs_theory(records: List[ConvergenceRecord], output_folder: Path) -> None:
    output_folder.mkdir(parents=True, exist_ok=True)

    room_sizes = [r.number_of_people for r in records]
    estimated = [r.stop_estimated_probability for r in records]
    theoretical = [theoretical_probability_of_shared_birthday(n) for n in room_sizes]

    plt.figure()
    plt.plot(room_sizes, estimated, marker="o", label="Monte Carlo (stopped when confident)")
    plt.plot(room_sizes, theoretical, label="Theoretical")
    plt.xlabel("Number of people in room")
    plt.ylabel("Probability of at least one shared birthday")
    plt.title("Birthday problem: simulation vs theory (room sizes 2..50)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_folder / "estimated_probability_vs_theory.png", dpi=180)
    plt.close()


# -----------------------------
# Main experiment runner
# -----------------------------

def run_experiment_for_room_sizes_two_through_fifty() -> None:
    output_folder = Path("birthday_problem_outputs_kid_friendly")
    output_folder.mkdir(parents=True, exist_ok=True)

    # These are the knobs you can tweak:
    confidence_level = 0.99
    absolute_tolerance = 0.005  # “within about half a percentage point”
    minimum_trials = 20_000
    maximum_trials = 2_000_000

    # Speed controls:
    rooms_per_batch = 10_000              # bigger batch = faster Python, heavier RAM
    batches_per_checkpoint = 1            # record each batch; increase to reduce saved points
    stability_window_checkpoints = 6      # how many checkpoints must look steady
    maximum_allowed_change_between_checkpoints = 0.0005

    random_generator = np.random.default_rng(seed=12345)

    records: List[ConvergenceRecord] = []

    print("\nRoom size summary")
    print("RoomSize | TrialsUsed | EstimatedProbability | HalfWidth | TheoreticalProbability")
    print("-" * 86)

    for number_of_people in range(2, 51):
        record = run_until_converged_for_one_room_size(
            random_generator,
            number_of_people,
            confidence_level=confidence_level,
            absolute_tolerance=absolute_tolerance,
            minimum_trials=minimum_trials,
            maximum_trials=maximum_trials,
            rooms_per_batch=rooms_per_batch,
            batches_per_checkpoint=batches_per_checkpoint,
            stability_window_checkpoints=stability_window_checkpoints,
            maximum_allowed_change_between_checkpoints=maximum_allowed_change_between_checkpoints
        )
        records.append(record)

        theoretical = theoretical_probability_of_shared_birthday(number_of_people)
        print(
            f"{number_of_people:8d} | {record.stop_trial_count:9,d} | "
            f"{record.stop_estimated_probability:19.6f} | {record.stop_confidence_half_width:8.6f} | "
            f"{theoretical:21.6f}"
        )

        # Per-room variance plot (as requested)
        plot_variance_over_trials(record, output_folder)

    # After all rooms: the cool “meta” plots you requested
    plot_trials_needed_by_room_size(records, output_folder)
    plot_estimated_probability_vs_theory(records, output_folder)

    print(f"\nSaved plots in: {output_folder.resolve()}")
    print("\nExample stop explanation (last room size):")
    print(records[-1].stopped_because)


if __name__ == "__main__":
    run_experiment_for_room_sizes_two_through_fifty()
