"""
String to type annotation map to replace overriden botocore literals.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Mapping
from typing import Final

from mypy_boto3_builder.constants import ALL
from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.utils.lookup_dict import LookupDict

# Mapping representing Required/NotRequired keys of output botocore shapes.
# ServiceName -> TypedDict name -> Argument name -> is_required (True/False)
# False means that argument should be marked as NotRequired.
# True means that argument should be marked as Required.
# None or missing value means that argument should be marked as is_required by default.
REQUIRED_ATTRIBUTE_MAP: Final[Mapping[ServiceName, Mapping[str, Mapping[str, bool]]]] = {
    ServiceNameCatalog.all: {
        ALL: {
            "NextToken": False,
            "PaginationToken": False,
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
    ServiceNameCatalog.sqs: {
        "ChangeMessageVisibilityBatchResultTypeDef": {
            "Successful": False,
            "Failed": False,
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


def get_attribute_required_override(
    service_name: ServiceName, typed_dict_name: str, argument_name: str
) -> bool | None:
    """
    Return the optional override value for an attribute.

    Arguments:
        service_name -- Service name.
        typed_dict_name -- Target TypedDict name.
        attribute_name -- Target attribute name.

    Returns:
        True or False if the field should be overridden to Required or NotRequired accordingly.
        If no override is set, returns None.
    """
    return _LOOKUP.get(service_name.name, typed_dict_name, argument_name)
