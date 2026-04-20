# Branch Run Notes - Plotting Foundations for CS2

## Branch
claude_plotting

## Date
2026-04-20

## What was built

- [x] Project folder structure (notebooks/, figures/, src/)
- [x] README.md with lesson guide
- [x] Notebook skeleton with 10 section headings
- [x] Part 1 - Why Plot? (teaching markdown cells)
- [x] Part 2 - First Line Plot (lists, labels, legend)
- [x] Part 3 - NumPy Arrays and Statistics
- [x] Part 4 - Score Curving with Array Transformation
- [x] Part 5 - Pandas DataFrames and Bar Charts
- [x] Part 6 - Monthly Status Line Plot (two series, savefig)
- [x] Part 7 - Scatter Plot with Marker Size
- [x] Part 8 - Subplots Comparison (two panels)
- [x] Part 9a - Fibonacci Implementations with Call Counter
- [x] Part 9b - Fibonacci Metrics Collection (timing + counts)
- [x] Part 9c - Fibonacci Growth Plots
- [x] Part 10 - Mini-Report Practice Template and Example
- [x] src/fibonacci_metrics.py (optional helper module)
- [x] tests/test_fibonacci_metrics.py (optional tests)

## Smoke test results

- Notebook executed top-to-bottom: PASS
- Figures saved: assignment_averages_bar.png, bad_vs_better_plot.png, basic_line_plot.png, broadway_style_subplots.png, capacity_gross_scatter.png, curved_scores_plot.png, exam_average_plot.png, fibonacci_growth.png, monthly_status_lineplot.png
- output_fig.png saved: yes
- subplots.png saved: yes
- pytest: PASS

## Git status at handoff

```text
On branch claude_plotting
Your branch is ahead of 'origin/claude_plotting' by 12 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
```

## Git log (last 10 commits)

```text
f1e399f test: notebook executes top-to-bottom without errors
8248299 fix: add conftest.py and __init__.py files so pytest can resolve src imports
e3c34ad feat: add optional fibonacci_metrics module and tests
361f7ef content: complete remaining notebook setup, sections, and plot savefig outputs
9b23f6d chore: add .gitignore and requirements.txt
5d6678c content: add Part 4 - score curving with array transformation and savefig
11f9706 content: add Part 3 - NumPy arrays, statistics, and reference line plot
aca2d6d content: add Part 2 - first line plot with labels and legend
12b43c4 content: add Part 1 - Why Plot teaching cells
fc515bf feat: add notebook skeleton with section headings
```

## Open items / known issues

- The `jupyter nbconvert` subcommand is not installed in this environment, so the smoke run used a direct Python cell executor fallback instead of `nbconvert --execute`.
- The fallback run wrote `notebooks/plotting_foundations_cs2_executed.ipynb` as a copied run artifact without rich execution outputs.
- `plt.show()` under the Agg backend emits expected non-interactive warnings during headless execution.

## Poison data check

- No real student names used: YES
- No real grades used: YES
- No Canvas data: YES
- No credentials or tokens: YES
- No .env values: YES
