"""
RDS service injected methods.
"""

from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.utils.type_checks import get_optional

generate_db_auth_token_method = Method(
    name="generate_db_auth_token",
    arguments=(
        Argument.self(),
        Argument("DBHostname", Type.str),
        Argument("Port", Type.int),
        Argument("DBUsername", Type.str),
        Argument("Region", get_optional(Type.str), Type.Ellipsis),
    ),
    return_type=Type.str,
)

CLIENT_METHODS = (generate_db_auth_token_method,)
