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

<<<<<<< ours
## Shared Validation Error Behavior

Invalid Fibonacci inputs should fail through one shared validation path before either
strategy starts calculation.

Planned error contract:

- raise `TypeError` when the value is not accepted as an integer input
- raise `ValueError` when the value is integer-like but less than `0`
- use the same exception types and message templates for both recursive and iterative
  strategies
- normalize accepted values to built-in `int` before calculation so later code does not
  need to preserve the original input type

Planned invalid-input categories:

- `bool` values should raise `TypeError` even though `bool` is a subclass of `int`
- strings, floats, and other non-integer-like values should raise `TypeError`
- objects that implement `__index__` should be accepted, normalized to `int`, and then
  checked for the non-negative rule
- negative integer inputs should raise `ValueError`

Planned message templates:

- type failures: `fibonacci input must be a non-boolean integer or support __index__`
- range failures: `fibonacci input must be greater than or equal to 0`

This keeps failure behavior explicit enough for shared validation tests and later
documentation to assert on exact exceptions and messages.
=======
## Iterative Fibonacci Contract

The iterative strategy should expose one small public function for direct calculation:

- `iterative_fibonacci(n: int) -> int`

Contract rules:

- accept the same public input shape as the recursive strategy so comparison code can call both strategies the same way
- treat `n` as the Fibonacci position index, not as a request for a whole sequence or a formatted report
- return one integer Fibonacci value for the validated index
- preserve standard base cases: `0` returns `0` and `1` returns `1`
- keep the unit focused on loop-based state updates after validation is complete

Validation usage:

- the public iterative function should call the shared Fibonacci validation helper before any loop logic runs
- the shared helper should own normalization and consistent exception behavior
- the iterative function should use the validated integer returned by that helper instead of re-checking types or ranges locally

Boundary reminders for this unit:

- no printing, markdown generation, benchmarking, or visualization preparation
- no sequence-building return value, metadata wrapper, or comparison payload
- no strategy-specific validation branch that would drift from the shared rules
>>>>>>> theirs

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

## Shared Validation Reuse Plan

Validation should be implemented once and reused by both Fibonacci strategies.

Recommended approach:

- place validation in a small shared helper module inside the future Fibonacci source area rather than inside either strategy module
- expose one helper function that validates and normalizes the incoming value before any recursive or iterative work begins
- have each public strategy call that helper as its first step and then continue with its own teaching-focused algorithm body

Shared helper responsibilities:

- reject `bool` and other non-integer-like inputs with a consistent `TypeError`
- reject negative integer-like inputs with a consistent `ValueError`
- convert accepted integer-like values to built-in `int`
- return the normalized `int` so both strategies operate on the same input form

Why this design is preferred:

- it removes duplicated validation branches from the recursive and iterative units
- it keeps the algorithm examples easy for students to read because the strategy bodies can focus on base cases, recursion, loops, and state updates
- it keeps the invalid-input contract in one place so tests and documentation only need one authoritative rule set

Boundary guidance:

- validation belongs at the public entry point for each strategy, not inside the recursive step logic itself
- the shared helper should stay narrowly focused on input checking and normalization, without computing Fibonacci values or formatting messages beyond the agreed exception text
- if the project stays small early on, the helper can remain a private utility within the Fibonacci package, but it should still be separated from the recursive and iterative implementation units

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

### Planned Commit Scope

The commit order should follow deliverable stages instead of the order problems happen to be discovered during development.

1. Planning commit
   - capture the implementation plan, repository layout decisions, and commit sequence before code is added
2. Project-structure commit
   - create the agreed source, test, and optional asset locations
   - place the main instructional markdown file in its final location
3. Implementation commits
   - add shared input validation before strategy-specific behavior depends on it
   - add recursive and iterative Fibonacci units as separate behavior-focused changes
   - add comparison and visualization support only after the core strategies exist
4. Testing commit
   - add automated tests after the main implementation units and helpers have stable interfaces
5. Documentation commit
   - complete the instructional markdown, Big O analysis, visualization writeup, design notes, and testing explanation after the behavior and tests are in place
6. Refactor commit
   - limit the final cleanup pass to naming, duplication removal, function boundaries, and other behavior-preserving improvements

This sequence is intentional because it keeps planning artifacts first, foundational structure ahead of implementation, validation separate from explanation, and behavior-preserving cleanup at the end.

## Open Decisions For Review

Before implementation, confirm:

- whether the final project should stay function-based or introduce small focused classes
- whether the main lesson should live in `README.md` or a dedicated markdown file
- whether the first visualization should remain pure markdown and ASCII
- how much design-pattern terminology is appropriate for the student audience
