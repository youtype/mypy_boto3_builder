"""
Product type for CLI.

Copyright 2024 Vlad Emelianov
"""

from enum import Enum


class ProductType(Enum):
    """
    Product type for CLI.
    """

    stubs = "stubs"
    service_stubs = "service_stubs"
    docs = "docs"
    full = "full"
    custom = "custom"
