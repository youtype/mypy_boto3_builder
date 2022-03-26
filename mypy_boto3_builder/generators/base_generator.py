"""
Base stubs/docs generator.
"""
from abc import ABC, abstractmethod
from collections.abc import Sequence
from pathlib import Path

from boto3.session import Session

from mypy_boto3_builder.constants import ProductType
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.package_data import BasePackageData
from mypy_boto3_builder.parsers.service_package import parse_service_package
from mypy_boto3_builder.parsers.service_package_postprocessor import ServicePackagePostprocessor
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.service_package import ServicePackage
from mypy_boto3_builder.utils.boto3_utils import get_boto3_resource
from mypy_boto3_builder.utils.pypi_manager import PyPIManager
from mypy_boto3_builder.writers.package_writer import PackageWriter


class BaseGenerator(ABC):
    """
    Base stubs/docs generator.

    Arguments:
        service_names -- Selected service names
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
        self.master_service_names = master_service_names
        self.output_path = output_path
        self.logger = get_logger()
        self.generate_setup = generate_setup
        self.skip_published = skip_published
        self.disable_smart_version = disable_smart_version
        self.version = version or self.get_library_version()
        self._enrich_service_names()

    @abstractmethod
    def get_library_version(self) -> str:
        """
        Get underlying library version.
        """
        raise NotImplementedError()

    def _get_package_version(self, pypi_name: str, version: str) -> str | None:
        pypi_manager = PyPIManager(pypi_name)
        if not pypi_manager.has_version(version):
            return version

        if self.skip_published:
            return None
        if self.disable_smart_version:
            return version

        return pypi_manager.get_next_version(version)

    def _enrich_service_names(self) -> None:
        for service_name in self.service_names:
            service_name.has_service_resource = bool(get_boto3_resource(self.session, service_name))
        for service_name in self.master_service_names:
            service_name.has_service_resource = bool(get_boto3_resource(self.session, service_name))

    @abstractmethod
    def generate_stubs(self) -> None:
        """
        Generate main stubs.
        """
        raise NotImplementedError()

    @abstractmethod
    def generate_service_stubs(self) -> None:
        """
        Generate service stubs.
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
        methods_map = {
            ProductType.stubs: self.generate_stubs,
            ProductType.service_stubs: self.generate_service_stubs,
            ProductType.docs: self.generate_docs,
        }

        methods_map[product_type]()

    def _get_available_regions(self) -> list[str]:
        """
        Get a sorted list of all available regions.
        """
        result = set()
        for service_name in self.master_service_names:
            result.update(self.session.get_available_regions(service_name.boto3_name))
        return list(sorted(result))

    def _parse_service_package(
        self,
        service_name: ServiceName,
        version: str | None,
        package_data: type[BasePackageData],
    ) -> ServicePackage:
        self.logger.debug(f"Parsing {service_name.boto3_name}")
        service_package = parse_service_package(self.session, service_name, package_data)
        if version:
            service_package.version = version

        postprocessor = ServicePackagePostprocessor(
            self.session, service_package, self.master_service_names
        )
        postprocessor.generate_docstrings()

        if package_data.IS_ASYNC:
            postprocessor.make_async()
            postprocessor.add_contextmanager_methods()

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
