"""
DynamoDB service injected methods.
"""

from boto3.dynamodb.table import BatchWriter

from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript

batch_writer_method = Method(
    "batch_writer",
    [
        Argument("self", None),
        Argument(
            "overwrite_by_pkeys",
            TypeSubscript(Type.List, [Type.str]),
            Type.Ellipsis,
        ),
    ],
    ExternalImport.from_class(BatchWriter),
)

TABLE_METHODS = [batch_writer_method]
