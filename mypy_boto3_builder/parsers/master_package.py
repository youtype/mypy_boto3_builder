"""
Parser that produces `structures.MasterPackage`.
"""
from collections.abc import Iterable

from boto3.session import Session

from mypy_boto3_builder.package_data import Boto3StubsPackageData
from mypy_boto3_builder.parsers.fake_service_package import parse_fake_service_package
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.master_package import MasterPackage


def parse_master_package(session: Session, service_names: Iterable[ServiceName]) -> MasterPackage:
    """
    Parse data for master package.

    Arguments:
        session -- boto3 session.
        service_names -- All available service names.

    Returns:
        MasterPackage structure.
    """
    result = MasterPackage(service_names=service_names)
    for service_name in result.service_names:
        result.service_packages.append(
            parse_fake_service_package(session, service_name, Boto3StubsPackageData)
        )

    return result
