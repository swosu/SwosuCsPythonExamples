# Minimum Viable Product Plan
## Asymmetric Shortest-Path / Hamiltonian Path Explorer

This project is a small, classroom-friendly system for exploring how different algorithms search for a short route through a set of cities.

We will work with an **asymmetric distance table**, meaning that the distance from City `i` to City `j` may be different from the distance from City `j` to City `i`.

Example:
- `distance(2, 5) = 7`
- `distance(5, 2) = 14`

That means our table represents a **directed weighted graph**.

The goal of the MVP is to let us:
1. generate a random asymmetric table for any number of cities
2. run multiple algorithms on the same table
3. compare the route each algorithm finds
4. compare how long each algorithm takes
5. study how the algorithms behave as the number of cities increases

---

# 1. Big MVP Goal

Build a small system that can answer this question:

**For a given number of cities and a given asymmetric distance table, which algorithm finds the best Hamiltonian path, and how long does it take?**

We are not trying to build the final kingdom.
We are building the first sturdy wooden bridge over the lava creek.

---

# 2. Core Mathematical Object

## Problem Type
We will focus on finding a **Hamiltonian path**:
- visit each city exactly once
- do not revisit cities
- do not need to return to the starting city

Later, this could be extended into a **Hamiltonian circuit** or **traveling salesperson problem**.

## Input
- number of cities: `n`
- asymmetric distance table of size `n x n`

## Output
For each algorithm:
- best path found
- total distance of that path
- runtime
- optional metadata such as number of candidate paths examined

---

# 3. Why Asymmetric?

We want the MVP to use an **asymmetric table** because:
- it is more general
- it models directed travel costs
- it prevents students from assuming travel is always reversible
- it makes the problem feel a little more realistic and a little more spicy

In this world, going uphill and coming back downhill are not the same thing.
Also, apparently City 4 is charging emotional tolls.

---

# 4. Required Features of the MVP

## Feature 1: Variable Number of Cities
The user can choose the number of cities:
- `n = 4`
- `n = 5`
- `n = 6`
- `n = 7`
- `n = 8`
and so on

Practical note:
- brute force becomes expensive very quickly
- so larger values of `n` may be used only for the non-exhaustive algorithms

## Feature 2: Random Asymmetric Table Generation
The system can generate an `n x n` table such that:
- diagonal entries are `X` or ignored
- all off-diagonal entries are random positive distances
- the table is asymmetric in general

Optional classroom version:
- use values from `1` to `20`, as if rolling a d20 for each directed edge

## Feature 3: Shared Evaluation Function
All algorithms must use the same path scoring function:
- add distances in order along the path
- reject invalid paths with repeated cities
- return the total cost

## Feature 4: Runtime Measurement
Each algorithm should be timed using the same timing method so results are comparable.

## Feature 5: Result Comparison
The final output should show:
- algorithm name
- best path found
- path length
- elapsed time
- whether the solution is guaranteed optimal

---

# 5. Algorithms to Include

We want the MVP to compare four approaches.

---

# 5.1 Guess and Check

## Idea
Generate random Hamiltonian paths and keep the best one seen so far.

## Behavior
- simple
- easy to explain
- may stumble into a good answer
- not guaranteed to find the optimal solution unless it runs for a very long time

## Classroom Interpretation
This is the algorithmic version of:
> “What if we just keep trying stuff and writing down the least embarrassing answer?”

## Minimal Implementation Idea
- choose a random permutation of the cities
- compute its total distance
- repeat for a fixed number of trials
- keep the best result

## Inputs
- number of trials
- random seed optional

## Outputs
- best path found
- best distance found
- total runtime

---

# 5.2 Brute Force

## Idea
Generate **every possible Hamiltonian path** and choose the shortest one.

## Behavior
- guaranteed to find the optimal solution
- becomes very slow as `n` grows
- best for showing the explosion of combinatorics

## Classroom Interpretation
This is the goblin who opens every drawer in the house because “what if the keys are in there.”

## Minimal Implementation Idea
- generate all permutations of the city list
- compute the distance for each path
- keep the minimum

