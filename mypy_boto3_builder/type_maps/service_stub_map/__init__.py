"""
Methods for boto3 injected methods.
"""
from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_maps.service_stub_map import dynamodb, s3

ClassTypeMap = dict[str, list[Method]]
ServiceStubMap = dict[ServiceName, ClassTypeMap]

SERVICE_STUB_MAP: ServiceStubMap = {
    ServiceNameCatalog.s3: {
        "Client": s3.CLIENT_METHODS,
        "Bucket": s3.BUCKET_METHODS,
        "Object": s3.OBJECT_METHODS,
    },
    ServiceNameCatalog.dynamodb: {
        "Table": dynamodb.TABLE_METHODS,
    },
}


def get_stub_method_map(service_name: ServiceName, parent: str) -> dict[str, Method]:
    """
    Get boto3 injected methods.
    """
    methods = SERVICE_STUB_MAP.get(service_name, {}).get(parent, [])
    return {method.name: method for method in methods}