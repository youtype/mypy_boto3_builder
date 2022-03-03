"""
Boto3 stubs/docs generator.
"""
from collections.abc import Iterable, Sequence
from pathlib import Path

from boto3.session import Session

from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.package_data import (
    Boto3StubsLitePackageData,
    Boto3StubsPackageData,
    BotocoreStubsPackageData,
    MypyBoto3PackageData,
)
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.utils.pypi_manager import PyPIManager
from mypy_boto3_builder.utils.version import get_boto3_version
from mypy_boto3_builder.writers.processors import (
    process_boto3_stubs,
    process_boto3_stubs_docs,
    process_boto3_stubs_lite,
    process_botocore_stubs,
    process_master,
    process_service,
    process_service_docs,
)


class Boto3Generator:
    """
    Boto3 stubs/docs generator.

    Arguments:
        service_names -- Enabled service names
        available_service_names -- All service names
        master_service_names -- Service names included in master
        session -- Botocore session
        output_path -- Path to write generated files
        generate_setup -- Whether to create package or installed module
        skip_published -- Whether to skip packages that are already published
        disable_smart_version -- Whether to create a new postrelease if version is already published
        version -- Package build version
    """

    def __init__(
        self,
        service_names: Sequence[ServiceName],
        available_service_names: Iterable[ServiceName],
        master_service_names: Sequence[ServiceName],
        session: Session,
        output_path: Path,
        generate_setup: bool,
        skip_published: bool,
        disable_smart_version: bool,
        version: str,
    ):
        self.session = session
        self.service_names = service_names
        self.available_service_names = available_service_names
        self.master_service_names = master_service_names
        self.output_path = output_path
        self.logger = get_logger()
        self.generate_setup = generate_setup
        self.skip_published = skip_published
        self.disable_smart_version = disable_smart_version
        self.version = version or get_boto3_version()

    def _get_package_version(self, pypi_name: str, version: str) -> str | None:
        pypi_manager = PyPIManager(pypi_name)
        if not pypi_manager.has_version(version):
            return version

        if self.skip_published:
            return None
        if self.disable_smart_version:
            return version

        return pypi_manager.get_next_version(version)

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
            process_service(
                session=self.session,
                output_path=self.output_path,
                service_name=service_name,
                generate_setup=self.generate_setup,
                service_names=self.master_service_names,
                version=version,
            )

    def generate_docs(self) -> None:
        """
        Generate service and master docs.
        """
        logger = get_logger()
        total_str = f"{len(self.service_names)}"

        logger.info(f"Generating {Boto3StubsPackageData.NAME} module docs")
        process_boto3_stubs_docs(
            self.session,
            self.output_path,
            self.service_names,
        )

        for index, service_name in enumerate(self.service_names):
            current_str = f"{{:0{len(total_str)}}}".format(index + 1)
            package_name = Boto3StubsPackageData.get_service_package_name(service_name)
            logger.info(f"[{current_str}/{total_str}] Generating {package_name} module docs")
            process_service_docs(
                session=self.session,
                output_path=self.output_path,
                service_name=service_name,
                service_names=self.available_service_names,
            )
