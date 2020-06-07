"""
Helper for Python import strings with not set master module name.
"""
from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.import_string import ImportString


class InternalImportRecord(ImportRecord):
    """
    Helper for Python import strings with not set master module name.

    Arguments:
        service_module_name -- Service module name.
        name -- Import name.
        alias -- Import local name.
    """

    def __init__(self, service_module_name: ServiceModuleName, name: str = "", alias: str = ""):
        super().__init__(ImportString(service_module_name.name), name=name, alias=alias)

    def get_external(self, module_name: str) -> ImportRecord:
        """
        Get full import record with `module_name` set as master module.

        Arguments:
            module_name -- Master module import string.

        Returns:
            A new non-internal ImportRecord.
        """
        source = ImportString(module_name) + self.source
        return ImportRecord(source=source, name=self.name, alias=self.alias,)
