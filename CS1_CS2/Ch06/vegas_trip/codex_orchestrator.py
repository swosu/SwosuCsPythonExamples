import json
import subprocess
from pathlib import Path

TASK_FILE = "codex_tasks.json"
TARGET_FILE = "vegas_trip_planner.py"
MAX_TASKS_PER_RUN = 1


def load_tasks():
    """Load task list from JSON."""
    with open(TASK_FILE, "r") as f:
        data = json.load(f)
    return data


def save_tasks(data):
    """Save updated task list."""
    with open(TASK_FILE, "w") as f:
        json.dump(data, f, indent=2)


def get_pending_tasks(data):
    """Return up to MAX_TASKS_PER_RUN tasks marked todo."""
    pending = [t for t in data["tasks"] if t["status"] == "todo"]
    return pending[:MAX_TASKS_PER_RUN]

def build_prompt(task):
    """Create prompt sent to Codex."""

    with open(TARGET_FILE, "r") as f:
        current_code = f.read()

    return f"""
You are editing an existing Python file.

TASK
{task['title']}

DESCRIPTION
{task['description']}

CURRENT FILE CONTENT
--------------------
{current_code}

STYLE RULES
-----------
- All function definitions must appear ABOVE the line:
  if __name__ == "__main__":
- Never place functions below main
- Avoid duplicate functions
- Keep imports at the top
- Follow clean Python style

INSTRUCTIONS
------------
Modify the program to complete the task.

Return the ENTIRE updated file.
Do not include markdown fences.
Return only Python code.
"""

def run_codex(prompt):
    """Execute Codex CLI with a prompt."""
    try:
        result = subprocess.run(
            ["codex", "exec", prompt],
            capture_output=True,
            text=True
        )

        return result.stdout

    except Exception as e:
        print("Codex execution failed:", e)
        return ""


def append_code(code):
    """Append generated code to the target file."""
    with open(TARGET_FILE, "a") as f:
        f.write("\n\n")
        f.write(code)


def execute_task(task):
    """Run a single task."""
    print("\n==============================")
    print("Executing Task:", task["id"])
    print(task["title"])
    print("------------------------------")

    prompt = build_prompt(task)

    print("Sending prompt to Codex...")
    generated_code = run_codex(prompt)

    print("\n--- Codex Output ---\n")
    print(generated_code)

    append_code(generated_code)

    print("\nCode appended to", TARGET_FILE)
    print("==============================\n")


def main():
    print("\nVegas Trip Planner Codex Builder")
    print("=================================\n")

    data = load_tasks()
    tasks = get_pending_tasks(data)

    if not tasks:
        print("No pending tasks found.")
        return

    print(f"Running {len(tasks)} tasks this session...\n")

    for task in tasks:
        execute_task(task)
        task["status"] = "done"

    save_tasks(data)

    print("\nRun complete.")
    print("Updated task file saved.")


if __name__ == "__main__":
    main()