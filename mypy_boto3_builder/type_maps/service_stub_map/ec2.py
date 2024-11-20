"""
EC2 service injected methods.

Copyright 2024 Vlad Emelianov
"""

from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_maps.typed_dicts import TagTypeDef

create_tags_method = Method(
    name="create_tags",
    arguments=(
        Argument.self(),
        Argument.kwflag(),
        Argument("Resources", TypeSubscript(Type.Sequence, [Type.str])),
        Argument("Tags", TypeSubscript(Type.Sequence, [TagTypeDef])),
        Argument("DryRun", Type.bool, Type.Ellipsis),
    ),
    return_type=Type.none,
    docstring=(
        "Adds or overwrites only the specified tags for"
        " the specified Amazon EC2 resource or resources."
    ),
)

delete_tags_method = Method(
    name="delete_tags",
    arguments=(
        Argument.self(),
        Argument.kwflag(),
        Argument("Resources", TypeSubscript(Type.Sequence, [Type.str])),
        Argument("Tags", TypeSubscript(Type.Sequence, [TagTypeDef]), Type.Ellipsis),
        Argument("DryRun", Type.bool, Type.Ellipsis),
    ),
    return_type=Type.none,
    docstring="Deletes the specified set of tags from the specified set of resources.",
)

CLIENT_METHODS = (
    create_tags_method.copy(),
    delete_tags_method.copy(),
)
INSTANCE_METHODS = (
    create_tags_method.copy().remove_argument("Resources"),
    delete_tags_method.copy().remove_argument("Resources"),
)
COMMON_METHODS = (create_tags_method.copy().remove_argument("Resources"),)
