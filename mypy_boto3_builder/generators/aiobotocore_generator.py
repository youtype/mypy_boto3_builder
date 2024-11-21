"""
AioBotocore stubs/docs generator.

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
    TypesAioBotocoreFullPackageData,
    TypesAioBotocoreLitePackageData,
    TypesAioBotocorePackageData,
)
from mypy_boto3_builder.postprocessors.aiobotocore import AioBotocorePostprocessor
from mypy_boto3_builder.structures.service_package import ServicePackage
from mypy_boto3_builder.writers.aiobotocore_processors import (
    process_types_aiobotocore,
    process_types_aiobotocore_docs,
    process_types_aiobotocore_full,
    process_types_aiobotocore_lite,
)


class AioBotocoreGenerator(BaseGenerator):
    """
    AioBotocore stubs/docs generator.
    """

    service_package_data = TypesAioBotocorePackageData
    service_template_path = TemplatePath.types_aiobotocore_service

    def _get_static_files_path(self) -> Path:
        return self._get_or_download_static_files_path(
            StaticStubsPath.types_aiobotocore,
            StaticStubsPullURL.types_aiobotocore,
        )

    def get_postprocessor(self, service_package: ServicePackage) -> AioBotocorePostprocessor:
        """
        Get postprocessor for service package.
        """
        return AioBotocorePostprocessor(service_package, self.master_service_names)

    def generate_stubs(self) -> None:
        """
        Generate `aiobotocore-stubs` package.
        """
        self._generate_stubs()
        self._generate_stubs_lite()

    def _generate_stubs(self) -> None:
        package_data = TypesAioBotocorePackageData
        try:
            version = self._get_package_version(package_data.PYPI_NAME, self.version)
        except AlreadyPublishedError:
            self.logger.info(f"Skipping {package_data.PYPI_NAME} {self.version}, already on PyPI")
            return

        self.logger.info(f"Generating {package_data.PYPI_NAME} {version}")
        process_types_aiobotocore(
            output_path=self.output_path,
            service_names=self.master_service_names,
            generate_setup=self.generate_setup,
            version=version,
            static_files_path=self._get_static_files_path(),
        )

    def _generate_stubs_lite(self) -> None:
        package_data = TypesAioBotocoreLitePackageData
        try:
            version = self._get_package_version(package_data.PYPI_NAME, self.version)
        except AlreadyPublishedError:
            self.logger.info(f"Skipping {package_data.PYPI_NAME} {self.version}, already on PyPI")
            return

        self.logger.info(f"Generating {package_data.PYPI_NAME} {version}")
        process_types_aiobotocore_lite(
            output_path=self.output_path,
            service_names=self.master_service_names,
            generate_setup=self.generate_setup,
            version=version,
            static_files_path=self._get_static_files_path(),
        )

    def generate_docs(self) -> None:
        """
        Generate service and master docs.
        """
        package_data = TypesAioBotocorePackageData
        total_str = f"{len(self.service_names)}"

        self.logger.info(f"Generating {package_data.PYPI_NAME} module docs")
        process_types_aiobotocore_docs(
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
                templates_path=TemplatePath.types_aiobotocore_service_docs,
                version=self.version,
            )

    def generate_full_stubs(self) -> None:
        """
        Generate full stubs.
        """
        package_data = TypesAioBotocoreFullPackageData
        try:
            version = self._get_package_version(package_data.PYPI_NAME, self.version)
        except AlreadyPublishedError:
            self.logger.info(f"Skipping {package_data.PYPI_NAME} {self.version}, already on PyPI")
            return

        self.logger.info(f"Generating {package_data.PYPI_NAME} {version}")
        package = process_types_aiobotocore_full(
            output_path=self.output_path,
            service_names=self.service_names,
            generate_setup=self.generate_setup,
            package_data=package_data,
            version=version,
        )
        self._generate_full_stubs_services(package)
