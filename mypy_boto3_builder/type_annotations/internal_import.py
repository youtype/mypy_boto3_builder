"""
Wrapper for simple type annotations from this module.

Copyright 2024 Vlad Emelianov
"""

from typing import Self

from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
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
        service_name: ServiceName | None = None,
        module_name: ServiceModuleName = ServiceModuleName.service_resource,
        *,
        stringify: bool = True,
        use_alias: bool = False,
    ) -> None:
        self.name: str = name
        self.service_name: ServiceName | None = service_name
        self.module_name: ServiceModuleName = module_name
        self.stringify: bool = stringify
        self.use_alias: bool = use_alias

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

    def render(self) -> str:
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

    def __copy__(self) -> Self:
        """
        Create a copy of type annotation wrapper.
        """
        return self.__class__(
            self.name,
            self.service_name,
            self.module_name,
            use_alias=self.use_alias,
            stringify=self.stringify,
        )
