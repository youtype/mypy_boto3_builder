"""
Alias map fixes added by botocore for documentation build.

# https://github.com/boto/botocore/blob/develop/botocore/handlers.py#L773
# https://github.com/boto/botocore/blob/develop/botocore/handlers.py#L1055
"""

from mypy_boto3_builder.constants import ALL
from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog

ARGUMENT_ALIASES: dict[ServiceName, dict[str, dict[str, str | None]]] = {
    ServiceNameCatalog.cloudsearchdomain: {"Search": {"return": "returnFields"}},
    ServiceNameCatalog.logs: {"CreateExportTask": {"from": "fromTime"}},
    ServiceNameCatalog.ec2: {ALL: {"Filter": "Filters"}},
    ServiceNameCatalog.s3: {
        "PutBucketAcl": {"ContentMD5": None},
        "PutBucketCors": {"ContentMD5": None},
        "PutBucketLifecycle": {"ContentMD5": None},
        "PutBucketLogging": {"ContentMD5": None},
        "PutBucketNotification": {"ContentMD5": None},
        "PutBucketPolicy": {"ContentMD5": None},
        "PutBucketReplication": {"ContentMD5": None},
        "PutBucketRequestPayment": {"ContentMD5": None},
        "PutBucketTagging": {"ContentMD5": None},
        "PutBucketVersioning": {"ContentMD5": None},
        "PutBucketWebsite": {"ContentMD5": None},
        "PutObjectAcl": {"ContentMD5": None},
    },
}


def get_argument_alias(
    service_name: ServiceName, operation_name: str, argument_name: str
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
    checks = (
        (service_name, operation_name),
        (service_name, ALL),
        (ServiceNameCatalog.all, operation_name),
        (ServiceNameCatalog.all, ALL),
    )
    for current_service_name, current_operation_name in checks:
        if current_service_name not in ARGUMENT_ALIASES:
            continue
        service_type_map = ARGUMENT_ALIASES[current_service_name]

        if current_operation_name not in service_type_map:
            continue
        operation_type_map = service_type_map[current_operation_name]

        if argument_name not in operation_type_map:
            continue

        return operation_type_map[argument_name]

    return argument_name
