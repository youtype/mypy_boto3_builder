"""
Package links structure.

Copyright 2024 Vlad Emelianov
"""

from mypy_boto3_builder.package_data import BasePackageData
from mypy_boto3_builder.utils.strings import get_pypi_link


class PackageURL:
    """
    Package links structure.
    """

    def __init__(self, pypi_name: str, data: BasePackageData) -> None:
        self.pypi_name = pypi_name
        self.data = data

    @property
    def pypi_badge(self) -> str:
        """
        Package name badge from shields.io.
        """
        return f"https://img.shields.io/pypi/v/{self.pypi_name}.svg?color=blue"

    @property
    def pyversions_badge(self) -> str:
        """
        Package Python version badge from shields.io.
        """
        return f"https://img.shields.io/pypi/pyversions/{self.pypi_name}.svg?color=blue"

    @property
    def rtd_badge(self) -> str:
        """
        ReadTheDocs badge from shields.io.
        """
        return "https://img.shields.io/readthedocs/boto3-stubs.svg?color=blue"

    @property
    def pepy_badge(self) -> str:
        """
        PePy total downloads badge.
        """
        return f"https://static.pepy.tech/badge/{self.pypi_name}"

    @property
    def montly_downloads_badge(self) -> str:
        """
        PyPi monthly downloads badge.
        """
        return f"https://img.shields.io/pypi/dm/{self.pypi_name}?color=blue"

    @property
    def pypi(self) -> str:
        """
        Get link to PyPI.
        """
        return get_pypi_link(self.pypi_name)

    @property
    def library_pypi(self) -> str:
        """
        Get link to PyPI underlying library.
        """
        return get_pypi_link(self.data.get_library_name())

    @property
    def stubs_pypi(self) -> str:
        """
        Get link to PyPI lite version of stubs.
        """
        return get_pypi_link(self.data.pypi_stubs_name)

    @property
    def stubs_lite_pypi(self) -> str:
        """
        Get link to PyPI lite version of stubs.
        """
        return get_pypi_link(self.data.pypi_lite_name)

    @property
    def stubs_full_pypi(self) -> str:
        """
        Get link to PyPI full version of stubs.
        """
        return get_pypi_link(self.data.pypi_full_name)

    @property
    def pepy(self) -> str:
        """
        PePy project link.
        """
        return f"https://pepy.tech/project/{self.pypi_name}"

    @property
    def pypistats(self) -> str:
        """
        PePy project link.
        """
        return f"https://pypistats.org/packages/{self.pypi_name}"

    @property
    def docs(self) -> str:
        """
        Documentation link.
        """
        return self.data.local_doc_link
