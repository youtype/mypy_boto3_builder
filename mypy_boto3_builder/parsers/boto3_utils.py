"""
Getters for boto3 client and resource from session.
"""
from typing import Optional

from boto3.exceptions import ResourceNotExistsError
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.session import Session
from botocore.client import BaseClient

from mypy_boto3_builder.service_name import ServiceName


def get_boto3_client(session: Session, service_name: ServiceName) -> BaseClient:
    """
    Get boto3 client from `session`.

    Arguments:
        session -- boto3 session.
        service_name -- ServiceName instance.

    Returns:
        Boto3 client.
    """
    return session.client(service_name.boto3_name)  # type: ignore


def get_boto3_resource(
    session: Session, service_name: ServiceName
) -> Optional[Boto3ServiceResource]:
    """
    Get boto3 resource from `session`.

    Arguments:
        session -- boto3 session.
        service_name -- ServiceName instance.

    Returns:
        Boto3 resource or None.
    """
    try:
        return session.resource(service_name.boto3_name)  # type: ignore
    except ResourceNotExistsError:
        return None
