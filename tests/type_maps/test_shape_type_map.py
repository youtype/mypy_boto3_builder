from mypy_boto3_builder.service_name import ServiceNameCatalog
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_maps.shape_type_map import (
    TableAttributeValueTypeDef,
    UniversalAttributeValueTypeDef,
    get_output_shape_type_stub,
    get_shape_type_stub,
)


def test_get_shape_type_stub() -> None:
    assert get_shape_type_stub(ServiceNameCatalog.dynamodb, "Client", "boolean") is Type.bool
    assert (
        get_shape_type_stub(ServiceNameCatalog.dynamodb, "Client", "AttributeValueTypeDef")
        is UniversalAttributeValueTypeDef
    )
    assert (
        get_shape_type_stub(ServiceNameCatalog.dynamodb, "Table", "AttributeValueTypeDef")
        is TableAttributeValueTypeDef
    )
    assert (
        get_shape_type_stub(
            ServiceNameCatalog.ec2,
            "Client",
            "ClientBatchGetItemRequestItemsKeysTypeDef",
        )
        is None
    )
    assert (
        get_shape_type_stub(
            ServiceNameCatalog.dynamodb,
            "Client",
            "ClientBatchGetItemRequestItems",
        )
        is None
    )


def test_get_output_shape_type_stub() -> None:
    assert (
        get_output_shape_type_stub(
            ServiceNameCatalog.dynamodb,
            "Client",
            "timestamp",
        )
        is Type.datetime
    )
    assert (
        get_output_shape_type_stub(
            ServiceNameCatalog.ec2,
            "Client",
            "ClientBatchGetItemRequestItemsKeysTypeDef",
        )
        is None
    )
    assert (
        get_output_shape_type_stub(
            ServiceNameCatalog.dynamodb,
            "Client",
            "ClientBatchGetItemRequestItems",
        )
        is None
    )
