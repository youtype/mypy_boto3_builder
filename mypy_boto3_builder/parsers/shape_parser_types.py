"""
Types for botocore shape files.
"""

from typing import Any, TypedDict

from typing_extensions import NotRequired


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

    name: str
    source: NotRequired[str]
    target: str


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
