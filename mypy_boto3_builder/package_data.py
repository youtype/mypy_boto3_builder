"""
PyPI package data constants.

Copyright 2024 Vlad Emelianov
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass

from mypy_boto3_builder.enums.product_library import ProductLibrary
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.utils.version_getters import (
    get_aioboto3_version,
    get_aiobotocore_version,
    get_boto3_version,
)


@dataclass(kw_only=True)
class BasePackageData(ABC):
    """
    Generic package data.
    """

    # package name
    name: str

    # package name on PyPI
    pypi_name: str

    # main stubs package name on PyPI
    pypi_stubs_name: str

    # lite stubs package name on PyPI
    pypi_lite_name: str

    # full stubs package name on PyPI
    pypi_full_name: str

    # underlying library: boto3, aiobotocore, aioboto3
    library: ProductLibrary

    # service package name prefix
    service_prefix: str

    # service package name prefix on PyPI
    service_pypi_prefix: str

    # link to local documentation
    local_doc_link: str

    # install_requires for setup.py
    install_requires: tuple[str, ...]

    # is package installable with VSCode extensions
    is_vscode_supported: bool = False

    # is the package released to conda-forge
    is_conda_forge_supported: bool = False

    def get_service_package_name(self, service_name: ServiceName) -> str:
        """
        Get service package name.
        """
        return f"{self.service_prefix}_{service_name.underscore_name}"

    def get_service_pypi_name(self, service_name: ServiceName) -> str:
        """
        Get service package PyPI name.
        """
        return f"{self.service_pypi_prefix}-{service_name.name}"

    def get_library_version(self) -> str:
        """
        Get underlying library version.
        """
        return self._get_library_version()

    @abstractmethod
    def _get_library_version(self) -> str:
        raise NotImplementedError("Method not implemented")

    def has_pypi_lite_package(self) -> bool:
        """
        Check if package has lite version.
        """
        return bool(self.pypi_lite_name and self.pypi_lite_name != self.pypi_name)

    def get_library_name(self) -> str:
        """
        Get PyPI library name.
        """
        return self.library.get_library_name()

    def get_library_chat_choice(self) -> str:
        """
        Get package library chat choice.
        """
        return self.library.get_chat_choice()


@dataclass(kw_only=True)
class TypesBoto3PackageData(BasePackageData):
    """
    types-boto3 package data.
    """

    name: str = "boto3-stubs"
    pypi_name: str = "types-boto3"
    pypi_stubs_name: str = "types-boto3"
    pypi_lite_name: str = "types-boto3-lite"
    pypi_full_name: str = "types-boto3-full"
    library: ProductLibrary = ProductLibrary.boto3
    service_prefix: str = "types_boto3"
    service_pypi_prefix: str = "types-boto3"
    local_doc_link: str = "https://youtype.github.io/types_boto3_docs/"
    install_requires: tuple[str, ...] = (
        "botocore-stubs",
        "types-s3transfer",
        'typing-extensions>=4.1.0; python_version<"3.12"',
    )
    is_vscode_supported: bool = True
    is_conda_forge_supported: bool = False

    def _get_library_version(self) -> str:
        return get_boto3_version()


@dataclass(kw_only=True)
class TypesBoto3LitePackageData(TypesBoto3PackageData):
    """
    types-boto3-lite package data.
    """

    pypi_name: str = TypesBoto3PackageData.pypi_lite_name
    pypi_lite_name: str = ""


@dataclass(kw_only=True)
class TypesBoto3FullPackageData(TypesBoto3PackageData):
    """
    boto3-stubs-full package data.
    """

    name: str = ""
    pypi_name: str = TypesBoto3PackageData.pypi_full_name
    is_conda_forge_supported: bool = False
    install_requires: tuple[str, ...] = ()

    def get_service_pypi_name(self, service_name: ServiceName) -> str:
        """
        Get service package PyPI name.
        """
        return self.pypi_name


@dataclass(kw_only=True)
class TypesBoto3CustomPackageData(TypesBoto3PackageData):
    """
    boto3-stubs-custom package data.
    """

    pypi_name: str = "types-boto3-custom"
    is_conda_forge_supported: bool = False

    def get_service_pypi_name(self, service_name: ServiceName) -> str:
        """
        Get service package PyPI name.
        """
        return self.pypi_name


@dataclass(kw_only=True)
class TypesAioBotocorePackageData(BasePackageData):
    """
    types-aiobotocore package data.
    """

    name: str = "aiobotocore-stubs"
    pypi_name: str = "types-aiobotocore"
    pypi_stubs_name: str = "types-aiobotocore"
    pypi_lite_name: str = "types-aiobotocore-lite"
    pypi_full_name: str = "types-aiobotocore-full"
    library: ProductLibrary = ProductLibrary.aiobotocore
    service_prefix: str = "types_aiobotocore"
    service_pypi_prefix: str = "types-aiobotocore"
    local_doc_link: str = "https://youtype.github.io/types_aiobotocore_docs/"
    install_requires: tuple[str, ...] = (
        "botocore-stubs",
        'typing-extensions>=4.1.0; python_version<"3.12"',
    )

    def _get_library_version(self) -> str:
        return get_aiobotocore_version()


@dataclass(kw_only=True)
class TypesAioBotocoreLitePackageData(TypesAioBotocorePackageData):
    """
    types-aiobotocore-lite package data.
    """

    pypi_name: str = TypesAioBotocorePackageData.pypi_lite_name
    pypi_lite_name: str = ""


@dataclass(kw_only=True)
class TypesAioBotocoreFullPackageData(TypesAioBotocorePackageData):
    """
    types-aiobotocore-full package data.
    """

    name: str = ""
    pypi_name: str = TypesAioBotocorePackageData.pypi_full_name
    is_conda_forge_supported: bool = False
    install_requires: tuple[str, ...] = ()

    def get_service_pypi_name(self, service_name: ServiceName) -> str:
        """
        Get service package PyPI name.
        """
        return self.pypi_name


@dataclass(kw_only=True)
class TypesAioBotocoreCustomPackageData(TypesAioBotocorePackageData):
    """
    types-aiobotocore-custom package data.
    """

    pypi_name: str = "types-aiobotocore-custom"
    is_conda_forge_supported: bool = False

    def get_service_pypi_name(self, service_name: ServiceName) -> str:
        """
        Get service package PyPI name.
        """
        return self.pypi_name


@dataclass(kw_only=True)
class Boto3StubsPackageData(BasePackageData):
    """
    boto3-stubs package data.
    """

    name: str = "boto3-stubs"
    pypi_name: str = "boto3-stubs"
    pypi_stubs_name: str = "boto3-stubs"
    pypi_lite_name: str = "boto3-stubs-lite"
    pypi_full_name: str = "boto3-stubs-full"
    service_prefix: str = "mypy_boto3"
    service_pypi_prefix: str = "mypy-boto3"
    library: ProductLibrary = ProductLibrary.boto3_legacy
    local_doc_link: str = "https://youtype.github.io/boto3_stubs_docs/"
    install_requires: tuple[str, ...] = (
        "botocore-stubs",
        "types-s3transfer",
        'typing-extensions>=4.1.0; python_version<"3.12"',
    )
    is_vscode_supported: bool = True
    is_conda_forge_supported: bool = True

    def _get_library_version(self) -> str:
        return get_boto3_version()


@dataclass(kw_only=True)
class Boto3StubsLitePackageData(Boto3StubsPackageData):
    """
    boto3-stubs-lite package data.
    """

    pypi_name: str = Boto3StubsPackageData.pypi_lite_name
    pypi_lite_name: str = ""


@dataclass(kw_only=True)
class Boto3StubsFullPackageData(Boto3StubsPackageData):
    """
    boto3-stubs-full package data.
    """

    name: str = ""
    pypi_name: str = Boto3StubsPackageData.pypi_full_name
    is_conda_forge_supported: bool = False
    install_requires: tuple[str, ...] = ()

    def get_service_pypi_name(self, service_name: ServiceName) -> str:
        """
        Get service package PyPI name.
        """
        return self.pypi_name


@dataclass(kw_only=True)
class Boto3StubsCustomPackageData(Boto3StubsPackageData):
    """
    boto3-stubs-custom package data.
    """

    pypi_name: str = "boto3-stubs-custom"
    is_conda_forge_supported: bool = False

    def get_service_pypi_name(self, service_name: ServiceName) -> str:
        """
        Get service package PyPI name.
        """
        return self.pypi_name


@dataclass(kw_only=True)
class MypyBoto3PackageData(Boto3StubsPackageData):
    """
    mypy-boto3 package data.
    """

    name: str = "mypy_boto3"
    pypi_name: str = "mypy-boto3"
    library: ProductLibrary = ProductLibrary.boto3_legacy
    is_vscode_supported: bool = False
    is_conda_forge_supported: bool = False


@dataclass(kw_only=True)
class TypesAioBoto3PackageData(BasePackageData):
    """
    types-aioboto3 package data.
    """

    name: str = "aioboto3-stubs"
    pypi_name: str = "types-aioboto3"
    pypi_stubs_name: str = "types-aioboto3"
    pypi_lite_name: str = "types-aioboto3-lite"
    pypi_full_name: str = TypesAioBotocorePackageData.pypi_full_name
    library: ProductLibrary = ProductLibrary.aioboto3
    service_prefix: str = "types_aiobotocore"
    service_pypi_prefix: str = "types-aiobotocore"
    local_doc_link: str = "https://youtype.github.io/types_aioboto3_docs/"
    install_requires: tuple[str, ...] = (
        "botocore-stubs",
        TypesAioBotocorePackageData.pypi_stubs_name,
        "types-s3transfer",
        'typing-extensions>=4.1.0; python_version<"3.12"',
    )

    def _get_library_version(self) -> str:
        return get_aioboto3_version()


@dataclass(kw_only=True)
class TypesAioBoto3LitePackageData(TypesAioBoto3PackageData):
    """
    types-aioboto3-lite package data.
    """

    pypi_name: str = TypesAioBoto3PackageData.pypi_lite_name
    pypi_lite_name: str = ""
    install_requires: tuple[str, ...] = (
        "botocore-stubs",
        TypesAioBotocorePackageData.pypi_lite_name,
        "types-s3transfer",
        'typing-extensions>=4.1.0; python_version<"3.12"',
    )


@dataclass(kw_only=True)
class TypesAioBoto3CustomPackageData(TypesAioBoto3PackageData):
    """
    types-aioboto3-custom package data.
    """

    pypi_name: str = "types-aioboto3-custom"
    is_conda_forge_supported: bool = False
    install_requires: tuple[str, ...] = (
        "botocore-stubs",
        "types-s3transfer",
        'typing-extensions>=4.1.0; python_version<"3.12"',
    )

    def get_service_pypi_name(self, service_name: ServiceName) -> str:
        """
        Get service package PyPI name.
        """
        return self.pypi_name
