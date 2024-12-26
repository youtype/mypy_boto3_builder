"""
Structure for types-boto3 module.

Copyright 2024 Vlad Emelianov
"""

from mypy_boto3_builder.structures.packages.wrapper_package import WrapperPackage


class TypesBoto3Package(WrapperPackage):
    """
    Structure for types-boto3 module.
    """

    def get_all_names(self) -> list[str]:
        """
        Get names for `__all__` directive.
        """
        result = [
            "session",
            "Session",
            "DEFAULT_SESSION",
            "setup_default_session",
            "set_stream_logger",
            "NullHandler",
            "client",
            "resource",
        ]
        return sorted(result)
