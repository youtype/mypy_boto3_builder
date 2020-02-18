import unittest
from unittest.mock import patch, MagicMock

from botocore.exceptions import UnknownServiceError

from mypy_boto3_builder.parsers.shape_parser import ShapeParser


# pylint: disable=protected-access
class ShapeParserTestCase(unittest.TestCase):
    def test_init(self) -> None:
        session_mock = MagicMock()
        service_name_mock = MagicMock()
        shape_parser = ShapeParser(session_mock, service_name_mock)
        self.assertEqual(shape_parser.service_name, service_name_mock)

        session_mock._loader.load_service_model.side_effect = UnknownServiceError(
            service_name="service_name", known_service_names="known_service_names",
        )
        ShapeParser(session_mock, service_name_mock)

    def test_get_paginator_names(self) -> None:
        session_mock = MagicMock()
        service_name_mock = MagicMock()
        session_mock._loader.load_service_model.return_value = {
            "pagination": ["c", "a", "b"]
        }
        shape_parser = ShapeParser(session_mock, service_name_mock)
        self.assertEqual(shape_parser.get_paginator_names(), ["a", "b", "c"])

        session_mock._loader.load_service_model.return_value = {
            "paginations": ["c", "a", "b"]
        }
        shape_parser = ShapeParser(session_mock, service_name_mock)
        self.assertEqual(shape_parser.get_paginator_names(), [])

    @patch("mypy_boto3_builder.parsers.shape_parser.ServiceModel")
    def test_get_client_method_map(self, ServiceModelMock: MagicMock) -> None:
        session_mock = MagicMock()
        service_name_mock = MagicMock()
        ServiceModelMock().operation_names = ["my_operation"]
        session_mock._loader.load_service_model.return_value = {
            "resources": ["c", "a", "b"]
        }
        shape_parser = ShapeParser(session_mock, service_name_mock)
        result = shape_parser.get_client_method_map()
        self.assertIn("can_paginate", result)
        self.assertIn("generate_presigned_url", result)

    @patch("mypy_boto3_builder.parsers.shape_parser.ServiceModel")
    def test_get_paginate_method(self, ServiceModelMock: MagicMock) -> None:
        session_mock = MagicMock()
        service_name_mock = MagicMock()
        operation_model_mock = MagicMock()
        required_arg_shape_mock = MagicMock()
        optional_arg_shape_mock = MagicMock()
        operation_model_mock.input_shape.members.items.return_value = [
            ("required_arg", required_arg_shape_mock,),
            ("optional_arg", optional_arg_shape_mock,),
            ("InputToken", optional_arg_shape_mock,),
            ("skip_arg", optional_arg_shape_mock,),
        ]
        ServiceModelMock().operation_names = ["my_paginator"]
        ServiceModelMock().operation_model.return_value = operation_model_mock
        session_mock._loader.load_service_model.return_value = {
            "pagination": {
                "my_paginator": {"input_token": "InputToken", "limit_key": "skip_arg"}
            },
            "resources": [],
        }
        shape_parser = ShapeParser(session_mock, service_name_mock)
        result = shape_parser.get_paginate_method("my_paginator")
        self.assertEqual(result.name, "paginate")
        self.assertEqual(len(result.arguments), 4)
        self.assertEqual(result.arguments[0].name, "self")
        self.assertEqual(result.arguments[1].name, "required_arg")
        self.assertEqual(result.arguments[2].name, "optional_arg")
        self.assertEqual(result.arguments[3].name, "PaginationConfig")

    @patch("mypy_boto3_builder.parsers.shape_parser.ServiceModel")
    def test_get_collection_filter_method(self, ServiceModelMock: MagicMock) -> None:
        session_mock = MagicMock()
        service_name_mock = MagicMock()
        operation_model_mock = MagicMock()
        required_arg_shape_mock = MagicMock()
        optional_arg_shape_mock = MagicMock()
        operation_model_mock.input_shape.required_members = ["required_arg"]
        operation_model_mock.input_shape.members.items.return_value = [
            ("required_arg", required_arg_shape_mock,),
            ("optional_arg", optional_arg_shape_mock,),
            ("InputToken", optional_arg_shape_mock,),
        ]
        ServiceModelMock().operation_names = ["my_operation"]
        ServiceModelMock().operation_model.return_value = operation_model_mock
        collection_mock = MagicMock()
        collection_mock.request.operation = "my_operation"
        shape_parser = ShapeParser(session_mock, service_name_mock)
        result = shape_parser.get_collection_filter_method(
            "MyCollection", collection_mock, "self_type"
        )
        self.assertEqual(result.name, "filter")
        self.assertEqual(len(result.decorators), 1)
        self.assertEqual(len(result.arguments), 3)
        self.assertEqual(result.arguments[0].name, "cls")
        self.assertEqual(result.arguments[1].name, "optional_arg")
        self.assertEqual(result.arguments[2].name, "InputToken")
