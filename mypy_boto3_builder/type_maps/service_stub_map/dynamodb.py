"""
DynamoDB service injected methods.

Copyright 2024 Vlad Emelianov
"""

from mypy_boto3_builder.import_helpers.import_helper import Import
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.type import Type

batch_writer_method = Method(
    name="batch_writer",
    arguments=(
        Argument.self(),
        Argument(
            "overwrite_by_pkeys",
            Type.wrap_list(Type.str),
            Type.Ellipsis,
        ),
    ),
    return_type=ExternalImport(Import.boto3 + "dynamodb" + "table", "BatchWriter"),
    docstring="Create a batch writer object.",
)

TABLE_METHODS = (batch_writer_method,)
