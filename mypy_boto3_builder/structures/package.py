"""
Parent class for all package structures.
"""


class Package:
    """
    Parent class for all package structures.
    """

    def __init__(self, name: str, pypi_name: str):
        self.name = name
        self.pypi_name = pypi_name
