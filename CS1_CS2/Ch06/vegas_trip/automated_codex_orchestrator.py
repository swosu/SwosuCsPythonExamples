import json
import subprocess
import difflib
import sys
from pathlib import Path

TASK_FILE = "codex_tasks.json"
TARGET_FILE = "vegas_trip_planner.py"

MAX_TASKS_PER_RUN = 5
MAX_RETRIES = 3


# ------------------------------------------------------------
# Utility Functions
# ------------------------------------------------------------

def load_tasks():
    with open(TASK_FILE, "r") as f:
        return json.load(f)


def save_tasks(data):
    with open(TASK_FILE, "w") as f:
        json.dump(data, f, indent=2)


def get_pending_tasks(data):
    pending = [t for t in data["tasks"] if t["status"] == "todo"]
    return pending[:MAX_TASKS_PER_RUN]


def read_current_code():
    path = Path(TARGET_FILE)

    if not path.exists():
        path.write_text("")

    return path.read_text()


def write_code(code):
    Path(TARGET_FILE).write_text(code)


# ------------------------------------------------------------
# Prompt Builder
# ------------------------------------------------------------

def build_prompt(task, current_code):

    return f"""
You are editing an existing Python file.

TASK
{task['title']}

DESCRIPTION
{task['description']}

CURRENT FILE
------------------------
{current_code}

STYLE RULES
-----------
1. All functions must appear ABOVE the main guard.
2. Never place functions below:

if __name__ == "__main__":

3. Avoid duplicate functions.
4. Keep imports at the top.
5. Maintain clean Python style.

FILE STRUCTURE
--------------
imports

helper functions

calculation functions

orchestrator functions

main()

if __name__ == "__main__":

INSTRUCTIONS
------------
Modify the file to complete the task.

Return the ENTIRE updated file.

Do not include markdown fences.
Return only Python code.
"""


# ------------------------------------------------------------
# Codex Runner
# ------------------------------------------------------------

def run_codex(prompt):

    result = subprocess.run(
        ["codex", "exec", prompt],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr)

    return result.stdout


# ------------------------------------------------------------
# Diff Viewer
# ------------------------------------------------------------

def show_diff(old, new):

    diff = difflib.unified_diff(
        old.splitlines(),
        new.splitlines(),
        fromfile="before",
        tofile="after",
        lineterm=""
    )

    print("\n===== CODE DIFF =====\n")

    for line in diff:
        print(line)


# ------------------------------------------------------------
# Code Validation
# ------------------------------------------------------------

def validate_python():

    result = subprocess.run(
        [sys.executable, "-m", "py_compile", TARGET_FILE],
        capture_output=True
    )

    if result.returncode != 0:
        print("\n❌ Syntax error detected")
        print(result.stderr.decode())
        return False

    print("\n✅ Syntax check passed")
    return True


# ------------------------------------------------------------
# Git Integration
# ------------------------------------------------------------

def git_commit(task_id):

    subprocess.run(["git", "add", TARGET_FILE])

    subprocess.run([
        "git",
        "commit",
        "-m",
        f"Codex task {task_id} completed"
    ])


def git_rollback():

    print("\n⚠ Rolling back last change...\n")

    subprocess.run([
        "git",
        "checkout",
        "--",
        TARGET_FILE
    ])


# ------------------------------------------------------------
# Task Executor
# ------------------------------------------------------------

def execute_task(task):

    print("\n======================================")
    print("Running Task:", task["id"])
    print(task["title"])
    print("======================================\n")

    retries = 0

    while retries < MAX_RETRIES:

        current_code = read_current_code()

        prompt = build_prompt(task, current_code)

        try:

            print("Sending prompt to Codex...\n")

            new_code = run_codex(prompt)

            show_diff(current_code, new_code)

            write_code(new_code)

            if validate_python():

                git_commit(task["id"])

                print("\n🎉 Task completed successfully\n")

                return True

            else:

                git_rollback()

        except Exception as e:

            print("\nCodex error:", e)

        retries += 1

        print(f"\nRetrying ({retries}/{MAX_RETRIES})...\n")

    print("\n❌ Task failed after retries\n")

    return False


# ------------------------------------------------------------
# Main Loop
# ------------------------------------------------------------

def main():

    print("\n======================================")
    print(" Automated Codex Orchestrator ")
    print("======================================\n")

    data = load_tasks()

    tasks = get_pending_tasks(data)

    if not tasks:
        print("No pending tasks.")
        return

    print(f"{len(tasks)} tasks scheduled this run\n")

    for task in tasks:

        success = execute_task(task)

        if success:
            task["status"] = "done"
        else:
            task["status"] = "failed"

        save_tasks(data)

    print("\nRun complete.\n")


# ------------------------------------------------------------

if __name__ == "__main__":
    main()
