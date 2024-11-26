"""
Boto3 stubs/docs generator.

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
from mypy_boto3_builder.structures.boto3_stubs_package import Boto3StubsPackage
from mypy_boto3_builder.structures.master_package import MasterPackage
from mypy_boto3_builder.structures.package import Package
from mypy_boto3_builder.structures.service_package import ServicePackage
from mypy_boto3_builder.structures.wrapper_package import WrapperPackage
from mypy_boto3_builder.writers.processors import (
    process_boto3_stubs,
    process_boto3_stubs_docs,
    process_boto3_stubs_full,
    process_boto3_stubs_lite,
    process_master,
)


class Boto3Generator(BaseGenerator):
    """
    Boto3 stubs/docs generator.
    """

    service_package_data = Boto3StubsPackageData
    service_template_path = TemplatePath.boto3_stubs_service

    def get_postprocessor(self, service_package: ServicePackage) -> BotocorePostprocessor:
        """
        Get postprocessor for service package.
        """
        return BotocorePostprocessor(service_package, self.master_service_names)

    def _generate_master(self) -> MasterPackage | None:
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
        return process_master(
            output_path=self.output_path,
            service_names=self.master_service_names,
            version=version,
            generate_package=self.is_package(),
        )

    def _get_static_files_path(self) -> Path:
        return self._get_or_download_static_files_path(
            StaticStubsPath.boto3_stubs,
            StaticStubsPullURL.boto3_stubs,
        )

    def _generate_boto3_stubs(self) -> Boto3StubsPackage | None:
        package_data = Boto3StubsPackageData
        try:
            version = self._get_package_version(package_data.PYPI_NAME, self.version)
        except AlreadyPublishedError:
            self.logger.info(f"Skipping {package_data.PYPI_NAME} {self.version}, already on PyPI")
            return None

        self.logger.info(f"Generating {package_data.PYPI_NAME} {version}")
        return process_boto3_stubs(
            output_path=self.output_path,
            service_names=self.master_service_names,
            generate_package=self.is_package(),
            version=version,
            static_files_path=self._get_static_files_path(),
        )

    def _generate_boto3_stubs_lite(self) -> Boto3StubsPackage | None:
        package_data = Boto3StubsLitePackageData
        try:
            version = self._get_package_version(package_data.PYPI_NAME, self.version)
        except AlreadyPublishedError:
            self.logger.info(f"Skipping {package_data.PYPI_NAME} {self.version}, already on PyPI")
            return None

        self.logger.info(f"Generating {package_data.PYPI_NAME} {version}")
        return process_boto3_stubs_lite(
            output_path=self.output_path,
            service_names=self.master_service_names,
            generate_package=self.is_package(),
            version=version,
            static_files_path=self._get_static_files_path(),
        )

    def generate_stubs(self) -> list[Package]:
        """
        Generate main stubs.
        """
        result: list[Package] = []
        package: Package | None = None

        package = self._generate_boto3_stubs()
        if package:
            result.append(package)

        if not self.config.skip_lite_package and self.is_package():
            package = self._generate_master()
            if package:
                result.append(package)

        if not self.config.skip_lite_package:
            package = self._generate_boto3_stubs_lite()
            if package:
                result.append(package)

        return result

    def generate_docs(self) -> None:
        """
        Generate service and master docs.
        """
        package_data = Boto3StubsPackageData
        total_str = f"{len(self.service_names)}"

        self.logger.info(f"Generating {package_data.NAME} module docs")
        process_boto3_stubs_docs(
            self.output_path,
            self.service_names,
            self.version,
        )

        for index, service_name in enumerate(self.service_names):
            current_str = f"{{:0{len(total_str)}}}".format(index + 1)
            package_name = package_data.get_service_package_name(service_name)
            self.logger.info(f"[{current_str}/{total_str}] Generating {package_name} module docs")
            self._process_service_docs(
                service_name=service_name,
                package_data=package_data,
                templates_path=TemplatePath.boto3_stubs_service_docs,
                version=self.version,
            )

    def generate_full_stubs(self) -> list[WrapperPackage]:
        """
        Generate full stubs.
        """
        package_data = Boto3StubsFullPackageData
        try:
            version = self._get_package_version(package_data.PYPI_NAME, self.version)
        except AlreadyPublishedError:
            self.logger.info(f"Skipping {package_data.PYPI_NAME} {self.version}, already on PyPI")
            return []

        self.logger.info(f"Generating {package_data.PYPI_NAME} {version}")
        package = process_boto3_stubs_full(
            self.output_path,
            self.service_names,
            version=version,
            generate_package=self.is_package(),
        )
        self._generate_full_stubs_services(package)
        return [package]

    def generate_custom_stubs(self) -> list[WrapperPackage]:
        """
        Do nothing.
        """
        return []
