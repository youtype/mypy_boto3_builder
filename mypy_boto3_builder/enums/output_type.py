"""
Output type choice for CLI.

Copyright 2024 Vlad Emelianov
"""

from enum import Enum


class OutputType(Enum):
    """
    Output type choice for CLI.
    """

    package = "package"
    wheel = "wheel"
    sdist = "sdist"
    installed = "installed"

    def is_installed(self) -> bool:
        """
        Whether output type is a ready-to-use directory.
        """
        return self is OutputType.installed

    def is_packaged(self) -> bool:
        """
        Whether output type is packaged for installation.
        """
        return self is OutputType.wheel or self is OutputType.sdist

    def is_preserved(self) -> bool:
        """
        Check if output is preserved.
        """
        return not self.is_packaged()
