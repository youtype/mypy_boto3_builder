from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog

from mypy_boto3_builder.type_maps.shape_type_map import (
    get_shape_type_stub,
    DynamoDBValue,
)


def test_get_shape_type_stub() -> None:
    assert (
        get_shape_type_stub(
            ServiceNameCatalog.dynamodb, "ClientBatchGetItemRequestItemsKeysTypeDef"
        )
        is DynamoDBValue
    )
    assert (
        get_shape_type_stub(
            ServiceNameCatalog.ec2, "ClientBatchGetItemRequestItemsKeysTypeDef"
        )
        is None
    )
    assert (
        get_shape_type_stub(
            ServiceNameCatalog.dynamodb, "ClientBatchGetItemRequestItems"
        )
        is None
    )
