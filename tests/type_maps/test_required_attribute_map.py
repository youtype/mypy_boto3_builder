from mypy_boto3_builder.service_name import ServiceNameCatalog
from mypy_boto3_builder.type_maps.required_attribute_map import get_attribute_required_override


def test_get_attribute_required_override() -> None:
    assert (
        get_attribute_required_override(ServiceNameCatalog.ec2, "RandomTypeDef", "PaginationToken")
        is False
    )
    assert (
        get_attribute_required_override(ServiceNameCatalog.dynamodb, "RandomTypeDef", "Key") is None
    )
    assert (
        get_attribute_required_override(
            ServiceNameCatalog.dynamodb, "RandomTypeDef", "LastEvaluatedKey"
        )
        is False
    )
    assert (
        get_attribute_required_override(
            ServiceNameCatalog.stepfunctions, "RandomTypeDef", "stopDate"
        )
        is None
    )
    assert (
        get_attribute_required_override(
            ServiceNameCatalog.stepfunctions, "DescribeExecutionOutputTypeDef", "stopDate"
        )
        is False
    )
    assert (
        get_attribute_required_override(
            ServiceNameCatalog.stepfunctions, "DescribeExecutionOutputTypeDef", "Date"
        )
        is None
    )
    assert (
        get_attribute_required_override(
            ServiceNameCatalog.sqs, "ChangeMessageVisibilityBatchResultTypeDef", "Successful"
        )
        is False
    )
    assert (
        get_attribute_required_override(
            ServiceNameCatalog.sqs, "ChangeMessageVisibilityBatchResultTypeDef", "Failed"
        )
        is False
    )
