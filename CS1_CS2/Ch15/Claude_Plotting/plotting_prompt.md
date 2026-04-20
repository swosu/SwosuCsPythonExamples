# Workbench Playbook - Plotting Notebook

Project copy created. Master playbook read and internalized. Intake begins.

## Source Template

This project playbook is based on the read-only Workbench master template named **Playbook**. The master template says the project copy should preserve the intake conversation, move quickly toward a `build_intent.md`, ask only necessary questions, give Wilbur a branch-safe launch artifact, and keep poison data out of durable artifacts.

Master playbook reminders captured for this project:

- The conversation is the Spark.
- Build Intent is the fuse.
- Wilbur never works on `main`.
- If files will change, Wilbur creates or confirms a project branch first.
- Student records, Canvas data, grades, submissions, names, IDs, emails, credentials, tokens, `.env` values, and secrets are poison data.
- This project is durable course material only and uses fake/synthetic data.

## 0. Raw Project Intent

Create a beginner-friendly, interactive Python/Jupyter notebook for Computer Science II students who have done no plotting before.

The notebook should teach:

- the mechanics of basic plotting
- why plotting matters
- how plots tell stories with data
- how to choose useful chart types
- how to avoid plot clutter and visual nonsense
- how to move from tiny examples to a more interesting computational story

A strong first interesting example is comparing iterative and recursive Fibonacci implementations because runtime, call counts, and growth curves become dramatic quickly.

This project should be educational material only. No student data, no Canvas data, no grading automation, no private records.

## 1. Working Project Title

Plotting Foundations for CS2

## 2. One-Sentence Intent

Create a branch-safe course-material prototype containing an interactive Jupyter notebook that introduces plotting fundamentals and builds toward a storytelling-with-data example comparing iterative and recursive Fibonacci behavior.

## 3. Why This Matters

CS2 students often learn algorithms as code first and evidence second. Plotting gives them a visual way to see how programs behave, how performance changes, and how a technical claim can become a readable story.

This notebook should help students move from:

```text
I ran code and got numbers.
```

to:

```text
I collected evidence, visualized it, and explained what the pattern means.
```

That is a big step. It turns code into a lantern instead of just a machine that coughs up output.

## 4. Desired Change

Create the initial repository artifact set for a plotting lesson/workbook.

### 4.1 `notebooks/plotting_foundations_cs2.ipynb`

Purpose:

- introduce plotting in Python using beginner-friendly examples
- assume students have little or no plotting background
- use hard-coded or synthetic data only
- teach plots as communication, not decoration
- build toward a computational example students can understand

Notebook style law:

1. Big opening markdown cell explaining the notebook purpose.
2. For every serious Python code cell:
   - markdown before: goal of the next code chunk
   - code cell: focused implementation
   - markdown after: implementation details
   - markdown after or included: why this matters for programming, algorithms, or storytelling with data
3. Keep code cells small enough for students to inspect.
4. Prefer plain `matplotlib` first. Optional later sections may mention pandas or seaborn, but the first pass should not require them.
5. Use fake/synthetic data only.

Possible notebook sequence:

- What is a plot?
- Why do programmers plot data?
- Importing `matplotlib.pyplot`
- First line plot with small hard-coded lists
- Adding title, axis labels, grid, and legend
- Scatter plot basics
- Bar chart basics
- Plotting multiple series
- Choosing the right plot for the question
- Bad plot vs better plot
- Mini-lab: tell a story from a small dataset
- Fibonacci setup
- Implement iterative Fibonacci
- Implement simple recursive Fibonacci
- Measure runtime and/or operation counts for small n
- Plot growth curves
- Explain why recursion explodes
- Reflection questions

### 4.2 `README.md` or `plotting_foundations_readme.md`

Purpose:

- explain what the lesson is
- list required Python packages
- explain how to open the notebook
- state that the notebook uses synthetic data only
- give a suggested classroom flow

### 4.3 Optional supporting files

Optional only if useful:

```text
src/fibonacci_metrics.py
tests/test_fibonacci_metrics.py
data/synthetic_plotting_examples.csv
```

Supporting files should exist only if they keep the notebook cleaner and more testable. Do not overbuild before the notebook exists.

