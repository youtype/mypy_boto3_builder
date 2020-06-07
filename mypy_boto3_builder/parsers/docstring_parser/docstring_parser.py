"""
Botocore docstring parser.
"""
import re
import textwrap
from typing import Dict, List, Optional, Pattern

from pyparsing import ParseException

from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.parsers.docstring_parser.syntax_grammar import SyntaxGrammar
from mypy_boto3_builder.parsers.docstring_parser.type_doc_grammar import TypeDocGrammar
from mypy_boto3_builder.parsers.docstring_parser.type_doc_line import TypeDocLine
from mypy_boto3_builder.parsers.docstring_parser.type_value import TypeValue
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.type_typed_dict import TypeTypedDict
from mypy_boto3_builder.type_maps.docstring_type_map import get_type_from_docstring
from mypy_boto3_builder.type_maps.method_type_map import get_method_type_stub
from mypy_boto3_builder.utils.strings import get_class_prefix, get_line_with_indented


class DocstringParser:
    """
    Botocore docstring parser.

    Arguments:
        prefix -- Prefix for generated TypeDict names.
        class_name -- Parent class name.
        method_name -- Method name.
        arguments -- List of arguments extracted from argspec.
    """

    # Regexp to parse `:param <name>` definitions
    RE_PARAM: Pattern[str] = re.compile("\n:param ")

    def __init__(
        self,
        service_name: ServiceName,
        class_name: str,
        method_name: str,
        arguments: List[Argument],
    ) -> None:
        self.prefix = f"{get_class_prefix(class_name)}{get_class_prefix(method_name)}"
        self.service_name = service_name
        self.class_name = class_name
        self.method_name = method_name
        self.logger = get_logger()
        self.arguments_map: Dict[str, Argument] = {a.name: a for a in arguments if not a.prefix}

    def _find_argument_or_append(self, name: str) -> Argument:
        if name in self.arguments_map:
            return self.arguments_map[name]

        self.arguments_map[name] = Argument(name, Type.Any, Type.none)
        return self.arguments_map[name]

    def _parse_request_syntax(self, input_string: str) -> None:
        if "**Request Syntax**" not in input_string:
            return

        request_syntax_index = input_string.index("**Request Syntax**")
        while request_syntax_index > 0 and input_string[request_syntax_index - 1] == " ":
            request_syntax_index = request_syntax_index - 1
        request_syntax_string = get_line_with_indented(input_string[request_syntax_index:], True)

        SyntaxGrammar.reset()
        SyntaxGrammar.enable_packrat()
        try:
            match = SyntaxGrammar.request_syntax.parseString(request_syntax_string)
        except ParseException as e:
            self.logger.warning(f"Cannot parse request syntax for {self.prefix}")
            self.logger.debug(e)
            return

        argument_groups = match.asDict().get("arguments", [])
        for argument_dict in argument_groups:
            argument_name = argument_dict["name"]
            argument_prefix = self.prefix + get_class_prefix(argument_name)
            argument_value = TypeValue(self.service_name, argument_prefix, argument_dict["value"])
            argument_type = argument_value.get_type()
            argument = self._find_argument_or_append(argument_name)
            argument.type = argument_type

    def _parse_types(self, input_string: str) -> None:
        if ":type " not in input_string:
            return

        type_strings = [i for i in input_string.split("\n") if i.startswith(":type ")]
        TypeDocGrammar.reset()
        for type_string in type_strings:
            try:
                match = TypeDocGrammar.type_definition.parseString(type_string)
            except ParseException as e:
                self.logger.warning(f"Cannot parse type definition {type_string} for {self.prefix}")
                self.logger.debug(e)
                continue

            match_dict = match.asDict()
            argument_name = match_dict["name"]
            type_str = match_dict["type_name"]
            argument = self._find_argument_or_append(argument_name)
            type_stub = get_method_type_stub(
                self.service_name, self.class_name, self.method_name, argument_name
            )
            if type_stub:
                argument.type = type_stub
            else:
                argument.type = get_type_from_docstring(type_str)

    def _parse_params(self, input_string: str) -> None:
        if ":param " not in input_string:
            return

        for re_match in self.RE_PARAM.finditer(input_string):
            start_index = re_match.start()
            param_string = get_line_with_indented(input_string[start_index + 1 :])

            TypeDocGrammar.reset()
            try:
                match = TypeDocGrammar.param_definition.parseString(param_string)
            except ParseException as e:
                self.logger.warning(
                    f"Cannot parse param definition {param_string} for {self.prefix}"
                )
                self.logger.debug(e)
                continue

            argument_line = TypeDocLine(**match.asDict())
            if not argument_line.name:
                continue

            argument_name = argument_line.name
            argument = self._find_argument_or_append(argument_name)
            if argument_line.required:
                argument.default = None

            if not argument.type:
                continue

            self._fix_keys(argument.type, argument_line)

    def _fix_keys(self, type_annotation: FakeAnnotation, argument_line: TypeDocLine) -> None:
        if not argument_line.indented:
            return

        if isinstance(type_annotation, TypeSubscript):
            if not type_annotation.children:
                return
            self._fix_keys_subscript(type_annotation, argument_line)

        if isinstance(type_annotation, TypeTypedDict):
            self._fix_keys_typed_dict(type_annotation, argument_line)

    def _fix_keys_typed_dict(self, typed_dict: TypeTypedDict, argument_line: TypeDocLine,) -> None:
        for line in argument_line.indented:
            if not line.name:
                continue

            attribute = typed_dict.get_attribute(line.name)
            attribute.required = line.required
            if attribute.type_annotation is Type.Any:
                attribute.type_annotation = get_type_from_docstring(line.type_name)
            if not line.indented:
                continue

            self._fix_keys(attribute.type_annotation, line)

    def _fix_keys_subscript(self, subscript: TypeSubscript, argument_line: TypeDocLine,) -> None:
        child = subscript.children[0]
        for line in argument_line.indented:
            if not line.type_name:
                continue
            self._fix_keys(child, line)

    def get_arguments(self, input_string: str) -> List[Argument]:
        """
        Get list of function arguments with type annottions.

        Arguments:
            input_string -- Function docstring.

        Returns:
            A list of `Argument` structures.
        """
        input_string = textwrap.dedent(input_string)
        self._parse_types(input_string)
        self._parse_request_syntax(input_string)
        self._parse_params(input_string)

        arguments = list(self.arguments_map.values())
        arguments.sort(key=lambda x: x.default is not None)
        arguments.sort(key=lambda x: x.prefix is not None)
        return arguments

    def _parse_returns(self, input_string: str) -> Optional[FakeAnnotation]:
        if ":return: " not in input_string and ":returns: " not in input_string:
            return None
        TypeDocGrammar.reset()
        returns_string = input_string[input_string.index(":return") :].split("\n", 1)[0]
        try:
            match = TypeDocGrammar.returns_definition.parseString(returns_string)
        except ParseException as e:
            self.logger.warning(f"Cannot parse returns for {self.prefix}: {e}")
            return None

        description = match.asDict()["description"]
        if description == "None":
            return Type.none

        if "True" in description or "False" in description:
            return Type.bool

        if "url" in description:
            return Type.str

        if description:
            self.logger.info(f"Unknown return type for return: {description}, fallback to None")

        return None

    def _parse_rtype(self, input_string: str) -> Optional[FakeAnnotation]:
        if ":rtype: " not in input_string:
            return None

        TypeDocGrammar.reset()
        rtype_string = input_string[input_string.index(":rtype: ") :].split("\n", 1)[0]
        try:
            match = TypeDocGrammar.rtype_definition.parseString(rtype_string)
        except ParseException as e:
            self.logger.warning(f"Cannot parse rtype for {self.prefix}: {e}")
            return None

        type_name = match.asDict()["type_name"]
        return get_type_from_docstring(type_name)

    def _parse_response_syntax(self, input_string: str) -> Optional[FakeAnnotation]:
        if "**Response Syntax**" not in input_string:
            return None

        response_syntax_index = input_string.index("**Response Syntax**")
        while response_syntax_index > 0 and input_string[response_syntax_index - 1] == " ":
            response_syntax_index -= 1
        response_syntax_string = get_line_with_indented(input_string[response_syntax_index:], True)

        SyntaxGrammar.reset()
        SyntaxGrammar.enable_packrat()
        try:
            match = SyntaxGrammar.response_syntax.parseString(response_syntax_string)
        except ParseException as e:
            self.logger.warning(f"Cannot parse response syntax for {self.prefix}")
            self.logger.debug(e)
            return None

        value = match.asDict()["value"]
        return TypeValue(self.service_name, f"{self.prefix}Response", value).get_type()

    def _parse_response_structure(self, input_string: str) -> Optional[TypeDocLine]:
        if "**Response Structure**" not in input_string:
            return None

        response_structure_index = input_string.index("**Response Structure**")
        while response_structure_index > 0 and input_string[response_structure_index - 1] == " ":
            response_structure_index -= 1

        response_structure_string = get_line_with_indented(
            input_string[response_structure_index:], True
        )
        response_structure_string = textwrap.dedent(response_structure_string)

        TypeDocGrammar.reset()
        try:
            match = TypeDocGrammar.response_structure.parseString(response_structure_string)
        except ParseException as e:
            self.logger.warning(f"Cannot parse response structure for {self.prefix}")
            self.logger.debug(e)
            return None

        return TypeDocLine(**match.asDict())

    def get_return_type(self, input_string: str) -> FakeAnnotation:
        """
        Get function return type annotation.

        Arguments:
            input_string -- Function docstring.

        Returns:
            A valid type annotation.
        """
        input_string = textwrap.dedent(input_string)
        return_type = self._parse_rtype(input_string)
        if return_type is None:
            returns_return_type = self._parse_returns(input_string)
            if returns_return_type:
                return returns_return_type

            return Type.none

        if not return_type.is_dict():
            return return_type

        syntax_return_type = self._parse_response_syntax(input_string)
        if syntax_return_type is None:
            return return_type

        if not isinstance(syntax_return_type, TypeTypedDict):
            return syntax_return_type

        response_structure = self._parse_response_structure(input_string)
        if response_structure:
            self._fix_keys(syntax_return_type, response_structure)

        return syntax_return_type
