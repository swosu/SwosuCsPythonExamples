# Git Status Gremlins Report

## Project

`CS1_CS2/Ch15/Claude_Plotting`

## Date

2026-04-20

## Current git status summary

- Branch: `main`
- Local branch is ahead of `origin/main` by 13 commits
- Working tree: clean

## Exact warning lines seen from `git status`

```text
warning: could not open directory 'CS1_CS2/Ch15/Claude_Plotting/pytest-cache-files-lv_hbpxp/': Permission denied
warning: could not open directory 'CS1_CS2/Ch15/Claude_Plotting/pytest-cache-files-szl83brb/': Permission denied
warning: could not open directory 'CS2/Ch06/Driveing_cost_project_FA_2025/tests/.pytest_cache/': Permission denied
```

## Likely cause

- These warnings appear to be filesystem permission issues, not tracked-file changes.
- Two warnings point to temporary pytest cache directories under this lesson folder.
- One warning points to a different project elsewhere in the same repository.

## Why this does not block the lesson work

- `git status` still reports: `nothing to commit, working tree clean`
- The lesson files merged into `main` successfully.
- The warnings do not indicate merge conflicts or modified tracked files.

## Suggested cleanup later

1. Check ownership and permissions on the two `pytest-cache-files-*` directories under this project.
2. Check permissions on `CS2/Ch06/Driveing_cost_project_FA_2025/tests/.pytest_cache/`.
3. Remove stale pytest cache/temp directories if they are safe to delete.
4. Re-run `git status` from the repository after cleanup to confirm the warnings are gone.

## Working directory when captured

`C:\Users\evertj\git\SwosuCsPythonExamples\CS1_CS2\Ch15\Claude_Plotting`
