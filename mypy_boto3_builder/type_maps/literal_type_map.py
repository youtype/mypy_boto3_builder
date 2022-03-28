"""
String to type annotation map to replace overriden botocore literals.
"""
from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog

LITERAL_TYPE_MAP: dict[ServiceName, dict[str, list[str]]] = {
    ServiceNameCatalog.s3: {
        # FIXME: https://github.com/boto/botocore/issues/2648
        "BucketLocationConstraintType": [
            "af-south-1",
            "ap-east-1",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-southeast-3",
            "ca-central-1",
            "eu-central-1",
            "eu-north-1",
            "eu-south-1",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "me-south-1",
            "sa-east-1",
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
        ],
    },
}


def get_literal_type_stub(service_name: ServiceName, literal_name: str) -> list[str] | None:
    """
    Get stub type for botocore literal.

    Arguments:
        service_name -- Service name.
        literal_name -- Target Literal name.

    Returns:
        Literal children or None.
    """
    if service_name not in LITERAL_TYPE_MAP:
        return None

    service_literal_type_map = LITERAL_TYPE_MAP[service_name]
    if literal_name not in service_literal_type_map:
        return None

    return service_literal_type_map[literal_name]