## 5. Non-Goals / Do Not Touch

- Do not use real student data.
- Do not use Canvas data.
- Do not create grading automation.
- Do not connect to any LMS or API.
- Do not use credentials, tokens, `.env` values, or private records.
- Do not work on `main`; Wilbur must create or confirm a project branch.
- Do not overbuild a full plotting curriculum before the first notebook exists.
- Do not hide the learning behind too much helper code.
- Do not require advanced plotting libraries for the first pass.

## 6. Likely Files, Commands, Repo Areas, or Systems

Likely Workbench project folder:

```text
workbench/projects/plotting-foundations-cs2/
  build_intent.md
  deliverables_snapshot.md
  notes/
  prompts/
  runs/
```

Likely target course/project files:

```text
README.md
notebooks/plotting_foundations_cs2.ipynb
src/fibonacci_metrics.py        # optional
tests/test_fibonacci_metrics.py # optional
data/                          # optional synthetic-only examples
```

Suggested branch pattern:

```text
wb/plotting-foundations-cs2-YYYYMMDD-HHMM
```

Likely commands after Wilbur builds:

```bash
git status
python -m pytest
jupyter notebook notebooks/plotting_foundations_cs2.ipynb
```

If notebook execution is tested non-interactively and the environment supports it:

```bash
jupyter nbconvert --to notebook --execute notebooks/plotting_foundations_cs2.ipynb --output plotting_foundations_cs2.executed.ipynb
```

## 7. Expected Outputs

### Durable course-material outputs

- A readable beginner-friendly plotting notebook.
- A README or lesson guide.
- Synthetic example data embedded in the notebook or stored as a safe local file.
- A Fibonacci comparison section that collects small timing/count data and plots it.
- Optional helper module and tests if they make the notebook cleaner.
- Branch run notes and git status receipts.

### Teaching style requirements

The notebook should be written like a guided workbook, not a code dump.

Each serious code cell should be surrounded by teaching text:

```text
Goal before code → focused code → explanation after code → why it matters
```

The voice should be clear, warm, and practical. It can be playful, but the technical concepts should stay clean.

## 8. First Successful Test

A first successful prototype exists when:

- the notebook opens successfully in Jupyter
- every code cell runs from top to bottom
- the notebook creates at least one line plot, scatter plot, and bar chart
- the notebook includes labels, titles, and legends where appropriate
- the Fibonacci section compares iterative and recursive behavior for safe small `n` values
- the notebook explains why the recursive version grows quickly
- no student data, Canvas data, credentials, or private records are used
- Wilbur leaves branch/run notes and a clean `git status` report

## 9. Poison-Data / Branch-Safety Risks

Poison data risk is low because this is course content using synthetic data only.

Still, Wilbur must avoid:

- student names
- grades
- submissions
- Canvas exports
- private files
- credentials
- API keys
- `.env` values

Branch safety is required. Wilbur must not work on `main`.

## 10. Open Questions

These can be resolved later without blocking the first build:

1. Should the first notebook use only `matplotlib`, or include a short optional pandas section?
2. Should Fibonacci metrics focus on wall-clock timing, operation counts, function calls, or all three?
3. Should the notebook be one long guided workbook or split into two notebooks later?
4. Should the Fibonacci section use memoization as a final “plot twist” extension?

Recommended first-pass choices:

- Start with `matplotlib` only.
- Include both operation counts and wall-clock timing, but keep `n` small for recursive Fibonacci.
- Use one notebook first.
- Mention memoization as an extension, not the main build.

## 11. Draft Build Intent

### 1. Working title

Plotting Foundations for CS2

### 2. One-sentence intent

Create a branch-safe educational Jupyter notebook that teaches CS2 students the mechanics and storytelling purpose of Python plotting, then uses iterative vs recursive Fibonacci behavior as a concrete algorithm-visualization example.

### 3. Why this matters

Students need to see that plots are not just pretty pictures. Plots are evidence. They help programmers compare algorithms, notice growth patterns, explain results, and communicate technical ideas clearly.

### 4. Desired change

Build the first version of a plotting workbook for CS2 with beginner-friendly explanations, small runnable examples, and a Fibonacci comparison arc.

### 5. Non-goals / do not touch

