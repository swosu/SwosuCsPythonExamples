# Codex Folder Summary

Date: 2026-04-08

## Scope

This report reviews the repository folder structure at a high level, with special attention to:

- weak or nearly empty chapters/folders
- programs that look unfinished
- files or folders that may be compromising, risky, or worth removing before sharing

I treated `.git` as internal metadata and did not analyze it as course content. I did include committed virtual environments and generated artifacts because they affect repo quality and risk.

## Executive Summary

This repository has a strong core in `CS1_CS2`, `Discrete_Structures`, `Monty_Hall`, `Software_Engineering`, and parts of `Other_Projects`, but it is uneven. Several top-level folders are very thin, multiple chapter areas look underdeveloped, and there are clear cleanup issues:

- a real-looking OMDb API key is hardcoded in `CS1_CS2/CS2_Review/test_omdb.py`
- multiple virtual environments, caches, executables, and generated files are committed
- a few student/project folders contain obvious `TODO` / `NotImplementedError` placeholders
- some chapters exist mostly as stubs, one-off notebooks, or very small bundles rather than complete teaching units

## Top-Level Folder Summary

### `.venv`

Large committed virtual environment at repo root. This is not teaching content and should not live in source control.

### `.vscode`

Minor editor settings folder. Neutral.

### `Algorithms`

Very small. It currently appears to contain only `ArraySorting/ArraySortingFixture.py`, so as a standalone topic area it feels underbuilt.

### `Artificial_Intelligence`

Contains one PDF (`Artificial_Intelligence_in_Finance.pdf`) and no real code structure. As a repo folder, this feels empty.

### `CS1_CS2`

This is the strongest and most substantial teaching area in the repo. It contains lots of chapter material, labs, projects, and student work. That said:

- the file count is inflated by committed environments and generated output
- `CS2_Review` contains a hardcoded OMDb API key
- several student exercise folders are clearly incomplete
- `Ch09` is massively bloated by a committed notebook virtual environment

Overall: useful and rich, but needs hygiene cleanup.

### `CS2`

Sparse and uneven. Several chapter folders appear to contain little more than caches, test leftovers, or single files. This area feels much weaker than `CS1_CS2`.

Overall: likely incomplete or mid-build.

### `Discrete_Structures`

Substantial overall, but uneven by chapter. Some parts are strong and creative, especially the larger chapter builds and examples, but a few chapter folders are thin enough to stand out as weak.

### `Git_Learning_and_Practice`

Small but coherent. Mostly notes and PDFs. Fine as a support folder, but not a large content area.

### `git_training`

Looks like one day-zero LaTeX slide deck plus generated artifacts (`.fls`, `.nav`, `.snm`, etc.). Useful, but narrow.

### `LaTeX_template`

Healthy utility/template folder. Small, but it has a clear purpose and does not feel compromised.

### `Monty_Hall`

Focused and reasonably healthy project area with scripts, diagrams, chapters, and outputs. One oddity: the README is a Mermaid class diagram rather than a normal project overview, so discoverability could be better.

### `Other_Projects`

Large mixed bag. There is interesting work here, but it is also one of the messiest areas:

- lots of miscellaneous experiments
- student dumps / unsorted work
- binary files and generated outputs
- naming inconsistency

Overall: valuable archive, but needs triage.

### `Software_Engineering`

Small but coherent. The `Unit_Tests` examples look solid for teaching purposes.

### `Student_Codes`

Substantial student-work archive. There is useful material here, but also duplication, unfinished work, and a committed venv inside Tyler Gray's scraper project.

### `Test_Driven_Development`

Very weak as a standalone top-level folder. It currently appears to be just one small file in `Stuck_in_the_mud`.

### `zybooks_python_examples`

Very thin. It currently looks like only `ch01` with four small files, so this feels more like a starter stub than a developed section.

## A. Chapters / Folders That Feel Empty or Weak

These are the clearest weak spots I found.

### Top-level folders

- `Artificial_Intelligence`: one PDF only
- `Algorithms`: effectively one small fixture/example
- `Test_Driven_Development`: one file in one subfolder
- `zybooks_python_examples`: only a tiny `ch01`
- `CS2`: exists, but many chapter folders feel skeletal

### `Discrete_Structures`

- `Discrete_Structures/Ch03`: only one script, so this chapter feels underdeveloped
- `Discrete_Structures/Ch08`: essentially one notebook bundle and checkpoint files
- `Discrete_Structures/Ch11`: only two scripts
- `Discrete_Structures/Ch05/student_workbook/chapters/ch03_fibonacci_natures_algorithm.tex`: explicitly says "Coming soon," which is a sign that the surrounding sequence is not finished

