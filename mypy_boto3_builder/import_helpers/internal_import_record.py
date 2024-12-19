"""
Helper for Python import strings without parent module name.

Copyright 2024 Vlad Emelianov
"""

from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.import_helpers.import_helper import Import
from mypy_boto3_builder.import_helpers.import_record import ImportRecord


class InternalImportRecord(ImportRecord):
    """
    Helper for Python import strings without parent module name.

    Arguments:
        service_module_name -- Service module name.
        name -- Import name.
        alias -- Import local name.
    """

    def __init__(
        self,
        service_module_name: ServiceModuleName,
        name: str = "",
        alias: str = "",
    ) -> None:
        source = Import.local(service_module_name.name)
        super().__init__(source, name=name, alias=alias)
