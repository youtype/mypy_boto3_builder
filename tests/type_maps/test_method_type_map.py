from mypy_boto3_builder.service_name import ServiceNameCatalog
from mypy_boto3_builder.type_maps.method_type_map import (
    get_default_value_stub,
    get_method_type_stub,
)


class TestMethodTypeMap:
    def test_get_method_type_stub(self) -> None:
        assert get_method_type_stub(ServiceNameCatalog.s3, "Client", "copy_object", "CopySource")
        assert (
            get_method_type_stub(ServiceNameCatalog.s3, "Client", "copy_object", "Unknown") is None
        )
        assert (
            get_method_type_stub(ServiceNameCatalog.logs, "Client", "copy_object", "Unknown")
            is None
        )
        assert get_method_type_stub(
            ServiceNameCatalog.sqs, "SomeResource", "receive_messages", "AttributeNames"
        )
        assert (
            get_method_type_stub(
                ServiceNameCatalog.sqs, "SomeResource", "receive_messages", "Attribute"
            )
            is None
        )

    def test_get_default_value_stub(self) -> None:
        assert get_default_value_stub(ServiceNameCatalog.glacier, "Client", "*", "accountId")
        assert get_default_value_stub(ServiceNameCatalog.glacier, "Client", "test", "accountId")
        assert get_default_value_stub(ServiceNameCatalog.glacier, "Client", "*", "any") is None
        assert get_default_value_stub(ServiceNameCatalog.ec2, "Client", "*", "accountId") is None
