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
        use_alias -- Use name alias.
    """

    def __init__(
        self,
        name: str,
        service_name: ServiceName | None = None,
        module_name: ServiceModuleName = ServiceModuleName.service_resource,
        *,
        use_alias: bool = False,
    ) -> None:
        self.name: str = name
        self.service_name: ServiceName | None = service_name
        self.module_name: ServiceModuleName = module_name
        self.use_alias: bool = use_alias

    @property
    def alias_name(self) -> str:
        """
        Import name alias.
        """
        return f"_{self.name}"

    def render(self) -> str:
        """
        Render type annotation to a valid Python code for local usage.

        Returns:
            A string with a valid type annotation.
        """
        if self.use_alias:
            return self.alias_name

        return self.name

    def __copy__(self) -> Self:
        """
        Create a copy of type annotation wrapper.
        """
        return self.__class__(
            self.name,
            self.service_name,
            self.module_name,
            use_alias=self.use_alias,
        )
