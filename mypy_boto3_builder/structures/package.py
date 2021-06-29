"""
Parent class for all package structures.
"""
import logging

from mypy_boto3_builder.constants import LOGGER_NAME


class Package:
    """
    Parent class for all package structures.
    """

    def __init__(self, name: str, pypi_name: str):
        self.name = name
        self.pypi_name = pypi_name
        self.logger = logging.getLogger(LOGGER_NAME)
