from datetime import datetime
"""
ledger.py
Domain logic for managing expenses (in-memory).

Design intent:
- Keep ONLY expense manipulation here (add/delete/list/summarize).
- Do NOT do any file reading/writing here (that lives in file_io.py).
- Keep functions small and single-purpose so main.py can orchestrate.

Expense model (simple & flexible):
    {"date": "YYYY-MM-DD", "category": "Food", "amount": 12.50, "note": "optional"}
"""

from typing import List, Dict, Optional

Expense = Dict[str, object]  # keys: "date" (str), "category" (str), "amount" (float), "note" (str | optional)

# Optional: define a few standard categories to guide users (you can expand later)
DEFAULT_CATEGORIES = ["Food", "Transport", "Groceries", "Rent", "Utilities", "Fun", "Other"]


def add_expense(expenses: List[Expense], date: str, category: str, amount: float, note: Optional[str] = None) -> int:
    """
    Add a new expense to the in-memory list and return its index.

    Hints:
    - Validate the date format 'YYYY-MM-DD' before accepting (helper function below).
    - Guard against negative/zero amounts; consider rounding to 2 decimals.
    - Normalize category casing (e.g., title-case) for consistent grouping later.
    - Append a dict; keep the same keys for all entries.

    Returns:
        int: index of the inserted expense (useful for delete-by-index later).
    """
    # TODO: implement validation, normalization, append, return index
    raise NotImplementedError


def delete_expense(expenses: List[Expense], index: int) -> bool:
    """
    Delete an expense by its index. Return True if removed, False if index invalid.

    Hints:
    - Check bounds before popping.
    - Consider returning False rather than throwing to keep main.py simple.
    """
    # TODO: bounds check, pop, return status
    raise NotImplementedError


def list_expenses(expenses: List[Expense]) -> List[Expense]:
    """
    Return a shallow copy of all expenses for display.

    Hints:
    - Keep this pure (no printing here). main.py handles presentation.
    - Consider sorting by date later if you want nicer output.
    """
    # TODO: return a copy (e.g., expenses[:])
    raise NotImplementedError


def get_total_spend(expenses: List[Expense]) -> float:
    """
    Sum all 'amount' values and return the total.

    Hints:
    - Be careful with types; amounts should be numeric.
    - Consider rounding to 2 decimals at the end only.
    """
    # TODO: iterate/sum amounts; return a float
    raise NotImplementedError


def get_totals_by_category(expenses: List[Expense]) -> Dict[str, float]:
    """
    Return a dict mapping category -> total spend.

    Hints:
    - Initialize missing categories to 0.0 as you go.
    - Keep categories normalized (whatever you chose in add_expense()).
    """
    # TODO: accumulate per-category totals; return dict
    raise NotImplementedError


# ---- Helpers (keep small/pure; they make testing easy) ----

def is_valid_date(date_str: str) -> bool:
    """
    Quick date format check for 'YYYY-MM-DD'.

    Hints:
    - You can use datetime.strptime for a strict check later.
    - For now, a light-weight check (lengths and dashes) is OK for a first pass.
    """

    def is_valid_date(date_str: str) -> bool:
  
        try:
            datetime.strptime(date_str, "%m-%d-%Y")
            return True
        except ValueError:
            return False


def normalize_category(category: str) -> str:
    """
    Normalize category input for consistency.
    """
    return category.strip().title()
