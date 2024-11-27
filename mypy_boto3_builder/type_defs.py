"""
Type definitions for builder.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Sequence
from typing import TypedDict

from mypy_boto3_builder.cli_parser import CLINamespace
from mypy_boto3_builder.service_name import ServiceName


class GeneratorKwargs(TypedDict):
    """
    Generator keyword arguments.
    """

    service_names: Sequence[ServiceName]
    master_service_names: Sequence[ServiceName]
    config: CLINamespace
    version: str
    cleanup: bool