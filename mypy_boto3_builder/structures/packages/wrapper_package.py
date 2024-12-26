"""
Structure for boto3-stubs module.

Copyright 2024 Vlad Emelianov
"""

from abc import ABC, abstractmethod
from collections.abc import Iterable
from typing import TYPE_CHECKING

from mypy_boto3_builder.constants import PACKAGE_NAME
from mypy_boto3_builder.import_helpers.import_record_group import ImportRecordGroup
from mypy_boto3_builder.package_data import BasePackageData
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.class_record import ClassRecord
from mypy_boto3_builder.structures.package import Package
from mypy_boto3_builder.utils.install_requires import InstallRequires
from mypy_boto3_builder.utils.version import get_builder_version

if TYPE_CHECKING:
    from mypy_boto3_builder.structures.function import Function
    from mypy_boto3_builder.structures.packages.service_package import ServicePackage
    from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral


class WrapperPackage(Package, ABC):
    """
    Main package module data.
    """

    def __init__(
        self,
        data: BasePackageData,
        service_names: Iterable[ServiceName],
        version: str,
    ) -> None:
        super().__init__(data, service_names, version)
        self.session_class = ClassRecord("Session")
        self.service_packages: list[ServicePackage] = []
        self.init_functions: list[Function] = []
        self.literals: list[TypeLiteral] = []
        self.setup_package_data: dict[str, tuple[str, ...]] = (
            {self.data.name: ("py.typed", "*.pyi", "*/*.pyi")} if self.data.name else {}
        )
        self._description = self.get_short_description()
        self.install_requires = InstallRequires(self.data.install_requires)

    @property
    def description(self) -> str:
        """
        Package description for setup.py.
        """
        return self._description

    def set_description(self, value: str) -> None:
        """
        Set package description for setup.py.
        """
        self._description = value

    def get_init_required_import_records(self) -> ImportRecordGroup:
        """
        Get import record group for `__init__.py[i]`.
        """
        result = ImportRecordGroup()
        for init_function in self.init_functions:
            result.add(*init_function.get_required_import_records())

        return result

    def get_session_required_import_records(self) -> ImportRecordGroup:
        """
        Get import record group for `session.py[i]`.
        """
        return ImportRecordGroup(self.session_class.get_required_import_records())

    @abstractmethod
    def get_all_names(self) -> list[str]:
        """
        Get names for `__all__` directive.
        """
        raise NotImplementedError("Method should be implemented in child class")

    def get_short_description(self, prefix: str = "Type annotations") -> str:
        """
        Get short description for the package in setup.py.
        """
        return (
            f"{prefix} for {self.library_name} {self.library_version}"
            f" generated with {PACKAGE_NAME} {get_builder_version()}"
        )
