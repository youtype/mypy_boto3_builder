"""
Structure for types-aioboto3 module.
"""

from collections.abc import Iterable

from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.package_data import BasePackageData
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.class_record import ClassRecord
from mypy_boto3_builder.structures.package import Package
from mypy_boto3_builder.structures.service_package import ServicePackage
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral


class TypesAioBoto3Package(Package):
    """
    Structure for types-aioboto3 module.
    """

    def __init__(
        self,
        data: type[BasePackageData],
        session_class: ClassRecord | None = None,
        service_names: Iterable[ServiceName] = tuple(),
        service_packages: Iterable[ServicePackage] = tuple(),
    ):
        super().__init__(data)
        self.session_class = session_class or ClassRecord("Session")
        self.service_names = list(service_names)
        self.service_packages = list(service_packages)

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
        Get import reciords for `session.py[i]`.
        """
        import_records: set[ImportRecord] = set(
            [
                ImportRecord(
                    ImportString("aioboto3", "resources", "factory"), "AIOBoto3ResourceFactory"
                ),
                ImportRecord(ImportString("aiobotocore", "config"), "AioConfig"),
                ImportRecord(ImportString("botocore", "credentials"), "Credentials"),
                ImportRecord(ImportString("botocore", "loaders"), "Loader"),
                ImportRecord(ImportString("botocore", "session"), "Session", "BotocoreSession"),
                ImportRecord(ImportString("typing"), "Any"),
                ImportRecord(ImportString("typing"), "List"),
                ImportRecord(ImportString("typing"), "Optional"),
                ImportRecord(ImportString("typing"), "Union"),
                ImportRecord(ImportString("sys")),
                TypeLiteral.get_typing_import_record(),
            ]
        )
        import_records.update(self.session_class.get_required_import_records())
        return list(sorted(import_records))

    def get_all_names(self) -> list[str]:
        """
        Get names for `__all__` directive.
        """
        result = [
            "Session",
        ]
        return list(sorted(result))
