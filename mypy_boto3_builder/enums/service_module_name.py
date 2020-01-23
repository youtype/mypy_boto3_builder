import enum


class ServiceModuleName(enum.Enum):
    """
    Enum for service modules.
    """

    client = "client"
    service_resource = "service_resource"
    paginator = "paginator"
    waiter = "waiter"
    type_defs = "type_defs"

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
        return f"{self.file_name}.jinja2"
