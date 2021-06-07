"""
Structure for boto3-stubs module.
"""

from typing import Iterable, List, Optional, Set

from mypy_boto3_builder.constants import BOTO3_STUBS_NAME
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.class_record import ClassRecord
from mypy_boto3_builder.structures.function import Function
from mypy_boto3_builder.structures.package import Package
from mypy_boto3_builder.structures.service_package import ServicePackage


class Boto3StubsPackage(Package):
    """
    Structure for boto3-stubs module.
    """

    def __init__(
        self,
        name: str = BOTO3_STUBS_NAME,
        pypi_name: str = BOTO3_STUBS_NAME,
        session_class: Optional[ClassRecord] = None,
        service_names: Iterable[ServiceName] = tuple(),
        service_packages: Iterable[ServicePackage] = tuple(),
        init_functions: Iterable[Function] = tuple(),
    ):
        super().__init__(name=name, pypi_name=pypi_name)
        self.session_class = session_class or ClassRecord("Session")
        self.service_names = list(service_names)
        self.service_packages = list(service_packages)
        self.init_functions = list(init_functions)

    @property
    def essential_service_names(self) -> List[ServiceName]:
        result: List[ServiceName] = []
        for service_name in self.service_names:
            if service_name.is_essential():
                result.append(service_name)
        return result

    def get_init_required_import_records(self) -> List[ImportRecord]:
        import_records: Set[ImportRecord] = set(
            [
                ImportRecord(ImportString("logging")),
                ImportRecord(ImportString("typing"), "Any"),
                ImportRecord(ImportString("sys")),
                ImportRecord(ImportString("importlib", "util")),
                ImportRecord(ImportString("boto3", "session")),
                ImportRecord(ImportString("boto3", "session"), "Session"),
                ImportRecord(
                    ImportString("typing"),
                    "Literal",
                    min_version=(3, 8),
                    fallback=ImportRecord(ImportString("typing_extensions"), "Literal"),
                ),
            ]
        )
        for init_function in self.init_functions:
            import_records.update(init_function.get_required_import_records())

        return list(sorted(import_records))

    def get_session_required_import_records(self) -> List[ImportRecord]:
        import_records: Set[ImportRecord] = set(
            [
                ImportRecord(ImportString("sys")),
                ImportRecord(ImportString("typing"), "Any"),
                ImportRecord(ImportString("typing"), "List"),
                ImportRecord(ImportString("boto3")),
                ImportRecord(ImportString("boto3", "utils")),
                ImportRecord(ImportString("boto3", "resources", "factory"), "ResourceFactory"),
                ImportRecord(ImportString("boto3", "exceptions"), "ResourceNotExistsError"),
                ImportRecord(ImportString("boto3", "exceptions"), "UnknownAPIVersionError"),
                ImportRecord(ImportString("botocore", "session")),
                ImportRecord(ImportString("botocore", "credentials"), "Credentials"),
                ImportRecord(ImportString("botocore", "loaders"), "Loader"),
                ImportRecord(ImportString("botocore", "model"), "ServiceModel"),
                ImportRecord(ImportString("botocore", "session"), "Session", "BotocoreSession"),
                ImportRecord(ImportString("botocore", "client"), "Config"),
                ImportRecord(ImportString("botocore", "exceptions"), "DataNotFoundError"),
                ImportRecord(ImportString("botocore", "exceptions"), "UnknownServiceError"),
                ImportRecord(
                    ImportString("typing"),
                    "Literal",
                    min_version=(3, 8),
                    fallback=ImportRecord(ImportString("typing_extensions"), "Literal"),
                ),
            ]
        )
        import_records.update(self.session_class.get_required_import_records())
        return list(sorted(import_records))

    def get_all_names(self) -> List[str]:
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
