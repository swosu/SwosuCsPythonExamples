"""
build_notebook.py
Generates recursion_reverse_string.ipynb using nbformat 4.4.
Run with: python build_notebook.py
"""

import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell

# ---------------------------------------------------------------------------
# Cell helpers
# ---------------------------------------------------------------------------

def md(source):
    return new_markdown_cell(source)

def code(source):
    return new_code_cell(source)

# ---------------------------------------------------------------------------
# Build cells
# ---------------------------------------------------------------------------

cells = []

# ============================================================
# OPENING MARKDOWN
# ============================================================
cells.append(md("""\
# Recursion Deep Dive: Reversing a String

## What is recursion?

**Recursion** is when a function solves a problem by calling *itself* on a
smaller version of the same problem.  Every recursive function has two parts:

| Part | What it does |
|---|---|
| **Base case** | The simplest version of the problem — answered directly, no self-call |
| **Recursive case** | Break the problem into one step + a smaller version, then call yourself |

If there is no base case, the function calls itself forever and Python raises a
`RecursionError`.

---

## Why is reversing a string a great first recursion problem?

- The input shrinks naturally: take one character off the front, the rest is
  a shorter string.
- The answer is easy to verify visually.
- It has a clean base case (`""` or `"a"`).
- The *order* in which characters are assembled teaches you the crucial idea of
  **building the answer on the way back out** of the call stack.

---

## ASCII call-stack diagram for `reverse_string("Hello")`

Read the arrows: `→` means *opening a frame*, `←` means *returning a value*.

```
→ reverse_string("Hello")
  → reverse_string("ello")
    → reverse_string("llo")
      → reverse_string("lo")
        → reverse_string("o")
          → reverse_string("")        ← base case, returns ""
          ← returns "" + "o"  = "o"
        ← returns "o"  + "l"  = "ol"
      ← returns "ol" + "l"  = "oll"
    ← returns "oll" + "e"  = "olle"
  ← returns "olle" + "H"  = "olleH"
```

Notice: `"H"` was *first* in the original string but gets appended *last*.
That is exactly what reversal means, and recursion achieves it automatically
by delaying the append until each frame **returns**.

---

## Reading guide

As you work through this notebook, watch for:

1. How the string shrinks one character at a time toward the base case.
2. How `s[0]` (first character) and `s[1:]` (the rest) split the work.
3. The difference between *going into* the stack and *coming back out*.
4. Why the `+ s[0]` at the **end** of the return statement is what reverses order.
"""))

# ============================================================
# STEP 1
# ============================================================
cells.append(md("""\
---
## Step 1 — The Problem Statement

### Goal of this step

Understand exactly what we want to produce before writing any function.
See concrete input/output pairs, and discover the key structural insight
that makes recursion natural for this problem.
"""))

cells.append(code("""\
# No function yet — just exploring the string structure we will recurse over.

s = "Hello"

# The final goal: reverse a string
print("Reversed with slicing:", s[::-1])
print()

# The key structural insight:
print(f"s[0]  = '{s[0]}'   ← first character")
print(f"s[1:] = '{s[1:]}' ← everything else")
print()

# More input/output pairs we will need to handle:
examples = [
    ("Hello",         "olleH"),
    ("Hello, world!", "!dlrow ,olleH"),
    ("",              ""),
    ("a",             "a"),
    ("racecar",       "racecar"),
]

print("Expected behaviour:")
for inp, out in examples:
    print(f"  reverse_string({inp!r:15s}) → {out!r}")
"""))

cells.append(md("""\
### What just happened?

`s[0]` is Python's way of grabbing the **first character** of a string.
`s[1:]` is a *slice* that gives you **every character after the first**.

```
s     = "Hello"
s[0]  = "H"
s[1:] = "ello"
```

This split is the natural setup for recursion:

> *To reverse `"Hello"`, reverse `"ello"` first, then append `"H"` at the end.*

The string passed to the recursive call (`s[1:]`) is always **one character
shorter** — that is what guarantees we eventually reach the base case.
"""))

