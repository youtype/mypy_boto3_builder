"""
TypeVar type annotation.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Iterator

from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type import Type


class TypeVarAnnotation(FakeAnnotation):
    """
    TypeVar type annotation.
    """

    def __init__(
        self,
        name: str,
        bound: FakeAnnotation | None = None,
        default: FakeAnnotation | None = None,
        *,
        covariant: bool = False,
        contravariant: bool = False,
    ) -> None:
        self.name = name
        self.bound = bound
        self.covariant = covariant
        self.contravariant = contravariant
        self.default = default

    def __hash__(self) -> int:
        """
        Calcualte hash value.
        """
        return hash((self.name, self.bound, self.default, self.covariant, self.contravariant))

    def render(self) -> str:
        """
        Render type annotation to a valid Python code for local usage.
        """
        return self.name

    def render_definition(self) -> str:
        """
        Render type annotation definition to a valid Python code.
        """
        args = self._get_args()
        args_str = ", ".join(f"{key}={value}" for key, value in args)
        return f"{self.name} = TypeVar(\"{self.name}\"{', ' if args_str else ''}{args_str})"

    def _get_args(self) -> tuple[tuple[str, str], ...]:
        args: list[tuple[str, str]] = []
        if self.bound:
            args.append(("bound", self.bound.render()))
        if self.covariant:
            args.append(("covariant", "True"))
        if self.contravariant:
            args.append(("contravariant", "True"))
        if self.default:
            args.append(("default", self.default.render()))
        return tuple(args)

    def iterate_types(self) -> Iterator[FakeAnnotation]:
        """
        Iterate over definition type annotations.
        """
        yield Type.TypeVar
        if self.bound:
            yield from self.bound.iterate_types()
        if self.default:
            yield from self.default.iterate_types()
