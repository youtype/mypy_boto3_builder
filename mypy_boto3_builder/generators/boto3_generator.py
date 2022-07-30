"""
Boto3 stubs/docs generator.
"""
from mypy_boto3_builder.constants import TEMPLATES_PATH
from mypy_boto3_builder.generators.base_generator import BaseGenerator
from mypy_boto3_builder.package_data import (
    Boto3StubsLitePackageData,
    Boto3StubsPackageData,
    MypyBoto3PackageData,
)
from mypy_boto3_builder.postprocessors.botocore import BotocorePostprocessor
from mypy_boto3_builder.structures.service_package import ServicePackage
from mypy_boto3_builder.utils.version import get_boto3_version
from mypy_boto3_builder.writers.processors import (
    process_boto3_stubs,
    process_boto3_stubs_docs,
    process_boto3_stubs_lite,
    process_master,
)


class Boto3Generator(BaseGenerator):
    """
    Boto3 stubs/docs generator.
    """

    service_package_data = Boto3StubsPackageData
    service_template_path = TEMPLATES_PATH / "boto3_service"

    def get_library_version(self) -> str:
        """
        Get underlying library version.
        """
        return get_boto3_version()

    def get_postprocessor(self, service_package: ServicePackage) -> BotocorePostprocessor:
        """
        Get postprocessor for service package.
        """
        return BotocorePostprocessor(self.session, service_package, self.master_service_names)

    def _generate_master(self) -> None:
        """
        Generate `mypy-boto3` package.
        """
        package_data = MypyBoto3PackageData
        version = self._get_package_version(package_data.PYPI_NAME, self.version)
        if not version:
            return

        self.logger.info(f"Generating {package_data.PYPI_NAME} {version}")
        process_master(
            self.session,
            self.output_path,
            service_names=self.master_service_names,
            generate_setup=self.generate_setup,
            version=version,
        )

    def _generate_boto3_stubs(self) -> None:
        package_data = Boto3StubsPackageData
        version = self._get_package_version(package_data.PYPI_NAME, self.version)
        if not version:
            return

        self.logger.info(f"Generating {package_data.PYPI_NAME} {version}")
        process_boto3_stubs(
            self.session,
            self.output_path,
            self.master_service_names,
            generate_setup=self.generate_setup,
            version=version,
        )

    def _generate_boto3_stubs_lite(self) -> None:
        package_data = Boto3StubsLitePackageData
        version = self._get_package_version(package_data.PYPI_NAME, self.version)
        if not version:
            return

        self.logger.info(f"Generating {package_data.PYPI_NAME} {version}")
        process_boto3_stubs_lite(
            self.session,
            self.output_path,
            self.master_service_names,
            generate_setup=self.generate_setup,
            version=version,
        )

    def generate_stubs(self) -> None:
        """
        Generate main stubs.
        """
        if self.generate_setup:
            self._generate_master()

        self._generate_boto3_stubs()
        self._generate_boto3_stubs_lite()

    def generate_docs(self) -> None:
        """
        Generate service and master docs.
        """
        package_data = Boto3StubsPackageData
        total_str = f"{len(self.service_names)}"

        self.logger.info(f"Generating {package_data.NAME} module docs")
        process_boto3_stubs_docs(
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
                templates_path=TEMPLATES_PATH / "boto3_service_docs",
            )
