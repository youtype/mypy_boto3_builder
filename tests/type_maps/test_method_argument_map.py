from mypy_boto3_builder.service_name import ServiceNameCatalog
from mypy_boto3_builder.type_maps.method_argument_map import get_method_arguments_stub


class TestMethodArgumentMap:
    def test_get_method_arguments_stub(self) -> None:
        assert get_method_arguments_stub(
            ServiceNameCatalog.ec2, "Instance", "delete_tags"
        )[0]
        assert (
            get_method_arguments_stub(ServiceNameCatalog.ec2, "Instance", "unknown")
            is None
        )
        assert (
            get_method_arguments_stub(ServiceNameCatalog.ec2, "unknown", "delete_tags")
            is None
        )
