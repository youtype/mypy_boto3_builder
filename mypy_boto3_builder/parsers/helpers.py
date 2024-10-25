"""
Helpers for parsing methods and attributes.
"""

import inspect
from types import MethodType

from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_annotations.type import Type


def get_public_methods(inspect_class: object) -> dict[str, MethodType]:
    """
    Extract public methods from any class.

    Arguments:
        inspect_class -- Inspect class.

    Returns:
        A dictionary of method name and method.
    """
    class_members = inspect.getmembers(inspect_class)
    methods: dict[str, MethodType] = {}
    for name, member in class_members:
        if not inspect.ismethod(member):
            continue

        if name.startswith("_"):
            continue

        methods[name] = member

    return methods


def get_dummy_method(name: str) -> Method:
    """
    Get a dummy method in case we cannot parse it.

    Arguments:
        name -- Method name.

    Returns:
        Method structure.
    """
    return Method(
        name=name,
        arguments=(
            Argument.self(),
            Argument("args", Type.Any, prefix="*"),
            Argument("kwargs", Type.Any, prefix="**"),
        ),
        return_type=Type.Any,
    )
