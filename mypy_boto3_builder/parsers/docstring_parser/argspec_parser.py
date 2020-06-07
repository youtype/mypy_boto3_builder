"""
Converter of function argspec to `Argument` list.
"""
import inspect
from types import FunctionType
from typing import List, Optional

from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_annotation import TypeAnnotation
from mypy_boto3_builder.type_annotations.type_constant import TypeConstant
from mypy_boto3_builder.type_maps.method_type_map import get_method_type_stub


class ArgSpecParser:
    """
    Converter of function argspec to `Argument` list.
    """

    def __init__(self, prefix: str, service_name: ServiceName) -> None:
        self.prefix = prefix
        self.service_name = service_name

    @staticmethod
    def _get_arguments_from_argspec(func: FunctionType) -> List[Argument]:
        arguments: List[Argument] = []
        argspec = inspect.getfullargspec(func)
        for argument_name in argspec.args:
            if argument_name == "factory_self":
                argument_name = "self"
            type_annotation: Optional[TypeAnnotation] = Type.Any
            if not arguments and argument_name in ("self", "cls"):
                type_annotation = None
            arguments.append(Argument(argument_name, type_annotation))
        if argspec.defaults:
            for index, default_value in enumerate(argspec.defaults):
                argument_index = len(arguments) - len(argspec.defaults) + index
                arguments[argument_index].default = TypeConstant(default_value)

        if argspec.varargs:
            arguments.append(Argument(argspec.varargs, Type.Any, prefix="*"))
        for argument_name in argspec.kwonlyargs:
            arguments.append(Argument(argument_name, Type.Any))
        if argspec.kwonlydefaults:
            for argument_name, default_value in argspec.kwonlydefaults.items():
                for argument in arguments:
                    if argument.name != argument_name:
                        continue
                    argument.default = TypeConstant(default_value)
                    break
        if argspec.varkw:
            arguments.append(Argument(argspec.varkw, Type.Any, prefix="**"))
        return arguments

    def get_arguments(
        self, class_name: str, method_name: str, func: FunctionType
    ) -> List[Argument]:
        arguments = self._get_arguments_from_argspec(func)

        for argument in arguments:
            if argument.type is not Type.Any:
                continue

            type_stub = get_method_type_stub(
                self.service_name, class_name, method_name, argument.name
            )
            if type_stub is not None:
                argument.type = type_stub

        return arguments

    def get_return_type(self, class_name: str, method_name: str) -> Optional[FakeAnnotation]:
        type_stub = get_method_type_stub(self.service_name, class_name, method_name, "return")
        if type_stub:
            return type_stub

        return None
