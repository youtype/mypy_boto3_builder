"""
Main entrypoint for builder.
"""
import sys
from collections.abc import Iterable

from boto3.session import Session

from mypy_boto3_builder.aiobotocore_generator import AioBotocoreGenerator
from mypy_boto3_builder.boto3_generator import Boto3Generator
from mypy_boto3_builder.cli_parser import parse_args
from mypy_boto3_builder.constants import DUMMY_REGION, Product
from mypy_boto3_builder.jinja_manager import JinjaManager
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.parsers.boto3_utils import get_boto3_resource
from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.utils.botocore_changelog import BotocoreChangelog
from mypy_boto3_builder.utils.strings import get_anchor_link, get_botocore_class_name
from mypy_boto3_builder.utils.version import get_botocore_version


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
        for updated_service_name in BotocoreChangelog().get_updated_service_names(botocore_version):
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

    for service_name in available_service_names:
        service_name.has_service_resource = bool(get_boto3_resource(session, service_name))
    for service_name in service_names:
        service_name.has_service_resource = bool(get_boto3_resource(session, service_name))

    JinjaManager.update_globals(
        builder_version=args.builder_version,
        get_anchor_link=get_anchor_link,
        render_docstrings=True,
        hasattr=hasattr,
        len=len,
    )

    boto3_generator = Boto3Generator(
        service_names=service_names,
        available_service_names=available_service_names,
        master_service_names=service_names if args.partial_overload else available_service_names,
        session=session,
        output_path=args.output_path,
        generate_setup=not args.installed,
        skip_published=args.skip_published,
        disable_smart_version=args.disable_smart_version,
        version=args.build_version,
    )
    aiobotocore_generator = AioBotocoreGenerator(
        service_names=service_names,
        available_service_names=available_service_names,
        master_service_names=service_names if args.partial_overload else available_service_names,
        session=session,
        output_path=args.output_path,
        generate_setup=not args.installed,
        skip_published=args.skip_published,
        disable_smart_version=args.disable_smart_version,
        version=args.build_version,
    )
    generators_map = {
        Product.boto3: boto3_generator.generate_stubs,
        Product.boto3_services: boto3_generator.generate_service_stubs,
        Product.boto3_docs: boto3_generator.generate_docs,
        Product.aiobotocore: aiobotocore_generator.generate_stubs,
        Product.aiobotocore_services: aiobotocore_generator.generate_service_stubs,
        Product.aiobotocore_docs: aiobotocore_generator.generate_docs,
    }
    generators = [generators_map[p] for p in args.products]
    for generator in generators:
        generator()

    logger.info("Completed")


if __name__ == "__main__":
    main()
