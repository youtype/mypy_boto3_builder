"""
String to type annotation map to replace overriden botocore literals.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Mapping
from typing import Final

from mypy_boto3_builder.constants import ALL
from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.utils.lookup_dict import LookupDict

# Mapping reresenting Required/NotRequired keys of output botocore shapes.
# ServiceName -> TypedDict name -> Argument name -> is_required (True/False)
# False means that argument should be marked as NotRequired.
# True means that argument should be marked as Required.
# None or missing value means that argument should be marked as is_required by default.
REQUIRED_ATTRIBUTE_MAP: Final[Mapping[ServiceName, Mapping[str, Mapping[str, bool]]]] = {
    ServiceNameCatalog.all: {
        ALL: {
            "NextToken": False,
            "nextToken": False,
            "Contents": False,
            "Item": False,
            "CommonPrefixes": False,
        },
    },
    ServiceNameCatalog.dynamodb: {
        ALL: {
            "LastEvaluatedKey": False,
        },
    },
    ServiceNameCatalog.stepfunctions: {
        "DescribeExecutionOutputTypeDef": {
            "stopDate": False,
            "output": False,
            "outputDetails": False,
            "error": False,
            "cause": False,
            "traceHeader": False,
            "redriveStatusReason": False,
            "mapRunArn": False,
            "redriveDate": False,
            "stateMachineAliasArn": False,
            "stateMachineVersionArn": False,
        },
    },
}

_LOOKUP: LookupDict[bool] = LookupDict(
    {ServiceNameCatalog.to_str(k): v for k, v in REQUIRED_ATTRIBUTE_MAP.items()},
)


def is_required(service_name: ServiceName, typed_dict_name: str, argument_name: str) -> bool:
    """
    Check if output shape argument should be marked as NotRequired.

    Arguments:
        service_name -- Service name.
        typed_dict_name -- Target TypedDict name.
        attribute_name -- Target attribute name.

    Returns:
        Literal children or None.
    """
    is_required = _LOOKUP.get(service_name.name, typed_dict_name, argument_name)
    return True if is_required is None else is_required