Do not use student data, Canvas data, grading workflows, API secrets, or main-branch changes. Do not build a full analytics platform. Do not require complex plotting libraries before the basics work.

### 6. Likely files, commands, repo areas, or systems

Likely files:

```text
README.md
notebooks/plotting_foundations_cs2.ipynb
src/fibonacci_metrics.py        # optional if helpful
tests/test_fibonacci_metrics.py # optional if helper code is created
workbench/projects/plotting-foundations-cs2/build_intent.md
workbench/projects/plotting-foundations-cs2/deliverables_snapshot.md
workbench/projects/plotting-foundations-cs2/branch_run_notes.md
```

Likely commands:

```bash
git status
python -m pytest
jupyter notebook notebooks/plotting_foundations_cs2.ipynb
```

### 7. Expected outputs

- One interactive Jupyter notebook for plotting foundations.
- One README/lesson guide.
- Synthetic/hard-coded data only.
- Fibonacci iterative vs recursive comparison with plots.
- Optional helper code/tests if needed.
- Branch and run receipts.

### 8. First successful test

The notebook runs top-to-bottom, produces several basic plots, explains plotting choices, compares iterative and recursive Fibonacci safely, and leaves no poison data or main-branch edits.

### 9. Poison-data / branch-safety risks

Low poison-data risk, but still no student data, Canvas data, names, grades, submissions, credentials, tokens, `.env` values, or private records. Wilbur must work on a branch.

### 10. Open questions

Matplotlib-only first pass is recommended. Memoization can be an extension. If runtime timing is noisy, operation/function-call counts should be used as the clearer teaching signal.

### 11. Handoff instruction for Wilbur

Read this playbook, create or update `workbench/projects/plotting-foundations-cs2/build_intent.md`, create or confirm a branch named like `wb/plotting-foundations-cs2-YYYYMMDD-HHMM`, build the notebook and README as durable course material, use only synthetic data, run available tests, and leave branch/run notes including git status.

## 12. Recommended Wilbur Command

```bash
wb gobble workbench/projects/plotting-foundations-cs2/build_intent.md
```

## 13. First Question for Refinement Later

Question:

What should the first plotting workbook optimize for?

Options:

A. **Mechanics-first plotting basics**

Best when: students need lots of tiny examples before algorithm analysis.

Tradeoff: the Fibonacci story arrives later.

B. **Algorithm-story-first notebook**

Best when: the main goal is showing how plotting reveals algorithm behavior quickly.

Tradeoff: some plotting basics may feel rushed.

C. **Two-layer notebook: basics first, Fibonacci story second**

Best when: we want students to learn the tools before using them for a meaningful CS2 comparison.

Tradeoff: slightly longer notebook, but better classroom flow.

My recommendation:

Choose **C. Two-layer notebook: basics first, Fibonacci story second**. Let the students learn how to hold the flashlight before sending them into the recursion cave.


## 14. Added Context from Current Chapter / Assignment Materials

This playbook has now been enriched with the chapter/lab material Jeremy provided after the first draft. The attached material describes the current grading pattern and several relevant NumPy, pandas, and matplotlib labs. The goal is not to copy the auto-graded lab solutions directly into the notebook. The goal is to use these topics as a bridge so the plotting workbook supports what students are already seeing in the chapter.

### 14.1 Current weekly coding practice structure

Students are expected to solve three problems and submit one PDF with three sections, one section per problem.

Each section should use these headings:

```text
Code
Run Results
Quick Reflection
```

Rubric emphasis:

- Code is the main thing: 22 points per problem.
- Run results matter: 6 points per problem.
- Quick reflection matters: 2 points per problem.
- Submission quality matters: clear labels, all three problems included, easy to follow.
- Extra credit can come from improvements, a short explanation video, or presenting in class.

Implication for the notebook:

The plotting workbook should model this same rhythm:

```text
Code → Run Results / visible output → Quick Reflection
```

Students should see that plots are a form of run result. A saved image such as `output_fig.png` or `subplots.png` is proof that the code ran and produced evidence.

### 14.2 Relevant chapter topics to connect

The current chapter/lab set includes:

