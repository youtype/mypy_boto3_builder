"""
PyPI package data constants.
"""

from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.utils.version import (
    get_aiobotocore_version,
    get_boto3_version,
    get_botocore_version,
)


class BasePackageData:
    """
    Generic package data.
    """

    NAME: str = "boto3-stubs"
    PYPI_NAME: str = "boto3-stubs"
    PYPI_LITE_NAME: str = ""
    LIBRARY_NAME: str = "boto3"
    SERVICE_PREFIX: str = "mypy_boto3"
    SERVICE_PYPI_PREFIX: str = "mypy-boto3"
    LOCAL_DOC_LINK: str = "https://vemel.github.io/boto3_stubs_docs/"

    @classmethod
    def get_service_package_name(cls, service_name: ServiceName) -> str:
        """
        Get service package name.
        """
        return f"{cls.SERVICE_PREFIX}_{service_name.underscore_name}"

    @classmethod
    def get_service_pypi_name(cls, service_name: ServiceName) -> str:
        """
        Get service package PyPI name.
        """
        return f"{cls.SERVICE_PYPI_PREFIX}-{service_name.name}"

    @staticmethod
    def get_library_version() -> str:
        """
        Get underlying library version.
        """
        return get_boto3_version()

    @classmethod
    def get_service_pypi_link(cls, service_name: ServiceName) -> str:
        """
        Get link to PyPI.
        """
        return f"https://pypi.org/project/{cls.get_service_pypi_name(service_name)}/"


class BotocoreStubsPackageData(BasePackageData):
    """
    botocore-stubs package data.
    """

    NAME = "botocore-stubs"
    PYPI_NAME = "botocore-stubs"
    LIBRARY_NAME = "botocore"

    @staticmethod
    def get_library_version() -> str:
        """
        Get underlying library version.
        """
        return get_botocore_version()


class TypesAioBotocorePackageData(BasePackageData):
    """
    aiobotocore-stubs package data.
    """

    NAME = "aiobotocore-stubs"
    PYPI_NAME = "types-aiobotocore"
    PYPI_LITE_NAME = "types-aiobotocore-lite"
    LIBRARY_NAME = "aiobotocore"
    SERVICE_PREFIX = "types_aiobotocore"
    SERVICE_PYPI_PREFIX = "types-aiobotocore"
    LOCAL_DOC_LINK = "https://vemel.github.io/types_aiobotocore_docs/"

    @staticmethod
    def get_library_version() -> str:
        """
        Get underlying library version.
        """
        return get_aiobotocore_version()


class TypesAioBotocoreLitePackageData(TypesAioBotocorePackageData):
    """
    types-aiobotocore-lite package data.
    """

    PYPI_NAME = "types-aiobotocore-lite"
    PYPI_LITE_NAME = ""


class Boto3StubsPackageData(BasePackageData):
    """
    boto3-stubs package data.
    """

    NAME = "boto3-stubs"
    PYPI_NAME = "boto3-stubs"
    PYPI_LITE_NAME = "boto3-stubs-lite"
    LIBRARY_NAME = "boto3"
    LOCAL_DOC_LINK = "https://vemel.github.io/boto3_stubs_docs/"


class Boto3StubsLitePackageData(Boto3StubsPackageData):
    """
    boto3-stubs-lite package data.
    """

    PYPI_NAME = "boto3-stubs-lite"
    PYPI_LITE_NAME = ""


class MypyBoto3PackageData(BasePackageData):
    """
    mypy-boto3 package data.
    """

    NAME = "mypy_boto3"
    PYPI_NAME = "mypy-boto3"
    LIBRARY_NAME = "boto3"
