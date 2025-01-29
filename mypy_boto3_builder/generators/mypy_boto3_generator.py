"""
Generator for mypy-boto3 package.

Copyright 2025 Vlad Emelianov
"""

from typing import NoReturn

from mypy_boto3_builder.constants import TemplatePath
from mypy_boto3_builder.exceptions import AlreadyPublishedError
from mypy_boto3_builder.generators.base_generator import BaseGenerator
from mypy_boto3_builder.package_data import Boto3StubsPackageData, MypyBoto3PackageData
from mypy_boto3_builder.parsers.mypy_boto3_package import parse_mypy_boto3_package
from mypy_boto3_builder.structures.packages.mypy_boto3_package import MypyBoto3Package
from mypy_boto3_builder.structures.packages.service_package import ServicePackage


class MypyBoto3Generator(BaseGenerator):
    """
    Generator for mypy-boto3 package.
    """

    service_package_data = Boto3StubsPackageData()

    def generate_stubs(self) -> MypyBoto3Package | None:
        """
        Generate main stubs.
        """
        package_data = MypyBoto3PackageData()
        try:
            version = self._get_package_build_version(package_data.pypi_name)
        except AlreadyPublishedError:
            return None

        self._log_generate(package_data.pypi_name, version)
        package = parse_mypy_boto3_package(service_names=self.main_service_names, version=version)
        self.package_writer.write_package(
            package,
            template_path=TemplatePath.mypy_boto3,
        )
        return package

    def generate_stubs_lite(self) -> NoReturn:
        """
        Not implemented.
        """
        raise NotImplementedError("Should never be called")

    def generate_full_stubs(self) -> NoReturn:
        """
        Not implemented.
        """
        raise NotImplementedError("Should never be called")

    def generate_custom_stubs(self) -> NoReturn:
        """
        Not implemented.
        """
        raise NotImplementedError("Should never be called")

    def generate_docs(self) -> None:
        """
        Not implemented.
        """
        raise NotImplementedError("Should never be called")

    def _get_postprocessor(self, service_package: ServicePackage) -> NoReturn:
        """
        Not implemented.
        """
        raise NotImplementedError("Should never be called")
