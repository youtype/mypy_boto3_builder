"""
Class method.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Iterator

from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.function import Function


class Method(Function):
    """
    Class method.
    """

    def get_self_argument(self) -> Argument | None:
        """
        Get `self` or `cls` argument.
        """
        if not self.arguments:
            return None
        first_argument = self.arguments[0]
        if first_argument.name in Argument.FIRST_NAMES:
            return first_argument

        return None

    def iterate_call_arguments(self) -> Iterator[Argument]:
        """
        Iterate over arguments that are used in method call.
        """
        self_argument = self.get_self_argument()
        for argument in super().iterate_call_arguments():
            if argument == self_argument:
                continue
            yield argument

    def iterate_packed_arguments(self) -> Iterator[Argument]:
        """
        Iterate over packed arguments for KW-only methods.
        """
        packed_arguments = super().iterate_packed_arguments()
        if not self.is_kw_only() or not self.request_type_annotation:
            yield from packed_arguments
            return

        self_argument = self.get_self_argument()
        if self_argument:
            yield self_argument

        yield from packed_arguments

    def has_arguments(self) -> bool:
        """
        Whether method has arguments.
        """
        self_argument = self.get_self_argument()
        if not self_argument:
            return super().has_arguments()

        return len(self.arguments) > 1
