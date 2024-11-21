"""
Methods for boto3 injected methods.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Mapping, Sequence
from typing import Final

from mypy_boto3_builder.constants import CLIENT
from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_maps.service_stub_map import dynamodb, ec2, rds, s3
from mypy_boto3_builder.utils.strings import get_type_def_name

ClassTypeMap = Mapping[str, Sequence[Method]]
ServiceStubMap = Mapping[ServiceName, ClassTypeMap]

SERVICE_STUB_MAP: Final[ServiceStubMap] = {
    ServiceNameCatalog.ec2: {
        CLIENT: ec2.CLIENT_METHODS,
        "Instance": ec2.INSTANCE_METHODS,
        "DhcpOptions": ec2.COMMON_METHODS,
        "Image": ec2.COMMON_METHODS,
        "InternetGateway": ec2.COMMON_METHODS,
        "NetworkAcl": ec2.COMMON_METHODS,
        "NetworkInterface": ec2.COMMON_METHODS,
        "SecurityGroup": ec2.COMMON_METHODS,
        "Snapshot": ec2.COMMON_METHODS,
        "Volume": ec2.COMMON_METHODS,
        "RouteTable": ec2.COMMON_METHODS,
        "Subnet": ec2.COMMON_METHODS,
        "Vpc": ec2.COMMON_METHODS,
    },
    ServiceNameCatalog.dynamodb: {
        "Table": dynamodb.TABLE_METHODS,
    },
    ServiceNameCatalog.rds: {
        CLIENT: rds.CLIENT_METHODS,
    },
    ServiceNameCatalog.s3: {
        CLIENT: s3.CLIENT_METHODS,
        "Bucket": s3.BUCKET_METHODS,
        "Object": s3.OBJECT_METHODS,
        "ObjectSummary": s3.OBJECT_SUMMARY_METHODS,
    },
}


def get_stub_method_map(service_name: ServiceName, parent: str) -> dict[str, Method]:
    """
    Get boto3 injected methods.
    """
    methods = SERVICE_STUB_MAP.get(service_name, {}).get(parent, [])
    for method in methods:
        method.create_request_type_annotation(get_type_def_name(parent, method.name, "Request"))
    return {method.name: method for method in methods}
