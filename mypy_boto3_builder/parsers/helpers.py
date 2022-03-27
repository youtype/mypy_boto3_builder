"""
Helpers for parsing methods and attributes.
"""
import inspect
import textwrap
from types import MethodType

from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.parsers.docstring_parser.argspec_parser import ArgSpecParser
from mypy_boto3_builder.parsers.docstring_parser.docstring_parser import DocstringParser
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_maps.method_argument_map import get_method_arguments_stub
from mypy_boto3_builder.utils.strings import get_class_prefix


def get_public_methods(inspect_class: object) -> dict[str, MethodType]:
    """
    Extract public methods from any class.

    Arguments:
        inspect_class -- Inspect class.

    Returns:
        A dictionary of method name and method.
    """
    class_members = inspect.getmembers(inspect_class)
    methods: dict[str, MethodType] = {}
    for name, member in class_members:
        if not inspect.ismethod(member):
            continue

        if name.startswith("_"):
            continue

        methods[name] = member

    return methods


def parse_method(
    parent_name: str, name: str, method: MethodType, service_name: ServiceName
) -> Method:
    """
    Parse method to a structure.

    Arguments:
        parent_name -- Parent class name.
        method -- Inspect method.

    Returns:
        Method structure.
    """
    logger = get_logger()
    docstring = textwrap.dedent(inspect.getdoc(method) or "")
    method_name = f"{parent_name}.{name}"

    logger.debug(f"Slow parsing of {method_name}: {len(docstring)} chars")
    prefix = f"{get_class_prefix(parent_name)}{get_class_prefix(name)}"
    arg_spec_parser = ArgSpecParser(prefix, service_name)

    arguments = get_method_arguments_stub(service_name, parent_name, name)
    if arguments is None:
        arguments = arg_spec_parser.get_arguments(parent_name, name, method)
        docstring_parser = DocstringParser(service_name, parent_name, name, arguments)
        arguments = docstring_parser.get_arguments(docstring)

    fullargspec = inspect.getfullargspec(method)
    if len(arguments) > 1 and fullargspec.kwonlyargs:
        arguments.insert(1, Argument.kwflag())

    return_type = arg_spec_parser.get_return_type(parent_name, name)
    if return_type is None:
        docstring_parser = DocstringParser(service_name, parent_name, name, [])
        return_type = docstring_parser.get_return_type(docstring)

    result = Method(name=name, arguments=arguments, return_type=return_type)
    result.create_request_type_annotation(f"{parent_name}{get_class_prefix(name)}RequestTypeDef")
    return result
