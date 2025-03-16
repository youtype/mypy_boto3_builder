from mypy_boto3_builder.service_name import ServiceNameCatalog
from mypy_boto3_builder.type_maps.required_attribute_map import is_required


def test_is_required() -> None:
    assert is_required(ServiceNameCatalog.ec2, "RandomTypeDef", "PaginationToken") is False
    assert is_required(ServiceNameCatalog.dynamodb, "RandomTypeDef", "Key") is True
    assert is_required(ServiceNameCatalog.dynamodb, "RandomTypeDef", "LastEvaluatedKey") is False
    assert is_required(ServiceNameCatalog.stepfunctions, "RandomTypeDef", "stopDate") is True
    assert (
        is_required(ServiceNameCatalog.stepfunctions, "DescribeExecutionOutputTypeDef", "stopDate")
        is False
    )
    assert (
        is_required(ServiceNameCatalog.stepfunctions, "DescribeExecutionOutputTypeDef", "Date")
        is True
    )
