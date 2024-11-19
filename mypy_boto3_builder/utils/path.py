"""
Path utils.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Generator, Iterable
from pathlib import Path


def print_path(path: Path) -> str:
    """
    Get path as a string relative to current workdir.
    """
    if path.is_absolute():
        cwd = Path.cwd()
        if path == cwd or path.parts <= cwd.parts:
            return path.as_posix()

        try:
            path = path.relative_to(cwd)
        except ValueError:
            return str(path)

    if len(path.parts) == 1:
        return f"./{path.as_posix()}"

    return path.as_posix()


def walk_path(
    parent: Path,
    exclude: Iterable[Path] = (),
    glob_pattern: str = "**/*",
) -> Generator[Path, None, None]:
    """
    Walk files except for `exclude`.

    Yields:
        Existing Path.
    """
    exclude_strs = {Path(i).as_posix() for i in exclude}
    for path in parent.glob(glob_pattern):
        if not path.is_file():
            continue

        if path.as_posix() in exclude_strs:
            continue

        yield path
