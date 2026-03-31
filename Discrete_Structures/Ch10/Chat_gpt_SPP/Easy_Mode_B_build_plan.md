# Easy Mode B Plan
## Asymmetric Hamiltonian Path Explorer
### A Straightforward MVP Goal for Building First, Then Expanding

This document defines the **build target** for our first practical version of the project.

We want a version that is:
- simple enough to finish
- clean enough to teach with
- structured enough to expand later
- honest about what it does and does not try to do yet

This is not the final empire.
This is the first sturdy wagon that actually rolls.

---

# 1. Project Goal

We want to build a small system that can compare four algorithms for finding a **short Hamiltonian path** through an **asymmetric distance table**.

The system should:
1. accept a chosen number of cities
2. either load a saved distance table or generate a new one
3. use the **same fixed start city** for all algorithms
4. run four algorithms on the same table
5. report the best path each algorithm finds
6. report the path length each algorithm finds
7. be structured so it can later be called as a function with different city counts

This first version is focused on **correctness, clarity, and expandability**.

We are not building a crystal palace with laser peacocks.
We are building the part that works.

---

# 2. Core Problem

## Mathematical Object
We are solving a **Hamiltonian path** problem on a **directed weighted graph**.

That means:
- each city is visited exactly once
- the route does **not** have to return to the starting city
- distances are stored in an **asymmetric table**
- distance from City `i` to City `j` may be different from distance from City `j` to City `i`

## Example
- `distance(2, 5) = 7`
- `distance(5, 2) = 14`

So the road system is directional.
The map has opinions.

---

# 3. Build Target

The MVP should support:

- **variable city count**
- **all four algorithms**
- **fixed start city**
- **saved table or generated table**
- **one experiment per city count**
- **easy expansion later into repeated trials and timing**

This version will prioritize:
- best path found
- total path cost

This version will **not yet prioritize**:
- repeated random trials
- large-scale benchmarking
- fancy visualizations
- deep parameter tuning
- performance plots

---

# 4. The Four Algorithms We Will Include

## 4.1 Guess and Check
Generate random valid Hamiltonian paths that begin at the fixed start city.
Keep the best one found.

## 4.2 Brute Force
Generate all valid Hamiltonian paths that begin at the fixed start city.
Choose the shortest one.

Important restriction:
- brute force should only run for small `n`
- recommended cap: `n <= 8`

## 4.3 Greedy
Start at the fixed start city.
At each step, move to the nearest unvisited city.

## 4.4 Guess and Check with Annealing
Start with one valid path from the fixed start city.
Make small changes to the path and sometimes accept worse ones temporarily so the search can escape local traps.

All four algorithms must use:
- the same distance table
- the same fixed starting city
- the same path scoring function

That keeps the comparison fair.

---

# 5. Simplifying Decisions We Are Intentionally Making

These decisions are not accidents.
They are deliberate simplifications to make the project easier to build.

## Decision A: Fixed Start City
Every algorithm starts from the same city.

Recommended default:
- start at City `1` if using one-based indexing
- or City `0` if using zero-based indexing

### Why this helps
- easier comparisons
- less code complexity
- easier debugging
- easier explanations for students

### What we give up
- some algorithms might do better from another starting city
- we are not searching all possible starts yet

That is okay for the MVP.

---

## Decision B: One Table Per Experiment
For a given city count `n`, we use one table for the experiment.

### Why this helps
- reproducible results
- easier comparison
- easier debugging
- easier notebook storytelling

### What we give up
- less statistical depth
- less evidence across many random cases

Again: acceptable for version 1.

---

## Decision C: Use a Flag for Table Source
The system should let us choose whether to:
- generate a new asymmetric distance table
- or use a saved distance table

### Why this helps
- we can debug on stable input
- we can later regenerate fresh examples when we want
- we can use classroom-created tables
- we can keep experiments reproducible

This flag is one of the most useful design decisions in the whole build.

---

## Decision D: Brute Force Has a Safety Cap
Brute force should only run when the city count is small.

Recommended rule:
- if `n <= 8`, allow brute force
- if `n > 8`, skip brute force and say so clearly

### Why this helps
- protects the notebook from combinatorial doom
- keeps the project responsive
- makes the growth of brute force easier to explain

The factorial monster is real.
We do not negotiate with it.
We put a fence around it.

---

## Decision E: Path Quality First, Timing Later
The first version should focus on:
- valid path generation
- correct path scoring
- comparison of path quality

Timing can be added after correctness is working.

### Why this helps
- reduces moving parts
- makes debugging easier
- helps us finish a working notebook sooner

### What we give up
- we will not initially compare speed
- one important CS dimension comes later

This is a good trade if it gets the engine built.

---

# 6. Functional Goal

We want the core system to be callable later as a function.

That means the design should revolve around a function like this in spirit:

- input:
  - city count
  - start city
  - whether to generate a new table or load a saved one
  - optional saved table path or object
  - algorithm settings

- output:
  - distance table used
  - best result from each algorithm
  - any skipped algorithms
  - comparison-ready summary

We do not need to finalize the exact function signature in this markdown file, but the implementation should clearly aim toward a reusable function-based design.

That is important.

We are not building a notebook-shaped pile of spaghetti.
We are building a notebook that can later grow a clean engine underneath it.

---

# 7. MVP Input Requirements

The system should accept these basic inputs:

## Required Inputs
- number of cities `n`
- fixed start city
- flag to determine table source

## Table Source Flag
Example concept:
- `generate_new_table = True` means create a new asymmetric table
- `generate_new_table = False` means use a saved table

## Optional Inputs
- saved table location
- random seed
- number of guess-and-check trials
- annealing settings
- brute force cap

