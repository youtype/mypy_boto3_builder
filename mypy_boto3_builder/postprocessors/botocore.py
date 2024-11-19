"""
Postprocessor for all classes and methods.

Copyright 2024 Vlad Emelianov
"""

from mypy_boto3_builder.postprocessors.base import BasePostprocessor


class BotocorePostprocessor(BasePostprocessor):
    """
    Postprocessor for botocore classes and methods.
    """

    def process_package(self) -> None:
        """
        Leave package as it is.
        """