# ============================================================
# STEP 2
# ============================================================
cells.append(md("""\
---
## Step 2 — Identifying the Base Case

### Goal of this step

Write *only* the stopping condition before touching the recursive logic.
Getting the base case right first is the safest way to build a recursive function.
"""))

cells.append(code("""\
def reverse_string(s):
    # Base case 1: empty string reverses to itself
    if len(s) == 0:
        return ""
    # Base case 2: single character reverses to itself
    if len(s) == 1:
        return s
    # Recursive case not implemented yet
    raise NotImplementedError("recursive case not yet implemented")


# These should both work fine:
print(repr(reverse_string("")))   # ""
print(repr(reverse_string("a")))  # "a"

# This line is left commented out — it would raise NotImplementedError:
# print(reverse_string("Hello"))
"""))

cells.append(md("""\
### What just happened?

We handle two base cases:

| Condition | Why it is a base case |
|---|---|
| `len(s) == 0` | The empty string is already reversed — return `""` immediately |
| `len(s) == 1` | A single character is already reversed — return it as-is |

**Why do we need two?**  Because we reduce `n` by 1 each call (`s[1:]` removes
one character), so we will hit `len(s) == 1` on odd-length strings and
`len(s) == 0` on even-length strings.  Handling both is safer than relying on
just one.

**What happens without a base case?**  Python limits the call stack to roughly
**1 000 frames** by default.  Without a stopping condition the function recurses
until it hits that limit and raises:

```
RecursionError: maximum recursion depth exceeded
```

Always write the base case first.
"""))

# ============================================================
# STEP 3
# ============================================================
cells.append(md("""\
---
## Step 3 — Visualising the Recursive Idea Before Coding It

### Goal of this step

Simulate what the call stack *will* do using a plain `while` loop — no actual
recursion yet.  Seeing the pattern manually makes it much easier to trust the
real recursive code when we write it in Step 4.
"""))

cells.append(code("""\
def simulate_reverse_stack(s):
    \"\"\"
    Simulates the recursive call stack using a list as a manual stack.
    No real recursion — just the same logic spelled out step by step.
    \"\"\"
    print(f"Imagining a call to reverse_string('{s}')")
    frames = []

    # Going INTO the recursion: peel characters off the front
    while len(s) > 1:
        print(f"  Peel off '{s[0]}', recurse on '{s[1:]}'")
        frames.append(s[0])
        s = s[1:]

    # Base case reached
    print(f"  Base case reached: '{s}'")
    result = s

    # Coming BACK OUT: append characters in reverse order
    while frames:
        char = frames.pop()
        result = result + char
        print(f"  Returning from frame: result so far = '{result}'")

    print(f"Final result: '{result}'")
    return result


simulate_reverse_stack("Hello")
"""))

cells.append(md("""\
### What just happened?

The `while` loop going *in* mimics the recursive calls opening one by one.
Each iteration peels `s[0]` off and saves it — just like each real recursive
call will remember its own `s[0]` in its local frame.

The `while frames: ... pop()` loop mimics the frames *closing* in reverse
order.  Because we used `pop()` (last-in, first-out), the character that was
*first* in the original string gets appended *last* to the result — which is
exactly what reversal requires.

```
Opening frames  (going in):  H  e  l  l  | o  ← base
Closing frames  (coming out):            o → ol → oll → olle → olleH
```

When you run the real recursive function in Step 4, the Python call stack does
exactly this — the `frames` list just becomes implicit, managed by Python
rather than by our code.
"""))

# ============================================================
# STEP 4
# ============================================================
cells.append(md("""\
---
## Step 4 — The Full Recursive Function

### Goal of this step

Write the real recursive implementation and verify it against a complete set of
test cases.
"""))

