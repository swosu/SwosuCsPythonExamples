#!/bin/bash
# Fix underscores & rebuild safe placeholder files

for ch in \
  ch01_foundations_solution \
  ch02_recursive_algorithms_solution \
  ch03_fibonacci_solution \
  ch04_measuring_recursion_solution \
  ch05_big_o_through_fib_solution \
  ch06_memoization_mind_solution \
  ch07_big_o_meets_reality_solution \
  ch08_teaching_tips_and_assessments
do
  cat > chapters/${ch}.tex <<EOF
\\chapter{${ch//_/ }}
\\label{${ch}}

This is a placeholder for \\texttt{${ch}.tex}.

% TODO: Add teacher notes, solutions, and discussion guidance here.

EOF
done

echo "[OK] Fixed underscores and placeholders. Run 'make clean && make' again."
