"""
AioBoto3 stubs generator.
"""

from pathlib import Path

from mypy_boto3_builder.constants import (
    StaticStubsPath,
    StaticStubsPullURL,
    TemplatePath,
)
from mypy_boto3_builder.generators.base_generator import BaseGenerator
from mypy_boto3_builder.package_data import TypesAioBoto3LitePackageData, TypesAioBoto3PackageData
from mypy_boto3_builder.postprocessors.aiobotocore import AioBotocorePostprocessor
from mypy_boto3_builder.structures.service_package import ServicePackage
from mypy_boto3_builder.utils.version_getters import get_aioboto3_version
from mypy_boto3_builder.writers.aioboto3_processors import (
    process_types_aioboto3,
    process_types_aioboto3_docs,
    process_types_aioboto3_lite,
)


class AioBoto3Generator(BaseGenerator):
    """
    AioBoto3 stubs generator.
    """

    service_package_data = TypesAioBoto3PackageData

    def _get_static_files_path(self) -> Path:
        return self._get_or_download_static_files_path(
            StaticStubsPath.types_aioboto3,
            StaticStubsPullURL.types_aioboto3,
        )

    def get_library_version(self) -> str:
        """
        Get underlying library version.
        """
        return get_aioboto3_version()

    def get_postprocessor(self, service_package: ServicePackage) -> AioBotocorePostprocessor:
        """
        Get postprocessor for service package.
        """
        return AioBotocorePostprocessor(self.session, service_package, self.master_service_names)

    def generate_stubs(self) -> None:
        """
        Generate `types-aioboto3` package.
        """
        self._generate_stubs()
        self._generate_stubs_lite()

    def _generate_stubs(self) -> None:
        package_data = TypesAioBoto3PackageData
        version = self._get_package_version(package_data.PYPI_NAME, self.version)
        if not version:
            return

        self.logger.info(f"Generating {package_data.PYPI_NAME} {version}")
        process_types_aioboto3(
            session=self.session,
            output_path=self.output_path,
            service_names=self.master_service_names,
            generate_setup=self.generate_setup,
            version=version,
            static_files_path=self._get_static_files_path(),
        )

    def _generate_stubs_lite(self) -> None:
        package_data = TypesAioBoto3LitePackageData
        version = self._get_package_version(package_data.PYPI_NAME, self.version)
        if not version:
            return

        self.logger.info(f"Generating {package_data.PYPI_NAME} {version}")
        process_types_aioboto3_lite(
            session=self.session,
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
        package_data = TypesAioBoto3PackageData
        total_str = f"{len(self.service_names)}"

        self.logger.info(f"Generating {package_data.PYPI_NAME} module docs")
        process_types_aioboto3_docs(
            self.session,
            self.output_path,
            self.service_names,
        )

        for index, service_name in enumerate(self.service_names):
            current_str = f"{{:0{len(total_str)}}}".format(index + 1)
            package_name = package_data.get_service_package_name(service_name)
            self.logger.info(f"[{current_str}/{total_str}] Generating {package_name} module docs")
            self._process_service_docs(
                service_name=service_name,
                package_data=package_data,
                templates_path=TemplatePath.types_aioboto3_service_docs,
            )

    def generate_service_stubs(self) -> None:
        """
        Do nothing.
        """

    def generate_full_stubs(self) -> None:
        """
        Do nothing.
        """
