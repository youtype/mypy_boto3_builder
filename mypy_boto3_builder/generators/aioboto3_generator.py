"""
AioBoto3 stubs generator.
"""
from mypy_boto3_builder.constants import TEMPLATES_PATH
from mypy_boto3_builder.generators.base_generator import BaseGenerator
from mypy_boto3_builder.package_data import TypesAioBoto3LitePackageData, TypesAioBoto3PackageData
from mypy_boto3_builder.postprocessors.aiobotocore import AioBotocorePostprocessor
from mypy_boto3_builder.structures.service_package import ServicePackage
from mypy_boto3_builder.utils.version import get_aiobotocore_version
from mypy_boto3_builder.writers.aioboto3_processors import (
    process_types_aioboto3,
    process_types_aioboto3_lite,
)


class AioBoto3Generator(BaseGenerator):
    """
    AioBoto3 stubs generator.
    """

    service_package_data = TypesAioBoto3PackageData
    service_template_path = TEMPLATES_PATH / "aioboto3_service"

    def get_library_version(self) -> str:
        """
        Get underlying library version.
        """
        return get_aiobotocore_version()

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
            self.session,
            self.output_path,
            self.master_service_names,
            generate_setup=self.generate_setup,
            version=version,
        )

    def _generate_stubs_lite(self) -> None:
        package_data = TypesAioBoto3LitePackageData
        version = self._get_package_version(package_data.PYPI_NAME, self.version)
        if not version:
            return

        self.logger.info(f"Generating {package_data.PYPI_NAME} {version}")
        process_types_aioboto3_lite(
            self.session,
            self.output_path,
            self.master_service_names,
            generate_setup=self.generate_setup,
            version=version,
        )

    def generate_docs(self) -> None:
        """
        Do nothing.
        """

    def generate_service_stubs(self) -> None:
        """
        Do nothing.
        """
