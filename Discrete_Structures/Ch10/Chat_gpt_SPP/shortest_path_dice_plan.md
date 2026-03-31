    # Shortest Path Problem with Dice: A Classroom Adventure
## Plan for a Hands-On Exploration of Section 10.6

Welcome, brave traveler. Today we ride into the land of **cities, dice, and suspiciously dramatic road trips**. 🗺️🎲

This lesson is inspired by **Section 10.6: Shortest-Path Problems**, where we study how to represent travel between places using **weighted graphs** and how to find efficient routes. Later in the section, the book also discusses the **traveling salesperson problem**, which asks for a route that visits every city exactly once and has the smallest possible total distance. :contentReference[oaicite:1]{index=1}

Our version will use:
- **6 cities** labeled `1, 2, 3, 4, 5, 6`
- A **6-sided die** to help choose cities
- A **20-sided die** to create road distances
- A **distance table** to record travel costs
- A **guess-and-check method** to build and compare Hamiltonian paths

---

# 1. Big Goal

We want students to:
1. Understand what a **shortest path problem** is.
2. Build a **distance table** for a set of cities.
3. Interpret the table as a **weighted graph**.
4. Generate a **Hamiltonian path**, meaning a path that visits each city exactly once.
5. Use **guess and check** to compare several possible routes and look for the smallest total distance.

This is like sending a tiny road-tripping goblin to six cities and asking it to waste as little gas money as possible. 🚗💨

---

# 2. Key Terms and Phrases

## Graph
A **graph** is a mathematical structure made of:
- **vertices** or **nodes**: the cities
- **edges**: the roads connecting the cities

## Weighted Graph
A **weighted graph** is a graph where each edge has a number attached to it.
That number is called a **weight**.

In our lesson:
- the **cities** are the vertices
- the **roads** are the edges
- the **distances** are the weights

## Distance Table
A **distance table** is a chart showing the distance from each city to every other city.

## Path
A **path** is a sequence of cities connected by roads.

Example:
`1 -> 4 -> 2 -> 6`

## Length of a Path
The **length** of a path is the sum of all the edge weights used in that path.

If:
- `1 -> 4 = 7`
- `4 -> 2 = 11`
- `2 -> 6 = 5`

then the total length is:

`7 + 11 + 5 = 23`

## Shortest Path
A **shortest path** is the path with the smallest total distance between two cities.

## Hamiltonian Path
A **Hamiltonian path** is a path that visits every vertex exactly once.

For our six-city activity, a Hamiltonian path might look like:

`3 -> 1 -> 5 -> 2 -> 6 -> 4`

Each city appears once. No repeats. No teleportation. No funny business.

## Circuit
A **circuit** starts and ends at the same city.

## Hamiltonian Circuit
A **Hamiltonian circuit** visits every city exactly once and returns to the starting city.

That idea connects closely to the **traveling salesperson problem** discussed in Section 10.6. :contentReference[oaicite:2]{index=2}

## Guess and Check
A **guess-and-check method** means:
1. generate a possible valid route
2. find its total distance
3. compare it to other routes
4. keep track of the smallest one found so far

This method is not the fastest possible algorithm, but it is great for helping students understand what the problem is actually asking.

---

# 3. Classroom Setup

We will use six cities:
- City 1
- City 2
- City 3
- City 4
- City 5
- City 6

We will create a distance table where:
- traveling from a city to itself is marked with an `X`
- traveling from one city to another has a positive distance determined by a die roll

Because the distances represent roads between cities, the table should be **asymmetric**:
- distance from City 1 to City 4 can be the same or different as the distance from City 4 to City 1
- distance from City 2 to City 5 can be the same or different as the distance from City 5 to City 2

That means we need to roll for the entire table and can't copy the values across.

---

# 4. How to Build the Distance Table

## Step A: Draw the blank table

