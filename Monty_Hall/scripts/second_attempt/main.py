"""
monty_hall/main.py

CLI entry point for the Monty Hall simulation.
- Parses command-line arguments
- Builds a Config
- Constructs the Game
- Runs the simulation

Run examples:
  python -m monty_hall.main
  python -m monty_hall.main --strategy switch --epsilon 0.01 --confidence 0.95 --seed 123
  python -m monty_hall.main --strategy coinflip --max-trials 50000 --outdir output
"""

from __future__ import annotations

import argparse
#from dataclasses import replace
from pathlib import Path
from typing import Optional


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="monty_hall",
        description="Monty Hall simulation with optional confidence-interval stopping rule.",
    )

    p.add_argument(
        "--strategy",
        choices=("stay", "switch", "coinflip"),
        default="switch",
        help="Contestant strategy: stay, switch, or coinflip (random each trial).",
    )
    p.add_argument(
        "--seed",
        type=int,
        default=123,
        help="RNG seed for reproducibility.",
    )
    p.add_argument(
        "--confidence",
        type=float,
        default=0.95,
        help="Confidence level for CI stopping rule (e.g., 0.95).",
    )
    p.add_argument(
        "--epsilon",
        type=float,
        default=0.01,
        help="Stop when CI half-width is below epsilon (smaller = more trials).",
    )
    p.add_argument(
        "--min-trials",
        type=int,
        default=2000,
        help="Minimum trials before allowing the CI stopping rule to stop.",
    )
    p.add_argument(
        "--max-trials",
        type=int,
        default=200_000,
        help="Hard cap on trials (safety valve).",
    )
    p.add_argument(
        "--outdir",
        type=Path,
        default=Path("output"),
        help="Directory for CSV/JSON/plots.",
    )
    p.add_argument(
        "--csv-name",
        type=str,
        default="trials.csv",
        help="CSV output filename (inside outdir).",
    )
    p.add_argument(
        "--json-name",
        type=str,
        default="summary.json",
        help="JSON output filename (inside outdir).",
    )
    p.add_argument(
        "--no-plots",
        action="store_true",
        help="Disable plot generation.",
    )
    p.add_argument(
        "--quiet",
        action="store_true",
        help="Reduce console output.",
    )

    return p


def main(argv: Optional[list[str]] = None) -> int:
    args = build_parser().parse_args(argv)

    # Lazily import project modules so argparse help works even if dependencies are missing.
    from monty_hall.config import Config
    from monty_hall.game import Game
    from monty_hall.contestant import Contestant
    from monty_hall.data import Data
    from monty_hall.results import Results
    from monty_hall.rng import RNG

    outdir: Path = args.outdir
    outdir.mkdir(parents=True, exist_ok=True)

    cfg = Config(
        doors=[1, 2, 3],
        seed=args.seed,
        strategy=args.strategy,
        confidence_level=args.confidence,
        epsilon=args.epsilon,
        min_trials=args.min_trials,
        max_trials=args.max_trials,
        outdir=outdir,
        csv_path=outdir / args.csv_name,
        json_path=outdir / args.json_name,
        make_plots=not args.no_plots,
        quiet=args.quiet,
    )

    rng = RNG(cfg.seed)
    contestant = Contestant(strategy=cfg.strategy)
    data = Data(
        confidence_level=cfg.confidence_level,
        epsilon=cfg.epsilon,
        min_trials=cfg.min_trials,
    )
    results = Results(
        csv_path=cfg.csv_path,
        json_path=cfg.json_path,
        outdir=cfg.outdir,
        make_plots=cfg.make_plots,
        quiet=cfg.quiet,
    )

    game = Game(
        doors=cfg.doors,
        rng=rng,
        contestant=contestant,
        data=data,
        results=results,
        max_trials=cfg.max_trials,
        quiet=cfg.quiet,
    )

    game.greet_user()
    game.run()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
