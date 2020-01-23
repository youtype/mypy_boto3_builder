"""
Parent class for all package structures.
"""

from dataclasses import dataclass


@dataclass
class Package:
    """
    Parent class for all package structures.
    """

    name: str
    pypi_name: str