- NumPy arrays and basic array math
- loading numeric data from text files
- calculating averages, medians, maximums, and counts
- curving scores by transforming an array
- pandas dataframe loading and sorting
- dataframe summary statistics such as max, median, mean, and standard deviation
- line plots with matplotlib
- scatter plots with marker size, color, and gridlines
- multiple plots/subplots in one figure
- saving figures with `plt.savefig()`

The notebook should connect plotting to these ideas instead of treating plotting as a random extra topic.

### 14.3 Suggested lab-aligned notebook arc

The notebook should still begin gently, but it can now align more clearly with the labs.

Recommended sequence:

1. **Why plot?**
   - A plot is evidence.
   - A plot helps us see patterns faster than raw numbers.
   - A plot helps communicate a result.

2. **Tiny hard-coded line plot**
   - Use simple lists.
   - Teach `plt.plot()`.
   - Add title, x-label, y-label, legend, and grid.

3. **NumPy arrays as plot data**
   - Create arrays for exam scores.
   - Compute average scores like the average exam scores lab.
   - Plot student number vs average score.
   - Add a horizontal reference line at 80 if useful.
   - Count how many averages are 80 or higher.

4. **File-style numeric data with NumPy**
   - Use a synthetic list or a tiny safe local text file.
   - Calculate median and average.
   - Demonstrate a curve: `curved_scores = scores + (100 - max_score)`.
   - Plot original scores and curved scores.
   - Explain transformation as a data story: same shape, shifted upward.

5. **Pandas dataframe statistics**
   - Build a tiny synthetic dataframe with names replaced by generic labels such as `Student A`, `Student B`, or fake names.
   - Sort by final score.
   - Use `.max(numeric_only=True)`, `.median(numeric_only=True)`, `.mean(numeric_only=True)`, and `.std(numeric_only=True)`.
   - Plot assignment averages as a bar chart.

6. **Line plot story: monthly counts**
   - Use a synthetic airport-style dataframe with columns like `Month`, `Delayed`, and `Cancelled`.
   - Calculate average delays and cancellations.
   - Plot delays and cancellations on the same figure.
   - Label the plot just like the flight-status lab: x-label, y-label, title, legend.
   - Save as `output_fig.png`.

7. **Scatter plot story: relationship between two values**
   - Use synthetic Broadway-style data with `Capacity` and `Gross Potential`.
   - Insert a `Size` column based on gross potential.
   - Plot capacity vs gross potential.
   - Include marker style, gridlines, axis labels, and title.
   - Save as `output_fig.png` or a different educational filename to avoid overwriting too early.

8. **Subplots: comparing two related datasets**
   - Use two small synthetic monthly datasets.
   - Create two scatter plots side by side.
   - Add a main figure title and subplot titles.
   - Save as `subplots.png`.

9. **Fibonacci algorithm story**
   - Implement iterative Fibonacci.
   - Implement naive recursive Fibonacci.
   - Measure call counts and runtime for safe small `n` values.
   - Plot growth using line plots.
   - Explain why recursive Fibonacci explodes.
   - Optional extension: memoized Fibonacci as the hero walking in with a fire extinguisher.

10. **Mini-report practice**
    - Ask students to choose one plot and write:
      - Code
      - Run Results
      - Quick Reflection
    - This mirrors the weekly coding practice PDF structure.

### 14.4 Lab-specific inspiration, not direct dependency

The notebook may reference these lab ideas as inspiration:

- Average exam scores with NumPy arrays
- Curve student scores with NumPy
- Course grade statistics with pandas
- Flight status line plot
- Broadway show scatter plot
- Broadway show multiple plots/subplots

However, the notebook should not depend on ZyBooks, Canvas, real student records, or private files. If file-loading examples are included, use tiny generated files inside the repo or hard-coded synthetic examples.

### 14.5 Concrete notebook requirements after enrichment

The first notebook should include these concepts:

- `import numpy as np`
- `import pandas as pd`
- `import matplotlib.pyplot as plt`
- line plot
- scatter plot
- bar chart
- subplot example
- `plt.savefig()` example
- dataframe sorting
- dataframe summary statistics
- array transformation
- visible output after code cells
- reflection prompts
- at least one saved figure file
- Fibonacci comparison plot

### 14.6 Figure filenames

