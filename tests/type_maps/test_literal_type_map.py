from mypy_boto3_builder.service_name import ServiceNameCatalog
from mypy_boto3_builder.type_maps.literal_type_map import get_type_literal_stub


def test_get_type_literal_stub() -> None:
    type_literal = get_type_literal_stub(ServiceNameCatalog.ec2, "PlatformValuesType")
    assert type_literal
    assert type_literal.children == {"windows"}
    assert get_type_literal_stub(ServiceNameCatalog.s3, "BucketLocationConstraintType") is None
    assert (
        get_type_literal_stub(ServiceNameCatalog.cloudformation, "NoneResourceStatusType") is None
    )
