#!/usr/bin/env python
# /// script
# requires-python = ">=3.12"
# ///
"""
CI-related stuff.

Copyright 2024 Vlad Emelianov
"""

from __future__ import annotations

import argparse
import datetime
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

ROOT_PATH = Path(__file__).resolve().parent.parent
WORKFLOW_PATH = ROOT_PATH / ".github" / "workflows"
TEST_PATH_NAMES = ["integration"]


def get_now() -> datetime.datetime:
    """
    Get current time.
    """
    return datetime.datetime.now(datetime.timezone.utc)


@dataclass
class Workflow:
    """
    GitHub workflow.
    """

    name: str
    status: str
    path: Path
    conclusion: str = ""
    branch: str = "-"
    started_at: datetime.datetime | None = None
    updated_at: datetime.datetime | None = None

    @property
    def check(self) -> str:
        """
        Checkmark.
        """
        if self.status == "completed":
            return "✅" if self.conclusion == "success" else "❌"
        if self.status == "in_progress":
            return "🕒"
        if self.status == "queued":
            return "🔄"
        if self.status == "failure":
            return "❌"
        if self.status == "new":
            return "🆕"
        return self.status

    @property
    def updated_ago(self) -> str:
        """
        Time since last update.
        """
        if self.started_at is None:
            return "never"
        delta = get_now() - self.started_at
        if delta.days:
            return f"{delta.days} day{'s' if delta.days > 1 else '' } ago"
        if delta.seconds > 60 * 60:
            hours = delta.seconds // 60 // 60
            return f"{hours} hour{'s' if hours > 1 else '' } ago"
        if delta.seconds > 60:  # noqa: PLR2004
            minutes = delta.seconds // 60
            return f"{minutes} minute{'s' if minutes > 1 else '' } ago"
        if delta.seconds > 5:  # noqa: PLR2004
            return f"{delta.seconds} seconds ago"

        return "just now"

    @property
    def duration(self) -> str:
        """
        Duration.
        """
        if self.started_at is None or self.updated_at is None:
            return "00:00"
        delta = self.updated_at - self.started_at
        if self.status not in {"completed", "failure"}:
            delta = get_now() - self.started_at
        minutes = delta.seconds // 60
        return f"{minutes:>02}:{delta.seconds % 60:>02}"

    def __str__(self) -> str:
        """
        Represent as string.
        """
        return (
            f"{self.check} {self.name:<30} {self.updated_ago:<15} {self.duration:<8} {self.branch}"
        )


@dataclass
class CLINamespace:
    """
    CLI namespace.
    """

    command: str


def parse_args() -> CLINamespace:
    """
    Parse CLI arguments.
    """
    parser = argparse.ArgumentParser(__file__)
    parser.add_argument(
        "command",
        choices=("list", "integration", "sanity"),
        default="list",
        nargs="?",
    )
    args = parser.parse_args()
    return CLINamespace(
        command=args.command,
    )


def get_workflow_paths() -> tuple[Path, ...]:
    """
    Get existing workflow paths.
    """
    result: list[Path] = []
    for path in WORKFLOW_PATH.iterdir():
        if path.suffix != ".yml":
            continue
        result.append(path.relative_to(ROOT_PATH))

    return tuple(sorted(result))


def filter_paths(paths: Sequence[Path], name_parts: Sequence[str]) -> tuple[Path, ...]:
    """
    Get existing test paths.
    """
    return tuple(path for path in paths if any(name_part in path.name for name_part in name_parts))


def run_gh(cmd: Sequence[str]) -> str:
    """
    Run `gh` command.
    """
    return subprocess.check_output(
        ["gh", *cmd],  # noqa: S607
        stderr=subprocess.STDOUT,
        encoding="utf8",
    )


def get_workflows(paths: Sequence[Path]) -> list[Workflow]:
    """
    Get existing workflows.
    """
    with ThreadPoolExecutor() as executor:
        workflows = list(executor.map(get_workflow, paths))

    result = [workflow for workflow in workflows if workflow is not None]
    return sorted(result, key=lambda x: x.name)


def get_workflow_name(path: Path) -> str:
    """
    Get workflow name.
    """
    data = path.read_text()
    for line in data.splitlines():
        if line.startswith("name:"):
            return line.split(":", 1)[1].strip().replace('"', "")

    raise ValueError(f"Workflow name not found in {path}")


def get_workflow(path: Path) -> Workflow | None:
    """
    Get existing workflow paths.
    """
    try:
        response = run_gh(
            [
                "run",
                "list",
                "--workflow",
                path.as_posix(),
                "--json",
                "name",
                "--json",
                "status",
                "--json",
                "conclusion",
                "--json",
                "startedAt",
                "--json",
                "updatedAt",
                "--json",
                "headBranch",
                "--json",
                "name",
                "--limit",
                "1",
            ]
        )
    except subprocess.CalledProcessError:
        sys.stderr.write(f"Failed to get workflow {path}\n")
        return None
    response_json = json.loads(response)
    if not response_json:
        return Workflow(
            name=get_workflow_name(path),
            status="new",
            path=path,
        )
    data = response_json[0]
    return Workflow(
        name=get_workflow_name(path),
        status=data["status"],
        conclusion=data["conclusion"],
        started_at=datetime.datetime.fromisoformat(data["startedAt"]),
        updated_at=datetime.datetime.fromisoformat(data["updatedAt"]),
        branch=data["headBranch"],
        path=path,
    )


def run_workflow(path: Path) -> None:
    """
    Run workflow.
    """
    run_gh(["workflow", "run", path.as_posix()])


def run_workflows(paths: Sequence[Path]) -> None:
    """
    Run test workflows.
    """
    with ThreadPoolExecutor() as executor:
        list(executor.map(run_workflow, paths))


def main() -> None:
    """
    Run main entrypoint.
    """
    args = parse_args()
    paths = get_workflow_paths()
    if args.command == "integration":
        paths = filter_paths(paths, ["integration"])
        run_workflows(paths)
    if args.command == "sanity":
        paths = filter_paths(paths, ["sanity"])
        run_workflows(paths)

    workflows = get_workflows(paths)
    for workflow in workflows:
        sys.stdout.write(f"{workflow}\n")


if __name__ == "__main__":
    main()
