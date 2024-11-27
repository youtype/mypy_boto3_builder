"""
Product type choice for CLI.

Copyright 2024 Vlad Emelianov
"""

from enum import Enum


class ProductType(Enum):
    """
    Product type choice for CLI.
    """

    stubs = "stubs"
    stubs_lite = "stubs_lite"
    service_stubs = "service_stubs"
    docs = "docs"
    full = "full"
    custom = "custom"