Use clear filenames that do not accidentally overwrite important examples unless intentionally demonstrating overwrite behavior.

Recommended filenames:

```text
figures/basic_line_plot.png
figures/exam_average_plot.png
figures/curved_scores_plot.png
figures/assignment_averages_bar.png
figures/monthly_status_lineplot.png
figures/capacity_gross_scatter.png
figures/broadway_style_subplots.png
figures/fibonacci_growth.png
```

If matching lab behavior directly, also demonstrate:

```text
output_fig.png
subplots.png
```

but explain that lab graders often require exact filenames.

### 14.7 Student-facing explanation style

The notebook should repeatedly say, in student-friendly language:

- A plot needs a question.
- Axis labels tell the reader what the numbers mean.
- A title tells the reader what story to look for.
- A legend is needed when more than one series appears.
- A grid can help readability, but too much visual clutter hurts.
- Saving a plot creates proof that the code ran.
- The best plot is not the fanciest plot. The best plot answers the question clearly.

### 14.8 Updated build intent for Wilbur / Codex

When resurrecting Wilbur, give Codex this richer instruction:

```text
You are building durable educational course material for CS2 students who are new to plotting.

Create or update a branch-safe project for Plotting Foundations for CS2. Do not work on main. Use synthetic data only. Do not use student records, Canvas data, grades from real students, submissions, names, IDs, emails, credentials, tokens, or .env values.

Primary deliverable: notebooks/plotting_foundations_cs2.ipynb
Secondary deliverable: README.md or docs/plotting_foundations_lesson_guide.md
Optional deliverables only if helpful: src/fibonacci_metrics.py, tests/test_fibonacci_metrics.py, figures/ output folder.

The notebook should teach plotting mechanics and storytelling with data. It should align with current chapter skills: NumPy arrays, pandas dataframes, summary statistics, line plots, scatter plots, bar charts, subplots, and saving figures.

The notebook should model this teaching rhythm for every serious code section:

Goal before code → focused code → visible run result or plot → explanation after code → quick reflection prompt.

Include sections inspired by these lab topics:

1. Average exam scores using NumPy arrays
2. Curving scores using NumPy transformation
3. Course grade statistics using pandas
4. Flight-status-style line plot with two series and a legend
5. Broadway-style scatter plot with marker size and gridlines
6. Two-panel subplot comparison
7. Iterative vs naive recursive Fibonacci comparison

Do not copy private assignment text into student-facing materials. Use the concepts and create fresh synthetic examples.

The notebook must run top-to-bottom. It should create a figures/ folder if needed. It should save example figures with clear filenames. It should include at least one example of plt.savefig("output_fig.png") and one example of plt.savefig("subplots.png") because students may encounter exact-filename graders.

For Fibonacci, keep recursive n small enough to avoid freezing student machines. Prefer call counts and timing together, but explain timing noise. Include an optional memoization extension only after the naive recursion plot.

Add a final mini-report practice section asking students to choose a plot and write Code, Run Results, and Quick Reflection.

After building, run available smoke checks. If possible, execute the notebook non-interactively with nbconvert. Leave a branch/run note with git status at the end, including proof of changed files and whether tests passed.
```

### 14.9 Updated first successful test

The enriched project is successful when:

- notebook opens in Jupyter
- notebook runs top-to-bottom
- code uses NumPy, pandas, and matplotlib
- notebook creates line, scatter, bar, and subplot figures
- notebook saves at least one figure with `plt.savefig()`
- notebook includes lab-aligned examples using synthetic data
- notebook includes Fibonacci iterative vs recursive comparison
- notebook includes mini-report/reflection practice
- no poison data appears
- branch/run notes include `git status`

### 14.10 Resurrection note

Wilbur died during the first attempt and will need to be resurrected later. When he returns, start with a smaller, safer task:

1. Create the branch.
2. Create only the project folder and `build_intent.md`.
3. Create the README/lesson guide.
4. Then create the notebook skeleton.
5. Only after the skeleton exists, fill notebook sections one at a time.
6. Run notebook smoke checks last.

Do not ask Wilbur to build the whole goblin cathedral in one bite. Start with bones, then muscles, then caffeinated flamethrower.

