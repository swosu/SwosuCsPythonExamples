#!/usr/bin/env python3
"""Run Fibonacci tasks with Codex workers in dependency order.

This script reads `fibonacci_task_list.json`, schedules ready tasks, launches
independent Codex workers in parallel git worktrees, and merges completed
changes back into the main checkout.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Sequence, Set


DEFAULT_TASKS = "fibonacci_task_list.json"
DEFAULT_STATE = ".fibo_task_runner_state.json"
DEFAULT_ARTIFACTS = ".fibo_task_runner"


WORKER_OUTPUT_SCHEMA: Dict[str, Any] = {
    "type": "object",
    "required": ["status", "summary", "changed_files", "tests_ran", "blockers"],
    "additionalProperties": False,
    "properties": {
        "status": {
            "type": "string",
            "enum": ["completed", "blocked", "failed"],
        },
        "summary": {"type": "string"},
        "changed_files": {
            "type": "array",
            "items": {"type": "string"},
        },
        "tests_ran": {
            "type": "array",
            "items": {"type": "string"},
        },
        "blockers": {
            "type": "array",
            "items": {"type": "string"},
        },
    },
}


DELIVERABLE_RESOURCE_MAP = {
    "project-structure": {"repo-structure"},
    "instructional-markdown-outline": {"docs-main"},
    "recursive-strategy-unit": {"recursive-impl"},
    "iterative-strategy-unit": {"iterative-impl"},
    "shared-input-validation": {"validation-impl"},
    "strategy-abstraction": {"architecture"},
    "comparison-data-support": {"comparison-impl"},
    "big-o-analysis-content": {"docs-main"},
    "visualization-data-support": {"visualization-impl"},
    "markdown-visualizations": {"docs-main"},
    "design-decision-notes": {"docs-main"},
    "unit-test-suite": {"tests"},
    "testing-strategy-documentation": {"docs-main"},
    "clean-code-review-pass": {"review"},
    "final-fibonacci-exploration-document": {"docs-main"},
    "commit-plan": {"process"},
}


@dataclass
class RunningTask:
    task_id: str
    process: subprocess.Popen[str]
    worker_dir: Path
    project_dir: Path
    log_path: Path
    output_path: Path
    started_at: float
    log_handle: Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Schedule Fibonacci tasks across as many Codex workers as dependency "
            "and file-safety heuristics allow."
        )
    )
    parser.add_argument(
        "--tasks",
        default=DEFAULT_TASKS,
        help=f"Task list JSON to execute. Default: {DEFAULT_TASKS}",
    )
    parser.add_argument(
        "--state",
        default=DEFAULT_STATE,
        help=f"Runner state file. Default: {DEFAULT_STATE}",
    )
    parser.add_argument(
        "--artifacts-dir",
        default=DEFAULT_ARTIFACTS,
        help=f"Directory for logs, schemas, patches, and worktrees. Default: {DEFAULT_ARTIFACTS}",
    )
    parser.add_argument(
        "--codex-bin",
        default="codex",
        help="Codex CLI executable. Default: codex",
    )
    parser.add_argument(
        "--model",
        default=None,
        help="Optional Codex model override.",
    )
    parser.add_argument(
        "--max-workers",
        type=int,
        default=max(1, min(4, (os.cpu_count() or 2))),
        help="Maximum parallel Codex workers. Default: min(4, CPU count)",
    )
    parser.add_argument(
        "--poll-interval",
        type=float,
        default=2.0,
        help="Seconds between scheduler polls. Default: 2.0",
    )
    parser.add_argument(
        "--keep-worktrees",
        action="store_true",
        help="Do not delete worker worktrees after completion.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the execution order that would be used without launching Codex.",
    )
    return parser.parse_args()


def resolve_cli_path(raw_path: str, *, base_dir: Path) -> Path:
    path = Path(raw_path)
    if path.is_absolute():
        return path
    return (base_dir / path).resolve()


def load_json_file(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def save_json_file(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")


def run_command(
    command: Sequence[str],
    *,
    cwd: Path,
    capture_output: bool = True,
    check: bool = True,
) -> subprocess.CompletedProcess[str]:
    completed = subprocess.run(
        list(command),
        cwd=cwd,
        text=True,
        capture_output=capture_output,
        check=False,
    )
    if check and completed.returncode != 0:
        message = completed.stderr.strip() or completed.stdout.strip()
        raise RuntimeError(f"Command failed ({completed.returncode}): {' '.join(command)}\n{message}")
    return completed


def discover_repo_root(start_dir: Path) -> Path:
    result = run_command(["git", "rev-parse", "--show-toplevel"], cwd=start_dir)
    return Path(result.stdout.strip())


def load_tasks(path: Path) -> List[Dict[str, Any]]:
    data = load_json_file(path)
    if not isinstance(data, list):
        raise ValueError(f"Task list must be a JSON list: {path}")
    return data


def validate_tasks(tasks: Sequence[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    tasks_by_id: Dict[str, Dict[str, Any]] = {}
    for task in tasks:
        task_id = task.get("id")
        if not isinstance(task_id, str) or not task_id:
            raise ValueError("Every task must have a non-empty string 'id'.")
        if task_id in tasks_by_id:
            raise ValueError(f"Duplicate task id: {task_id}")
        tasks_by_id[task_id] = task

    for task in tasks:
        for dependency in task.get("dependencies", []):
            if dependency not in tasks_by_id:
                raise ValueError(
                    f"Task {task['id']} references missing dependency: {dependency}"
                )

    visiting: Set[str] = set()
    visited: Set[str] = set()

    def visit(task_id: str) -> None:
        if task_id in visited:
            return
        if task_id in visiting:
            raise ValueError(f"Dependency cycle detected at task: {task_id}")
        visiting.add(task_id)
        for dependency in tasks_by_id[task_id].get("dependencies", []):
            visit(dependency)
        visiting.remove(task_id)
        visited.add(task_id)

    for task_id in tasks_by_id:
        visit(task_id)

    return tasks_by_id


def build_children_map(tasks_by_id: Dict[str, Dict[str, Any]]) -> Dict[str, List[str]]:
    children = {task_id: [] for task_id in tasks_by_id}
    for task_id, task in tasks_by_id.items():
        for dependency in task.get("dependencies", []):
            children[dependency].append(task_id)
    return children


def compute_longest_path_scores(
    tasks_by_id: Dict[str, Dict[str, Any]]
) -> Dict[str, int]:
    children = build_children_map(tasks_by_id)
    memo: Dict[str, int] = {}

    def score(task_id: str) -> int:
        if task_id in memo:
            return memo[task_id]
        if not children[task_id]:
            memo[task_id] = 1
            return 1
        memo[task_id] = 1 + max(score(child_id) for child_id in children[task_id])
        return memo[task_id]

    for task_id in tasks_by_id:
        score(task_id)
    return memo


def initialize_state(tasks: Sequence[Dict[str, Any]], state_path: Path) -> Dict[str, Any]:
    if state_path.exists():
        state = load_json_file(state_path)
        if not isinstance(state, dict):
            raise ValueError(f"Runner state must be a JSON object: {state_path}")
    else:
        state = {
            "created_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
            "tasks": {},
        }

    task_states = state.setdefault("tasks", {})
    if not isinstance(task_states, dict):
        raise ValueError(f"State file has invalid 'tasks' object: {state_path}")

    for task in tasks:
        entry = task_states.setdefault(
            task["id"],
            {
                "status": task.get("status", "pending"),
                "attempts": 0,
                "history": [],
            },
        )
        if entry.get("status") == "running":
            entry["status"] = "pending"
            entry.setdefault("history", []).append(
                {
                    "event": "reset-after-restart",
                    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
                }
            )

    return state


def classify_resources(task: Dict[str, Any]) -> Set[str]:
    resources: Set[str] = set()
    task_id = task["id"]
    title = task.get("title", "").lower()
    source_deliverables = task.get("source_deliverables", [])

    for deliverable in source_deliverables:
        resources.update(DELIVERABLE_RESOURCE_MAP.get(deliverable, set()))

    if any(word in task_id for word in ["document-", "draft-", "outline-"]):
        resources.add("docs-main")

    if "recursive" in task_id and "docs-main" not in resources:
        resources.add("recursive-impl")
    if "iterative" in task_id and "docs-main" not in resources:
        resources.add("iterative-impl")
    if "validation" in task_id and "docs-main" not in resources:
        resources.add("validation-impl")
    if "comparison" in task_id and "docs-main" not in resources:
        resources.add("comparison-impl")
    if "visualization" in task_id and "docs-main" not in resources:
        resources.add("visualization-impl")

    if "test" in task_id or "test" in title:
        resources.add("tests")
    if "commit" in task_id or "commit" in title:
        resources.add("process")
    if "review" in task_id or "review" in title:
        resources.add("review")

    return resources or {"general"}


def collect_dependency_context(
    task: Dict[str, Any],
    tasks_by_id: Dict[str, Dict[str, Any]],
    state: Dict[str, Any],
) -> List[Dict[str, Any]]:
    details = []
    for dependency_id in task.get("dependencies", []):
        dependency_task = tasks_by_id[dependency_id]
        dependency_state = state["tasks"].get(dependency_id, {})
        details.append(
            {
                "id": dependency_id,
                "title": dependency_task.get("title", ""),
                "description": dependency_task.get("description", ""),
                "summary": dependency_state.get("summary", ""),
                "changed_files": dependency_state.get("applied_files", []),
            }
        )
    return details


def build_worker_prompt(
    task: Dict[str, Any],
    dependency_context: List[Dict[str, Any]],
    project_root: Path,
) -> str:
    task_json = json.dumps(task, indent=2)
    dependency_json = json.dumps(dependency_context, indent=2)
    project_root_text = str(project_root)
    return f"""You are working on a single scheduled task in the Fibonacci exploration project.

