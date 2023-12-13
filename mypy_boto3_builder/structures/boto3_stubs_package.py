"""
Structure for boto3-stubs module.
"""

from mypy_boto3_builder.structures.wrapper_package import WrapperPackage


class Boto3StubsPackage(WrapperPackage):
    """
    Structure for boto3-stubs module.
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
