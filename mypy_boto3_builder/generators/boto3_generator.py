"""
Boto3 stubs/docs generator.
"""
from mypy_boto3_builder.constants import TEMPLATES_PATH
from mypy_boto3_builder.generators.base_generator import BaseGenerator
from mypy_boto3_builder.package_data import (
    Boto3StubsLitePackageData,
    Boto3StubsPackageData,
    BotocoreStubsPackageData,
    MypyBoto3PackageData,
)
from mypy_boto3_builder.utils.version import get_boto3_version
from mypy_boto3_builder.writers.processors import (
    process_boto3_stubs,
    process_boto3_stubs_docs,
    process_boto3_stubs_lite,
    process_botocore_stubs,
    process_master,
)


class Boto3Generator(BaseGenerator):
    """
    Boto3 stubs/docs generator.
    """

    def get_library_version(self) -> str:
        """
        Get underlying library version.
        """
        return get_boto3_version()

    def _generate_master(self) -> None:
        """
        Generate `mypy-boto3` package.
        """
        package_data = MypyBoto3PackageData
        version = self._get_package_version(package_data.PYPI_NAME, self.version)
        if not version:
            self.logger.info(f"Skipping {package_data.PYPI_NAME} {self.version}, already on PyPI")
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
            self.logger.info(f"Skipping {package_data.PYPI_NAME} {self.version}, already on PyPI")
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
            self.logger.info(f"Skipping {package_data.PYPI_NAME} {self.version}, already on PyPI")
            return

        self.logger.info(f"Generating {package_data.PYPI_NAME} {version}")
        process_boto3_stubs_lite(
            self.session,
            self.output_path,
            self.master_service_names,
            generate_setup=self.generate_setup,
            version=version,
        )

    def _generate_botocore_stubs(self) -> None:
        """
        Generate `botocore-stubs` package.
        """
        package_data = BotocoreStubsPackageData
        version = self._get_package_version(
            package_data.PYPI_NAME, package_data.get_library_version()
        )
        if not version:
            self.logger.info(
                f"Skipping {package_data.PYPI_NAME} {package_data.get_library_version()}, already"
                " on PyPI"
            )
            return

        self.logger.info(f"Generating {package_data.PYPI_NAME} {version}")
        process_botocore_stubs(
            self.output_path,
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
        self._generate_botocore_stubs()

    def generate_service_stubs(self) -> None:
        """
        Generate service stubs.
        """
        total_str = f"{len(self.service_names)}"
        for index, service_name in enumerate(self.service_names):
            current_str = f"{{:0{len(total_str)}}}".format(index + 1)

            pypi_name = Boto3StubsPackageData.get_service_pypi_name(service_name)
            package_name = Boto3StubsPackageData.get_service_package_name(service_name)
            version = self._get_package_version(pypi_name, self.version)
            if not version:
                self.logger.info(
                    f"[{current_str}/{total_str}]"
                    f" Skipping {package_name} {self.version}, already on PyPI"
                )
                continue

            self.logger.info(f"[{current_str}/{total_str}] Generating {package_name} {version}")
            self._process_service(
                service_name=service_name,
                version=version,
                package_data=Boto3StubsPackageData,
                templates_path=TEMPLATES_PATH / "boto3_service",
            )

    def generate_docs(self) -> None:
        """
        Generate service and master docs.
        """
        total_str = f"{len(self.service_names)}"

        self.logger.info(f"Generating {Boto3StubsPackageData.NAME} module docs")
        process_boto3_stubs_docs(
            self.session,
            self.output_path,
            self.service_names,
        )

        for index, service_name in enumerate(self.service_names):
            current_str = f"{{:0{len(total_str)}}}".format(index + 1)
            package_name = Boto3StubsPackageData.get_service_package_name(service_name)
            self.logger.info(f"[{current_str}/{total_str}] Generating {package_name} module docs")
            self._process_service_docs(
                service_name=service_name,
                package_data=Boto3StubsPackageData,
                templates_path=TEMPLATES_PATH / "boto3_service_docs",
            )
