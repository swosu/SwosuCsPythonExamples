"""
monty_hall/config.py

Holds the simulation configuration in a single, typed dataclass.
This keeps "knobs and dials" out of core logic so Game/Data stay clean.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Literal


Strategy = Literal["stay", "switch", "coinflip"]


@dataclass(frozen=True, slots=True)
class Config:
    # Core game setup
    doors: list[int]

    # Reproducibility / behavior
    seed: int
    strategy: Strategy

    # Stopping rule (confidence interval half-width)
    confidence_level: float
    epsilon: float
    min_trials: int
    max_trials: int

    # Output locations
    outdir: Path
    csv_path: Path
    json_path: Path

    # Presentation / extras
    make_plots: bool = True
    quiet: bool = False

    def __post_init__(self) -> None:
        # Basic sanity checks to fail fast with helpful error messages.
        if len(self.doors) < 3:
            raise ValueError("doors must contain at least 3 doors (e.g., [1,2,3]).")

        if not (0.0 < self.confidence_level < 1.0):
            raise ValueError("confidence_level must be between 0 and 1 (e.g., 0.95).")

        if self.epsilon <= 0:
            raise ValueError("epsilon must be > 0 (e.g., 0.01).")

        if self.min_trials < 1:
            raise ValueError("min_trials must be >= 1.")

        if self.max_trials < self.min_trials:
            raise ValueError("max_trials must be >= min_trials.")

        if self.csv_path.suffix.lower() != ".csv":
            raise ValueError("csv_path must end with .csv")

        if self.json_path.suffix.lower() != ".json":
            raise ValueError("json_path must end with .json")
