# Vegas Trip Planner Code Review Findings

Date: 2026-03-04  
Scope reviewed: root application modules and tests in `tests/`

## 1) Unhandled user input can crash the app
Severity: High

Evidence:
- `trip_inputs.py:6`, `trip_inputs.py:11`, `trip_inputs.py:16`, `trip_inputs.py:21`, `trip_inputs.py:26`
- `transportation_inputs.py:15`, `transportation_inputs.py:20`, `transportation_inputs.py:25`, `transportation_inputs.py:30`
- `budget_inputs.py:6`, `budget_inputs.py:11`, `budget_inputs.py:16`, `budget_inputs.py:21`, `budget_inputs.py:26`, `budget_inputs.py:31`, `budget_inputs.py:36`, `budget_inputs.py:41`

Concern:
- Inputs are cast directly with `int(...)`/`float(...)` without retry logic. Any non-numeric value raises `ValueError` and terminates the run.

Recommendation:
- Centralize numeric prompting in reusable validated input helpers that loop until valid input is entered.

## 2) Divide-by-zero failures are reachable
Severity: High

Evidence:
- `trip_calculations.py:6` (`distance / mpg`)
- `trip_calculations.py:80` (`total_cost / travelers`)
- Call path: `main.py:45` and `main.py:96`

Concern:
- `travelers=0` causes `ZeroDivisionError` in cost-per-person calculation.
- `mpg=0` causes `ZeroDivisionError` in gallons-needed calculation.
- No guard exists in input layer or calculation layer.

Recommendation:
- Enforce positive, non-zero values for `travelers` and `mpg` before calculation.
- Add explicit validation errors with clear messages.

## 3) Negative numbers are accepted for costs and counts
Severity: Medium

Evidence:
- Input functions across `trip_inputs.py`, `transportation_inputs.py`, and `budget_inputs.py` accept any numeric values.
- Totals are directly summed in `trip_calculations.py:64-75`.

Concern:
- Negative budgets or counts create nonsensical totals (for example, negative food/hotel/fuel costs).

Recommendation:
- Add minimum-value constraints by field type:
  - Counts: integer `>= 1`
  - Costs/budgets/distances: float `>= 0`

## 4) Currency math uses binary floating-point
Severity: Medium

Evidence:
- Monetary calculations in `trip_calculations.py:9-75` are all `float` operations.

Concern:
- `float` can introduce rounding artifacts for money, especially with many additions.

Recommendation:
- Use `Decimal` (or integer cents) for all money values end-to-end.
- Add tests that assert correct cent-level rounding behavior.

## 5) Repository has duplicate/stale implementations
Severity: Medium

Evidence:
- Working implementation in root modules (for example, `main.py`).
- Stubbed/empty parallel structure under `src/`:
  - `src/main.py:6` contains `pass`
  - several `src/*.py` files are docstring-only placeholders.

Concern:
- Ambiguous project structure can cause confusion about what is executable and testable.
- Future changes can accidentally target wrong files.

Recommendation:
- Pick one canonical layout:
  - either keep root modules and remove `src/` placeholders,
  - or move canonical code to `src/` and update imports/tests accordingly.

## 6) Test suite misses key behavior and failure paths
Severity: Medium

Evidence:
- Existing tests focus on pure calculation helpers:
  - `tests/test_calculations.py`
  - `tests/test_transportation.py`
  - `tests/test_miscellaneous.py`

Concern:
- No tests for input validation, retry behavior, or `plan_vegas_trip()` orchestration.
- No tests for divide-by-zero and invalid numeric boundaries.
- No tests for summary output correctness.

Recommendation:
- Add tests for:
  - validation/re-prompt behavior (mocking `input`)
  - edge cases (`travelers=0`, `mpg=0`, negatives)
  - orchestration happy path (`plan_vegas_trip`) with mocked I/O
  - printed summary formatting and category consistency

## 7) Summary output does not expose a full itemized breakdown
Severity: Low

Evidence:
- `print_trip_summary` only prints selected categories in `trip_summary.py:14-20`.

Concern:
- Users cannot easily reconcile printed line items with total cost because major categories like lodging, food, and transportation are omitted from the summary.

Recommendation:
- Print all major components used in total calculation for traceability.

