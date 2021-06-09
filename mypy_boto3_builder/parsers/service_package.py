"""
Parser that produces `structures.ServiceModule`.
"""

from typing import List

from boto3.session import Session
from botocore import xform_name

from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.parsers.client import parse_client
from mypy_boto3_builder.parsers.service_resource import parse_service_resource
from mypy_boto3_builder.parsers.shape_parser import ShapeParser
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.paginator import Paginator
from mypy_boto3_builder.structures.service_package import ServicePackage
from mypy_boto3_builder.structures.waiter import Waiter


def parse_service_package(session: Session, service_name: ServiceName) -> ServicePackage:
    """
    Extract all data from boto3 service package.

    Arguments:
        session -- boto3 session.
        service_name -- Target service name.

    Returns:
        ServiceModule structure.
    """
    logger = get_logger()
    logger.debug("Parsing Shapes")
    shape_parser = ShapeParser(session, service_name)
    logger.debug("Parsing Client")
    client = parse_client(session, service_name, shape_parser)
    service_resource = parse_service_resource(session, service_name, shape_parser)

    result = ServicePackage(
        name=service_name.module_name,
        pypi_name=service_name.pypi_name,
        service_name=service_name,
        client=client,
        service_resource=service_resource,
    )

    waiter_names: List[str] = client.boto3_client.waiter_names
    for waiter_name in waiter_names:
        logger.debug(f"Parsing Waiter {waiter_name}")
        waiter = client.boto3_client.get_waiter(waiter_name)
        waiter_record = Waiter(
            name=f"{waiter.name}Waiter",
            waiter_name=waiter_name,
            service_name=service_name,
        )

        wait_method = shape_parser.get_wait_method(waiter.name)
        wait_method.docstring = (
            "[Show boto3 documentation]"
            f"({service_name.get_boto3_doc_link('Waiter', waiter_record.name)})\n"
            "[Show boto3-stubs documentation]"
            f"({service_name.get_doc_link('waiters', waiter.name)})"
        )
        waiter_record.methods.append(wait_method)
        result.waiters.append(waiter_record)

    for paginator_name in shape_parser.get_paginator_names():
        logger.debug(f"Parsing Paginator {paginator_name}")
        operation_name = xform_name(paginator_name)
        # boto3_paginator = client.boto3_client.get_paginator(operation_name)
        paginator_record = Paginator(
            name=f"{paginator_name}Paginator",
            paginator_name=paginator_name,
            operation_name=operation_name,
            service_name=service_name,
        )

        paginate_method = shape_parser.get_paginate_method(paginator_name)
        paginate_method.docstring = (
            "[Show boto3 documentation]"
            f"({service_name.get_boto3_doc_link('Paginator', paginator_name, 'paginate')})\n"
            "[Show boto3-stubs documentation]"
            f"({service_name.get_doc_link('paginators', paginator_record.name)})"
        )
        paginator_record.methods.append(paginate_method)
        result.paginators.append(paginator_record)

    if result.paginators:
        if len(result.paginators) == 1:
            method = result.paginators[0].get_client_method()
            method.decorators.clear()
            result.client.methods.append(method)
        else:
            for paginator in result.paginators:
                method = paginator.get_client_method()
                result.client.methods.append(method)

    if result.waiters:
        if len(result.waiters) == 1:
            method = result.waiters[0].get_client_method()
            method.decorators.clear()
            result.client.methods.append(method)
        else:
            for package_waiter in result.waiters:
                method = package_waiter.get_client_method()
                result.client.methods.append(method)

    result.typed_dicts = result.extract_typed_dicts()
    result.literals = result.extract_literals()
    result.validate()

    return result
