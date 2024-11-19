"""
Enum for service modules.

Copyright 2024 Vlad Emelianov
"""

from enum import Enum


class ServiceModuleName(Enum):
    """
    Enum for service modules.
    """

    client = "client"
    service_resource = "service_resource"
    paginator = "paginator"
    waiter = "waiter"
    type_defs = "type_defs"
    literals = "literals"

    @property
    def stub_file_name(self) -> str:
        """
        Module file name.
        """
        return f"{self.value}.pyi"

    @property
    def file_name(self) -> str:
        """
        Module file name.
        """
        return f"{self.value}.py"

    @property
    def template_name(self) -> str:
        """
        Module template file name.
        """
        return f"{self.value}.pyi.jinja2"
