"""
Alias map fixes added by botocore for documentation build.

# https://github.com/boto/botocore/blob/develop/botocore/handlers.py#L773
# https://github.com/boto/botocore/blob/develop/botocore/handlers.py#L1055
"""

from collections.abc import Mapping
from typing import Final

from mypy_boto3_builder.constants import ALL, DELETE
from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.utils.lookup_dict import LookupDict

# Mapping to rename for botocore method arguments.
# ServiceName -> Operation name -> Argument name -> alias name
# DELETE means that argument has to be deleted.
ARGUMENT_ALIASES: Final[Mapping[ServiceName, Mapping[str, Mapping[str, str]]]] = {
    ServiceNameCatalog.cloudsearchdomain: {"Search": {"return": "returnFields"}},
    ServiceNameCatalog.logs: {"CreateExportTask": {"from": "fromTime"}},
    ServiceNameCatalog.ec2: {ALL: {"Filter": "Filters"}},
    ServiceNameCatalog.s3: {
        "PutBucketAcl": {"ContentMD5": DELETE},
        "PutBucketCors": {"ContentMD5": DELETE},
        "PutBucketLifecycle": {"ContentMD5": DELETE},
        "PutBucketLogging": {"ContentMD5": DELETE},
        "PutBucketNotification": {"ContentMD5": DELETE},
        "PutBucketPolicy": {"ContentMD5": DELETE},
        "PutBucketReplication": {"ContentMD5": DELETE},
        "PutBucketRequestPayment": {"ContentMD5": DELETE},
        "PutBucketTagging": {"ContentMD5": DELETE},
        "PutBucketVersioning": {"ContentMD5": DELETE},
        "PutBucketWebsite": {"ContentMD5": DELETE},
        "PutObjectAcl": {"ContentMD5": DELETE},
    },
}

_LOOKUP: LookupDict[str] = LookupDict(
    {ServiceNameCatalog.to_str(k): v for k, v in ARGUMENT_ALIASES.items()}
)


def get_argument_alias(
    service_name: ServiceName,
    operation_name: str,
    argument_name: str,
) -> str | None:
    """
    Get argument alias for operation.

    Args:
        service_name -- Service name
        operation_name -- Resource operation name
        argument_name -- Argument name

    Returns:
        Argument alias name or None if argument has to be deleted.
    """
    lookup_argument_name = _LOOKUP.get(service_name.name, operation_name, argument_name)
    if lookup_argument_name == DELETE:
        return None

    return lookup_argument_name or argument_name
