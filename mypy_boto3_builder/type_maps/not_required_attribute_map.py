"""
String to type annotation map to replace overriden botocore literals.
"""

from collections.abc import Mapping
from typing import Final

from mypy_boto3_builder.constants import ALL
from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.utils.lookup_dict import LookupDict

NOT_REQUIRED_ATTRIBUTE_MAP: Final[Mapping[ServiceName, Mapping[str, Mapping[str, bool]]]] = {
    ServiceNameCatalog.all: {
        ALL: {
            "NextToken": True,
            "nextToken": True,
            "Contents": True,
            "Item": True,
            "CommonPrefixes": True,
        }
    },
    ServiceNameCatalog.stepfunctions: {
        "DescribeExecutionOutputTypeDef": {
            "stopDate": True,
            "output": True,
            "outputDetails": True,
            "error": True,
            "cause": True,
            "traceHeader": True,
            "redriveStatusReason": True,
            "mapRunArn": True,
            "redriveDate": True,
            "stateMachineAliasArn": True,
            "stateMachineVersionArn": True,
        }
    },
}

_LOOKUP: LookupDict[bool] = LookupDict(
    {ServiceNameCatalog.to_str(k): v for k, v in NOT_REQUIRED_ATTRIBUTE_MAP.items()}
)


def is_not_required(service_name: ServiceName, typed_dict_name: str, argument_name: str) -> bool:
    """
    Check if output shape argument should be marked as NotRequired.

    Arguments:
        service_name -- Service name.
        typed_dict_name -- Target TypedDict name.
        attribute_name -- Target attribute name.

    Returns:
        Literal children or None.
    """
    return _LOOKUP.get(service_name.name, typed_dict_name, argument_name) or False