| From \\ To | 1 | 2 | 3 | 4 | 5 | 6 |
|-----------|---|---|---|---|---|---|
| **1** | X |   |   |   |   |   |
| **2** |   | X |   |   |   |   |
| **3** |   |   | X |   |   |   |
| **4** |   |   |   | X |   |   |
| **5** |   |   |   |   | X |   |
| **6** |   |   |   |   |   | X |

## Step B: Roll a 20-sided die for each pair of different cities

For example:
- `1 to 2` roll a d20
- `1 to 3` roll a d20
- `1 to 4` roll a d20
- and so on


This table is our **distance map**.
It can also be thought of as an **adjacency matrix** for a weighted graph.

Fancy words. Same road snacks.

---

# 5. How to Read the Table

Suppose we want to know the distance from:
- City 3 to City 5

Look at row 3, column 5.
That distance is `4`.

Suppose our path is:

`1 -> 4 -> 3 -> 5 -> 6 -> 2`

Then the total length is:

- `1 -> 4 = 5`
- `4 -> 3 = 7`
- `3 -> 5 = 4`
- `5 -> 6 = 3`
- `6 -> 2 = 18`

Total:

`5 + 7 + 4 + 3 + 18 = 37`

That is the length of the Hamiltonian path.

---

# 6. Guess-and-Check Method for a Hamiltonian Path

For this activity, we are not starting with Dijkstra’s algorithm.
Instead, we are using a hands-on **guess-and-check** method to understand the structure of the problem first.

## Goal
Create a Hamiltonian path:
- start at one city
- visit each of the six cities exactly once
- do not repeat a city
- add up the total distance
- compare different routes

## Basic Dice Procedure

### Step 1: Choose a starting city
Roll a 6-sided die.

Example:
- Roll = `3`
- Start at City 3

### Step 2: Choose the next city
Roll a 6-sided die again until you get a city that has not already been used.

If you started at City 3:
- you cannot choose 3 again
- if you roll 3, ignore it and roll again
- if you roll 5, move to City 5

### Step 3: Keep going
Continue rolling until all six cities have been used exactly once.

Example outcome:
- Start: `3`
- Next: `5`
- Next: `6`
- Next: `1`
- Next: `4`
- Next: `2`

This gives the Hamiltonian path:

`3 -> 5 -> 6 -> 1 -> 4 -> 2`

### Step 4: Find the total distance
Use the table to add the distances for each step.

### Step 5: Record the result
Write the route and the total.

### Step 6: Repeat
Generate several different Hamiltonian paths and compare totals.

The smallest total found so far becomes the current champion. 🏆

---

# 7. Worked Example Using Guess and Check

We use this distance table:

| From \\ To | 1 | 2 | 3 | 4 | 5 | 6 |
|-----------|---|---|---|---|---|---|
| **1** | X | 8 | 14 | 5 | 17 | 10 |
| **2** | 8 | X | 6 | 12 | 9 | 18 |
| **3** | 14 | 6 | X | 7 | 4 | 11 |
| **4** | 5 | 12 | 7 | X | 15 | 13 |
| **5** | 17 | 9 | 4 | 15 | X | 3 |
| **6** | 10 | 18 | 11 | 13 | 3 | X |

## Trial 1
Suppose the die rolls give:

`2 -> 3 -> 5 -> 6 -> 1 -> 4`

Now compute the total:

- `2 -> 3 = 6`
- `3 -> 5 = 4`
- `5 -> 6 = 3`
- `6 -> 1 = 10`
- `1 -> 4 = 5`

Total:
`6 + 4 + 3 + 10 + 5 = 28`

## Trial 2
Another route:

`4 -> 1 -> 2 -> 5 -> 3 -> 6`

Distances:
- `4 -> 1 = 5`
- `1 -> 2 = 8`
- `2 -> 5 = 9`
- `5 -> 3 = 4`
- `3 -> 6 = 11`

Total:
`5 + 8 + 9 + 4 + 11 = 37`

## Trial 3
Another route:

`1 -> 4 -> 3 -> 2 -> 5 -> 6`

Distances:
- `1 -> 4 = 5`
- `4 -> 3 = 7`
- `3 -> 2 = 6`
- `2 -> 5 = 9`
- `5 -> 6 = 3`

