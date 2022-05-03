from mypy_boto3_builder.service_name import ServiceNameCatalog
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_maps.shape_type_map import (
    AttributeValueTypeDef,
    InputAttributeValueType,
    get_output_shape_type_stub,
    get_shape_type_stub,
)


def test_get_shape_type_stub() -> None:
    assert get_shape_type_stub(ServiceNameCatalog.dynamodb, "boolean") is Type.bool
    assert (
        get_shape_type_stub(ServiceNameCatalog.dynamodb, "AttributeValueTypeDef")
        is InputAttributeValueType
    )
    assert (
        get_shape_type_stub(ServiceNameCatalog.ec2, "ClientBatchGetItemRequestItemsKeysTypeDef")
        is None
    )
    assert (
        get_shape_type_stub(ServiceNameCatalog.dynamodb, "ClientBatchGetItemRequestItems") is None
    )


def test_get_output_shape_type_stub() -> None:
    assert get_output_shape_type_stub(ServiceNameCatalog.dynamodb, "timestamp") is Type.datetime
    assert (
        get_output_shape_type_stub(ServiceNameCatalog.dynamodb, "AttributeValueTypeDef")
        is AttributeValueTypeDef
    )
    assert (
        get_output_shape_type_stub(
            ServiceNameCatalog.ec2, "ClientBatchGetItemRequestItemsKeysTypeDef"
        )
        is None
    )
    assert (
        get_output_shape_type_stub(ServiceNameCatalog.dynamodb, "ClientBatchGetItemRequestItems")
        is None
    )
