"""
Structure for aiobotocore-stubs module.
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


class AioBotocoreStubsPackage(Package):
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
        Get import reciords for `session.py[i]`.
        """
        import_records: set[ImportRecord] = set(
            [
                ImportRecord(
                    ImportString("aiobotocore", "client"), "AioBaseClient", "AioBaseClient"
                ),
                ImportRecord(
                    ImportString("aiobotocore", "client"), "AioClientCreator", "AioClientCreator"
                ),
                ImportRecord(
                    ImportString("aiobotocore", "credentials"), "AioCredentials", "AioCredentials"
                ),
                ImportRecord(
                    ImportString("aiobotocore", "credentials"),
                    "create_credential_resolver",
                    "create_credential_resolver",
                ),
                ImportRecord(
                    ImportString("aiobotocore", "handlers"),
                    "inject_presigned_url_ec2",
                    "inject_presigned_url_ec2",
                ),
                ImportRecord(
                    ImportString("aiobotocore", "handlers"),
                    "inject_presigned_url_rds",
                    "inject_presigned_url_rds",
                ),
                ImportRecord(
                    ImportString("aiobotocore", "hooks"),
                    "AioHierarchicalEmitter",
                    "AioHierarchicalEmitter",
                ),
                ImportRecord(
                    ImportString("aiobotocore", "parsers"),
                    "AioResponseParserFactory",
                    "AioResponseParserFactory",
                ),
                ImportRecord(
                    ImportString("aiobotocore", "signers"),
                    "add_generate_db_auth_token",
                    "add_generate_db_auth_token",
                ),
                ImportRecord(
                    ImportString("aiobotocore", "signers"),
                    "add_generate_presigned_post",
                    "add_generate_presigned_post",
                ),
                ImportRecord(
                    ImportString("aiobotocore", "signers"),
                    "add_generate_presigned_url",
                    "add_generate_presigned_url",
                ),
                ImportRecord(ImportString("botocore", "model"), "ServiceModel"),
                ImportRecord(ImportString("botocore", "session"), "Session"),
                ImportRecord(ImportString("typing"), "Any"),
                ImportRecord(ImportString("typing"), "List"),
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
            "get_session",
            "Session",
        ]
        return list(sorted(result))
