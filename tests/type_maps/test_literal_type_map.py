from mypy_boto3_builder.service_name import ServiceNameCatalog
from mypy_boto3_builder.type_maps.literal_type_map import get_literal_type_stub


def test_get_literal_type_stub() -> None:
    # assert get_literal_type_stub(ServiceNameCatalog.s3, "BucketLocationConstraintType")
    assert get_literal_type_stub(ServiceNameCatalog.s3, "BucketLocationConstraintType") is None
    assert (
        get_literal_type_stub(ServiceNameCatalog.cloudformation, "NoneResourceStatusType") is None
    )
