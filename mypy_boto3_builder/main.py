"""
Main entrypoint for builder.
"""
import sys
from collections.abc import Iterable
from typing import Sequence

from boto3.session import Session

from mypy_boto3_builder.cli_parser import Namespace, parse_args
from mypy_boto3_builder.constants import DUMMY_REGION, Product, ProductLibrary
from mypy_boto3_builder.generators.aiobotocore_generator import AioBotocoreGenerator
from mypy_boto3_builder.generators.base_generator import BaseGenerator
from mypy_boto3_builder.generators.boto3_generator import Boto3Generator
from mypy_boto3_builder.jinja_manager import JinjaManager
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.utils.botocore_changelog import BotocoreChangelog
from mypy_boto3_builder.utils.strings import get_anchor_link, get_botocore_class_name
from mypy_boto3_builder.utils.version import get_botocore_version, get_builder_version


def get_selected_service_names(
    selected: Iterable[str],
    available: Iterable[ServiceName],
) -> list[ServiceName]:
    """
    Get a list of selected service names.

    Supports `updated` to select only services updated in currect `boto3` release.
    Supports `all` to select all available service names.

    Arguments:
        selected -- Selected service names as strings.
        available -- All ServiceNames available in current boto3 release.

    Returns:
        A list of selected ServiceNames.
    """
    logger = get_logger()
    available_map = {i.name: i for i in available}
    result: list[ServiceName] = []
    selected_service_names = list(selected)
    botocore_version = get_botocore_version()
    if ServiceName.ALL in selected_service_names:
        return list(available)
    if ServiceName.UPDATED in selected_service_names:
        selected_service_names.remove(ServiceName.UPDATED)
        updated_service_names = BotocoreChangelog().get_updated_service_names(botocore_version)
        for updated_service_name in updated_service_names:
            if updated_service_name in available_map:
                selected_service_names.append(updated_service_name)

    for service_name_str in selected_service_names:
        if service_name_str not in available_map:
            logger.info(f"Service {service_name_str} is not provided by botocore, skipping")
            continue
        result.append(available_map[service_name_str])

    return result


def get_available_service_names(session: Session) -> list[ServiceName]:
    """
    Get a list of boto3 supported service names.

    Arguments:
        session -- Boto3 session

    Returns:
        A list of supported services.
    """
    available_services = session.get_available_services()
    botocore_session = session._session
    result: list[ServiceName] = []
    for name in available_services:
        service_data = botocore_session.get_service_data(name)
        metadata = service_data["metadata"]
        class_name = get_botocore_class_name(metadata)
        service_name = ServiceNameCatalog.add(name, class_name)
        result.append(service_name)
    return result


def generate_product(
    product: Product,
    args: Namespace,
    session: Session,
    service_names: Sequence[ServiceName],
    master_service_names: Sequence[ServiceName],
) -> None:
    """
    Generate a selected product.

    Arguments:
        product -- Product to generate
        args -- CLI namespace
        session -- Boto3 session
        service_names -- Selected service names
        master_service_names -- Service names included in master
    """
    generator_cls = {
        ProductLibrary.boto3: Boto3Generator,
        ProductLibrary.aiobotocore: AioBotocoreGenerator,
    }[product.get_library()]
    generator: BaseGenerator = generator_cls(
        service_names=service_names,
        master_service_names=master_service_names,
        session=session,
        output_path=args.output_path,
        generate_setup=not args.installed,
        skip_published=args.skip_published,
        disable_smart_version=args.disable_smart_version,
        version=args.build_version,
    )
    generator.generate_product(product.get_type())


def main() -> None:
    """
    Main entrypoint for builder.
    """
    args = parse_args(sys.argv[1:])
    logger = get_logger(level=args.log_level)
    session = Session(region_name=DUMMY_REGION)

    botocore_session = session._session
    botocore_session.set_credentials("access_key", "secret_key", "token")

    args.output_path.mkdir(exist_ok=True, parents=True)
    available_service_names = get_available_service_names(session)

    logger.info(f"{len(available_service_names)} supported boto3 services discovered")
    if args.list_services:
        for service_name in available_service_names:
            print(
                f"- {service_name.name} : {service_name.class_name} {service_name.boto3_doc_link}"
            )
        return

    service_names = get_selected_service_names(args.service_names, available_service_names)
    master_service_names = service_names if args.partial_overload else available_service_names

    JinjaManager.update_globals(
        builder_version=get_builder_version(),
        get_anchor_link=get_anchor_link,
        render_docstrings=True,
        hasattr=hasattr,
        len=len,
        sorted=sorted,
    )

    for product in args.products:
        logger.info(f"Generating {product} product")
        generate_product(product, args, session, service_names, master_service_names)

    logger.info("Completed")


if __name__ == "__main__":
    main()
