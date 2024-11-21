from unittest.mock import MagicMock, Mock, patch

from mypy_boto3_builder.parsers.shape_parser import ShapeParser, TypedDictMap
from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_typed_dict import TypedDictAttribute, TypeTypedDict


class TestShapeParser:
    shape_parser: ShapeParser
    service_name: ServiceName
    loader: MagicMock

    def setup_method(self) -> None:
        self.service_name = ServiceNameCatalog.s3
        self.shape_parser = ShapeParser(self.service_name)
        self.shape_parser._resource_loader = MagicMock()
        self.loader = self.shape_parser._resource_loader

    def test_init(self) -> None:
        assert self.shape_parser.service_name == self.service_name
        ShapeParser(self.service_name)

    def test_get_paginator_names(self) -> None:
        self.loader.load_paginators.return_value = {"pagination": ["c", "a", "b"]}
        assert self.shape_parser.get_paginator_names() == ["a", "b", "c"]

        self.loader.load_paginators.return_value = {"paginations": ["c", "a", "b"]}
        assert self.shape_parser.get_paginator_names() == []

    @patch("mypy_boto3_builder.parsers.shape_parser.ServiceModel")
    def test_get_client_method_map(self, ServiceModelMock: MagicMock) -> None:
        service_name_mock = MagicMock()
        operation_model_mock = MagicMock()
        operation_model_mock.output_shape.serialization = {}
        ServiceModelMock().operation_names = ["my_operation"]
        ServiceModelMock().operation_model.return_value = operation_model_mock
        self.loader.load_service_model.return_value = {
            "resources": {"c": None, "a": None, "b": None},
        }
        shape_parser = ShapeParser(service_name_mock)
        result = shape_parser.get_client_method_map()
        assert "can_paginate" in result
        assert "generate_presigned_url" in result

    def test_get_paginate_method(self) -> None:
        operation_model_mock = MagicMock()
        required_arg_shape_mock = MagicMock()
        optional_arg_shape_mock = MagicMock()
        required_arg_shape_mock.serialization = {}
        optional_arg_shape_mock.serialization = {}
        operation_model_mock.output_shape.serialization = {}
        operation_model_mock.input_shape.serialization = {}
        operation_model_mock.input_shape.members.items.return_value = [
            (
                "required_arg",
                required_arg_shape_mock,
            ),
            (
                "optional_arg",
                optional_arg_shape_mock,
            ),
            (
                "InputToken",
                optional_arg_shape_mock,
            ),
            (
                "skip_arg",
                optional_arg_shape_mock,
            ),
        ]
        service_model_mock = MagicMock()
        service_model_mock.operation_names = ["my_paginator"]
        service_model_mock.operation_model.return_value = operation_model_mock
        self.loader.load_paginators.return_value = {
            "pagination": {"my_paginator": {"input_token": "InputToken", "limit_key": "skip_arg"}},
            "resources": {},
        }
        shape_parser = self.shape_parser
        self.shape_parser.service_model = service_model_mock
        result = shape_parser.get_paginate_method("my_paginator")
        assert result.name == "paginate"
        assert len(result.arguments) == 5
        assert result.arguments[0].name == "self"
        assert result.arguments[1].is_kwflag()
        assert result.arguments[2].name == "required_arg"
        assert result.arguments[3].name == "optional_arg"
        assert result.arguments[4].name == "PaginationConfig"

    @patch("mypy_boto3_builder.parsers.shape_parser.ServiceModel")
    def test_get_collection_filter_method(self, ServiceModelMock: MagicMock) -> None:
        service_name_mock = MagicMock()
        operation_model_mock = MagicMock()
        required_arg_shape_mock = MagicMock()
        optional_arg_shape_mock = MagicMock()
        required_arg_shape_mock.serialization = {}
        optional_arg_shape_mock.serialization = {}
        operation_model_mock.output_shape.serialization = {}
        operation_model_mock.input_shape.serialization = {}
        operation_model_mock.input_shape.required_members = ["required_arg"]
        operation_model_mock.input_shape.members.items.return_value = [
            (
                "required_arg",
                required_arg_shape_mock,
            ),
            (
                "optional_arg",
                optional_arg_shape_mock,
            ),
            (
                "InputToken",
                optional_arg_shape_mock,
            ),
        ]
        ServiceModelMock().operation_names = ["my_operation"]
        ServiceModelMock().operation_model.return_value = operation_model_mock
        collection_mock = MagicMock()
        collection_mock.request.operation = "my_operation"
        shape_parser = ShapeParser(service_name_mock)
        result = shape_parser.get_collection_filter_method(
            "MyCollection",
            collection_mock,
            Type.Any,
        )
        assert result.name == "filter"
        assert len(result.decorators) == 0
        assert len(result.arguments) == 4
        assert result.arguments[0].name == "self"
        assert result.arguments[1].is_kwflag()
        assert result.arguments[2].name == "optional_arg"
        assert result.arguments[3].name == "InputToken"

    def test_fix_typed_dict_names(self) -> None:
        service_name_mock = MagicMock()
        shape_parser = ShapeParser(service_name_mock)
        shape_parser._typed_dict_map = TypedDictMap(
            {
                "TestTypeDef": TypeTypedDict(
                    "TestTypeDef",
                    [
                        TypedDictAttribute("Test", Type.Any, required=False),
                    ],
                ),
                "Test2TypeDef": TypeTypedDict(
                    "Test2TypeDef",
                    [
                        TypedDictAttribute("Test2", Type.Any, required=False),
                    ],
                ),
                "Test3TypeDef": TypeTypedDict(
                    "Test3TypeDef",
                    [
                        TypedDictAttribute("Test3", Type.Any, required=True),
                    ],
                ),
                "Test2ResponseTypeDef": TypeTypedDict(
                    "Test2ResponseTypeDef",
                    [
                        TypedDictAttribute("ResponseMetadata", Type.Any, required=False),
                    ],
                ),
            },
        )
        shape_parser._output_typed_dict_map = TypedDictMap(
            {
                "TestTypeDef": TypeTypedDict(
                    "TestTypeDef",
                    [
                        TypedDictAttribute("Test", Type.Any, required=True),
                    ],
                ),
            },
        )
        shape_parser._response_typed_dict_map = TypedDictMap(
            {
                "Test2TypeDef": TypeTypedDict(
                    "Test2TypeDef",
                    [
                        TypedDictAttribute("Test2", Type.Any, required=True),
                    ],
                ),
            },
        )
        shape_parser.fix_typed_dict_names()
        assert len(shape_parser._typed_dict_map) == 4
        assert len(shape_parser._output_typed_dict_map) == 1
        assert len(shape_parser._response_typed_dict_map) == 1
        assert shape_parser._output_typed_dict_map["TestOutputTypeDef"].name == "TestOutputTypeDef"
        assert shape_parser._output_typed_dict_map["TestOutputTypeDef"].has_optional() is False
        assert (
            shape_parser._response_typed_dict_map["Test2ExtraResponseTypeDef"].has_optional()
            is False
        )

    def test_get_literal_name(self) -> None:
        shape_parser = self.shape_parser

        shape = MagicMock()
        shape.enum = ["as", "b"]
        shape.name = "Type"
        assert shape_parser._get_literal_name(shape) == "TypeType"

        shape.name = "_Type"
        assert shape_parser._get_literal_name(shape) == "TypeType"

        shape.name = "__Type"
        assert shape_parser._get_literal_name(shape) == "TypeType"

        shape.name = "__string"
        assert shape_parser._get_literal_name(shape) == "AsBType"

        shape.name = "Protocol"
        assert shape_parser._get_literal_name(shape) == "ProtocolType"

        shape.name = "Other"
        assert shape_parser._get_literal_name(shape) == "OtherType"

    def test_parse_shape_string(self) -> None:
        shape_parser = self.shape_parser
        shape = Mock()
        shape.name = "MyShape"
        shape.enum = []
        shape.metadata = {"pattern": "any"}
        assert shape_parser._parse_shape_string(shape).render() == "str"

        shape.enum = ["a", "b"]
        assert shape_parser._parse_shape_string(shape).render() == "MyShapeType"
        assert shape_parser._parse_shape_string(shape).render() == "MyShapeType"
        assert shape_parser._parse_shape_string(shape).children == {"a", "b"}

    def test_get_resource_method_map(self) -> None:
        self.loader.load_resources.return_value = {
            "resources": {
                "c": {
                    "actions": {
                        "MyAction": {
                            "resource": {"type": "str"},
                            "request": {
                                "operation": "extract",
                                "params": [
                                    {
                                        "source": "identifier",
                                        "target": "list.new[0]",
                                        "name": "param1",
                                        "type": "bool",
                                    },
                                    {
                                        "source": "string",
                                        "target": "list.new[0]",
                                        "name": "param2",
                                        "type": "str",
                                    },
                                ],
                            },
                        },
                    },
                    "waiters": {"MyWaiter": {"operation": "MyOperation"}},
                    "has": {
                        "SubResource": {
                            "resource": {
                                "identifiers": [
                                    {"source": "input", "name": "ident", "type": "bool"},
                                    {"source": "noinput", "name": "ident", "type": "bool"},
                                ],
                                "type": "str",
                            },
                        },
                        "NoSubResource": {},
                    },
                },
            },
        }
        result = self.shape_parser.get_resource_method_map("c")
        assert len(result.keys()) == 4
