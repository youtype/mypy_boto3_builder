"""
DynamoDB service injected methods.
"""

from boto3.dynamodb.table import BatchWriter

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
            Type.list(Type.str),
            Type.Ellipsis,
        ),
    ),
    return_type=ExternalImport.from_class(BatchWriter),
)

TABLE_METHODS = (batch_writer_method,)
