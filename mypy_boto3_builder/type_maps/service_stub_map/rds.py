"""
RDS service injected methods.
"""

from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript

generate_db_auth_token_method = Method(
    "generate_db_auth_token",
    [
        Argument("self", None),
        Argument("DBHostname", Type.str),
        Argument("Port", Type.int),
        Argument("DBUsername", Type.str),
        Argument("Region", TypeSubscript(Type.Optional, [Type.str]), Type.Ellipsis),
    ],
    Type.str,
)

CLIENT_METHODS = [
    generate_db_auth_token_method,
]
