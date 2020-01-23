"""
Wrapper for path that represents it as relative to workdir.
"""
from pathlib import Path


class NicePath:
    """
    Wrapper for path that represents it as relative to workdir.

    Arguments:
        path -- Original path.
    """

    def __init__(self, path: Path) -> None:
        self.path = path

    def __str__(self) -> str:
        path = self.path
        try:
            path = path.relative_to(Path.cwd())
        except ValueError:
            pass

        return path.as_posix()
