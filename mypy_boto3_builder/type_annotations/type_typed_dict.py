"""
Wrapper for `typing/typing_extensions.TypedDict` type annotations.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Iterable, Iterator
from pathlib import Path
from typing import Self

from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.exceptions import TypeAnnotationError
from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.internal_import_record import InternalImportRecord
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_def_sortable import TypeDefSortable
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral
from mypy_boto3_builder.type_annotations.type_parent import TypeParent
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.utils.jinja2 import render_jinja2_template


class TypedDictAttribute:
    """
    TypedDict attribute wrapper.

    Arguments:
        name -- Attribute name.
        type_annotation -- Attribute type annotation.
        required -- Whether the attribute has to be set.
    """

    def __init__(self, name: str, type_annotation: FakeAnnotation, *, required: bool) -> None:
        self.name = name
        self.required = required
        self.type_annotation = type_annotation

    def __hash__(self) -> int:
        """
        Calculate hash value based on name, required and type annotation.
        """
        return hash((self.name, self.required, self.type_annotation.get_sort_key()))

    def get_type_annotation(self) -> FakeAnnotation:
        """
        Get wrapped for non-required type annotation or raw type annotation.
        """
        if self.is_required():
            return self.type_annotation

        return TypeSubscript(Type.NotRequired, [self.type_annotation])

    def render(self) -> str:
        """
        Render attribute to use in function-based TypedDict definition.

        Returns:
            A string with argument definition.
        """
        return f'"{self.name}": {self.get_type_annotation().render()}'

    def render_attribute(self) -> str:
        """
        Render attribute to use in class-based TypedDict definition.

        Returns:
            A string with argument definition.
        """
        return f"{self.name}: {self.get_type_annotation().render()}"

    def iterate_types(self) -> Iterator[FakeAnnotation]:
        """
        Itera over type annotations.
        """
        yield from self.type_annotation.iterate_types()

    def is_required(self) -> bool:
        """
        Whether argument is required.
        """
        return self.required

    def mark_as_required(self) -> None:
        """
        Mark attribute as required.
        """
        self.required = True


class TypeTypedDict(TypeParent, TypeDefSortable):
    """
    Wrapper for `typing/typing_extensions.TypedDict` type annotations.

    Arguments:
        name -- Type name.
        children -- Typed dict attributes.
        docstring -- Docstring for render.
        stringify -- Convert type annotation to string to avoid circular deps.
    """

    def __init__(
        self,
        name: str,
        children: Iterable[TypedDictAttribute] = (),
        docstring: str = "",
        *,
        stringify: bool = False,
    ) -> None:
        self.name = name
        self.children = list(children)
        self.docstring = docstring
        self._stringify = stringify
        self.is_safe_as_class = True

    def is_stringified(self) -> bool:
        """
        Whether TypedDict usage should be rendered as a string.
        """
        return self._stringify

    def stringify(self) -> None:
        """
        Render TypedDict usage as a string.
        """
        self._stringify = True

    def get_sort_key(self) -> str:
        """
        Sort Typed Dicts by name.
        """
        return self.name

    def __hash__(self) -> int:
        """
        Calculate hash value based on name and children.
        """
        return hash((self.name, *self.children))

    def render(self) -> str:
        """
        Render type annotation to a valid Python code for local usage.

        Returns:
            A string with a valid type annotation.
        """
        if self.is_stringified():
            return f'"{self.name}"'

        return self.name

    def render_definition(self) -> str:
        """
        Render type annotation definition.
        """
        template = (
            Path("common/typed_dict_class.py.jinja2")
            if self.is_safe_as_class
            else Path("common/typed_dict.py.jinja2")
        )
        return render_jinja2_template(template, {"type_def": self})

    def get_definition_import_records(self) -> set[ImportRecord]:
        """
        Get import record required for using TypedDict.
        """
        result = Type.TypedDict.get_import_records()
        for child in self.iterate_children():
            result.update(child.get_type_annotation().get_import_records())
        return result

    def _get_import_records(self) -> set[ImportRecord]:
        """
        Get import record required for using type annotation.
        """
        return {InternalImportRecord(ServiceModuleName.type_defs, name=self.name)}

    def add_attribute(self, name: str, type_annotation: FakeAnnotation, *, required: bool) -> None:
        """
        Add new attribute to a dictionary.

        Arguments:
            name -- Argument name.
            type_annotation -- Argument type annotation.
            required -- Whether argument has to be set.
        """
        self.children.append(TypedDictAttribute(name, type_annotation, required=required))

    def is_dict(self) -> bool:
        """
        Whether type annotation is `Dict` or `TypedDict`.
        """
        return True

    def has_optional(self) -> bool:
        """
        Whether TypedDict has optional keys.
        """
        return any(not child.is_required() for child in self.children)

    def has_required(self) -> bool:
        """
        Whether TypedDict has required keys.
        """
        return any(child.is_required() for child in self.children)

    def get_required(self) -> tuple[TypedDictAttribute, ...]:
        """
        Get a list of required attributes.
        """
        return tuple(child for child in self.children if child.is_required())

    def get_optional(self) -> tuple[TypedDictAttribute, ...]:
        """
        Get a list of optional attributes.
        """
        return tuple(child for child in self.children if not child.is_required())

    def __copy__(self) -> Self:
        """
        Create a copy of type annotation wrapper.
        """
        return self.__class__(
            self.name,
            list(self.children),
            docstring=self.docstring,
            stringify=self.is_stringified(),
        )

    def is_same(self, other: Self) -> bool:
        """
        Check whether typed dict attributes are the same as `other`.
        """
        return hash(self) == hash(other)

    def get_children_types(self) -> set[FakeAnnotation]:
        """
        Extract required type annotations from attributes.
        """
        result: set[FakeAnnotation] = set()
        for child in self.children:
            result.update(child.iterate_types())
        return result

    def iterate_direct_type_annotations(self) -> Iterator[FakeAnnotation]:
        """
        Iterate over children type annotations.
        """
        for child in self.children:
            yield child.type_annotation

    def get_children_literals(self, processed: Iterable[str] = ()) -> set[TypeLiteral]:
        """
        Extract required TypeLiteral list from attributes.
        """
        result: set[TypeLiteral] = set()
        if self.name in processed:
            return result
        children_types = self.get_children_types()
        for type_annotation in children_types:
            if isinstance(type_annotation, TypeLiteral):
                result.add(type_annotation)
            if isinstance(type_annotation, TypeDefSortable):
                result.update(type_annotation.get_children_literals((self.name, *processed)))
        return result

    def iterate_children(self) -> Iterator[TypedDictAttribute]:
        """
        Iterate over children from required to optional.
        """
        yield from self.get_required()
        yield from self.get_optional()

    def get_local_types(self) -> list[FakeAnnotation]:
        """
        Get internal types generated by builder.
        """
        return [self]

    @property
    def type_hint_annotations(self) -> list[FakeAnnotation]:
        """
        Type annotations list from arguments and return type with internal types.
        """
        return [
            child.type_annotation
            for child in self.children
            if child.type_annotation.get_local_types()
        ]

    def is_type_def(self) -> bool:
        """
        Whether type annotation is a TypeDef.
        """
        return True

    def replace_child(self, child: FakeAnnotation, new_child: FakeAnnotation) -> Self:
        """
        Replace child type annotation with a new one.
        """
        children_types = [i.type_annotation for i in self.children]
        if child not in children_types:
            raise TypeAnnotationError(f"Child not found: {child}")

        indices = [i for i, x in enumerate(children_types) if x == child]
        for index in indices:
            self.children[index].type_annotation = new_child

        return self
