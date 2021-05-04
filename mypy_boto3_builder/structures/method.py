"""
Class method.
"""
from typing import List

from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.function import Function


class Method(Function):
    """
    Class method.
    """

    @property
    def call_arguments(self) -> List[Argument]:
        """
        Arguments that are used in method call.
        """
        if self.arguments and self.arguments[0].name in ("self", "cls"):
            return self.arguments[1:]

        return self.arguments
