"""
Helpers for parsing methods and attributes.
"""
import inspect
import textwrap
from types import FunctionType
from typing import Any, Dict, List

from boto3.resources.base import ServiceResource as Boto3ServiceResource

from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.parsers.docstring_parser.argspec_parser import ArgSpecParser
from mypy_boto3_builder.parsers.docstring_parser.docstring_parser import DocstringParser
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.attribute import Attribute
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_maps.docstring_type_map import get_type_from_docstring
from mypy_boto3_builder.type_maps.method_argument_map import get_method_arguments_stub
from mypy_boto3_builder.type_maps.method_type_map import get_method_type_stub
from mypy_boto3_builder.utils.strings import get_class_prefix


def get_public_methods(inspect_class: Any) -> Dict[str, FunctionType]:
    """
    Extract public methods from any class.

    Arguments:
        inspect_class -- Inspect class.

    Returns:
        A dictionary of method name and method.
    """
    class_members = inspect.getmembers(inspect_class)
    methods: Dict[str, FunctionType] = {}
    for name, member in class_members:
        if not inspect.ismethod(member):
            continue

        if name.startswith("_"):
            continue

        methods[name] = member

    return methods


def parse_attributes(
    service_name: ServiceName, resource_name: str, resource: Boto3ServiceResource
) -> List[Attribute]:
    """
    Extract attributes from boto3 resource.

    Arguments:
        resource -- boto3 service resource.

    Returns:
        A list of Attribute structures.
    """
    result: List[Attribute] = []
    if not resource.meta.client:
        return result
    if not resource.meta.resource_model:
        return result

    service_model = resource.meta.client.meta.service_model
    if resource.meta.resource_model.shape:
        shape = service_model.shape_for(resource.meta.resource_model.shape)
        attributes = resource.meta.resource_model.get_attributes(shape)
        for name, attribute in attributes.items():
            argument_type = get_method_type_stub(service_name, resource_name, "_attributes", name)
            if argument_type is None:
                argument_type = get_type_from_docstring(attribute[1].type_name)
            result.append(Attribute(name, argument_type))

    return result


def parse_method(
    parent_name: str, name: str, method: FunctionType, service_name: ServiceName
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

    return_type = arg_spec_parser.get_return_type(parent_name, name)
    if return_type is None:
        return_type = DocstringParser(service_name, parent_name, name, []).get_return_type(
            docstring
        )

    return Method(name=name, arguments=arguments, return_type=return_type)
