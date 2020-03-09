from mypy_boto3_builder.service_name import ServiceNameCatalog
from mypy_boto3_builder.type_maps.method_type_map import get_method_type_stub


class TestMethodTypeMap:
    def test_get_method_type_stub(self) -> None:
        assert get_method_type_stub(
            ServiceNameCatalog.s3, "Client", "copy_object", "CopySource"
        )
        assert get_method_type_stub(
            ServiceNameCatalog.ec2, "Any", "create_tags", "Resources"
        )
        assert (
            get_method_type_stub(
                ServiceNameCatalog.s3, "Client", "copy_object", "Unknown"
            )
            is None
        )
        assert (
            get_method_type_stub(
                ServiceNameCatalog.logs, "Client", "copy_object", "Unknown"
            )
            is None
        )
