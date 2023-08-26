"""
Structure for types-aiobotocore module.
"""

from collections.abc import Iterable

from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.package_data import BasePackageData
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.class_record import ClassRecord
from mypy_boto3_builder.structures.function import Function
from mypy_boto3_builder.structures.package import Package
from mypy_boto3_builder.structures.service_package import ServicePackage


class AioBotocoreStubsPackage(Package):
    """
    Structure for types-aiobotocore module.
    """

    def __init__(
        self,
        data: type[BasePackageData],
        session_class: ClassRecord | None = None,
        service_names: Iterable[ServiceName] = (),
        service_packages: Iterable[ServicePackage] = (),
        init_functions: Iterable[Function] = (),
    ):
        super().__init__(data)
        self.session_class = session_class or ClassRecord("Session")
        self.service_names = list(service_names)
        self.service_packages = list(service_packages)
        self.init_functions = list(init_functions)

    @property
    def essential_service_names(self) -> list[ServiceName]:
        """
        Service names marked as essential.
        """
        result: list[ServiceName] = []
        for service_name in self.service_names:
            if service_name.is_essential():
                result.append(service_name)
        return result

    def get_session_required_import_records(self) -> list[ImportRecord]:
        """
        Get import records for `session.py[i]`.
        """
        import_records = self.session_class.get_required_import_records()
        return sorted(import_records)

    def get_all_names(self) -> list[str]:
        """
        Get names for `__all__` directive.
        """
        result = [
            "get_session",
            "Session",
        ]
        return sorted(result)
