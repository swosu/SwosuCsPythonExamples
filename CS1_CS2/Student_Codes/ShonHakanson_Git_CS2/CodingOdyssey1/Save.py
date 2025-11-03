"""
file_io.py
Persistence layer (reading/writing expenses to disk).

Design intent:
- Keep ALL file operations here (JSON or CSV).
- Keep functions small; raise clean exceptions or return safe defaults.
- Let main.py decide when to save/load; ledger.py shouldn't touch disk.
"""

from typing import List, Dict
import json
import os

Expense = Dict[str, object]

# Default file path (you can change this; keep it in one place)
DATA_FILE = "expenses.json"


def load_expenses(filepath: str = DATA_FILE) -> List[Expense]:
    """
    Load expenses from disk. Return an empty list if file doesn't exist.

    Hints:
    - Use try/except around file reading.
    - If file is empty/corrupted, consider returning [] and let main.py warn the user.
    - Validate that each item looks like an Expense dict before returning.
    """
    # TODO: open file if exists, json.load, basic validation, return list
    raise NotImplementedError


def save_expenses(expenses: List[Expense], filepath: str = DATA_FILE) -> None:
    """
    Save expenses to disk atomically if possible.

    Hints:
    - Consider writing to a temp file and then replacing (reduces corruption risk).
    - Use indent=2 for readability.
    - Keep only serializable types (str, float, etc.).
    """
    # TODO: json.dump with safe write approach
    raise NotImplementedError
