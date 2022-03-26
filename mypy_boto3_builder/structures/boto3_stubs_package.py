"""
Structure for boto3-stubs module.
"""

from collections.abc import Iterable

from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.package_data import BasePackageData
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.class_record import ClassRecord
from mypy_boto3_builder.structures.function import Function
from mypy_boto3_builder.structures.package import Package
from mypy_boto3_builder.structures.service_package import ServicePackage
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral


class Boto3StubsPackage(Package):
    """
    Structure for boto3-stubs module.
    """

    def __init__(
        self,
        data: type[BasePackageData],
        session_class: ClassRecord | None = None,
        service_names: Iterable[ServiceName] = tuple(),
        service_packages: Iterable[ServicePackage] = tuple(),
        init_functions: Iterable[Function] = tuple(),
        literals: Iterable[TypeLiteral] = tuple(),
    ):
        super().__init__(data)
        self.session_class = session_class or ClassRecord("Session")
        self.service_names = list(service_names)
        self.service_packages = list(service_packages)
        self.init_functions = list(init_functions)
        self.literals = list(literals)

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

    def get_init_required_import_records(self) -> list[ImportRecord]:
        """
        Get import records for `__init__.py[i]`.
        """
        import_records: set[ImportRecord] = set(
            [
                ImportRecord(ImportString("logging")),
                ImportRecord(ImportString("typing"), "Any"),
                ImportRecord(ImportString("sys")),
                ImportRecord(ImportString("importlib", "util")),
                ImportRecord(ImportString("boto3", "session"), alias="session"),
                ImportRecord(ImportString("boto3", "session"), "Session"),
                TypeLiteral.get_typing_import_record(),
            ]
        )
        for init_function in self.init_functions:
            import_records.update(init_function.get_required_import_records())

        return list(sorted(import_records))

    def get_session_required_import_records(self) -> list[ImportRecord]:
        """
        Get import reciords for `session.py[i]`.
        """
        import_records: set[ImportRecord] = set(
            [
                ImportRecord(ImportString("sys")),
                ImportRecord(ImportString("typing"), "Any"),
                ImportRecord(ImportString("typing"), "List"),
                ImportRecord(ImportString("typing"), "Optional"),
                ImportRecord(ImportString("boto3")),
                ImportRecord(ImportString("boto3", "utils")),
                ImportRecord(ImportString("boto3", "resources", "factory"), "ResourceFactory"),
                ImportRecord(
                    ImportString("boto3", "exceptions"),
                    "ResourceNotExistsError",
                    "ResourceNotExistsError",
                ),
                ImportRecord(
                    ImportString("boto3", "exceptions"),
                    "UnknownAPIVersionError",
                    "UnknownAPIVersionError",
                ),
                ImportRecord(ImportString("botocore", "session")),
                ImportRecord(ImportString("botocore", "credentials"), "Credentials"),
                ImportRecord(ImportString("botocore", "loaders"), "Loader"),
                ImportRecord(ImportString("botocore", "model"), "ServiceModel", "ServiceModel"),
                ImportRecord(ImportString("botocore", "session"), "Session", "BotocoreSession"),
                ImportRecord(ImportString("botocore", "client"), "Config"),
                ImportRecord(
                    ImportString("botocore", "exceptions"), "DataNotFoundError", "DataNotFoundError"
                ),
                ImportRecord(
                    ImportString("botocore", "exceptions"),
                    "UnknownServiceError",
                    "UnknownServiceError",
                ),
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
            "session",
            "Session",
            "DEFAULT_SESSION",
            "setup_default_session",
            "set_stream_logger",
            "NullHandler",
            "client",
            "resource",
        ]
        return list(sorted(result))
