import json
import subprocess
import difflib
import sys
from pathlib import Path

TASK_FILE = "codex_refactor_vegas_trip_tasks.json"
SOURCE_FILE = "starter_wall_of_code_vegas_trip_planner.py"

MAX_TASKS_PER_RUN = 2
MAX_RETRIES = 3


# ---------------------------------------------------------
# Task Utilities
# ---------------------------------------------------------

def load_tasks():
    with open(TASK_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def get_pending_tasks(tasks):
    pending = [t for t in tasks if t.get("status", "todo") == "todo"]
    return pending[:MAX_TASKS_PER_RUN]


# ---------------------------------------------------------
# File Utilities
# ---------------------------------------------------------

def read_source_code():
    return Path(SOURCE_FILE).read_text()


def snapshot_project():
    files = {}
    for path in Path(".").glob("*.py"):
        files[path.name] = path.read_text()
    return files


# ---------------------------------------------------------
# Prompt Builder
# ---------------------------------------------------------

def build_prompt(task, source_code):

    return f"""
You are acting as a senior Python software engineer performing a controlled refactor.

PROJECT GOAL
------------
Refactor a single "wall of code" Python program into a clean modular architecture.

SOURCE FILE
-----------
starter_wall_of_code_vegas_trip_planner.py

SOURCE CODE
-----------
{source_code}

CURRENT TASK
------------
{task['title']}

TASK DESCRIPTION
----------------
{task['description']}

EXPECTED RESULT
---------------
{task.get('expected_output', '')}

ARCHITECTURE RULES
------------------
The final project structure should evolve toward:

main.py
trip_greeting.py
trip_inputs.py
transportation_inputs.py
budget_inputs.py
trip_calculations.py
trip_summary.py
tests/

CODING RULES
------------
1. Do NOT rewrite logic unless required.
2. Only reorganize and modularize code.
3. Preserve function names and behavior.
4. Use meaningful module names.
5. main.py must orchestrate the program.
6. Modules should contain logically grouped functions.

STYLE RULES
-----------
• imports at top
• functions above main guard
• clear docstrings
• readable structure

OUTPUT FORMAT
-------------
Return ONLY the files that need to change.

Use this format:

FILE: filename.py
<file contents>

Do not include markdown.
"""


# ---------------------------------------------------------
# Codex Execution
# ---------------------------------------------------------

def run_codex(prompt):

    result = subprocess.run(
        ["codex", "exec", prompt],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr)

    return result.stdout


# ---------------------------------------------------------
# Apply Codex Output
# ---------------------------------------------------------

def apply_changes(output):

    current_file = None
    buffer = []

    for line in output.splitlines():

        if line.startswith("FILE:"):
            if current_file:
                Path(current_file).write_text("\n".join(buffer))
                buffer = []

            current_file = line.replace("FILE:", "").strip()

        else:
            buffer.append(line)

    if current_file:
        Path(current_file).write_text("\n".join(buffer))


# ---------------------------------------------------------
# Git helpers
# ---------------------------------------------------------

def git_commit(task_id):

    subprocess.run(["git", "add", "."])

    subprocess.run([
        "git",
        "commit",
        "-m",
        f"Codex refactor task {task_id}"
    ])


# ---------------------------------------------------------
# Task Execution
# ---------------------------------------------------------

def execute_task(task):

    print("\n===================================")
    print("Running:", task["id"], "-", task["title"])
    print("===================================\n")

    source_code = read_source_code()

    prompt = build_prompt(task, source_code)

    retries = 0

    while retries < MAX_RETRIES:

        try:

            output = run_codex(prompt)

            apply_changes(output)

            subprocess.run([sys.executable, "-m", "py_compile", SOURCE_FILE])

            git_commit(task["id"])

            print("✅ Task completed\n")

            return True

        except Exception as e:

            print("Codex error:", e)
            retries += 1

    return False


# ---------------------------------------------------------
# Main Loop
# ---------------------------------------------------------

def main():

    print("\n===================================")
    print(" Codex Refactor Orchestrator ")
    print("===================================\n")

    tasks = load_tasks()

    pending = get_pending_tasks(tasks)

    if not pending:
        print("No tasks remaining.")
        return

    print(f"{len(pending)} tasks scheduled this run\n")

    for task in pending:

        success = execute_task(task)

        if success:
            task["status"] = "done"
        else:
            task["status"] = "failed"

        save_tasks(tasks)

    print("\nRun complete\n")


if __name__ == "__main__":
    main()
