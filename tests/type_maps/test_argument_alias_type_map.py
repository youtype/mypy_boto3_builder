from mypy_boto3_builder.service_name import ServiceNameCatalog
from mypy_boto3_builder.type_maps.argument_alias_map import get_argument_alias


class TestArgumentAliasTypeMap:
    def test_get_argument_alias(self):
        assert (
            get_argument_alias(ServiceNameCatalog.cloudsearchdomain, "Search", "return")
            == "returnFields"
        )
        assert (
            get_argument_alias(ServiceNameCatalog.cloudsearchdomain, "NoSearch", "return")
            == "return"
        )
        assert (
            get_argument_alias(ServiceNameCatalog.cloudsearchdomain, "Search", "other") == "other"
        )

        assert get_argument_alias(ServiceNameCatalog.ec2, "MyOperation", "Filter") == "Filters"
        assert get_argument_alias(ServiceNameCatalog.ec2, "MyOperation", "Other") == "Other"

        assert get_argument_alias(ServiceNameCatalog.s3, "PutBucketCors", "ContentMD5") is None
        assert (
            get_argument_alias(ServiceNameCatalog.s3, "PutBucketCors", "ContentSHA256")
            == "ContentSHA256"
        )
