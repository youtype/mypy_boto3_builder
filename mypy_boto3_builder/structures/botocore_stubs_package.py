"""
Structure for botocore-stubs package.
"""
from mypy_boto3_builder.package_data import BotocoreStubsPackageData
from mypy_boto3_builder.structures.package import Package


class BotocoreStubsPackage(Package):
    """
    Structure for botocore-stubs package.
    """

    def __init__(self) -> None:
        super().__init__(BotocoreStubsPackageData)
