"""
Parser that produces `structures.MasterModule`.
"""
from typing import List

from boto3.session import Session

from mypy_boto3_builder.parsers.fake_service_package import parse_fake_service_package
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.master_package import MasterPackage


def parse_master_package(session: Session, service_names: List[ServiceName]) -> MasterPackage:
    """
    Parse data for master package.

    Arguments:
        session -- boto3 session.

    Returns:
        MasterModule structure.
    """
    result = MasterPackage(service_names=service_names)
    for service_name in result.service_names:
        result.service_packages.append(parse_fake_service_package(session, service_name))

    return result
