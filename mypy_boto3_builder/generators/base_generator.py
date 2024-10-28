"""
Base stubs/docs generator.
"""

import shutil
import tempfile
from abc import ABC, abstractmethod
from collections.abc import Sequence
from pathlib import Path
from typing import ClassVar

from mypy_boto3_builder.cli_parser import CLINamespace
from mypy_boto3_builder.enums.product import ProductType
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.package_data import BasePackageData
from mypy_boto3_builder.parsers.service_package_parser import ServicePackageParser
from mypy_boto3_builder.postprocessors.base import BasePostprocessor
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.package import Package
from mypy_boto3_builder.structures.service_package import ServicePackage
from mypy_boto3_builder.utils.boto3_utils import get_boto3_session
from mypy_boto3_builder.utils.github import download_and_extract
from mypy_boto3_builder.utils.pypi_manager import PyPIManager
from mypy_boto3_builder.writers.package_writer import PackageWriter


class BaseGenerator(ABC):
    """
    Base stubs/docs generator.

    Arguments:
        service_names -- Selected service names
        master_service_names -- Service names included in master
        output_path -- Path to write generated files
        generate_setup -- Whether to create package or installed module
        skip_published -- Whether to skip packages that are already published
        disable_smart_version -- Whether to create a new postrelease based on latest PyPI version
        download_static_stubs -- Whether to download static stubs from GitHub repositories
        version -- Package build version
        cleanup -- Whether to cleanup generated files
    """

    service_package_data: ClassVar[type[BasePackageData]]
    service_template_path: ClassVar[Path]

    def __init__(
        self,
        service_names: Sequence[ServiceName],
        master_service_names: Sequence[ServiceName],
        config: CLINamespace,
        version: str,
        cleanup: bool,
    ) -> None:
        self.session = get_boto3_session()
        self.service_names = service_names
        self.master_service_names = master_service_names
        self.config = config
        self.output_path = config.output_path
        self.logger = get_logger()
        self.generate_setup = not config.installed
        self.version = version or self.get_library_version()
        self.cleanup = cleanup
        self.package_writer = PackageWriter(
            output_path=self.config.output_path,
            generate_setup=self.generate_setup,
            cleanup=cleanup,
        )
        self._downloaded_static_files_path: Path | None = None
        self._cleanup_dirs: list[Path] = []

    def _get_or_download_static_files_path(
        self, static_path: Path, download_url: str | None = None
    ) -> Path:
        """
        Get path to static files. Download if needed.
        """
        if not self.config.download_static_stubs or not download_url:
            return static_path

        if self._downloaded_static_files_path:
            return self._downloaded_static_files_path

        self.logger.debug(f"Downloading static files from {download_url}")
        with tempfile.TemporaryDirectory(delete=False) as temp_dir:
            temp_dir_path = Path(temp_dir)
            self._cleanup_dirs.append(temp_dir_path)
            self._downloaded_static_files_path = download_and_extract(download_url, temp_dir_path)

        self.logger.debug(f"Downloaded static files to {self._downloaded_static_files_path}")

        return self._downloaded_static_files_path

    @abstractmethod
    def get_postprocessor(self, service_package: ServicePackage) -> BasePostprocessor:
        """
        Get postprocessor for service package.
        """

    @abstractmethod
    def get_library_version(self) -> str:
        """
        Get underlying library version.
        """
        raise NotImplementedError("Method should be implemented in child class")

    def _get_package_version(self, pypi_name: str, version: str) -> str | None:
        if self.config.disable_smart_version:
            return version
        pypi_manager = PyPIManager(pypi_name)
        if not pypi_manager.has_version(version):
            return version

        if self.config.skip_published:
            self.logger.info(f"Skipping {pypi_name} {version}, already on PyPI")
            return None

        return pypi_manager.get_next_version(version)

    @abstractmethod
    def generate_stubs(self) -> None:
        """
        Generate main stubs.
        """
        raise NotImplementedError("Method should be implemented in child class")

    @abstractmethod
    def generate_full_stubs(self) -> None:
        """
        Generate full stubs.
        """
        raise NotImplementedError("Method should be implemented in child class")

    def _generate_full_stubs_services(self, package: Package) -> None:
        package_writer = PackageWriter(
            output_path=self.output_path / package.directory_name,
            generate_setup=False,
            cleanup=False,
        )
        total_str = f"{len(self.service_names)}"
        for index, service_name in enumerate(self.service_names):
            current_str = f"{{:0{len(total_str)}}}".format(index + 1)
            progress_str = f"[{current_str}/{total_str}]"

            self.logger.info(
                f"{progress_str} Generating {service_name.boto3_name} package directory"
            )
            service_package = self._parse_service_package(
                service_name, package.version, package.data
            )
            service_package.pypi_name = package.pypi_name
            service_package.version = package.version
            package_writer.write_service_package(
                service_package,
                templates_path=self.service_template_path,
            )

    @abstractmethod
    def generate_docs(self) -> None:
        """
        Generate service and master docs.
        """

    def generate_product(self, product_type: ProductType) -> None:
        """
        Run generator for a product type.
        """
        match product_type:
            case ProductType.stubs:
                self.generate_stubs()
            case ProductType.service_stubs:
                self.generate_service_stubs()
            case ProductType.docs:
                self.generate_docs()
            case ProductType.full:
                self.generate_full_stubs()

    def _parse_service_package(
        self,
        service_name: ServiceName,
        version: str | None,
        package_data: type[BasePackageData],
    ) -> ServicePackage:
        self.logger.debug(f"Parsing {service_name.boto3_name}")
        parser = ServicePackageParser(self.session, service_name, package_data)
        service_package = parser.parse()
        if version:
            service_package.version = version

        postprocessor = self.get_postprocessor(service_package)
        postprocessor.generate_docstrings()
        postprocessor.process_package()

        postprocessor.extend_literals()
        postprocessor.replace_self_ref_typed_dicts()
        return service_package

    def _process_service(
        self,
        service_name: ServiceName,
        version: str,
        package_data: type[BasePackageData],
        templates_path: Path,
    ) -> ServicePackage:
        service_package = self._parse_service_package(service_name, version, package_data)
        ServicePackageParser.mark_unsafe_typed_dicts(service_package)

        self.logger.debug(f"Writing {service_name.boto3_name}")
        self.package_writer.write_service_package(
            service_package,
            templates_path=templates_path,
        )
        return service_package

    def _process_service_docs(
        self,
        service_name: ServiceName,
        package_data: type[BasePackageData],
        templates_path: Path,
    ) -> ServicePackage:
        service_package = self._parse_service_package(
            service_name=service_name,
            version=None,
            package_data=package_data,
        )

        self.logger.debug(f"Writing {service_name.boto3_name}")
        self.package_writer.write_service_docs(
            service_package,
            templates_path=templates_path,
        )
        return service_package

    def _generate_service(self, service_name: ServiceName) -> ServicePackage:
        pypi_name = self.service_package_data.get_service_pypi_name(service_name)
        version = self._get_package_version(pypi_name, self.version)
        if not version:
            return ServicePackage(data=self.service_package_data, service_name=service_name)

        return self._process_service(
            service_name=service_name,
            version=version,
            package_data=self.service_package_data,
            templates_path=self.service_template_path,
        )

    def generate_service_stubs(self) -> None:
        """
        Generate service stubs.
        """
        total_str = f"{len(self.service_names)}"
        for index, service_name in enumerate(self.service_names):
            current_str = f"{{:0{len(total_str)}}}".format(index + 1)
            progress_str = f"[{current_str}/{total_str}]"

            pypi_name = self.service_package_data.get_service_pypi_name(service_name)
            version = self._get_package_version(pypi_name, self.version)
            if not version:
                continue

            self.logger.info(f"{progress_str} Generating {pypi_name} {version}")
            self._generate_service(service_name)

    def cleanup_temporary_files(self) -> None:
        """
        Cleanup temporary files.
        """
        for dir_path in self._cleanup_dirs:
            if not dir_path.exists():
                continue

            self.logger.debug(f"Removing {dir_path}")
            shutil.rmtree(dir_path)
