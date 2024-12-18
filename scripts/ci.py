#!/usr/bin/env python
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "python-dateutil",
# ]
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

from dateutil import relativedelta

ROOT_PATH = Path(__file__).resolve().parent.parent
WORKFLOW_PATH = ROOT_PATH / ".github" / "workflows"
TEST_PATH_NAMES = ["integration"]


@dataclass
class Workflow:
    """
    GitHub workflow.
    """

    name: str
    status: str
    started_at: datetime.datetime
    updated_at: datetime.datetime
    branch: str
    path: Path

    @property
    def check(self) -> str:
        """
        Checkmark.
        """
        if self.status == "completed":
            return "✅"
        if self.status == "in_progress":
            return "🕒"
        if self.status == "queued":
            return "🔄"
        if self.status == "failure":
            return "❌"
        return self.status

    @property
    def updated_ago(self) -> str:
        """
        Time since last update.
        """
        now = datetime.datetime.now(datetime.timezone.utc)
        delta = relativedelta.relativedelta(now, self.updated_at)
        if delta.months or delta.years:
            return "long time ago"
        if delta.days > 1:
            return f"{delta.days} days ago"
        if delta.hours > 1:
            return f"{delta.hours} hours ago"
        if delta.minutes > 1:
            return f"{delta.minutes} minutes ago"
        if delta.seconds > 1:
            return f"{delta.seconds} seconds ago"

        return "just now"

    @property
    def duration(self) -> str:
        """
        Duration.
        """
        delta = self.updated_at - self.started_at
        return f"{(delta.seconds // 60):>02}:{delta.seconds % 60:>02}"

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
        result.append(path.relative_to(WORKFLOW_PATH))

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


def get_workflow(path: Path) -> Workflow | None:
    """
    Get existing workflow paths.
    """
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
    response_json = json.loads(response)
    if not response_json:
        return None
    data = response_json[0]
    return Workflow(
        name=data["name"],
        status=data["status"],
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
        executor.map(run_workflow, paths)


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
