"""
Class method.
"""
from dataclasses import dataclass

from mypy_boto3_builder.structures.function import Function


@dataclass
class Method(Function):
    """
    Class method.
    """
