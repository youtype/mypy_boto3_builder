import unittest

from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog


class ServiceNameTestCase(unittest.TestCase):
    def test_init(self) -> None:
        service_name = ServiceName("my-service", "MyService")
        self.assertEqual(service_name.name, "my-service")
        self.assertEqual(service_name.import_name, "my_service")
        self.assertEqual(service_name.class_name, "MyService")
        self.assertEqual(service_name.boto3_version, "latest")
        self.assertEqual(service_name.boto3_name, "my-service")
        self.assertEqual(service_name.module_name, "mypy_boto3_my_service")
        self.assertEqual(service_name.pypi_name, "mypy-boto3-my-service")
        self.assertEqual(service_name.extras_name, "my-service")
        self.assertEqual(
            service_name.doc_link,
            "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/my-service.html#MyService",
        )

    def test_special_name(self) -> None:
        self.assertEqual(ServiceName("lambda", "MyService").import_name, "lambda_")
        self.assertEqual(
            ServiceName("lambda", "MyService").module_name, "mypy_boto3_lambda"
        )

    def test_is_essential(self) -> None:
        self.assertFalse(ServiceName("my-service", "MyService").is_essential())
        self.assertTrue(ServiceName("lambda", "MyService").is_essential())


class ServiceNameCatalogTestCase(unittest.TestCase):
    def test_find(self) -> None:
        self.assertEqual(ServiceNameCatalog.find("ec2").name, "ec2")

        with self.assertRaises(ValueError):
            ServiceNameCatalog.find("unknown")
