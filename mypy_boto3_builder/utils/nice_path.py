"""
Path that represents it as relative to workdir.
"""
from collections.abc import Iterable, Iterator
from pathlib import Path
from typing import TypeVar

_R = TypeVar("_R", bound=Path)


class NicePath(Path):
    """
    Path that represents it as relative to workdir.
    """

    _flavour = type(Path())._flavour  # type: ignore

    def __str__(self) -> str:
        path = Path(self)
        if self.is_absolute():
            cwd = self.cwd()
            if path == cwd or path.parts <= cwd.parts:
                return str(path)

            try:
                path = Path(self).relative_to(cwd)
            except ValueError:
                return str(path)

        if len(path.parts) == 1:
            return f"./{path}"

        return str(path)

    def walk(
        self: _R, exclude: Iterable[Path] = tuple(), glob_pattern: str = "**/*"
    ) -> Iterator[_R]:
        """
        Walk files except for `exclude`.

        Yields:
            Existing Path.
        """
        exclude_strs = {self.__class__(i).as_posix() for i in exclude}
        for path in self.glob(glob_pattern):
            if not path.is_file():
                continue

            if path.as_posix() in exclude_strs:
                continue

            yield self.__class__(path)
