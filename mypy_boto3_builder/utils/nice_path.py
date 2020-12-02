"""
Wrapper for path that represents it as relative to workdir.
"""
from pathlib import Path


class NicePath(type(Path())):
    """
    Wrapper for path that represents it as relative to workdir.

    Arguments:
        path -- Original path.
    """

    def __str__(self) -> str:
        path = Path(self)
        if self.is_absolute():
            cwd = self.cwd()
            if path == cwd or path.parts <= cwd.parts:
                return str(path)

            try:
                path = Path(self.relative_to(cwd))
            except ValueError:
                return str(path)

        if len(path.parts) == 1:
            return f"./{path}"

        return str(path)
