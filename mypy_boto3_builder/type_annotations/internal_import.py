"""
Wrapper for simple type annotations from this module.
"""
from typing import Optional

from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.internal_import_record import (
    InternalImportRecord,
)
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.enums.service_module_name import ServiceModuleName


class InternalImport(FakeAnnotation):
    """
    Wrapper for simple type annotations from this module.

    Arguments:
        name -- Import name.
        service_name -- Service that import belongs to.
        module_name -- Service module name.
    """

    def __init__(
        self,
        name: str,
        service_name: Optional[ServiceName] = None,
        module_name: ServiceModuleName = ServiceModuleName.service_resource,
    ) -> None:
        self.name = name
        self.service_name = service_name
        self.module_name = module_name

    def render(self, parent_name: str = "") -> str:
        """
        Render type annotation to a valid Python code for local usage.

        Returns:
            A string with a valid type annotation.
        """
        return f'"{self.scope}.{self.name}"'

    @property
    def scope(self) -> str:
        return f"{self.module_name.name}_scope"

    def get_import_record(self) -> ImportRecord:
        """
        Get import record required for using type annotation.
        """
        if self.service_name is not None:
            return ImportRecord(
                source=ImportString(
                    self.service_name.module_name, self.module_name.name
                ),
                alias=self.scope,
            )
        return InternalImportRecord(self.module_name, alias=self.scope)

    def copy(self) -> "InternalImport":
        """
        Create a copy of type annotation wrapper.
        """
        return InternalImport(self.name, self.service_name, self.module_name)
