"""
Main entrypoint for builder.
"""
import sys
from collections.abc import Iterable, Sequence

from boto3 import __version__ as boto3_version
from boto3.session import Session
from botocore import __version__ as botocore_version

from mypy_boto3_builder.cli_parser import Namespace, parse_args
from mypy_boto3_builder.constants import (
    BOTO3_STUBS_NAME,
    BOTOCORE_STUBS_NAME,
    DUMMY_REGION,
    MODULE_NAME,
    PYPI_NAME,
)
from mypy_boto3_builder.jinja_manager import JinjaManager
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.utils.strings import (
    get_anchor_link,
    get_botocore_class_name,
    get_min_build_version,
)
from mypy_boto3_builder.writers.processors import (
    process_boto3_stubs,
    process_boto3_stubs_docs,
    process_botocore_stubs,
    process_master,
    process_service,
    process_service_docs,
)


def get_available_service_names(session: Session) -> list[ServiceName]:
    """
    Get a list of boto3 supported service names.

    Arguments:
        session -- Boto3 session

    Returns:
        A list of supported services.
    """
    available_services = session.get_available_services()
    botocore_session = session._session  # type: ignore
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
    args.output_path.mkdir(exist_ok=True)
    available_service_names = get_available_service_names(session)
    available_service_names_set = {i.name for i in available_service_names}
    service_names: list[ServiceName] = []

    logger.info(f"{len(available_service_names_set)} supported boto3 services discovered")
    if args.list_services:
        for service_name in available_service_names:
            print(
                f"- {service_name.name} : {service_name.class_name} {service_name.boto3_doc_link}"
            )
        return

    selected_service_names = args.service_names or [i.name for i in available_service_names]

    for service_name_str in selected_service_names:
        if service_name_str not in available_service_names_set:
            logger.info(f"Service {service_name_str} is not provided by boto3, skipping")
            continue

        service_name = ServiceNameCatalog.find(service_name_str)
        service_names.append(service_name)

    build_version = args.build_version or boto3_version
    min_build_version = get_min_build_version(build_version)
    botocore_build_version = botocore_version
    if args.build_version and ".post" in args.build_version:
        post_release = args.build_version.split(".post")[-1]
        botocore_build_version = f"{botocore_version}.post{post_release}"
    JinjaManager.update_globals(
        master_pypi_name=PYPI_NAME,
        master_module_name=MODULE_NAME,
        boto3_stubs_name=BOTO3_STUBS_NAME,
        boto3_version=boto3_version,
        botocore_version=botocore_version,
        build_version=build_version,
        min_build_version=min_build_version,
        botocore_build_version=botocore_build_version,
        builder_version=args.builder_version,
        get_anchor_link=get_anchor_link,
        render_docstrings=True,
        hasattr=hasattr,
    )

    logger.info(f"Bulding version {build_version}")

    if args.generate_docs:
        generate_docs(args, service_names, available_service_names, session)
    else:
        generate_stubs(args, service_names, available_service_names, session)

    logger.info("Completed")


def generate_stubs(
    args: Namespace,
    service_names: Sequence[ServiceName],
    available_service_names: Iterable[ServiceName],
    session: Session,
) -> None:
    """
    Generate service and master stubs.

    Arguments:
        args -- Config namespace
        service_names -- Enabled service names
        available_service_names -- All service names
        session -- Botocore session
    """
    logger = get_logger()
    if not args.skip_services:
        total_str = f"{len(service_names)}"
        for index, service_name in enumerate(service_names):
            current_str = f"{{:0{len(total_str)}}}".format(index + 1)
            logger.info(f"[{current_str}/{total_str}] Generating {service_name.module_name} module")
            service_name.boto3_version = boto3_version
            process_service(
                session=session,
                output_path=args.output_path,
                service_name=service_name,
                generate_setup=not args.installed,
                service_names=available_service_names,
            )
            service_name.boto3_version = ServiceName.LATEST

    if not args.skip_master:
        if not args.installed:
            logger.info(f"Generating {MODULE_NAME} module")
            process_master(
                session,
                args.output_path,
                available_service_names,
                generate_setup=not args.installed,
            )

        logger.info(f"Generating {BOTO3_STUBS_NAME} module")
        process_boto3_stubs(
            session,
            args.output_path,
            available_service_names,
            generate_setup=not args.installed,
        )

        logger.info(f"Generating {BOTOCORE_STUBS_NAME} module")
        process_botocore_stubs(
            args.output_path,
            generate_setup=not args.installed,
        )


def generate_docs(
    args: Namespace,
    service_names: Sequence[ServiceName],
    available_service_names: Iterable[ServiceName],
    session: Session,
) -> None:
    """
    Generate service and master docs.

    Arguments:
        args -- Config namespace
        service_names -- Enabled service names
        available_service_names -- All service names
        session -- Botocore session
    """
    logger = get_logger()
    if not args.skip_services:
        total_str = f"{len(service_names)}"
        for index, service_name in enumerate(service_names):
            current_str = f"{{:0{len(total_str)}}}".format(index + 1)
            logger.info(f"[{current_str}/{total_str}] Generating {service_name.module_name} module")
            process_service_docs(
                session=session,
                output_path=args.output_path,
                service_name=service_name,
                service_names=available_service_names,
            )

    if not args.skip_master:
        logger.info(f"Generating {BOTO3_STUBS_NAME} module")
        process_boto3_stubs_docs(
            session,
            args.output_path,
            service_names,
        )


if __name__ == "__main__":
    main()