## Inputs
- city count `n`

## Outputs
- optimal path
- optimal distance
- total runtime
- number of paths checked

## Important Note
For Hamiltonian paths on `n` cities:
- number of candidate paths is `n!`

That grows very fast.

Example:
- `4! = 24`
- `5! = 120`
- `6! = 720`
- `7! = 5040`
- `8! = 40320`

This is where the computer starts sweating through its little silicon shirt.

---

# 5.3 Greedy

## Idea
Start at a city and repeatedly move to the nearest unvisited city.

## Behavior
- fast
- intuitive
- often decent
- not guaranteed to be optimal

## Classroom Interpretation
This is the algorithm that says:
> “I shall make the best local choice every time and hope the future sorts itself out.”

Sometimes that works.
Sometimes it drives directly into a swamp.

## Minimal Implementation Idea
For a chosen start city:
1. mark current city
2. among all unvisited cities, choose the one with smallest outgoing distance
3. move there
4. repeat until all cities are visited

We may run greedy:
- from one fixed start city
- or from every possible start city and keep the best greedy result

The second option is better for the MVP.

## Inputs
- start city or all possible starts

## Outputs
- greedy path found
- total distance
- runtime

---

# 5.4 Guess and Check with Annealing

## Idea
Start with a path, make small changes, and sometimes accept a worse path temporarily so the search can escape local traps.

This is a simplified **simulated annealing** approach.

## Behavior
- more sophisticated than random guess-and-check
- can improve over time
- not guaranteed optimal
- excellent for demonstrating modern heuristic thinking

## Classroom Interpretation
This algorithm occasionally says:
> “This new path is worse... but I have a feeling.”
And sometimes that weird little feeling saves the day.

## Minimal Implementation Idea
1. start with a random Hamiltonian path
2. measure its cost
3. create a neighboring path by swapping two cities
4. if the new path is better, accept it
5. if the new path is worse, maybe still accept it with a probability based on temperature
6. gradually lower the temperature
7. keep track of the best path ever seen

## Inputs
- initial temperature
- cooling rate
- number of iterations

## Outputs
- best path found
- best distance found
- runtime

---

# 6. MVP Scope Decisions

To keep the project minimal and teachable, the MVP should include:

## In Scope
- random asymmetric table generation
- variable city count
- all four algorithms
- timing
- comparison output
- one notebook or script to run experiments

## Out of Scope for MVP
- visualization on a map
- GUI
- file saving
- advanced graph libraries
- parallelization
- exact branch-and-bound methods
- genetic algorithms
- ant colony optimization
- heroic orchestral soundtrack

Those can come later when the beast has bones.

---

# 7. Data Model

## Cities
Represent cities as integers:
- `0, 1, 2, ..., n-1`
or
- `1, 2, 3, ..., n`

The MVP should pick one convention and stay faithful to it.

## Distance Table
Represent the asymmetric table as:
- a 2D list
- or a NumPy array

Requirements:
- `table[i][i]` should be ignored or marked as invalid
- `table[i][j]` is a positive integer if `i != j`

---

# 8. Shared Utility Functions

The MVP should be organized around a few shared building blocks.

## 8.1 Generate Asymmetric Table
Purpose:
- create a random valid distance table for `n` cities

Rules:
- diagonal is invalid
- off-diagonal values are random positive integers
- values need not be symmetric

## 8.2 Validate Path
Purpose:
- confirm a path visits every city exactly once

## 8.3 Score Path
Purpose:
- compute the total distance of a Hamiltonian path

## 8.4 Time Algorithm Run
Purpose:
- measure runtime for one algorithm call

## 8.5 Compare Results
Purpose:
- present all algorithm outputs in a clear summary table

---

# 9. Suggested Experiment Design

For a given `n`:

1. generate one asymmetric table
2. run all four algorithms on the same table
3. record:
   - best path
   - path cost
   - runtime
4. compare results

Then repeat for multiple values of `n`.

Suggested values:
- `n = 4`
- `n = 5`
- `n = 6`
- `n = 7`
- `n = 8`

