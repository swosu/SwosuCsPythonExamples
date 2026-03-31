# Fibonacci Exploration And Implementation Plan

## Purpose

Create a future Fibonacci exploration that does more than explain the sequence. The work should also model sound software engineering practices, including:

- clear file organization
- clean, readable code
- small focused functions
- useful abstraction boundaries
- separation of responsibilities
- unit testing
- documentation that explains design choices

This document is a plan only. It does not include implementation code.

## Project Goals

The final project should:

- explain the Fibonacci sequence in a student-friendly way
- compare recursive and iterative approaches
- include Big O analysis
- visualize how Fibonacci values and algorithm cost change as input grows
- demonstrate good code organization and maintainability

## Guiding Design Principles

The future implementation should follow these principles:

- Keep functions small and focused on one task.
- Prefer descriptive names over clever shortcuts.
- Separate calculation logic from display and reporting logic.
- Avoid mixing visualization concerns with sequence-generation logic.
- Keep documentation, computation, and tests in clearly separated files.
- Make it easy to add new Fibonacci strategies later without rewriting unrelated parts.

## Planned Responsibilities

The future work should be split by responsibility rather than placing everything in one file.

Recommended responsibility areas:

- Fibonacci calculation logic
- complexity and comparison explanation
- visualization or reporting support
- command-line or user-facing entry point if one is later added
- unit tests
- markdown documentation

## Planned File Management

The project should use a clear layout so readers can quickly find where each concern belongs.

Suggested future structure:

- `README.md` or a dedicated markdown lesson file for the main explanation
- `src/` for implementation files
- `tests/` for unit tests
- `assets/` only if later visual artifacts are added

Suggested implementation file direction:

- one module for Fibonacci sequence generation
- one module for visualization/report formatting if needed
- one test module focused on recursive and iterative behavior

The plan should avoid a single oversized file that mixes:

- algorithm logic
- user interaction
- formatting
- test code
- instructional notes

## Planned Abstraction Strategy

The implementation should make room for good abstraction from the start.

Recommended approach:

- Define a clear interface or pattern for Fibonacci strategies.
- Keep recursive and iterative implementations separate.
- Use a higher-level coordinator only if there is a real need to compare or report on multiple strategies.
- Do not create unnecessary abstraction early, but do separate concerns where responsibilities clearly differ.

### Class Responsibility Guidance

If classes are used, each class should have one clear responsibility.

Possible future class roles:

- a class responsible for recursive Fibonacci calculation
- a class responsible for iterative Fibonacci calculation
- a class or utility focused on presenting comparison data or visual summaries

Important design constraint:

- do not place computation, printing, formatting, and testing behavior inside the same class

If the final solution stays function-based instead of class-based, the same responsibility boundaries should still apply.

## Planned Function Design

The future code should prefer small functions with narrow responsibilities.

Examples of function-level responsibilities:

- validate an input value
- compute a Fibonacci number recursively
- compute a Fibonacci number iteratively
- generate a list of values for a range of inputs
- prepare comparison data for display
- prepare visualization data

The implementation should avoid large multi-purpose functions that:

- calculate values
- print output
- build tables
- handle errors
- run comparisons

all in one place.

## Planned Documentation Content

The final markdown should include the following instructional sections:

1. Introduction to the Fibonacci sequence
2. Recursive implementation concept
3. Iterative implementation concept
4. Side-by-side comparison
5. Big O analysis
6. Visualization of increasing inputs
7. Notes on code organization and design decisions
8. Testing strategy overview

## Recursive vs Iterative Comparison Plan

The comparison should cover both algorithm behavior and code design tradeoffs.

Planned comparison categories:

- conceptual simplicity
- readability
- repeated work
- runtime growth
- memory usage
- ease of testing
- ease of maintenance
- suitability for large inputs

Planned format:

- a markdown comparison table
- a short explanation below the table

## Big O Analysis Plan

The final explanation should include both time and space complexity.

Planned points:

- naive recursive Fibonacci
  - time complexity: `O(2^n)` in common introductory analysis
  - space complexity: `O(n)` because of call stack depth
- iterative Fibonacci
  - time complexity: `O(n)`
  - space complexity: `O(1)` when tracking only the needed prior values

The document should also explain:

- why repeated recursive calls create high cost
- why iteration scales better for larger inputs
- why algorithm analysis belongs alongside implementation choices

## Visualization Plan

The future project should visualize more than just the Fibonacci numbers themselves.

Recommended visualization topics:

- growth of Fibonacci values as `n` increases
- growth of computational work for recursive and iterative approaches

Markdown-friendly options for the first version:

- comparison tables
- simple ASCII bars
- small recursion-tree sketches for low input values
- a table of selected inputs such as `5, 10, 15, 20, 25, 30`

Important distinction to preserve:

- one visualization should focus on sequence value growth
- another should focus on algorithm cost growth

## Testing Plan

Unit testing should be part of the design from the beginning, not added at the end.

The future tests should verify:

- correct base-case behavior
- correct values for a range of small inputs
- matching results between recursive and iterative implementations
- expected handling of invalid inputs if validation is added
- behavior of helper functions that prepare comparison or visualization data

Testing guidance:

- keep tests independent from output formatting when possible
- avoid coupling tests to display text unless formatting itself is the feature under test
- test small units directly rather than only through a top-level script

## Clean Code Expectations

The final implementation should aim for:

- short files with clear purpose
- predictable naming
- minimal duplication
- simple control flow
- comments only where they add real clarity
- low coupling between modules
- straightforward testability

The work should avoid:

- oversized functions
- hidden side effects
- duplicated recursive and iterative comparison logic
- mixing educational prose with executable implementation details in the same module

## Planned Development Sequence

Recommended later implementation order:

1. define the final markdown outline and project structure
2. implement Fibonacci calculation units with clean separation
3. add comparison-support helpers
4. add visualization-support helpers
5. add unit tests
6. complete the instructional markdown
7. refine naming, organization, and readability

## Acceptance Criteria

The future deliverable should meet these standards:

- the repository structure is easy to understand
- recursive and iterative logic are kept separate
- functions are small and responsibility-focused
- responsibilities are not mixed across classes or modules
- the Fibonacci explanation is clear for students
- Big O analysis is included and correct at an introductory level
- visualization of increasing inputs is included
- unit tests cover core logic
- documentation explains both algorithm tradeoffs and design decisions

## Planned Commit Messages

Recommended commit sequence:

1. `docs: revise fibonacci project plan around clean architecture`
2. `docs: define fibonacci project structure and responsibility boundaries`
3. `feat: add separated recursive and iterative fibonacci implementations`
4. `feat: add comparison and visualization support modules`
5. `test: add unit tests for fibonacci strategies and helpers`
6. `docs: write fibonacci analysis and implementation walkthrough`
7. `refactor: simplify function boundaries and improve naming`

## Open Decisions For Review

Before implementation, confirm:

- whether the final project should stay function-based or introduce small focused classes
- whether the main lesson should live in `README.md` or a dedicated markdown file
- whether the first visualization should remain pure markdown and ASCII
- how much design-pattern terminology is appropriate for the student audience
