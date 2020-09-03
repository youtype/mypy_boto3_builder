"""
Structure for boto3-stubs module.
"""

from dataclasses import dataclass, field
from typing import List, Set

from mypy_boto3_builder.constants import BOTO3_STUBS_NAME
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.class_record import ClassRecord
from mypy_boto3_builder.structures.function import Function
from mypy_boto3_builder.structures.package import Package
from mypy_boto3_builder.structures.service_package import ServicePackage


@dataclass
class Boto3StubsPackage(Package):
    """
    Structure for boto3-stubs module.
    """

    name: str = BOTO3_STUBS_NAME
    pypi_name: str = BOTO3_STUBS_NAME
    session_class: ClassRecord = field(default_factory=lambda: ClassRecord("Session"))
    service_names: List[ServiceName] = field(default_factory=lambda: [])
    service_packages: List[ServicePackage] = field(default_factory=lambda: [])
    init_functions: List[Function] = field(default_factory=lambda: [])

    @property
    def essential_service_names(self) -> List[ServiceName]:
        result: List[ServiceName] = []
        for service_name in self.service_names:
            if service_name.is_essential():
                result.append(service_name)
        return result

    def get_init_required_import_records(self) -> List[ImportRecord]:
        import_records: Set[ImportRecord] = set()
        import_records.update(
            [
                ImportRecord(ImportString("logging")),
                ImportRecord(ImportString("typing"), "Any"),
                ImportRecord(ImportString("sys")),
                ImportRecord(ImportString("importlib", "util")),
                ImportRecord(ImportString("boto3", "session")),
                ImportRecord(ImportString("boto3", "session"), "Session"),
            ]
        )
        for init_function in self.init_functions:
            import_records.update(init_function.get_required_import_records())

        return list(sorted(import_records))

    def get_session_required_import_records(self) -> List[ImportRecord]:
        import_records: Set[ImportRecord] = set()
        import_records.update(
            [
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
                ImportRecord(ImportString("botocore", "client"), "Config"),
                ImportRecord(ImportString("botocore", "exceptions"), "DataNotFoundError"),
                ImportRecord(ImportString("botocore", "exceptions"), "UnknownServiceError"),
            ]
        )
        import_records.update(self.session_class.get_required_import_records())
        return list(sorted(import_records))