Total:
`5 + 7 + 6 + 9 + 3 = 30`

## Compare the trials

| Trial | Hamiltonian Path | Total Distance |
|------|------------------|----------------|
| 1 | 2 -> 3 -> 5 -> 6 -> 1 -> 4 | 28 |
| 2 | 4 -> 1 -> 2 -> 5 -> 3 -> 6 | 37 |
| 3 | 1 -> 4 -> 3 -> 2 -> 5 -> 6 | 30 |

So far, the best route is:

`2 -> 3 -> 5 -> 6 -> 1 -> 4`

with total distance `28`.

It is not guaranteed to be the absolute best possible route, but it is the best one we have found yet using guess and check.

---

# 8. Why This Matters

This activity helps students see several important ideas:

## A. Data can represent movement
The table is not just numbers.
It tells a story about travel choices.

## B. Some routes are better than others
Two valid Hamiltonian paths can have very different totals.

## C. Randomness can help us explore possibilities
Using dice makes the process tactile and playful.

## D. Brute force gets big fast
Even with only six cities, there are many possible orders.
This shows why mathematicians and computer scientists care about efficient algorithms.

## E. This connects naturally to bigger ideas
This classroom activity can lead into:
- weighted graphs
- shortest path algorithms
- Dijkstra’s algorithm
- Hamiltonian paths
- Hamiltonian circuits
- the traveling salesperson problem

Section 10.6 develops these ideas by first discussing shortest paths in weighted graphs and then moving into the traveling salesperson problem, where the challenge becomes visiting all cities with minimum total distance. :contentReference[oaicite:3]{index=3}

---

# 9. Suggested Lesson Flow

## Day 1 or Part 1: Build the Table
- Introduce cities and roads
- Define weighted graph
- Roll the d20 distances
- Fill in the distance table

## Day 2 or Part 2: Generate Paths
- Review path and Hamiltonian path
- Use the d6 to generate city order
- Reject repeated-city rolls
- Write complete routes

## Day 3 or Part 3: Compare Results
- Compute totals
- Make a class leaderboard
- Ask which route is best so far
- Discuss whether guess and check guarantees the best answer

## Extension
Ask students:
- What changes if we must return to the starting city?
- What if we use 8 cities instead of 6?
- What if one road is extremely long?
- What if we wanted the shortest route from City 1 to City 6 only, instead of visiting all cities?

That last question creates a lovely bridge into **Dijkstra’s algorithm**, which Section 10.6 also presents. :contentReference[oaicite:4]{index=4}

---

# 10. Important Teaching Notes

## About the diagonal
We mark `city to same city` as `X` because:
- we are not traveling anywhere
- in this activity, revisiting cities is not allowed

## About repeated rolls
If a student rolls a city already used in the route:
- ignore it
- roll again

This preserves the Hamiltonian path rule.

## About symmetry
If roads are undirected, then:
- `distance(i, j) = distance(j, i)`

That is the easiest classroom version.

## About "shortest path" versus "visit every city"
These are related, but not identical:
- A **shortest path problem** often means finding the minimum route between two chosen cities.
- A **Hamiltonian path problem** means visiting every city exactly once.
- A **traveling salesperson problem** usually asks for a Hamiltonian circuit of minimum total length.

Students often blur these together at first, which is extremely normal and honestly kind of mathematically adorable.

---

# 11. Simple Summary for Students

We are going to:
1. make six cities
2. roll distances between them
3. build a distance table
4. use dice to create a route through all six cities
5. add the total distance
6. compare routes to see which is shortest

In other words:

**Roll roads. Build map. Wander heroically. Add numbers. Seek glory.** 🎲🧭

---

# 12. Bridge to Future Python Work

Once the class understands the process by hand, we can later write Python code to:
- generate the distance table automatically
- simulate many Hamiltonian paths
- compare totals quickly
- search for better paths
- eventually introduce more systematic methods

But first, the students should touch the math with their hands.
Let the dice do their little plastic thunder.