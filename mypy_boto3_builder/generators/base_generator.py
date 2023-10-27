"""
Base stubs/docs generator.
"""

from abc import ABC, abstractmethod
from collections.abc import Sequence
from pathlib import Path

from mypy_boto3_builder.constants import ProductType
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.package_data import BasePackageData
from mypy_boto3_builder.parsers.service_package_parser import ServicePackageParser
from mypy_boto3_builder.postprocessors.base import BasePostprocessor
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.service_package import ServicePackage
from mypy_boto3_builder.utils.boto3_utils import get_boto3_session
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
        version -- Package build version
    """

    service_package_data: type[BasePackageData]
    service_template_path: Path

    def __init__(
        self,
        service_names: Sequence[ServiceName],
        master_service_names: Sequence[ServiceName],
        output_path: Path,
        generate_setup: bool,
        skip_published: bool,
        disable_smart_version: bool,
        version: str,
    ):
        self.session = get_boto3_session()
        self.service_names = service_names
        self.master_service_names = master_service_names
        self.output_path = output_path
        self.logger = get_logger()
        self.generate_setup = generate_setup
        self.skip_published = skip_published
        self.disable_smart_version = disable_smart_version
        self.version = version or self.get_library_version()

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
        raise NotImplementedError()

    def _get_package_version(self, pypi_name: str, version: str) -> str | None:
        if self.disable_smart_version:
            return version
        pypi_manager = PyPIManager(pypi_name)
        if not pypi_manager.has_version(version):
            return version

        if self.skip_published:
            self.logger.info(f"Skipping {pypi_name} {version}, already on PyPI")
            return None

        return pypi_manager.get_next_version(version)

    @abstractmethod
    def generate_stubs(self) -> None:
        """
        Generate main stubs.
        """
        raise NotImplementedError()

    @abstractmethod
    def generate_docs(self) -> None:
        """
        Generate service and master docs.
        """

    def generate_product(self, product_type: ProductType) -> None:
        """
        Run generator for a product type.
        """
        if product_type == ProductType.stubs:
            return self.generate_stubs()
        if product_type == ProductType.service_stubs:
            return self.generate_service_stubs()
        if product_type == ProductType.docs:
            return self.generate_docs()

        raise ValueError(f"Unknown product type: {product_type}")

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

        self.logger.debug(f"Writing {service_name.boto3_name}")
        package_writer = PackageWriter(
            output_path=self.output_path, generate_setup=self.generate_setup
        )
        package_writer.write_service_package(
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
        package_writer = PackageWriter(
            output_path=self.output_path, generate_setup=self.generate_setup
        )
        package_writer.write_service_docs(
            service_package,
            templates_path=templates_path,
        )
        return service_package

    def _generate_service(self, service_name: ServiceName) -> ServicePackage:
        pypi_name = self.service_package_data.get_service_pypi_name(service_name)
        version = self._get_package_version(pypi_name, self.version)
        if not version:
            return ServicePackage(self.service_package_data, service_name)

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
