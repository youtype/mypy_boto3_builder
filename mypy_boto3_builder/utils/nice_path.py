"""
Path that represents it as relative to workdir.
"""
from collections.abc import Iterable, Iterator
from pathlib import Path


class NicePath(type(Path())):  # type: ignore
    """
    Path that represents it as relative to workdir.
    """

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

    def walk(self, exclude: Iterable[Path] = tuple(), glob_pattern: str = "**/*") -> Iterator[Path]:
        """
        Walk files except for `exclude`.

        Yields:
            Existing Path.
        """
        exclude_strs = {NicePath(i).as_posix() for i in exclude}
        for path in self.glob(glob_pattern):
            if not path.is_file():
                continue

            if path.as_posix() in exclude_strs:
                continue

            yield path
