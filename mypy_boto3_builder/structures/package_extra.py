"""
Package extra entry.

Copyright 2024 Vlad Emelianov
"""

from typing import NamedTuple


class PackageExtra(NamedTuple):
    """
    Package extra entry.
    """

    name: str
    packages: tuple[str, ...]
    description: str = ""
