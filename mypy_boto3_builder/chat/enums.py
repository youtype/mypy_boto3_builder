"""
Chat enums.

Copyright 2024 Vlad Emelianov
"""

from enum import Enum
from pathlib import Path

from mypy_boto3_builder.chat.text_style import TextStyle
from mypy_boto3_builder.chat.type_defs import Message
from mypy_boto3_builder.enums.product import Product
from mypy_boto3_builder.enums.product_library import ProductLibrary
from mypy_boto3_builder.package_data import (
    Boto3StubsCustomPackageData,
    TypesAioBoto3CustomPackageData,
    TypesAioBotocoreCustomPackageData,
    TypesBoto3CustomPackageData,
)


class ServiceActions(Enum):
    """
    Available service actions.
    """

    build = "Continue"
    add = "Add another service"
    add_all = "Add all available services"
    recommended = "Add only recommended services"
    remove = "Remove selected service"
    remove_all = "Remove all selected services"


class PackageManager(Enum):
    """
    Available package managers.
    """

    pip = "pip"
    uv = "uv"
    poetry = "poetry"
    pipenv = "pipenv"

    @property
    def url(self) -> str:
        """
        Get package manager URL.
        """
        match self:
            case PackageManager.pip:
                return "https://pypi.org/project/pip/"
            case PackageManager.uv:
                return "https://docs.astral.sh/uv/"
            case PackageManager.poetry:
                return "https://python-poetry.org/"
            case PackageManager.pipenv:
                return "https://pipenv.pypa.io/en/latest/"

    def get_install_cmd(self, whl_path: Path) -> str:
        """
        Get install command.
        """
        match self:
            case PackageManager.uv:
                return f"uv add --dev {whl_path}"
            case PackageManager.pip:
                return f"pip install {whl_path}"
            case PackageManager.poetry:
                return f"poetry add -G dev {whl_path}"
            case PackageManager.pipenv:
                return f"pipenv install --dev {whl_path}"


class Library(Enum):
    """
    Library type.
    """

    boto3 = "boto3"
    aiobotocore = "aiobotocore"
    aioboto3 = "aioboto3"
    boto3_legacy = "boto3-stubs"

    @property
    def product_library(self) -> ProductLibrary:
        """
        Get product library.
        """
        match self:
            case Library.boto3:
                return ProductLibrary.boto3
            case Library.aiobotocore:
                return ProductLibrary.aiobotocore
            case Library.aioboto3:
                return ProductLibrary.aioboto3
            case Library.boto3_legacy:
                return ProductLibrary.boto3_legacy

    @property
    def text(self) -> Message:
        """
        Get choice user text.
        """
        match self:
            case Library.boto3_legacy:
                return [
                    "boto3",
                    TextStyle.text.wrap(", but it also already has "),
                    TextStyle.tag.wrap("boto3-stubs"),
                ]
            case _:
                return [self.value]

    @property
    def title(self) -> Message:
        """
        Get choice title.
        """
        return [f"{self.value:<14}"]

    @property
    def title_info(self) -> str:
        """
        Get choice title.
        """
        match self:
            case Library.boto3:
                return "AWS SDK for Python"
            case Library.aiobotocore:
                return "Async client for amazon services using botocore and aiohttp/asyncio."
            case Library.aioboto3:
                return "Async AWS SDK for Python"
            case Library.boto3_legacy:
                return "Legacy type annotations for AWS SDK for Python"

    @property
    def documentation_url(self) -> str:
        """
        Link to documentation.
        """
        match self:
            case Library.boto3:
                return TypesBoto3CustomPackageData.local_doc_link
            case Library.boto3_legacy:
                return Boto3StubsCustomPackageData.local_doc_link
            case Library.aiobotocore:
                return TypesAioBotocoreCustomPackageData.local_doc_link
            case Library.aioboto3:
                return TypesAioBoto3CustomPackageData.local_doc_link

    def get_package_prefix(self) -> str:
        """
        Get *.whl package name prefix.
        """
        match self:
            case Library.boto3:
                return "types_boto3"
            case Library.boto3_legacy:
                return "boto3_stubs"
            case Library.aiobotocore:
                return "types_aiobotocore"
            case Library.aioboto3:
                return "types_aioboto3"

    @property
    def product(self) -> Product:
        """
        Get product.
        """
        match self:
            case Library.boto3:
                return Product.types_boto3_custom
            case Library.boto3_legacy:
                return Product.boto3_custom
            case Library.aiobotocore:
                return Product.aiobotocore_custom
            case Library.aioboto3:
                return Product.aioboto3_custom
