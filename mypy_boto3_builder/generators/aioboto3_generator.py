"""
Generator for types-aioboto3 packages.

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
    TypesAioBoto3CustomPackageData,
    TypesAioBoto3LitePackageData,
    TypesAioBoto3PackageData,
    TypesAioBotocorePackageData,
)
from mypy_boto3_builder.parsers.parse_wrapper_package import (
    parse_types_aioboto3_package,
    parse_types_aiobotocore_package,
)
from mypy_boto3_builder.postprocessors.aioboto3 import AioBoto3Postprocessor
from mypy_boto3_builder.structures.package import Package
from mypy_boto3_builder.structures.packages.service_package import ServicePackage
from mypy_boto3_builder.writers.package_writer import PackageWriter


class AioBoto3Generator(BaseGenerator):
    """
    Generator for types-aioboto3 packages.
    """

    service_package_data = TypesAioBoto3PackageData()
    service_template_path = TemplatePath.types_aiobotocore_service

    def _get_static_files_path(self) -> Path:
        return self._get_or_download_static_files_path(
            StaticStubsPath.types_aioboto3,
            StaticStubsPullURL.types_aioboto3,
        )

    def _get_aiobotocore_static_files_path(self) -> Path:
        return self._get_or_download_static_files_path(
            StaticStubsPath.types_aiobotocore,
            StaticStubsPullURL.types_aiobotocore,
        )

    def _get_postprocessor(self, service_package: ServicePackage) -> AioBoto3Postprocessor:
        """
        Get postprocessor for service package.
        """
        return AioBoto3Postprocessor(service_package, self.main_service_names)

    def generate_stubs(self) -> list[Package]:
        """
        Generate `types-aioboto3` package.
        """
        package_data = TypesAioBoto3PackageData()
        try:
            version = self._get_package_version(package_data.pypi_name, self.version)
        except AlreadyPublishedError:
            self.logger.info(f"Skipping {package_data.pypi_name} {self.version}, already on PyPI")
            return []

        self.logger.info(f"Generating {package_data.pypi_name} {version}")
        package = parse_types_aioboto3_package(
            service_names=self.main_service_names,
            package_data=package_data,
            version=version,
        )
        package.extras.extend(self._get_wrapper_package_extras(package))
        package.set_description(package.get_short_description())
        self.package_writer.write_package(
            package=package,
            template_path=TemplatePath.types_aioboto3,
            static_files_path=self._get_static_files_path(),
        )
        return [package]

    def generate_stubs_lite(self) -> Package | None:
        """
        Generate `types-aioboto3-lite` package.
        """
        package_data = TypesAioBoto3LitePackageData()
        try:
            version = self._get_package_version(package_data.pypi_name, self.version)
        except AlreadyPublishedError:
            self.logger.info(f"Skipping {package_data.pypi_name} {self.version}, already on PyPI")
            return None

        self.logger.info(f"Generating {package_data.pypi_name} {version}")
        package = parse_types_aioboto3_package(
            service_names=self.main_service_names,
            package_data=package_data,
            version=version,
        )
        package.extras.extend(self._get_wrapper_package_extras(package))
        package.set_description(package.get_short_description("Lite type annotations"))
        self.package_writer.write_package(
            package,
            template_path=TemplatePath.types_aioboto3,
            static_files_path=self._get_static_files_path(),
            exclude_template_names=("session.pyi.jinja2",),
        )
        return package

    def generate_docs(self) -> None:
        """
        Generate service and main docs.
        """
        package_data = TypesAioBoto3PackageData()
        total_str = f"{len(self.service_names)}"

        self.logger.info(f"Generating {package_data.pypi_name} module docs")
        package = parse_types_aioboto3_package(
            service_names=self.service_names,
            package_data=package_data,
            version=self.version,
        )
        self.package_writer.write_docs(
            package,
            templates_path=TemplatePath.types_aioboto3_docs,
        )

        for index, service_name in enumerate(self.service_names):
            current_str = f"{{:0{len(total_str)}}}".format(index + 1)
            package_name = package_data.get_service_package_name(service_name)
            self.logger.info(f"[{current_str}/{total_str}] Generating {package_name} module docs")
            self._process_service_docs(
                service_name=service_name,
                package_data=package_data,
                templates_path=TemplatePath.types_aioboto3_service_docs,
                version=self.version,
            )

    def generate_service_stubs(self) -> list[ServicePackage]:
        """
        Do nothing.
        """
        return []

    def generate_full_stubs(self) -> None:
        """
        Do nothing.
        """

    def generate_custom_stubs(self) -> Package:
        """
        Generate `types-aioboto3-custom` package.
        """
        package_data = TypesAioBoto3CustomPackageData()
        aiobotocore_package_data = TypesAioBotocorePackageData()

        self.logger.info(f"Generating {package_data.pypi_name} {self.version}")
        package = parse_types_aioboto3_package(
            service_names=self.service_names,
            package_data=package_data,
            version=self.version,
        )
        package.setup_package_data[aiobotocore_package_data.name] = ("py.typed", "*.pyi", "*/*.pyi")
        for service_name in self.service_names:
            package.setup_package_data[package_data.get_service_package_name(service_name)] = (
                "py.typed",
                "*.pyi",
            )
        package.set_description(package.get_short_description("Custom type annotations"))
        self.package_writer.write_package(
            package=package,
            template_path=TemplatePath.types_aioboto3_custom,
            static_files_path=self._get_static_files_path(),
        )

        aiobotocore_package = parse_types_aiobotocore_package(
            service_names=self.service_names,
            package_data=aiobotocore_package_data,
            version=aiobotocore_package_data.get_library_version(),
        )
        aiobotocore_package_writer = PackageWriter(
            output_path=self.output_path / package.directory_name,
            generate_package=False,
            cleanup=False,
            is_typings=False,
        )
        aiobotocore_package_writer.write_package(
            package=aiobotocore_package,
            template_path=TemplatePath.types_aiobotocore,
            static_files_path=self._get_aiobotocore_static_files_path(),
        )

        self._generate_full_stubs_services(package)
        self.setup_package_writer.write_package(
            package,
            template_path=TemplatePath.types_aioboto3_custom,
            include_template_names=("setup.py.jinja2",),
        )
        return package
