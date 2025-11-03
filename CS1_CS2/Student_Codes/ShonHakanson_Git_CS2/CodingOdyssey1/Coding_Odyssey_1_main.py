"""
main.py
CLI entry point and orchestration.

Design intent:
- Present a simple text menu (loop).
- Delegate actual work to ledger.py and file_io.py.
- Handle user input, basic validation, and display formatting here.
"""

from typing import List
from ledger import (
    Expense,
    add_expense,
    delete_expense,
    list_expenses,
    get_total_spend,
    get_totals_by_category,
)
from file_io import load_expenses, save_expenses


def print_menu() -> None:
    """
    Show available actions.

    Hints:
    - Keep the menu short (Add, List, Totals, Delete, Save, Quit).
    - Consider single-letter commands (A/L/T/D/S/Q) for speed.
    """
    # TODO: print menu options cleanly
    pass


def prompt_for_expense() -> Expense:
    """
    Ask the user for date, category, amount, (optional) note.

    Hints:
    - Gather raw strings here; let ledger functions validate/normalize.
    - Convert amount to float carefully (handle bad input).
    - Return a dict matching the Expense model keys.
    """
    # TODO: input() prompts; construct and return an Expense-like dict
    raise NotImplementedError


def run() -> None:
    """
    Main application loop.

    Hints:
    - Load expenses at startup.
    - Loop: show menu -> get choice -> call ledger/file_io as needed.
    - Keep printing/formatting here; ledger/file_io should stay logic/persistence only.
    - Save on explicit command and/or on exit (your choice).
    """
    # TODO: orchestrate the loop; call helper functions; handle bad choices
    raise NotImplementedError


if __name__ == "__main__":
    # Intentional: avoid auto-running the unfinished loop so you can implement step-by-step.
    # Uncomment when you're ready to wire up the menu.
    # run()
    print("Budget Buddy skeleton created. Implement functions step-by-step, then enable run().")
