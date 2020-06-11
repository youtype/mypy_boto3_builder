"""
String to type annotation map to replace overriden botocore shapes.
"""
from typing import Dict, Optional

from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript

DynamoDBValue = TypeSubscript(
    Type.Union,
    [
        Type.bytes,
        Type.bytearray,
        Type.str,
        Type.int,
        Type.Decimal,
        Type.bool,
        TypeSubscript(Type.Set, [Type.int]),
        TypeSubscript(Type.Set, [Type.Decimal]),
        TypeSubscript(Type.Set, [Type.str]),
        TypeSubscript(Type.Set, [Type.bytes]),
        TypeSubscript(Type.Set, [Type.bytearray]),
        Type.ListAny,
        Type.DictStrAny,
        Type.none,
    ],
)

SHAPE_TYPE_MAP: Dict[ServiceName, Dict[str, FakeAnnotation]] = {
    ServiceNameCatalog.dynamodb: {
        "AttributeValueTypeDef": DynamoDBValue,
        "ClientBatchGetItemRequestItemsKeysTypeDef": DynamoDBValue,
        "ClientBatchGetItemResponseResponsesTypeDef": DynamoDBValue,
        "ClientBatchGetItemResponseUnprocessedKeysKeysTypeDef": DynamoDBValue,
        "ClientBatchWriteItemRequestItemsDeleteRequestKeyTypeDef": DynamoDBValue,
        "ClientBatchWriteItemRequestItemsPutRequestItemTypeDef": DynamoDBValue,
        "ClientBatchWriteItemResponseItemCollectionMetricsItemCollectionKeyTypeDef": DynamoDBValue,
        "ClientBatchWriteItemResponseUnprocessedItemsDeleteRequestKeyTypeDef": DynamoDBValue,
        "ClientBatchWriteItemResponseUnprocessedItemsPutRequestItemTypeDef": DynamoDBValue,
        "ClientDeleteItemExpectedAttributeValueListTypeDef": DynamoDBValue,
        "ClientDeleteItemExpectedValueTypeDef": DynamoDBValue,
        "ClientDeleteItemExpressionAttributeValuesTypeDef": DynamoDBValue,
        "ClientDeleteItemKeyTypeDef": DynamoDBValue,
        "ClientDeleteItemResponseAttributesTypeDef": DynamoDBValue,
        "ClientDeleteItemResponseItemCollectionMetricsItemCollectionKeyTypeDef": DynamoDBValue,
        "ClientGetItemKeyTypeDef": DynamoDBValue,
        "ClientGetItemResponseItemTypeDef": DynamoDBValue,
        "ClientPutItemExpectedAttributeValueListTypeDef": DynamoDBValue,
        "ClientPutItemExpectedValueTypeDef": DynamoDBValue,
        "ClientPutItemExpressionAttributeValuesTypeDef": DynamoDBValue,
        "ClientPutItemItemTypeDef": DynamoDBValue,
        "ClientPutItemResponseAttributesTypeDef": DynamoDBValue,
        "ClientPutItemResponseItemCollectionMetricsItemCollectionKeyTypeDef": DynamoDBValue,
        "ClientQueryExclusiveStartKeyTypeDef": DynamoDBValue,
        "ClientQueryExpressionAttributeValuesTypeDef": DynamoDBValue,
        "ClientQueryKeyConditionsAttributeValueListTypeDef": DynamoDBValue,
        "ClientQueryQueryFilterAttributeValueListTypeDef": DynamoDBValue,
        "ClientQueryResponseItemsTypeDef": DynamoDBValue,
        "ClientQueryResponseLastEvaluatedKeyTypeDef": DynamoDBValue,
        "ClientScanExclusiveStartKeyTypeDef": DynamoDBValue,
        "ClientScanExpressionAttributeValuesTypeDef": DynamoDBValue,
        "ClientScanResponseItemsTypeDef": DynamoDBValue,
        "ClientScanResponseLastEvaluatedKeyTypeDef": DynamoDBValue,
        "ClientScanScanFilterAttributeValueListTypeDef": DynamoDBValue,
        "ClientTransactGetItemsResponseResponsesItemTypeDef": DynamoDBValue,
        "ClientTransactGetItemsTransactItemsGetKeyTypeDef": DynamoDBValue,
        "ClientTransactWriteItemsResponseItemCollectionMetricsItemCollectionKeyTypeDef": DynamoDBValue,
        "ClientTransactWriteItemsTransactItemsConditionCheckExpressionAttributeValuesTypeDef": DynamoDBValue,
        "ClientTransactWriteItemsTransactItemsConditionCheckKeyTypeDef": DynamoDBValue,
        "ClientTransactWriteItemsTransactItemsDeleteExpressionAttributeValuesTypeDef": DynamoDBValue,
        "ClientTransactWriteItemsTransactItemsDeleteKeyTypeDef": DynamoDBValue,
        "ClientTransactWriteItemsTransactItemsPutExpressionAttributeValuesTypeDef": DynamoDBValue,
        "ClientTransactWriteItemsTransactItemsPutItemTypeDef": DynamoDBValue,
        "ClientTransactWriteItemsTransactItemsUpdateExpressionAttributeValuesTypeDef": DynamoDBValue,
        "ClientTransactWriteItemsTransactItemsUpdateKeyTypeDef": DynamoDBValue,
        "ClientUpdateItemAttributeUpdatesValueTypeDef": DynamoDBValue,
        "ClientUpdateItemExpectedAttributeValueListTypeDef": DynamoDBValue,
        "ClientUpdateItemExpectedValueTypeDef": DynamoDBValue,
        "ClientUpdateItemExpressionAttributeValuesTypeDef": DynamoDBValue,
        "ClientUpdateItemKeyTypeDef": DynamoDBValue,
        "ClientUpdateItemResponseAttributesTypeDef": DynamoDBValue,
        "ClientUpdateItemResponseItemCollectionMetricsItemCollectionKeyTypeDef": DynamoDBValue,
    },
}


def get_shape_type_stub(
    service_name: ServiceName, typed_dict_name: str
) -> Optional[FakeAnnotation]:
    """
    Get stub type for botocore shape.

    Arguments:
        service_name -- Service name.
        typed_dict_name -- Target TypedDict name.

    Returns:
        Type annotation or None.
    """
    if service_name not in SHAPE_TYPE_MAP:
        return None

    service_shape_type_map = SHAPE_TYPE_MAP[service_name]
    if typed_dict_name not in service_shape_type_map:
        return None

    return service_shape_type_map[typed_dict_name]
