from unittest.mock import MagicMock

from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.parsers.docstring_parser.docstring_parser import DocstringParser


class TestDocstringParser:
    def test_init(self) -> None:
        argument_mock = MagicMock()
        argument_mock.name = "argument_name"
        argument_mock.prefix = "*"
        service_name_mock = MagicMock()
        docstring_parser = DocstringParser(
            service_name_mock, "ClassName", "method_name", [argument_mock]
        )
        assert docstring_parser.service_name == service_name_mock
        assert docstring_parser.prefix == "ClassNameMethodName"
        assert docstring_parser.class_name == "ClassName"
        assert docstring_parser.method_name == "method_name"
        assert docstring_parser.arguments_map == {}

    def test_get_return_type(self) -> None:
        input_string = """
        :type name: string
        :param name: The Bucket's name identifier. This **must** be set.

        :rtype: :py:class:`S3.Bucket`
        :returns: A Bucket resource
        """
        service_name_mock = MagicMock()
        docstring_parser = DocstringParser(
            service_name_mock, "ClassName", "method_name", []
        )
        result = docstring_parser.get_return_type(input_string)
        assert result.name == "Bucket"

        input_string = """
        :type name: string
        :param name: The Bucket's name identifier. This **must** be set.

        :rtype: dict
        :returns: 

        **Response Syntax** 

        ::

            {
                'RequestCharged': 'requester'
            }
        **Response Structure** 

        - *(dict) --* 

            - **RequestCharged** *(string) --* 

            If present, indicates that the requester was successfully charged for the request.
        """

        result = docstring_parser.get_return_type(input_string)
        assert result.name == "ClassNameMethodNameResponseTypeDef"

        input_string = ":returns: None"
        result = docstring_parser.get_return_type(input_string)
        assert result == Type.none

        input_string = ":returns: Always returns False"
        result = docstring_parser.get_return_type(input_string)
        assert result == Type.bool

        input_string = ":returns: unknown"
        result = docstring_parser.get_return_type(input_string)
        assert result == Type.none

        input_string = """
        :returninvalid
        :returns: real
        """
        result = docstring_parser.get_return_type(input_string)
        assert result == Type.none

        input_string = ""
        result = docstring_parser.get_return_type(input_string)
        assert result == Type.none

    def test_get_arguments(self) -> None:
        input_string = """
        :type name: string
        :param name: The Bucket's name identifier. This **must** be set.
        """
        service_name_mock = MagicMock()
        docstring_parser = DocstringParser(
            service_name_mock, "ClassName", "method_name", []
        )
        result = docstring_parser.get_arguments(input_string)
        assert len(result) == 1
        assert result[0].name == "name"
        assert result[0].type == Type.str
