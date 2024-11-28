"""
Generator for boto3-stubs packages.

Copyright 2024 Vlad Emelianov
"""

from pathlib import Path

from mypy_boto3_builder.constants import (
    StaticStubsPath,
    StaticStubsPullURL,
    TemplatePath,
)
from mypy_boto3_builder.exceptions import AlreadyPublishedError
from mypy_boto3_builder.generators.base_generator import BaseGenerator
from mypy_boto3_builder.package_data import (
    Boto3StubsFullPackageData,
    Boto3StubsLitePackageData,
    Boto3StubsPackageData,
    MypyBoto3PackageData,
)
from mypy_boto3_builder.postprocessors.botocore import BotocorePostprocessor
from mypy_boto3_builder.structures.mypy_boto3_package import MypyBoto3Package
from mypy_boto3_builder.structures.package import Package
from mypy_boto3_builder.structures.service_package import ServicePackage
from mypy_boto3_builder.structures.types_boto3_package import TypesBoto3Package
from mypy_boto3_builder.writers.processors import (
    process_mypy_boto3,
    process_types_boto3,
    process_types_boto3_docs,
    process_types_boto3_full,
    process_types_boto3_lite,
)


class Boto3Generator(BaseGenerator):
    """
    Generator for boto3-stubs packages.
    """

    service_package_data = Boto3StubsPackageData
    service_template_path = TemplatePath.types_boto3_service

    def _get_postprocessor(self, service_package: ServicePackage) -> BotocorePostprocessor:
        """
        Get postprocessor for service package.
        """
        return BotocorePostprocessor(service_package, self.main_service_names)

    def _generate_mypy_boto3(self) -> MypyBoto3Package | None:
        """
        Generate `mypy-boto3` package.
        """
        package_data = MypyBoto3PackageData
        try:
            version = self._get_package_version(package_data.PYPI_NAME, self.version)
        except AlreadyPublishedError:
            self.logger.info(f"Skipping {package_data.PYPI_NAME} {self.version}, already on PyPI")
            return None

        self.logger.info(f"Generating {package_data.PYPI_NAME} {version}")
        return process_mypy_boto3(
            output_path=self.output_path,
            service_names=self.main_service_names,
            version=version,
            generate_package=self.is_package(),
        )

    def _get_static_files_path(self) -> Path:
        return self._get_or_download_static_files_path(
            StaticStubsPath.types_boto3,
            StaticStubsPullURL.types_boto3,
        )

    def _generate_stubs(self) -> TypesBoto3Package | None:
        package_data = Boto3StubsPackageData
        try:
            version = self._get_package_version(package_data.PYPI_NAME, self.version)
        except AlreadyPublishedError:
            self.logger.info(f"Skipping {package_data.PYPI_NAME} {self.version}, already on PyPI")
            return None

        self.logger.info(f"Generating {package_data.PYPI_NAME} {version}")
        return process_types_boto3(
            output_path=self.output_path,
            service_names=self.main_service_names,
            generate_package=self.is_package(),
            package_data=package_data,
            version=version,
            static_files_path=self._get_static_files_path(),
        )

    def _generate_stubs_lite(self) -> TypesBoto3Package | None:
        package_data = Boto3StubsLitePackageData
        try:
            version = self._get_package_version(package_data.PYPI_NAME, self.version)
        except AlreadyPublishedError:
            self.logger.info(f"Skipping {package_data.PYPI_NAME} {self.version}, already on PyPI")
            return None

        self.logger.info(f"Generating {package_data.PYPI_NAME} {version}")
        return process_types_boto3_lite(
            output_path=self.output_path,
            service_names=self.main_service_names,
            generate_package=self.is_package(),
            package_data=package_data,
            version=version,
            static_files_path=self._get_static_files_path(),
        )

    def generate_stubs(self) -> list[Package]:
        """
        Generate `boto3-stubs` package.
        """
        result: list[Package] = []
        package: Package | None = None

        package = self._generate_stubs()
        if package:
            result.append(package)

        if not self.is_package():
            package = self._generate_mypy_boto3()
            if package:
                result.append(package)

        return result

    def generate_stubs_lite(self) -> list[Package]:
        """
        Generate `boto3-stubs-lite` package.
        """
        package = self._generate_stubs_lite()
        if package:
            return [package]
        return []

    def generate_docs(self) -> None:
        """
        Generate service and docs.
        """
        package_data = Boto3StubsPackageData
        total_str = f"{len(self.service_names)}"

        self.logger.info(f"Generating {package_data.NAME} module docs")
        process_types_boto3_docs(
            output_path=self.output_path,
            service_names=self.service_names,
            package_data=package_data,
            version=self.version,
        )

        for index, service_name in enumerate(self.service_names):
            current_str = f"{{:0{len(total_str)}}}".format(index + 1)
            package_name = package_data.get_service_package_name(service_name)
            self.logger.info(f"[{current_str}/{total_str}] Generating {package_name} module docs")
            self._process_service_docs(
                service_name=service_name,
                package_data=package_data,
                templates_path=TemplatePath.types_boto3_service_docs,
                version=self.version,
            )

    def generate_full_stubs(self) -> list[Package]:
        """
        Generate `boto3-stubs-full` package.
        """
        package_data = Boto3StubsFullPackageData
        try:
            version = self._get_package_version(package_data.PYPI_NAME, self.version)
        except AlreadyPublishedError:
            self.logger.info(f"Skipping {package_data.PYPI_NAME} {self.version}, already on PyPI")
            return []

        self.logger.info(f"Generating {package_data.PYPI_NAME} {version}")
        package = process_types_boto3_full(
            output_path=self.output_path,
            service_names=self.service_names,
            package_data=package_data,
            version=version,
            generate_package=self.is_package(),
        )
        self._generate_full_stubs_services(package)
        return [package]

    def generate_custom_stubs(self) -> list[Package]:
        """
        Do nothing.
        """
        return []
