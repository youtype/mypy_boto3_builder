"""
Type checking utils.
"""

from typing_extensions import TypeIs

from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_def_sortable import TypeDefSortable
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral
from mypy_boto3_builder.type_annotations.type_typed_dict import TypeTypedDict
from mypy_boto3_builder.type_annotations.type_union import TypeUnion


def is_typed_dict(annotation: FakeAnnotation) -> TypeIs[TypeTypedDict]:
    """
    Whether type annotation is TypedDict.
    """
    return isinstance(annotation, TypeTypedDict)


def is_union(annotation: FakeAnnotation) -> TypeIs[TypeUnion]:
    """
    Whether type annotation is a Union.
    """
    return isinstance(annotation, TypeUnion)


def is_literal(annotation: FakeAnnotation) -> TypeIs[TypeLiteral]:
    """
    Whether type annotation is a literal.
    """
    return isinstance(annotation, TypeLiteral)


def is_type_def(annotation: FakeAnnotation) -> TypeIs[TypeDefSortable]:
    """
    Whether type annotation is a named TypeDefSortable.
    """
    if is_typed_dict(annotation):
        return True

    if is_union(annotation):
        return annotation.is_named()

    return False
