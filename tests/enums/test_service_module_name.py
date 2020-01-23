import unittest

from mypy_boto3_builder.enums.service_module_name import ServiceModuleName


class ServiceModuleNameTestCase(unittest.TestCase):
    def test_properties(self) -> None:
        self.assertEqual(ServiceModuleName.paginator.file_name, "paginator.py")
        self.assertEqual(
            ServiceModuleName.paginator.template_name, "paginator.py.jinja2"
        )