cells.append(code("""\
def reverse_string(s):
    # Base cases
    if len(s) == 0:
        return ""
    if len(s) == 1:
        return s
    # Recursive case: reverse the tail, then append the head at the end
    return reverse_string(s[1:]) + s[0]


# --- Test suite ---
test_cases = [
    ("Hello",         "olleH"),
    ("Hello, world!", "!dlrow ,olleH"),
    ("",              ""),
    ("a",             "a"),
    ("racecar",       "racecar"),
]

all_passed = True
for input_str, expected in test_cases:
    result = reverse_string(input_str)
    status = "PASS" if result == expected else "FAIL"
    if status == "FAIL":
        all_passed = False
    print(f"[{status}] reverse_string({input_str!r:15s}) = {result!r}  (expected: {expected!r})")

print()
print("All tests passed!" if all_passed else "Some tests FAILED — check above.")
"""))

cells.append(md("""\
### What just happened?

The entire function is two lines of logic:

```python
return reverse_string(s[1:]) + s[0]
```

Break that down:

| Part | Meaning |
|---|---|
| `s[1:]` | The string with the first character removed — a **smaller** input |
| `reverse_string(s[1:])` | Trust the recursion: this returns the reversed tail |
| `+ s[0]` | Append the **first** character of the original string at the **end** |

Why does `+ s[0]` at the *end* reverse the string?

- The outermost call has `s[0] = "H"`.
- Before `"H"` is appended, *all* inner calls must return first.
- By the time control returns to the outermost frame, the tail `"ello"` has
  already been reversed to `"olle"`.
- Appending `"H"` gives `"olleH"`.

**Key insight:** characters are appended *on the way back out* of the call
stack, not on the way in.  That reversal of order is what recursion gives us
for free.
"""))

# ============================================================
# STEP 5
# ============================================================
cells.append(md("""\
---
## Step 5 — Watching the Real Call Stack

### Goal of this step

Instrument the actual recursive function with print statements so you can
watch each frame open and close in real time.  This makes the call stack
visible instead of invisible.
"""))

cells.append(code("""\
depth = 0   # global counter so we can indent output by recursion depth

def reverse_string_verbose(s):
    global depth
    indent = "  " * depth

    print(f"{indent}→ reverse_string_verbose({s!r})")

    if len(s) == 0:
        print(f"{indent}  base case: returning ''")
        return ""
    if len(s) == 1:
        print(f"{indent}  base case: returning {s!r}")
        return s

    depth += 1
    partial = reverse_string_verbose(s[1:])   # recursive call
    depth -= 1

    result = partial + s[0]
    print(f"{indent}← returning {result!r}  "
          f"(partial={partial!r} + first_char={s[0]!r})")
    return result


print("=== Tracing reverse_string_verbose('Hello') ===\\n")
depth = 0   # reset before tracing
final = reverse_string_verbose("Hello")
print(f"\\nFinal answer: {final!r}")
"""))

cells.append(md("""\
### What just happened?

Read the trace from top to bottom:

- Every `→` line is a **new frame opening** — the function was called with a
  shorter string.
- The deepest `→` line is the **base case**: it returns immediately without
  opening another frame.
- Every `←` line is a **frame closing** — the function is returning a value
  back to its caller.

The indentation tells you how deep in the stack you are at each moment.

```
→ (depth 0)  called with "Hello"
  → (depth 1)  called with "ello"
    → (depth 2)  called with "llo"
      ...
          → (depth 4)  called with ""  ← base case
          ← returning ""
        ← returning "o"   (depth 3 returns)
      ← returning "ol"    (depth 2 returns)
    ← returning "oll"     (depth 1 returns)
  ← returning "olle"      (depth 0 intermediate)
← returning "olleH"       (depth 0 final)
```

Notice that each `←` line shows exactly how the result is *assembled*:
`partial + s[0]`.  The last character appended (`"H"`) was the *first*
character of the original input.
"""))

# ============================================================
# STEP 6
# ============================================================
cells.append(md("""\
---
## Step 6 — Comparing to the Iterative Version

### Goal of this step

See how a `for` loop solves the same problem, then compare the two approaches
honestly.  Neither is wrong — they reflect different ways of thinking.
"""))

