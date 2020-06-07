"""
Wrapper for simple type annotations from this module.
"""
from typing import Optional

from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation


class InternalImport(FakeAnnotation):
    """
    Wrapper for simple type annotations from this module.

    Arguments:
        name -- Import name.
        service_name -- Service that import belongs to.
        module_name -- Service module name.
        stringify -- Convert type annotation to string to avoid circular deps.
        use_alias -- Use name alias.
    """

    def __init__(
        self,
        name: str,
        service_name: Optional[ServiceName] = None,
        module_name: ServiceModuleName = ServiceModuleName.service_resource,
        stringify: bool = True,
        use_alias: bool = False,
    ) -> None:
        self.name = name
        self.service_name = service_name
        self.module_name = module_name
        self.stringify = stringify
        self.use_alias = use_alias

    @staticmethod
    def get_alias(name: str) -> str:
        """
        Get import name alias.

        Arguments:
            name -- Original name.

        Returns:
            Name prefixed with underscore.
        """
        return f"_{name}"

    def render(self, parent_name: str = "") -> str:
        """
        Render type annotation to a valid Python code for local usage.

        Returns:
            A string with a valid type annotation.
        """
        result = self.name
        if self.use_alias:
            result = self.get_alias(self.name)

        if self.stringify:
            return f'"{result}"'

        return result

    def get_import_record(self) -> ImportRecord:
        """
        Get import record required for using type annotation.
        """
        return ImportRecord.empty()

    def copy(self) -> "InternalImport":
        """
        Create a copy of type annotation wrapper.
        """
        return InternalImport(
            self.name,
            self.service_name,
            self.module_name,
            use_alias=self.use_alias,
            stringify=self.stringify,
        )


class AliasInternalImport(InternalImport):
    """
    Internal import for safe local usages.

    Arguments:
        name -- Import name.
        service_name -- Service that import belongs to.
    """

    def __init__(self, name: str, service_name: Optional[ServiceName] = None) -> None:
        super().__init__(
            name=name,
            service_name=service_name,
            module_name=ServiceModuleName.service_resource,
            stringify=False,
            use_alias=True,
        )
