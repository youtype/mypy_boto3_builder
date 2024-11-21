"""
Types for botocore shape files.

Copyright 2024 Vlad Emelianov
"""

from typing import Any, NotRequired, TypedDict


class PaginatorShape(TypedDict):
    """
    Paginator shape.
    """

    input_token: list[str] | str
    limit_key: NotRequired[str]


class PaginatorsShape(TypedDict):
    """
    Paginators shape.
    """

    pagination: dict[str, PaginatorShape]


class IdentifierShape(TypedDict):
    """
    Identifier shape.
    """

    name: NotRequired[str]
    target: NotRequired[str]
    source: NotRequired[str]
    type: NotRequired[str]


class SubResourceShape(TypedDict):
    """
    SubResource shape.
    """

    type: str
    identifiers: NotRequired[list[IdentifierShape]]
    path: NotRequired[str]


class HasShape(TypedDict):
    """
    Has shape.
    """

    resource: NotRequired[SubResourceShape]


class ParamShape(TypedDict):
    """
    Param shape.
    """

    target: str
    source: str
    value: str | int | float | None


class RequestShape(TypedDict):
    """
    Request shape.
    """

    operation: str
    params: NotRequired[list[ParamShape]]


class ActionShape(TypedDict):
    """
    Action shape.
    """

    request: RequestShape
    resource: SubResourceShape


class WaiterShape(TypedDict):
    """
    Waiter shape.
    """

    operation: str


class WaitersShape(TypedDict):
    """
    Waiters shape.
    """

    waiters: dict[str, WaiterShape]


class ResourceShape(TypedDict):
    """
    Resource shape.
    """

    shape: NotRequired[str]
    identifiers: NotRequired[list[IdentifierShape]]
    actions: NotRequired[dict[str, Any]]
    waiters: NotRequired[dict[str, WaiterShape]]
    has: NotRequired[dict[str, HasShape]]


class ResourcesShape(TypedDict):
    """
    Resources shape.
    """

    service: ResourceShape
    resources: NotRequired[dict[str, ResourceShape]]
