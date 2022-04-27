from mypy_boto3_builder.service_name import ServiceNameCatalog
from mypy_boto3_builder.type_maps.shape_type_map import AttributeValueTypeDef, get_shape_type_stub


def test_get_shape_type_stub() -> None:
    assert (
        get_shape_type_stub(ServiceNameCatalog.dynamodb, "AttributeValueTypeDef")
        is AttributeValueTypeDef
    )
    assert (
        get_shape_type_stub(ServiceNameCatalog.ec2, "ClientBatchGetItemRequestItemsKeysTypeDef")
        is None
    )
    assert (
        get_shape_type_stub(ServiceNameCatalog.dynamodb, "ClientBatchGetItemRequestItems") is None
    )
