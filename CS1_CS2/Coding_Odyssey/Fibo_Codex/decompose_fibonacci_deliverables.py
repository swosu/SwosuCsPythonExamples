#!/usr/bin/env python3
"""Decompose deliverables into an integrated task list with Codex.

This script:
1. Opens `fibonacci_exploration_deliverables.json`
2. Reads one deliverable at a time
3. Sends the deliverable and current task list to `codex exec`
4. Asks Codex to break the deliverable into tasks and merge them into the task list
5. Repeats until every deliverable has been processed
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict, List


DEFAULT_DELIVERABLES = "fibonacci_exploration_deliverables.json"
DEFAULT_TASK_LIST = "fibonacci_task_list.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Decompose Fibonacci deliverables into an integrated task list by calling Codex."
    )
    parser.add_argument(
        "--deliverables",
        default=DEFAULT_DELIVERABLES,
        help=f"Path to the deliverables JSON file. Default: {DEFAULT_DELIVERABLES}",
    )
    parser.add_argument(
        "--tasks",
        default=DEFAULT_TASK_LIST,
        help=f"Path to the evolving task-list JSON file. Default: {DEFAULT_TASK_LIST}",
    )
    parser.add_argument(
        "--codex-bin",
        default="codex",
        help="Codex CLI executable to invoke. Default: codex",
    )
    parser.add_argument(
        "--model",
        default=None,
        help="Optional Codex model override.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the prompts that would be sent to Codex without invoking it.",
    )
    return parser.parse_args()


def load_json_file(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_deliverables(path: Path) -> List[Dict[str, Any]]:
    data = load_json_file(path)
    if not isinstance(data, list):
        raise ValueError(f"Deliverables file must contain a JSON list: {path}")
    return data


def load_task_list(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        return []
    data = load_json_file(path)
    if not isinstance(data, list):
        raise ValueError(f"Task list file must contain a JSON list: {path}")
    return data


def save_task_list(path: Path, tasks: List[Dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        json.dump(tasks, handle, indent=2)
        handle.write("\n")


def build_prompt(deliverable: Dict[str, Any], current_tasks: List[Dict[str, Any]]) -> str:
    deliverable_json = json.dumps(deliverable, indent=2)
    current_tasks_json = json.dumps(current_tasks, indent=2)
    return f"""You are helping decompose a Fibonacci exploration project into actionable tasks.

Look at the deliverable below and then look at the current list of tasks.

Your job:
1. Review the deliverable.
2. Review the current list of tasks.
3. Break the deliverable apart into a concrete list of implementation or documentation tasks.
4. Integrate those new tasks into the existing task list.
5. Remove duplicates or near-duplicates.
6. Keep the list clear, ordered, and practical.

Return only a JSON object with a single key named `tasks`.
The value of `tasks` must be a JSON array of task objects.

Task object requirements:
- `id`: short kebab-case identifier
- `title`: short action-oriented title
- `description`: one or two sentence description
- `status`: use `pending`
- `source_deliverables`: list of deliverable ids that this task supports
- `dependencies`: list of task ids that should come first, or an empty list

Rules:
- Preserve useful existing tasks.
- Merge overlapping tasks instead of creating duplicates.
- Keep tasks small enough to complete independently.
- Keep responsibilities separated when naming tasks.
- Favor clean code, testing, file management, and documentation concerns where relevant.
- Do not include commentary outside the JSON object.

Deliverable:
{deliverable_json}

Current task list:
{current_tasks_json}
"""


def build_output_schema() -> Dict[str, Any]:
    return {
        "type": "object",
        "required": ["tasks"],
        "additionalProperties": False,
        "properties": {
            "tasks": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": [
                        "id",
                        "title",
                        "description",
                        "status",
                        "source_deliverables",
                        "dependencies",
                    ],
                    "additionalProperties": False,
                    "properties": {
                        "id": {"type": "string"},
                        "title": {"type": "string"},
                        "description": {"type": "string"},
                        "status": {"type": "string", "enum": ["pending"]},
                        "source_deliverables": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "dependencies": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                },
            }
        },
    }


def run_codex(
    codex_bin: str,
    prompt: str,
    schema_path: Path,
    output_path: Path,
    model: str | None,
    workdir: Path,
) -> List[Dict[str, Any]]:
    command = [
        codex_bin,
        "exec",
        "--skip-git-repo-check",
        "--sandbox",
        "read-only",
        "--color",
        "never",
        "--output-schema",
        str(schema_path),
        "--output-last-message",
        str(output_path),
        "-",
    ]

    if model:
        command.extend(["--model", model])

    completed = subprocess.run(
        command,
        input=prompt,
        text=True,
        cwd=workdir,
        capture_output=True,
        check=False,
    )

    if completed.returncode != 0:
        message = completed.stderr.strip() or completed.stdout.strip()
        raise RuntimeError(f"Codex exec failed with code {completed.returncode}: {message}")

    result = load_json_file(output_path)

    if not isinstance(result, dict):
        raise RuntimeError("Codex output must be a JSON object.")

    tasks = result.get("tasks")
    if not isinstance(tasks, list):
        raise RuntimeError("Codex output must contain a 'tasks' list.")

    return tasks


def process_deliverables(
    deliverables: List[Dict[str, Any]],
    tasks_path: Path,
    codex_bin: str,
    model: str | None,
    dry_run: bool,
    workdir: Path,
) -> None:
    current_tasks = load_task_list(tasks_path)

    with tempfile.TemporaryDirectory() as tmp_dir_name:
        tmp_dir = Path(tmp_dir_name)
        schema_path = tmp_dir / "task_list_schema.json"
        schema_path.write_text(json.dumps(build_output_schema(), indent=2), encoding="utf-8")

        for index, deliverable in enumerate(deliverables, start=1):
            prompt = build_prompt(deliverable, current_tasks)

            if dry_run:
                print(f"\n--- Deliverable {index}: {deliverable.get('id', 'unknown')} ---\n")
                print(prompt)
                continue

            output_path = tmp_dir / f"codex_output_{index}.json"
            current_tasks = run_codex(
                codex_bin=codex_bin,
                prompt=prompt,
                schema_path=schema_path,
                output_path=output_path,
                model=model,
                workdir=workdir,
            )
            save_task_list(tasks_path, current_tasks)
            print(
                f"Processed deliverable {index}/{len(deliverables)}: "
                f"{deliverable.get('id', 'unknown')} -> {tasks_path.name}"
            )


def main() -> int:
    args = parse_args()
    workdir = Path.cwd()
    deliverables_path = Path(args.deliverables)
    tasks_path = Path(args.tasks)

    if not deliverables_path.exists():
        print(f"Deliverables file not found: {deliverables_path}", file=sys.stderr)
        return 1

    try:
        deliverables = load_deliverables(deliverables_path)
        process_deliverables(
            deliverables=deliverables,
            tasks_path=tasks_path,
            codex_bin=args.codex_bin,
            model=args.model,
            dry_run=args.dry_run,
            workdir=workdir,
        )
    except (ValueError, RuntimeError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
