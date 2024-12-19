"""
Type checking utils.

Copyright 2024 Vlad Emelianov
"""

from typing import TypeGuard

from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_def_sortable import TypeDefSortable
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral
from mypy_boto3_builder.type_annotations.type_parent import TypeParent
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.type_typed_dict import TypeTypedDict
from mypy_boto3_builder.type_annotations.type_union import TypeUnion


def is_typed_dict(annotation: FakeAnnotation) -> TypeGuard[TypeTypedDict]:
    """
    Whether type annotation is TypedDict.
    """
    return isinstance(annotation, TypeTypedDict)


def is_union(annotation: FakeAnnotation) -> TypeGuard[TypeUnion]:
    """
    Whether type annotation is a Union.
    """
    return isinstance(annotation, TypeUnion)


def is_literal(annotation: FakeAnnotation) -> TypeGuard[TypeLiteral]:
    """
    Whether type annotation is a literal.
    """
    return isinstance(annotation, TypeLiteral)


def is_type_def(annotation: FakeAnnotation) -> TypeGuard[TypeDefSortable]:
    """
    Whether type annotation is a named TypeDefSortable.
    """
    if is_typed_dict(annotation):
        return True

    if is_union(annotation):
        return annotation.is_named()

    return False


def is_type_parent(annotation: FakeAnnotation) -> TypeGuard[TypeParent]:
    """
    Whether type annotation is a TypeParent.
    """
    return isinstance(annotation, TypeParent)


def is_external_import(annotation: FakeAnnotation) -> TypeGuard[ExternalImport]:
    """
    Whether type annotation is a ExternalImport.
    """
    return isinstance(annotation, ExternalImport)


def is_type_subscript(annotation: FakeAnnotation) -> TypeGuard[TypeSubscript]:
    """
    Whether type annotation is a TypeSubscript.
    """
    return isinstance(annotation, TypeSubscript)


def get_optional(wrapped: FakeAnnotation) -> TypeUnion:
    """
    Get Optional type annotation.
    """
    if is_union(wrapped):
        result = wrapped.copy()
        result.add_child(Type.none)
        return result

    return TypeUnion([wrapped, Type.none])