cells.append(code("""\
def reverse_string_iterative(s):
    result = ""
    for char in s:
        result = char + result   # prepend each character
    return result


def reverse_string_recursive(s):
    if len(s) == 0:
        return ""
    if len(s) == 1:
        return s
    return reverse_string_recursive(s[1:]) + s[0]


# Verify both produce the same results
test_inputs = ["Hello", "Hello, world!", "", "a", "racecar", "Python"]

print(f"{'Input':<18} {'Iterative':<18} {'Recursive':<18} Match")
print("-" * 65)
for s in test_inputs:
    it  = reverse_string_iterative(s)
    rec = reverse_string_recursive(s)
    print(f"{s!r:<18} {it!r:<18} {rec!r:<18} {it == rec}")
"""))

cells.append(md("""\
### What just happened?

Both functions produce identical output.  The difference is how they think:

| | Iterative | Recursive |
|---|---|---|
| **Control flow** | `for` loop, explicit counter | function calls itself |
| **State** | `result` variable mutated in place | result assembled on the way back out |
| **Readability** | Familiar to most beginners | Matches the mathematical definition |
| **Stack usage** | O(1) — no extra call frames | O(n) — one frame per character |
| **Risk** | None for any string length | `RecursionError` for strings > ~1 000 chars |

**When to prefer recursive:**
- When the problem is defined recursively (trees, file systems, expression parsers)
- When the recursive solution is substantially clearer than a loop
- In academic/competitive settings where elegance matters

**When to prefer iterative:**
- When performance or stack depth is a concern
- When the problem maps naturally to a `for`/`while` loop
- In production code where a `RecursionError` would be a bug

For *reversing a string* in real Python code you would just write `s[::-1]`.
The point of this notebook was never the destination — it was learning to
think recursively along the way.
"""))

# ============================================================
# CLOSING MARKDOWN
# ============================================================
cells.append(md("""\
---
## Summary and Next Steps

### Three things every recursive function needs

1. **A base case** — the smallest input answered directly, with no self-call.
2. **Shrinking input** — every recursive call must move *closer* to the base
   case (here: `s[1:]` is always shorter than `s`).
3. **Trust the recursion** — assume the recursive call returns the correct
   answer for the smaller input, then use it to build the answer for the
   current input.

### Try it yourself

Write recursive functions for each of these.  Use the same pattern:
*base case → shrink → trust the recursion → combine*.

| Challenge | Hint |
|---|---|
| Count the characters in a string | `count("Hello") = 1 + count("ello")` |
| Check if a string is a palindrome | Compare first and last, recurse on the middle |
| Compute the sum of a list | `sum([1,2,3]) = 1 + sum([2,3])` |
| Flatten a nested list | Check if the first element is itself a list |

---

### Python's recursion limit

Python limits call-stack depth to **1 000 frames** by default.  You can read
or change it:

```python
import sys

print(sys.getrecursionlimit())   # default: 1000

sys.setrecursionlimit(5000)      # increase if needed (use with care)
```

For most real-world recursive algorithms the default is plenty.  If you find
yourself needing to raise it significantly, consider whether an iterative
approach or an explicit stack would be cleaner.

---

*Well done for working through this notebook.  Recursion feels strange at
first because it asks you to trust a call that hasn't returned yet.  Once
that trust becomes natural, a whole class of elegant solutions opens up.*
"""))

# ---------------------------------------------------------------------------
# Assemble and write the notebook
# ---------------------------------------------------------------------------

nb = new_notebook()
nb["cells"] = cells
nb["metadata"] = {
    "kernelspec": {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3",
    },
    "language_info": {
        "name": "python",
        "version": "3.11.0",
    },
}

output_path = "recursion_reverse_string.ipynb"
with open(output_path, "w", encoding="utf-8") as f:
    nbformat.write(nb, f, version=4)

print(f"Notebook written to {output_path} — open it in VS Code and run all cells.")
