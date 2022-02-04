"""
Structure for botocore-stubs package.
"""
from botocore import __version__ as botocore_version

from mypy_boto3_builder.constants import BOTOCORE_STUBS_NAME
from mypy_boto3_builder.structures.package import Package


class BotocoreStubsPackage(Package):
    """
    Structure for botocore-stubs package.
    """

    def __init__(self) -> None:
        super().__init__(name=BOTOCORE_STUBS_NAME, pypi_name=BOTOCORE_STUBS_NAME)
        self.library_name = "botocore"
        self.library_version = botocore_version
