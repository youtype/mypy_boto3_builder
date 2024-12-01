"""
CLI parser.

Copyright 2024 Vlad Emelianov
"""

import argparse
import enum
import logging
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from mypy_boto3_builder.constants import OUTPUT_PATH_SENTINEL, PROG_NAME
from mypy_boto3_builder.enums.output_type import OutputType
from mypy_boto3_builder.enums.product import Product
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.utils.path import print_path
from mypy_boto3_builder.utils.version import get_builder_version


def get_absolute_path(path: str) -> Path:
    """
    Get absolute path from a string.

    Arguments:
        path -- String containing path.

    Returns:
        Absolute path.
    """
    return Path(path).absolute()


class EnumListAction(argparse.Action):
    """
    Argparse action for handling Enums.
    """

    def __init__(
        self,
        *,
        type: type[enum.Enum],  # noqa: A002
        option_strings: Sequence[str],
        dest: str,
        help: str,  # noqa: A002
        default: Sequence[enum.Enum] | None = None,
        nargs: str | None = None,
        required: bool = False,
        **kwargs: str | None,
    ) -> None:
        self._enum_type = type
        self.nargs = nargs or "?"
        choices = tuple(e.value for e in self._enum_type)
        help_str = f"{help}\nChoices: {', '.join(choices)}."

        if default:
            if isinstance(default, enum.Enum):
                help_str += f"\nDefault: {default.value}."
            else:
                help_str += f"\nDefault: {', '.join(e.value for e in default)}."

        super().__init__(
            choices=choices,
            option_strings=option_strings,
            default=default,
            dest=dest,
            nargs=self.nargs,
            type=None,
            help=help_str,
            required=required,
            **kwargs,
        )

    def __call__(
        self,
        parser: argparse.ArgumentParser,
        namespace: argparse.Namespace,
        value: str | Sequence[Any] | None,
        _option_string: str | None = None,
    ) -> None:
        """
        Convert value back into an Enum.
        """
        value_list: list[str] = []
        if isinstance(value, str):
            value_list.append(value)
        if isinstance(value, list):
            value_list.extend([i for i in value if isinstance(i, str)])
        enum_values = [self._enum_type(i) for i in value_list]
        result = enum_values if self.nargs != "?" else enum_values[0]
        setattr(namespace, self.dest, result)


@dataclass(kw_only=True, slots=True)
class CLINamespace:
    """
    CLI arguments namespace.
    """

    log_level: int
    output_path: Path
    service_names: list[str]
    build_version: str
    output_types: list[OutputType]
    products: list[Product]
    list_services: bool = False
    partial_overload: bool = False
    skip_published: bool = False
    disable_smart_version: bool = False
    download_static_stubs: bool = True

    def to_cmd(self) -> tuple[str, ...]:
        """
        Convert namespace to shlex arguments.
        """
        return tuple(
            filter(
                None,
                (
                    PROG_NAME,
                    print_path(self.output_path),
                    "--no-smart-version" if self.disable_smart_version else None,
                    "--skip-published" if self.skip_published else None,
                    "--partial-overload" if self.partial_overload else None,
                    "--download-static-stubs" if self.download_static_stubs else None,
                    "--list-services" if self.list_services else None,
                    f"--build-version {self.build_version}" if self.build_version else None,
                    f"--product {' '.join(i.value for i in self.products)}"
                    if self.products
                    else None,
                    f"--output-type {' '.join(i.value for i in self.output_types)}"
                    if self.output_types
                    else None,
                    f"--services {' '.join(self.service_names)}" if self.service_names else None,
                    "-d" if self.log_level == logging.DEBUG else None,
                ),
            )
        )


def parse_args(args: Sequence[str]) -> CLINamespace:
    """
    Parse CLI arguments.

    Returns:
        Argument parser.
    """
    version = get_builder_version()

    parser = argparse.ArgumentParser(
        PROG_NAME,
        description="Type annotations generator for boto3, aiobotocore and aioboto3.",
    )
    parser.add_argument("-d", "--debug", action="store_true", help="Show debug messages")
    parser.add_argument(
        "-b",
        "--build-version",
        help="Set custom output version, otherwise smart versioning is used.",
    )
    parser.add_argument("-V", "--version", action="version", version=version)
    parser.add_argument(
        "--product",
        dest="products",
        type=Product,
        action=EnumListAction,
        metavar="PRODUCT",
        nargs="+",
        default=(Product.boto3, Product.boto3_services),
        help="Package to generate.",
    )
    parser.add_argument(
        "--skip-published",
        action="store_true",
        help="Skip packages that are already on PyPI.",
    )
    parser.add_argument(
        "--no-smart-version",
        action="store_true",
        help=(
            "Disable version bump based od last PyPI version. "
            "Set this flag to run packages build in offline mode. "
            "skip-published flag is ignored in this case."
        ),
    )
    parser.add_argument(
        "--download-static-stubs",
        action="store_true",
        help="Download static stubs from GitHub repositories instead of using built-in files.",
    )
    parser.add_argument(
        "--panic",
        action="store_true",
        help="Raise exception on logger warning and above",
    )
    parser.add_argument(
        "output_path",
        metavar="OUTPUT_PATH",
        help="Output path",
        type=get_absolute_path,
        default=OUTPUT_PATH_SENTINEL,
        nargs="?",
    )
    parser.add_argument(
        "-s",
        "--services",
        dest="service_names",
        nargs="*",
        metavar="NAME",
        help=(
            "List of AWS services, by default all services are used."
            " Use `updated` to build only services updated in the release."
            " Use `essential` to build only essential services."
            " Use `all` to build all services. (default: all)"
        ),
        default=(ServiceName.ALL,),
    )
    parser.add_argument(
        "--partial-overload",
        action="store_true",
        help="Build client/service overload only for selected services",
    )
    parser.add_argument(
        "--installed",
        action="store_true",
        help=(
            "Generate already installed packages for typings directory."
            " Deprecated, use --output-type=installed instead."
        ),
    )
    parser.add_argument(
        "--output-type",
        type=OutputType,
        action=EnumListAction,
        metavar="OUTPUT_TYPE",
        nargs="*",
        default=(OutputType.package,),
        help="Product output type.",
    )
    parser.add_argument(
        "--list-services",
        action="store_true",
        help="List supported boto3 service names.",
    )
    result = parser.parse_args(args)

    if result.installed:
        result.output_type = [OutputType.installed]

    return CLINamespace(
        log_level=logging.DEBUG if result.debug else logging.INFO,
        output_path=result.output_path,
        service_names=result.service_names,
        products=result.products,
        build_version=result.build_version,
        output_types=result.output_type,
        list_services=result.list_services,
        partial_overload=result.partial_overload,
        skip_published=result.skip_published,
        disable_smart_version=result.no_smart_version,
        download_static_stubs=result.download_static_stubs,
    )
