"""
Chat enums.

Copyright 2024 Vlad Emelianov
"""

from enum import Enum


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