Project root:
{project_root_text}

Target task:
{task_json}

Completed dependency context:
{dependency_json}

Requirements:
1. Complete only the target task above.
2. Respect existing files and integrate with the current codebase instead of rewriting unrelated work.
3. Prefer the smallest correct set of edits that advances this task cleanly.
4. Run targeted verification when it is practical, and record what you ran.
5. Do not create commits.
6. If the task depends on information that is still missing in the repository, explain the blocker clearly.

Return only JSON that matches the provided schema.
"""


def ensure_schema_file(artifacts_dir: Path) -> Path:
    schema_path = artifacts_dir / "worker_output_schema.json"
    if not schema_path.exists():
        save_json_file(schema_path, WORKER_OUTPUT_SCHEMA)
    return schema_path


def mark_task_event(
    state: Dict[str, Any],
    task_id: str,
    *,
    status: str | None = None,
    **extra: Any,
) -> None:
    task_state = state["tasks"][task_id]
    if status is not None:
        task_state["status"] = status
    task_state.update(extra)
    task_state.setdefault("history", []).append(
        {
            "event": status or "update",
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
            **extra,
        }
    )


def create_worker_worktree(
    repo_root: Path,
    worktrees_dir: Path,
    task_id: str,
) -> Path:
    worker_dir = worktrees_dir / task_id
    if worker_dir.exists():
        shutil.rmtree(worker_dir)
    run_command(["git", "worktree", "add", "--detach", str(worker_dir), "HEAD"], cwd=repo_root)
    return worker_dir


def build_patch(worker_dir: Path, patch_path: Path) -> List[str]:
    changed_files_result = run_command(
        ["git", "diff", "--name-only", "HEAD", "--"],
        cwd=worker_dir,
    )
    changed_files = [line.strip() for line in changed_files_result.stdout.splitlines() if line.strip()]
    diff_result = run_command(
        ["git", "diff", "--binary", "HEAD", "--"],
        cwd=worker_dir,
    )
    patch_path.write_text(diff_result.stdout, encoding="utf-8")
    return changed_files


def apply_patch_to_main(repo_root: Path, patch_path: Path) -> None:
    if patch_path.stat().st_size == 0:
        return
    run_command(["git", "apply", "--3way", str(patch_path)], cwd=repo_root)


def finalize_task(
    *,
    running_task: RunningTask,
    repo_root: Path,
    artifacts_dir: Path,
    state: Dict[str, Any],
    keep_worktrees: bool,
) -> None:
    task_id = running_task.task_id
    running_task.log_handle.close()
    return_code = running_task.process.returncode

    if return_code != 0:
        mark_task_event(
            state,
            task_id,
            status="failed",
            summary=f"Codex exited with code {return_code}. See log for details.",
            blockers=[f"codex-exit-{return_code}"],
            finished_at=time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        )
        cleanup_worktree(repo_root, running_task.worker_dir, keep_worktrees)
        return

    if not running_task.output_path.exists():
        mark_task_event(
            state,
            task_id,
            status="failed",
            summary="Codex did not produce the expected structured output file.",
            blockers=["missing-worker-output"],
            finished_at=time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        )
        cleanup_worktree(repo_root, running_task.worker_dir, keep_worktrees)
        return

    try:
        worker_output = load_json_file(running_task.output_path)
    except json.JSONDecodeError as exc:
        mark_task_event(
            state,
            task_id,
            status="failed",
            summary=f"Worker output was not valid JSON: {exc}",
            blockers=["invalid-worker-output-json"],
            finished_at=time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        )
        cleanup_worktree(repo_root, running_task.worker_dir, keep_worktrees)
        return

    task_artifacts = artifacts_dir / "tasks" / task_id
    patch_path = task_artifacts / "changes.patch"
    patch_path.parent.mkdir(parents=True, exist_ok=True)

    final_status = worker_output.get("status", "failed")
    changed_files = build_patch(running_task.worker_dir, patch_path)
    applied_files: List[str] = []

    if final_status == "completed":
        try:
            apply_patch_to_main(repo_root, patch_path)
        except RuntimeError as exc:
            mark_task_event(
                state,
                task_id,
                status="failed",
                summary=str(exc),
                blockers=["patch-apply-failed"],
                changed_files=worker_output.get("changed_files", []),
                detected_changed_files=changed_files,
                finished_at=time.strftime("%Y-%m-%dT%H:%M:%S%z"),
            )
            cleanup_worktree(repo_root, running_task.worker_dir, keep_worktrees)
            return
        applied_files = changed_files

    mark_task_event(
        state,
        task_id,
        status=final_status,
        summary=worker_output.get("summary", ""),
        blockers=worker_output.get("blockers", []),
        tests_ran=worker_output.get("tests_ran", []),
        changed_files=worker_output.get("changed_files", []),
        detected_changed_files=changed_files,
        applied_files=applied_files,
        finished_at=time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        duration_seconds=round(time.time() - running_task.started_at, 2),
    )
    cleanup_worktree(repo_root, running_task.worker_dir, keep_worktrees)


def cleanup_worktree(repo_root: Path, worker_dir: Path, keep_worktrees: bool) -> None:
    if keep_worktrees:
        return
    if worker_dir.exists():
        run_command(["git", "worktree", "remove", "--force", str(worker_dir)], cwd=repo_root)


def runnable_tasks(
    tasks: Sequence[Dict[str, Any]],
    state: Dict[str, Any],
    locked_resources: Set[str],
) -> List[Dict[str, Any]]:
    ready = []
    for task in tasks:
        task_state = state["tasks"][task["id"]]
        if task_state.get("status") != "pending":
            continue
        if any(state["tasks"][dep]["status"] != "completed" for dep in task.get("dependencies", [])):
            continue
        resources = classify_resources(task)
        if resources & locked_resources:
            continue
        ready.append(task)
    return ready


def dry_run_schedule(
    tasks: Sequence[Dict[str, Any]],
    state: Dict[str, Any],
    longest_path_scores: Dict[str, int],
    max_workers: int,
) -> List[List[str]]:
    schedule: List[List[str]] = []
    simulated = json.loads(json.dumps(state))

    while True:
        batch: List[str] = []
        locked_resources: Set[str] = set()
        ready = sorted(
            runnable_tasks(tasks, simulated, locked_resources),
            key=lambda task: (-longest_path_scores[task["id"]], task["id"]),
        )
        if not ready:
            break

        for task in ready:
            resources = classify_resources(task)
            if resources & locked_resources:
                continue
            batch.append(task["id"])
            locked_resources.update(resources)
            simulated["tasks"][task["id"]]["status"] = "completed"
            if len(batch) >= max_workers:
                break

        if not batch:
            break
        schedule.append(batch)

    return schedule


def start_ready_tasks(
    *,
    tasks: Sequence[Dict[str, Any]],
    running: Dict[str, RunningTask],
    tasks_by_id: Dict[str, Dict[str, Any]],
    repo_root: Path,
    project_root: Path,
    project_relpath: Path,
    artifacts_dir: Path,
    state: Dict[str, Any],
    schema_path: Path,
    codex_bin: str,
    model: str | None,
    max_workers: int,
    longest_path_scores: Dict[str, int],
) -> None:
    locked_resources: Set[str] = set()
    for task_id in running:
        locked_resources.update(classify_resources(tasks_by_id[task_id]))

    ready = sorted(
        runnable_tasks(tasks, state, locked_resources),
        key=lambda task: (-longest_path_scores[task["id"]], task["id"]),
    )

    for task in ready:
        if len(running) >= max_workers:
            break
        resources = classify_resources(task)
        if resources & locked_resources:
            continue
        dependency_context = collect_dependency_context(task, tasks_by_id, state)
        running_task = launch_task_with_context(
            task=task,
            dependency_context=dependency_context,
            repo_root=repo_root,
            project_root=project_root,
            project_relpath=project_relpath,
            artifacts_dir=artifacts_dir,
            state=state,
            schema_path=schema_path,
            codex_bin=codex_bin,
            model=model,
        )
        running[task["id"]] = running_task
        locked_resources.update(resources)


def launch_task_with_context(
    *,
    task: Dict[str, Any],
    dependency_context: List[Dict[str, Any]],
    repo_root: Path,
    project_root: Path,
    project_relpath: Path,
    artifacts_dir: Path,
    state: Dict[str, Any],
    schema_path: Path,
    codex_bin: str,
    model: str | None,
) -> RunningTask:
    task_id = task["id"]
    task_artifacts = artifacts_dir / "tasks" / task_id
    logs_dir = task_artifacts / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)
    worktrees_dir = artifacts_dir / "worktrees"
    worktrees_dir.mkdir(parents=True, exist_ok=True)

    worker_dir = create_worker_worktree(repo_root, worktrees_dir, task_id)
    worker_project_dir = worker_dir / project_relpath
    output_path = task_artifacts / "worker_output.json"
    log_path = logs_dir / f"attempt_{state['tasks'][task_id]['attempts'] + 1}.log"
    prompt = build_worker_prompt(task, dependency_context, project_root)

    command = [
        codex_bin,
        "exec",
        "--full-auto",
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

    log_handle = log_path.open("w", encoding="utf-8")
    process = subprocess.Popen(
        command,
        cwd=worker_project_dir,
        stdin=subprocess.PIPE,
        stdout=log_handle,
        stderr=subprocess.STDOUT,
        text=True,
    )
    assert process.stdin is not None
    process.stdin.write(prompt)
    process.stdin.close()

    attempts = state["tasks"][task_id]["attempts"] + 1
    mark_task_event(
        state,
        task_id,
        status="running",
        attempts=attempts,
        resources=sorted(classify_resources(task)),
        log_path=str(log_path),
        worker_dir=str(worker_dir),
        output_path=str(output_path),
        started_at=time.strftime("%Y-%m-%dT%H:%M:%S%z"),
    )

    return RunningTask(
        task_id=task_id,
        process=process,
        worker_dir=worker_dir,
        project_dir=worker_project_dir,
        log_path=log_path,
        output_path=output_path,
        started_at=time.time(),
        log_handle=log_handle,
    )


def poll_running_tasks(
    *,
    running: Dict[str, RunningTask],
    tasks_by_id: Dict[str, Dict[str, Any]],
    repo_root: Path,
    artifacts_dir: Path,
    state: Dict[str, Any],
    keep_worktrees: bool,
) -> None:
    finished_ids = []
    for task_id, running_task in running.items():
        return_code = running_task.process.poll()
        if return_code is None:
            continue
        finished_ids.append(task_id)
        finalize_task(
            running_task=running_task,
            repo_root=repo_root,
            artifacts_dir=artifacts_dir,
            state=state,
            keep_worktrees=keep_worktrees,
        )

    for task_id in finished_ids:
        running.pop(task_id, None)


def summarize_state(state: Dict[str, Any]) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for task_state in state["tasks"].values():
        status = task_state.get("status", "pending")
        counts[status] = counts.get(status, 0) + 1
    return counts


def print_status_line(state: Dict[str, Any], running: Dict[str, RunningTask]) -> None:
    counts = summarize_state(state)
    summary = ", ".join(f"{name}={counts[name]}" for name in sorted(counts))
    running_text = ", ".join(sorted(running)) or "none"
    print(f"[scheduler] {summary} | running: {running_text}", flush=True)


def main() -> int:
    args = parse_args()
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent
    tasks_path = resolve_cli_path(args.tasks, base_dir=script_dir)
    state_path = resolve_cli_path(args.state, base_dir=script_dir)
    artifacts_dir = resolve_cli_path(args.artifacts_dir, base_dir=script_dir)
    repo_root = discover_repo_root(project_root)
    project_relpath = project_root.relative_to(repo_root)

    if not tasks_path.exists():
        print(f"Task list not found: {tasks_path}", file=sys.stderr)
        return 1

    tasks = load_tasks(tasks_path)
    tasks_by_id = validate_tasks(tasks)
    longest_path_scores = compute_longest_path_scores(tasks_by_id)
    state = initialize_state(tasks, state_path)
    schema_path = ensure_schema_file(artifacts_dir)

    if args.dry_run:
        schedule = dry_run_schedule(tasks, state, longest_path_scores, args.max_workers)
        for index, batch in enumerate(schedule, start=1):
            print(f"Wave {index}: {', '.join(batch)}")
        if not schedule:
            print("No runnable tasks found.")
        return 0

    running: Dict[str, RunningTask] = {}
    save_json_file(state_path, state)

    while True:
        start_ready_tasks(
            tasks=tasks,
            running=running,
            tasks_by_id=tasks_by_id,
            repo_root=repo_root,
            project_root=project_root,
            project_relpath=project_relpath,
            artifacts_dir=artifacts_dir,
            state=state,
            schema_path=schema_path,
            codex_bin=args.codex_bin,
            model=args.model,
            max_workers=args.max_workers,
            longest_path_scores=longest_path_scores,
        )
        save_json_file(state_path, state)
        print_status_line(state, running)

        if not running:
            remaining = [
                task["id"]
                for task in tasks
                if state["tasks"][task["id"]]["status"] == "pending"
            ]
            if not remaining:
                break
            blocked = [
                task_id
                for task_id in remaining
                if any(
                    state["tasks"][dependency]["status"] != "completed"
                    for dependency in tasks_by_id[task_id].get("dependencies", [])
                )
            ]
            if blocked:
                print(
                    "No runnable tasks remain. Pending tasks are blocked by unfinished dependencies:",
                    file=sys.stderr,
                )
                for task_id in blocked:
                    deps = tasks_by_id[task_id].get("dependencies", [])
                    unmet = [
                        dependency
                        for dependency in deps
                        if state["tasks"][dependency]["status"] != "completed"
                    ]
                    print(f"  - {task_id}: {', '.join(unmet)}", file=sys.stderr)
                return 2
            break

        time.sleep(args.poll_interval)
        poll_running_tasks(
            running=running,
            tasks_by_id=tasks_by_id,
            repo_root=repo_root,
            artifacts_dir=artifacts_dir,
            state=state,
            keep_worktrees=args.keep_worktrees,
        )
        save_json_file(state_path, state)

    final_counts = summarize_state(state)
    print("Run complete.")
    for status_name in sorted(final_counts):
        print(f"  {status_name}: {final_counts[status_name]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