Practical note:
- brute force may need to stop at `n = 8` or even earlier depending on the environment
- the other algorithms can continue further

---

# 10. Metrics to Report

For each algorithm, the MVP should report at least:

## Required Metrics
- algorithm name
- number of cities
- best path found
- total distance
- elapsed time in seconds
- optimality guarantee: yes or no

## Nice Extra Metrics
- number of candidate paths considered
- number of iterations
- start city used
- relative gap from brute force optimum when brute force is available

---

# 11. Recommended Comparison Table

For each experiment, display something like this:

| Algorithm | Cities | Best Path | Distance | Time (s) | Guaranteed Optimal? |
|----------|--------|-----------|----------|----------|---------------------|
| Guess and Check | 6 | 2 -> 5 -> 1 -> 4 -> 6 -> 3 | 41 | 0.012 | No |
| Brute Force | 6 | 1 -> 4 -> 2 -> 5 -> 6 -> 3 | 37 | 0.095 | Yes |
| Greedy | 6 | 3 -> 2 -> 5 -> 6 -> 1 -> 4 | 39 | 0.001 | No |
| Annealing | 6 | 2 -> 4 -> 1 -> 5 -> 6 -> 3 | 38 | 0.020 | No |

This makes the story visible:
- brute force is the truth oracle for small cases
- greedy is fast
- guess-and-check is simple
- annealing is a more clever explorer

---

# 12. Suggested Notebook Structure

The MVP should ultimately live in a Jupyter notebook with sections like these:

## Section 1: Objective
Explain the goal of comparing algorithms on asymmetric Hamiltonian path problems.

## Section 2: Key Vocabulary
Include:
- weighted graph
- directed graph
- asymmetric distance table
- Hamiltonian path
- brute force
- greedy
- heuristic
- annealing

## Section 3: Build a Random Distance Table
Generate and display one example table.

## Section 4: Shared Scoring Logic
Explain how a route is scored.

## Section 5: Algorithm 1, Guess and Check
Explain and test.

## Section 6: Algorithm 2, Brute Force
Explain and test.

## Section 7: Algorithm 3, Greedy
Explain and test.

## Section 8: Algorithm 4, Guess and Check with Annealing
Explain and test.

## Section 9: Comparison Table
Compare results for one value of `n`.

## Section 10: Scaling Experiments
Repeat for multiple values of `n` and discuss time growth.

---

# 13. Minimal Success Criteria

The MVP is successful if it can:

1. accept a city count `n`
2. generate one asymmetric distance table
3. run all four algorithms on that same table
4. compute the best route each algorithm finds
5. measure runtime for each algorithm
6. print a comparison table

That is enough to demonstrate the big idea without building a cathedral on day one.

---

# 14. Pedagogical Value

This MVP helps students see:

## Guess and Check
Random exploration can sometimes work, but it is unreliable.

## Brute Force
Trying everything guarantees the best answer, but becomes expensive quickly.

## Greedy
A fast local strategy can be attractive, but local choices do not always lead to global best solutions.

## Annealing
A heuristic can balance exploration and improvement, sometimes beating naive random search without checking everything.

This is a beautiful little four-act play:
- chaos
- certainty
- confidence
- cunning

---

# 15. Future Extensions After MVP

After the MVP works, we could add:

- return-to-start circuits
- side-by-side plots of runtime versus number of cities
- histograms of solution quality
- repeated trials over many random tables
- branch-and-bound
- Dijkstra for true shortest path between two cities
- classroom dice mode where distances are entered by hand
- notebook widgets for changing `n`

But first: tiny engine, clear output, honest comparison.

---

# 16. Final MVP Summary

We will build a small experimental system that:

- uses an **asymmetric distance table**
- allows the **number of cities to change**
- compares **guess and check**, **brute force**, **greedy**, and **guess and check with annealing**
- reports both:
  - the **shortest path found**
  - the **time taken**

This gives us a concrete way to show the tradeoff between:
- simplicity
- speed
- optimality
- cleverness

Or, put another way:

**One algorithm wanders.  
One checks everything.  
One grabs the nearest shiny object.  
One learns to wander with style.**