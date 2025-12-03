# monty_hall_game.py
from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass(frozen=True)
class GameResult:
    """Outcome summary for a single Monty Hall round."""
    winning_door: int
    initial_pick: int
    revealed_losing_door: int
    final_pick: int
    switched: bool
    won: bool


class MontyHallGame:
    """
    Standalone Game class for the 3-door Monty Hall problem.

    Responsibilities (for now):
      - greet_user()
      - pick_winning_door()
      - reveal_losing_door()
      - determine win/lose (play_round)
    """

    def __init__(self, rng: Optional[random.Random] = None) -> None:
        self._rng = rng or random.Random()
        self._doors = (1, 2, 3)

    def greet_user(self) -> str:
        """Return a friendly intro message (UI can print this)."""
        return (
            "Welcome to Monty Hall!\n"
            "There are 3 doors: behind ONE is a prize, behind TWO are goats.\n"
            "You pick a door. I reveal a different door with a goat.\n"
            "Then you can stay or switch. Let's see what happens!"
        )

    def pick_winning_door(self) -> int:
        """Randomly choose which door has the prize."""
        return self._rng.choice(self._doors)

    def reveal_losing_door(self, winning_door: int, player_pick: int) -> int:
        """
        Host reveals a losing door:
          - cannot be the winning door
          - cannot be the player's pick
        """
        if player_pick not in self._doors:
            raise ValueError(f"player_pick must be 1, 2, or 3 (got {player_pick}).")
        if winning_door not in self._doors:
            raise ValueError(f"winning_door must be 1, 2, or 3 (got {winning_door}).")

        candidates = [d for d in self._doors if d != winning_door and d != player_pick]
        # In Monty Hall, there is always at least one valid losing door to reveal
        return self._rng.choice(candidates)

    def play_round(self, player_pick: int, switch: bool) -> GameResult:
        """
        Run one full round:
          1) pick winning door
          2) reveal a losing door
          3) optionally switch
          4) return win/lose

        Args:
            player_pick: contestant's initial choice (1..3)
            switch: True to switch, False to stay

        Returns:
            GameResult describing the round.
        """
        winning_door = self.pick_winning_door()
        revealed = self.reveal_losing_door(winning_door=winning_door, player_pick=player_pick)

        if switch:
            final_pick = self._switch_pick(player_pick=player_pick, revealed_door=revealed)
        else:
            final_pick = player_pick

        won = (final_pick == winning_door)
        return GameResult(
            winning_door=winning_door,
            initial_pick=player_pick,
            revealed_losing_door=revealed,
            final_pick=final_pick,
            switched=switch,
            won=won,
        )

    def _switch_pick(self, player_pick: int, revealed_door: int) -> int:
        """Return the only remaining door when the contestant switches."""
        remaining = [d for d in self._doors if d != player_pick and d != revealed_door]
        if len(remaining) != 1:
            raise RuntimeError(
                f"Switch logic error: expected 1 remaining door, got {remaining}."
            )
        return remaining[0]


if __name__ == "__main__":
    # Tiny demo (optional). This is NOT another class—just a quick test.
    game = MontyHallGame()
    print(game.greet_user())

    # Example: contestant picks door 1 and switches
    result = game.play_round(player_pick=1, switch=True)
    print("\n--- Round Result ---")
    print(f"Winning door:        {result.winning_door}")
    print(f"Initial pick:        {result.initial_pick}")
    print(f"Revealed losing door:{result.revealed_losing_door}")
    print(f"Final pick:          {result.final_pick} (switched={result.switched})")
    print("Outcome:             " + ("WIN 🎉" if result.won else "LOSE 🐐"))
