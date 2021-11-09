"""
Parent class for all package structures.
"""
from mypy_boto3_builder.logger import get_logger


class Package:
    """
    Parent class for all package structures.
    """

    def __init__(self, name: str, pypi_name: str) -> None:
        self.name = name
        self.pypi_name = pypi_name
        self.version = "0.0.0"
        self.logger = get_logger()