The first version should use sensible defaults whenever possible.

---

# 8. MVP Output Requirements

For each algorithm, the MVP should report:

- algorithm name
- whether it ran or was skipped
- best path found
- total path cost
- note about whether the result is guaranteed optimal

Because timing is deferred for now, this first summary does **not** need runtime yet.

## Example Output Shape

| Algorithm | Ran? | Best Path | Path Cost | Guaranteed Optimal? | Notes |
|----------|------|-----------|-----------|----------------------|-------|
| Guess and Check | Yes | 1 -> 4 -> 2 -> 5 -> 3 -> 6 | 31 | No | Random search |
| Brute Force | Yes | 1 -> 3 -> 5 -> 2 -> 6 -> 4 | 28 | Yes | Exhaustive |
| Greedy | Yes | 1 -> 4 -> 5 -> 3 -> 2 -> 6 | 35 | No | Local-choice heuristic |
| Annealing | Yes | 1 -> 3 -> 2 -> 5 -> 6 -> 4 | 29 | No | Heuristic improvement |

If brute force is skipped:

| Algorithm | Ran? | Best Path | Path Cost | Guaranteed Optimal? | Notes |
|----------|------|-----------|-----------|----------------------|-------|
| Brute Force | No | N/A | N/A | Yes, if run | Skipped because `n > 8` |

---

# 9. Data Model

## Cities
Use a consistent city labeling system.

Recommended classroom-friendly choice:
- `1, 2, 3, ..., n`

## Distance Table
Use an `n x n` structure where:
- the diagonal is invalid or ignored
- all off-diagonal entries are positive integers
- the table is asymmetric in general

Example:

| From \\ To | 1 | 2 | 3 | 4 |
|-----------|---|---|---|---|
| **1** | X | 8 | 13 | 4 |
| **2** | 6 | X | 10 | 7 |
| **3** | 2 | 14 | X | 9 |
| **4** | 11 | 5 | 3 | X |

This table represents a directed weighted graph.

---

# 10. Shared Core Functions the Build Should Aim For

The implementation should be organized around a few shared pieces.

## 10.1 Table Builder or Loader
Purpose:
- either generate a new asymmetric table
- or load a saved one

## 10.2 Path Validator
Purpose:
- confirm a path starts at the fixed start city
- confirm it visits every city exactly once

## 10.3 Path Scorer
Purpose:
- compute the total cost of a valid Hamiltonian path

## 10.4 Algorithm Runner
Purpose:
- run one algorithm on the table using shared rules

## 10.5 Comparison Builder
Purpose:
- collect results from all algorithms into one summary object or table

## 10.6 Main Experiment Function
Purpose:
- accept city count and settings
- prepare the distance table
- run the algorithms
- return the results in one clean structure

This is the heart of the architecture.

---

# 11. Suggested Build Order

To make the implementation straightforward, we should build in this order.

## Step 1: Build the distance table system
- support asymmetric table creation
- support saved-table usage
- confirm the table shape is correct

## Step 2: Build path scoring
- validate paths
- compute path cost correctly

## Step 3: Build guess and check
- simplest algorithm to get working quickly

## Step 4: Build greedy
- easy to compare against random search

## Step 5: Build brute force
- add exhaustive truth for small `n`

## Step 6: Build annealing
- add the more advanced heuristic last

## Step 7: Build unified comparison output
- gather all results in one place

## Step 8: Wrap the whole experiment in one reusable function
- make later notebook usage easy
- make future experiments easier

This order keeps the danger low and the momentum high.

---

# 12. Notebook Goal

The first notebook built from this plan should aim to do exactly one clean demonstration:

## Demonstration Goal
For a chosen city count:
1. get an asymmetric table
2. run all four algorithms from the same fixed start city
3. compare the best path and path cost for each

That is enough for the first working notebook.

A second notebook or later revision can add:
- runtime measurement
- repeated trials
- scaling studies
- charts

---

# 13. Success Criteria

The MVP is successful if it can do all of the following:

1. accept a city count
2. accept a fixed start city
3. accept a flag for table generation versus saved table
4. produce or load one asymmetric distance table
5. run guess and check
6. run greedy
7. run brute force when allowed
8. run annealing
9. score each result correctly
10. report a clean comparison table

If those ten things work, the MVP is a success.

Not fancy-success.
Not conference-poster-success.
Not angel-choir-success.

Real success:
**it works, it teaches, and it gives us a base to grow from.**

---

# 14. What We Are Giving Up to Keep This Easy

To make the project easier to build, we are deliberately giving up:

- repeated random trials for each city count
- immediate runtime benchmarking
- all-start-city comparisons
- advanced statistical analysis
- plots and dashboards
- large-`n` brute force experiments
- extra algorithm variations

These are not failures.
These are deferred luxuries.

---

# 15. What This Build Makes Easier Later

By choosing this simpler structure now, we make it easier later to add:

- runtime measurement
- repeated runs per `n`
- plots of path quality
- plots of runtime
- comparison against optimality gap
- alternate start city policies
- classroom dice-generated tables
- notebook widgets
- saved experiment files

Good architecture is a gift to Future Us.
Future Us deserves snacks and less regret.

---

# 16. Final Build Statement

We are building a reusable, notebook-friendly system that compares four algorithms for Hamiltonian paths on an asymmetric distance table.

The system will:
- support different city counts
- use a fixed start city
- allow either generated or saved tables
- include guess and check, brute force, greedy, and annealing
- compare path quality first
- postpone timing until after correctness is working

This is our Easy Mode B target.

It is ambitious enough to be interesting.
It is small enough to actually finish.
It is structured enough to become something larger later.

**Build the cart.  
Roll the cart.  
Then add the gold trim.**