### `CS2`

This area looks especially thin chapter-by-chapter. Examples:

- `CS2/Ch06`: mostly a project shell plus test cache leftovers
- `CS2/Ch12`: contains a suspicious `-p` directory entry and does not look complete
- `CS2/Ch13`: one file
- `CS2/Ch14`: very light notes structure
- `CS2/Ch15`: appears to rely heavily on cache/output rather than source

## B. Programs That Look Completely Unfinished

These are the strongest unfinished-program signals I found.

### Clearly unfinished

- `CS1_CS2/Student_Codes/ShonHakanson_Git_CS2/CodingOdyssey1/Coding_Odyssey_1_main.py`
  - contains multiple `TODO` items
  - raises `NotImplementedError`
  - explicitly says the loop is unfinished

- `CS1_CS2/Student_Codes/ShonHakanson_Git_CS2/CodingOdyssey1/Coding_Odyssey_1_Calcs_Module.py`
  - core functions still raise `NotImplementedError`

- `CS1_CS2/Student_Codes/ShonHakanson_Git_CS2/CodingOdyssey1/Save.py`
  - persistence functions still raise `NotImplementedError`

- duplicate copies of the same unfinished Coding Odyssey files also exist under top-level `Student_Codes/ShonHakanson_Git_CS2/CodingOdyssey1`

- `Discrete_Structures/Ch06/jeremy_solution/scripts/presidents_engine.py`
  - raises `NotImplementedError`

- `Discrete_Structures/Ch06/jeremy_solution/scripts/presidents_of_virtue_round.py`
  - raises `NotImplementedError`

- `Discrete_Structures/Ch06/jeremy_solution/scripts/simulate_game_llm_duel.py`
  - marked as placeholder and raises `NotImplementedError`

### Partially unfinished / assignment-template style

- several student files in `CS1_CS2/Student_Codes/ShonHakanson_Git_CS2` still have `TODO` markers and look like incomplete submissions or starter code
- `CS1_CS2/Student_Codes/Nathan_Christmon/GPT_9.14.py` still contains unresolved `TODO` prompts

## C. Potentially Compromising or Should-Be-Removed Items

These are the most important cleanup candidates.

### Highest priority

- `CS1_CS2/CS2_Review/test_omdb.py`
  - contains a hardcoded OMDb API key: `7ad6b576`
  - even if this is low-stakes, it is still a real credential pattern and should be removed from source control

### Repo hygiene / likely remove from git

- root `.venv`
- `CS1_CS2/Ch09/jupyter_notebook_practice/.venv`
- `CS1_CS2/CS2_Review/movie_venv`
- `Student_Codes/Tyler_Gray/cdl-scraper/venv`
- `Discrete_Structures/Ch05/Stress_And_Recursion/venv`

These virtual environments add huge bulk and noise and make chapter counts look misleading.

### Generated / compiled artifacts worth removing

- many `__pycache__` folders
- `.pyc` files in `CS2`
- committed `.exe` files in student C++ folders under `CS1_CS2/Student_Codes/Justin_Wiederkehr`
- C# `bin/` and `obj/` outputs in `Other_Projects/Student_Codes/CS2/Tanner_Thompson/VS C#/Maps`
- `.class` file in `Discrete_Structures/Unused Files/Exams`
- LaTeX build outputs in `git_training`
- root `debug.log`

### Public-facing caution items

- root `README.md` includes a direct email address
  - not necessarily bad, but worth deciding intentionally if the repo is public

- `Other_Projects/NSF_CC_Star_Funding/Awards.csv`
  - appears to contain names, email addresses, addresses, and phone numbers from grant data
  - this may be public-source data, but if you want a cleaner classroom repo, this is worth reviewing

## Recommended Cleanup Order

1. Remove or rotate the OMDb API key in `CS1_CS2/CS2_Review/test_omdb.py`.
2. Remove committed virtual environments, caches, binaries, and logs from git.
3. Decide whether unfinished student skeletons should stay in the main teaching repo or move to an archive/staging area.
4. Consolidate duplicate student folders where the same project appears in both `CS1_CS2/Student_Codes` and top-level `Student_Codes`.
5. Strengthen or merge the thinnest chapter folders (`Algorithms`, `Artificial_Intelligence`, `Test_Driven_Development`, weak `CS2` chapters, weak `Discrete_Structures` chapters).

## Bottom Line

The repo has a lot of good teaching material, but it also has visible clutter and a few real risks. The biggest immediate concern is the hardcoded OMDb API key. After that, the main quality issue is repository hygiene: committed environments, caches, binaries, and unfinished skeletons are making the project look less intentional than it probably is.
