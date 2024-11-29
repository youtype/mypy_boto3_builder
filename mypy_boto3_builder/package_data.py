"""
PyPI package data constants.

Copyright 2024 Vlad Emelianov
"""

import typing
from typing import ClassVar

from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.utils.version_getters import (
    get_aioboto3_version,
    get_aiobotocore_version,
    get_boto3_version,
    get_botocore_version,
)


class BasePackageData:
    """
    Generic package data.
    """

    NAME: ClassVar[str] = "boto3-stubs"
    PYPI_NAME: ClassVar[str] = "boto3-stubs"
    PYPI_STUBS_NAME: ClassVar[str] = ""
    PYPI_LITE_NAME: ClassVar[str] = ""
    PYPI_FULL_NAME: ClassVar[str] = ""
    LIBRARY_NAME: ClassVar[str] = "boto3"
    SERVICE_PREFIX: ClassVar[str] = "mypy_boto3"
    SERVICE_PYPI_PREFIX: ClassVar[str] = "mypy-boto3"
    LOCAL_DOC_LINK: ClassVar[str] = "https://youtype.github.io/boto3_stubs_docs/"
    IS_VSCODE_SUPPORTED: ClassVar[bool] = False
    IS_CONDA_FORGE_SUPPORTED: ClassVar[bool] = False

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

    @staticmethod
    def get_botocore_version() -> str:
        """
        Get underlying botocore version.
        """
        return get_botocore_version()

    @classmethod
    def has_pypi_lite_package(cls) -> bool:
        """
        Check if package has lite version.
        """
        return bool(cls.PYPI_LITE_NAME)


class TypesBoto3PackageData(BasePackageData):
    """
    types-boto3 package data.
    """

    NAME = "boto3-stubs"
    PYPI_NAME = "types-boto3"
    PYPI_STUBS_NAME = "types-boto3"
    PYPI_LITE_NAME = "types-boto3-lite"
    PYPI_FULL_NAME = "types-boto3-full"
    LIBRARY_NAME = "boto3"
    SERVICE_PREFIX = "types_boto3"
    SERVICE_PYPI_PREFIX = "types-boto3"
    LOCAL_DOC_LINK = "https://youtype.github.io/types_boto3_docs/"
    IS_VSCODE_SUPPORTED = True
    IS_CONDA_FORGE_SUPPORTED = False


class TypesBoto3LitePackageData(TypesBoto3PackageData):
    """
    types-boto3-lite package data.
    """

    PYPI_NAME = TypesBoto3PackageData.PYPI_LITE_NAME
    PYPI_LITE_NAME = ""


class TypesBoto3FullPackageData(TypesBoto3PackageData):
    """
    boto3-stubs-full package data.
    """

    NAME = ""
    PYPI_NAME = TypesBoto3PackageData.PYPI_FULL_NAME
    IS_CONDA_FORGE_SUPPORTED = False

    @typing.override
    @classmethod
    def get_service_pypi_name(cls, service_name: ServiceName) -> str:
        """
        Get service package PyPI name.
        """
        return cls.PYPI_NAME


class TypesAioBotocorePackageData(BasePackageData):
    """
    types-aiobotocore package data.
    """

    NAME = "aiobotocore-stubs"
    PYPI_NAME = "types-aiobotocore"
    PYPI_STUBS_NAME = "types-aiobotocore"
    PYPI_LITE_NAME = "types-aiobotocore-lite"
    PYPI_FULL_NAME = "types-aiobotocore-full"
    LIBRARY_NAME = "aiobotocore"
    SERVICE_PREFIX = "types_aiobotocore"
    SERVICE_PYPI_PREFIX = "types-aiobotocore"
    LOCAL_DOC_LINK = "https://youtype.github.io/types_aiobotocore_docs/"

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


class TypesAioBotocoreFullPackageData(TypesAioBotocorePackageData):
    """
    types-aiobotocore-full package data.
    """

    NAME = ""
    PYPI_NAME = "types-aiobotocore-full"
    IS_CONDA_FORGE_SUPPORTED = False

    @typing.override
    @classmethod
    def get_service_pypi_name(cls, service_name: ServiceName) -> str:
        """
        Get service package PyPI name.
        """
        return cls.PYPI_NAME


class Boto3StubsPackageData(BasePackageData):
    """
    boto3-stubs package data.
    """

    NAME = "boto3-stubs"
    PYPI_NAME = "boto3-stubs"
    PYPI_STUBS_NAME = "boto3-stubs"
    PYPI_LITE_NAME = "boto3-stubs-lite"
    PYPI_FULL_NAME = "boto3-stubs-full"
    LIBRARY_NAME = "boto3"
    LOCAL_DOC_LINK = "https://youtype.github.io/boto3_stubs_docs/"
    IS_VSCODE_SUPPORTED = True
    IS_CONDA_FORGE_SUPPORTED = True


class Boto3StubsLitePackageData(Boto3StubsPackageData):
    """
    boto3-stubs-lite package data.
    """

    PYPI_NAME = Boto3StubsPackageData.PYPI_LITE_NAME
    PYPI_LITE_NAME = ""


class Boto3StubsFullPackageData(Boto3StubsPackageData):
    """
    boto3-stubs-full package data.
    """

    NAME = ""
    PYPI_NAME = Boto3StubsPackageData.PYPI_FULL_NAME
    IS_CONDA_FORGE_SUPPORTED = False

    @typing.override
    @classmethod
    def get_service_pypi_name(cls, service_name: ServiceName) -> str:
        """
        Get service package PyPI name.
        """
        return cls.PYPI_NAME


class MypyBoto3PackageData(BasePackageData):
    """
    mypy-boto3 package data.
    """

    NAME = "mypy_boto3"
    PYPI_NAME = "mypy-boto3"
    LIBRARY_NAME = "boto3"


class TypesAioBoto3PackageData(BasePackageData):
    """
    types-aioboto3 package data.
    """

    NAME = "aioboto3-stubs"
    PYPI_NAME = "types-aioboto3"
    PYPI_STUBS_NAME = "types-aioboto3"
    PYPI_LITE_NAME = "types-aioboto3-lite"
    PYPI_FULL_NAME = "types-aiobotocore-full"
    LIBRARY_NAME = "aioboto3"
    SERVICE_PREFIX = "types_aiobotocore"
    SERVICE_PYPI_PREFIX = "types-aiobotocore"
    AIOBOTOCORE_NAME = "types-aiobotocore"
    LOCAL_DOC_LINK = "https://youtype.github.io/types_aioboto3_docs/"

    @staticmethod
    def get_library_version() -> str:
        """
        Get underlying library version.
        """
        return get_aioboto3_version()


class TypesAioBoto3LitePackageData(TypesAioBoto3PackageData):
    """
    types-aioboto3-lite package data.
    """

    PYPI_NAME = "types-aioboto3-lite"
    PYPI_LITE_NAME = ""
    AIOBOTOCORE_NAME = TypesAioBoto3PackageData.PYPI_LITE_NAME
