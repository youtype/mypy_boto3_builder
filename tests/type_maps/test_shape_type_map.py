from mypy_boto3_builder.service_name import ServiceNameCatalog
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_maps.shape_type_map import (
    OUTPUT_SHAPE_TYPE_MAP,
    SHAPE_TYPE_MAP,
    TableAttributeValueType,
    UniversalAttributeValueTypeDef,
    get_shape_type_stub,
)


def test_get_shape_type_stub() -> None:
    assert (
        get_shape_type_stub([SHAPE_TYPE_MAP], ServiceNameCatalog.dynamodb, "Client", "boolean")
        is Type.bool
    )
    assert (
        get_shape_type_stub(
            [SHAPE_TYPE_MAP], ServiceNameCatalog.dynamodb, "Client", "AttributeValueTypeDef"
        )
        is UniversalAttributeValueTypeDef
    )
    assert (
        get_shape_type_stub(
            [SHAPE_TYPE_MAP], ServiceNameCatalog.dynamodb, "Table", "AttributeValueTypeDef"
        )
        is TableAttributeValueType
    )
    assert (
        get_shape_type_stub(
            [SHAPE_TYPE_MAP],
            ServiceNameCatalog.ec2,
            "Client",
            "ClientBatchGetItemRequestItemsKeysTypeDef",
        )
        is None
    )
    assert (
        get_shape_type_stub(
            [SHAPE_TYPE_MAP],
            ServiceNameCatalog.dynamodb,
            "Client",
            "ClientBatchGetItemRequestItems",
        )
        is None
    )

    assert (
        get_shape_type_stub(
            [OUTPUT_SHAPE_TYPE_MAP, SHAPE_TYPE_MAP],
            ServiceNameCatalog.dynamodb,
            "Client",
            "timestamp",
        )
        is Type.datetime
    )
    assert (
        get_shape_type_stub(
            [OUTPUT_SHAPE_TYPE_MAP],
            ServiceNameCatalog.ec2,
            "Client",
            "ClientBatchGetItemRequestItemsKeysTypeDef",
        )
        is None
    )
    assert (
        get_shape_type_stub(
            [OUTPUT_SHAPE_TYPE_MAP],
            ServiceNameCatalog.dynamodb,
            "Client",
            "ClientBatchGetItemRequestItems",
        )
        is None
    )
