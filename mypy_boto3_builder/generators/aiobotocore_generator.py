"""
Generator for types-aiobotocore packages.

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
    TypesAioBotocoreCustomPackageData,
    TypesAioBotocoreFullPackageData,
    TypesAioBotocoreLitePackageData,
    TypesAioBotocorePackageData,
)
from mypy_boto3_builder.parsers.parse_wrapper_package import parse_types_aiobotocore_package
from mypy_boto3_builder.postprocessors.aiobotocore import AioBotocorePostprocessor
from mypy_boto3_builder.structures.package import Package
from mypy_boto3_builder.structures.packages.service_package import ServicePackage


class AioBotocoreGenerator(BaseGenerator):
    """
    Generator for types-aiobotocore packages.
    """

    service_package_data = TypesAioBotocorePackageData()
    service_template_path = TemplatePath.types_aiobotocore_service

    def _get_static_files_path(self) -> Path:
        return self._get_or_download_static_files_path(
            StaticStubsPath.types_aiobotocore,
            StaticStubsPullURL.types_aiobotocore,
        )

    def _get_postprocessor(self, service_package: ServicePackage) -> AioBotocorePostprocessor:
        """
        Get postprocessor for service package.
        """
        return AioBotocorePostprocessor(service_package, self.main_service_names)

    def generate_stubs(self) -> list[Package]:
        """
        Generate `types-aiobotocore` package.
        """
        package_data = TypesAioBotocorePackageData()
        try:
            version = self._get_package_version(package_data.pypi_name, self.version)
        except AlreadyPublishedError:
            self.logger.info(f"Skipping {package_data.pypi_name} {self.version}, already on PyPI")
            return []

        self.logger.info(f"Generating {package_data.pypi_name} {version}")

        package = parse_types_aiobotocore_package(
            service_names=self.main_service_names,
            package_data=package_data,
            version=version,
        )
        package.extras.extend(self._get_wrapper_package_extras(package))
        package.set_description(package.get_short_description())
        self.package_writer.write_package(
            package,
            template_path=TemplatePath.types_aiobotocore,
            static_files_path=self._get_static_files_path(),
        )
        return [package]

    def generate_stubs_lite(self) -> Package | None:
        """
        Generate `types-aiobotocore-lite` package.
        """
        package_data = TypesAioBotocoreLitePackageData()
        try:
            version = self._get_package_version(package_data.pypi_name, self.version)
        except AlreadyPublishedError:
            self.logger.info(f"Skipping {package_data.pypi_name} {self.version}, already on PyPI")
            return None

        self.logger.info(f"Generating {package_data.pypi_name} {version}")
        package = parse_types_aiobotocore_package(
            service_names=self.main_service_names,
            package_data=package_data,
            version=version,
        )
        package.extras.extend(self._get_wrapper_package_extras(package))
        package.set_description(package.get_short_description("Lite type annotations"))
        self.package_writer.write_package(
            package,
            template_path=TemplatePath.types_aiobotocore,
            static_files_path=self._get_static_files_path(),
            exclude_template_names=("session.pyi.jinja2",),
        )
        return package

    def generate_docs(self) -> None:
        """
        Generate service and main docs.
        """
        package_data = TypesAioBotocorePackageData()
        total_str = f"{len(self.service_names)}"

        self.logger.info(f"Generating {package_data.pypi_name} module docs")
        package = parse_types_aiobotocore_package(
            service_names=self.service_names,
            package_data=package_data,
            version=self.version,
        )
        self.package_writer.write_docs(
            package,
            templates_path=TemplatePath.types_aiobotocore_docs,
        )

        for index, service_name in enumerate(self.service_names):
            current_str = f"{{:0{len(total_str)}}}".format(index + 1)
            package_name = package_data.get_service_package_name(service_name)
            self.logger.info(f"[{current_str}/{total_str}] Generating {package_name} module docs")
            self._process_service_docs(
                service_name=service_name,
                package_data=package_data,
                templates_path=TemplatePath.types_aiobotocore_service_docs,
                version=self.version,
            )

    def generate_full_stubs(self) -> Package | None:
        """
        Generate `types-aiobotocore-full` package.
        """
        package_data = TypesAioBotocoreFullPackageData()
        try:
            version = self._get_package_version(package_data.pypi_name, self.version)
        except AlreadyPublishedError:
            self.logger.info(f"Skipping {package_data.pypi_name} {self.version}, already on PyPI")
            return None

        self.logger.info(f"Generating {package_data.pypi_name} {version}")
        package = parse_types_aiobotocore_package(
            service_names=self.service_names,
            package_data=package_data,
            version=version,
        )
        package.setup_package_data.clear()
        for service_name in self.service_names:
            package.setup_package_data[package_data.get_service_package_name(service_name)] = (
                "py.typed",
                "*.pyi",
            )
        package.set_description(package.get_short_description("All-in-one type annotations"))
        self.package_writer.write_package(
            package,
            template_path=TemplatePath.types_aiobotocore_full,
        )
        self._generate_full_stubs_services(package)
        self.setup_package_writer.write_package(
            package,
            template_path=TemplatePath.types_aiobotocore_full,
            include_template_names=("setup.py.jinja2",),
        )
        return package

    def generate_custom_stubs(self) -> Package:
        """
        Generate `types-aiobotocore-custom` package.
        """
        package_data = TypesAioBotocoreCustomPackageData()

        self.logger.info(f"Generating {package_data.pypi_name} {self.version}")
        package = parse_types_aiobotocore_package(
            service_names=self.service_names,
            package_data=package_data,
            version=self.version,
        )
        for service_name in self.service_names:
            package.setup_package_data[package_data.get_service_package_name(service_name)] = (
                "py.typed",
                "*.pyi",
            )
        package.set_description(package.get_short_description("Custom type annotations"))
        self.package_writer.write_package(
            package=package,
            template_path=TemplatePath.types_aiobotocore_custom,
            static_files_path=self._get_static_files_path(),
        )

        self._generate_full_stubs_services(package)
        self.setup_package_writer.write_package(
            package,
            template_path=TemplatePath.types_aiobotocore_custom,
            include_template_names=("setup.py.jinja2",),
        )
        return package
