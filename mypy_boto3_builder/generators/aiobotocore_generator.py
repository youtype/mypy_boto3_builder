"""
AioBotocore stubs/docs generator.
"""
from mypy_boto3_builder.constants import TEMPLATES_PATH
from mypy_boto3_builder.generators.base_generator import BaseGenerator
from mypy_boto3_builder.package_data import (
    TypesAioBotocoreLitePackageData,
    TypesAioBotocorePackageData,
)
from mypy_boto3_builder.postprocessors.aiobotocore import AioBotocorePostprocessor
from mypy_boto3_builder.structures.service_package import ServicePackage
from mypy_boto3_builder.utils.version import get_aiobotocore_version
from mypy_boto3_builder.writers.aiobotocore_processors import (
    process_aiobotocore_stubs,
    process_aiobotocore_stubs_docs,
    process_aiobotocore_stubs_lite,
)


class AioBotocoreGenerator(BaseGenerator):
    """
    AioBotocore stubs/docs generator.
    """

    service_package_data = TypesAioBotocorePackageData
    service_template_path = TEMPLATES_PATH / "aiobotocore_service"

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
        Generate `aiobotocore-stubs` package.
        """
        self._generate_stubs()
        self._generate_stubs_lite()

    def _generate_stubs(self) -> None:
        package_data = TypesAioBotocorePackageData
        version = self._get_package_version(package_data.PYPI_NAME, self.version)
        if not version:
            return

        self.logger.info(f"Generating {package_data.PYPI_NAME} {version}")
        process_aiobotocore_stubs(
            self.session,
            self.output_path,
            self.master_service_names,
            generate_setup=self.generate_setup,
            version=version,
        )

    def _generate_stubs_lite(self) -> None:
        package_data = TypesAioBotocoreLitePackageData
        version = self._get_package_version(package_data.PYPI_NAME, self.version)
        if not version:
            return

        self.logger.info(f"Generating {package_data.PYPI_NAME} {version}")
        process_aiobotocore_stubs_lite(
            self.session,
            self.output_path,
            self.master_service_names,
            generate_setup=self.generate_setup,
            version=version,
        )

    def generate_docs(self) -> None:
        """
        Generate service and master docs.
        """
        package_data = TypesAioBotocorePackageData
        total_str = f"{len(self.service_names)}"

        self.logger.info(f"Generating {package_data.PYPI_NAME} module docs")
        process_aiobotocore_stubs_docs(
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
                templates_path=TEMPLATES_PATH / "aiobotocore_service_docs",
            )
