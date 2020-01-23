import unittest

from mypy_boto3_builder.service_name import ServiceNameCatalog
from mypy_boto3_builder.type_maps.method_type_map import get_method_type_stub


class MethodTypeMapTestCase(unittest.TestCase):
    def test_get_method_type_stub(self) -> None:
        self.assertTrue(
            get_method_type_stub(
                ServiceNameCatalog.s3, "Client", "copy_object", "CopySource"
            )
        )
        self.assertTrue(
            get_method_type_stub(
                ServiceNameCatalog.ec2, "Any", "create_tags", "Resources"
            )
        )
        self.assertIsNone(
            get_method_type_stub(
                ServiceNameCatalog.s3, "Client", "copy_object", "Unknown"
            )
        )
        self.assertIsNone(
            get_method_type_stub(
                ServiceNameCatalog.logs, "Client", "copy_object", "Unknown"
            )
        )
