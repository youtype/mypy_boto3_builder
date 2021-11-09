"""
Main entrypoint for builder.
"""
import sys
from collections.abc import Iterable, Sequence

from boto3 import __version__ as boto3_version
from boto3.session import Session
from botocore import __version__ as botocore_version
from newversion.version import Version

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
from mypy_boto3_builder.utils.boto3_changelog import Boto3Changelog
from mypy_boto3_builder.utils.pypi_manager import PyPIManager
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
    if ServiceName.ALL in selected_service_names:
        return list(available)
    if ServiceName.UPDATED in selected_service_names:
        selected_service_names.remove(ServiceName.UPDATED)
        for updated_service_name in Boto3Changelog().get_updated_service_names(boto3_version):
            if updated_service_name in available_map:
                selected_service_names.append(updated_service_name)

    for service_name_str in selected_service_names:
        if service_name_str not in available_map:
            logger.info(f"Service {service_name_str} is not provided by boto3, skipping")
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

    args.output_path.mkdir(exist_ok=True)
    available_service_names = get_available_service_names(session)

    logger.info(f"{len(available_service_names)} supported boto3 services discovered")
    if args.list_services:
        for service_name in available_service_names:
            print(
                f"- {service_name.name} : {service_name.class_name} {service_name.boto3_doc_link}"
            )
        return

    service_names = get_selected_service_names(args.service_names, available_service_names)

    build_version = args.build_version or boto3_version
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
        min_build_version=get_min_build_version(build_version),
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
        generate_stubs(
            args=args,
            service_names=service_names,
            available_service_names=available_service_names,
            session=session,
        )

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
        build_version -- Package build version
    """
    logger = get_logger()
    master_service_names = service_names if args.partial_overload else available_service_names

    if not args.skip_services:
        total_str = f"{len(service_names)}"
        for index, service_name in enumerate(service_names):
            current_str = f"{{:0{len(total_str)}}}".format(index + 1)
            service_name.boto3_version = boto3_version

            pypi_manager = PyPIManager(service_name.pypi_name)
            package_version = args.build_version or boto3_version
            if args.skip_published and pypi_manager.has_version(package_version):
                logger.info(
                    f"[{current_str}/{total_str}]"
                    f" Skipping {service_name.module_name} {package_version}, already on PyPI"
                )
                continue
            if pypi_manager.has_version(package_version):
                package_version = pypi_manager.get_next_version(package_version)

            logger.info(
                f"[{current_str}/{total_str}]"
                f" Generating {service_name.module_name} {package_version}"
            )
            process_service(
                session=session,
                output_path=args.output_path,
                service_name=service_name,
                generate_setup=not args.installed,
                service_names=master_service_names,
                version=package_version,
            )
            service_name.boto3_version = ServiceName.LATEST

    if not args.skip_master:
        if not args.installed:
            generate_master(args, session, master_service_names)

        generate_boto3_stubs(args, session, master_service_names)
        generate_botocore_stubs(args)


def generate_master(
    args: Namespace,
    session: Session,
    service_names: Iterable[ServiceName],
) -> None:
    """
    Generate `mypy-boto3` package.
    """
    logger = get_logger()
    pypi_manager = PyPIManager(PYPI_NAME)
    package_version = args.build_version or boto3_version
    if args.skip_published and pypi_manager.has_version(package_version):
        logger.info(f"Skipping {PYPI_NAME} {package_version}, already on PyPI")
        return

    if pypi_manager.has_version(package_version):
        package_version = pypi_manager.get_next_version(package_version)

    logger.info(f"Generating {PYPI_NAME} {package_version}")
    process_master(
        session,
        args.output_path,
        service_names=service_names,
        generate_setup=not args.installed,
        version=package_version,
    )


def generate_boto3_stubs(
    args: Namespace,
    session: Session,
    service_names: Iterable[ServiceName],
) -> None:
    """
    Generate `boto3-stubs` package.
    """
    logger = get_logger()
    pypi_manager = PyPIManager(BOTO3_STUBS_NAME)
    package_version = args.build_version or boto3_version
    if args.skip_published and pypi_manager.has_version(package_version):
        logger.info(f"Skipping {BOTO3_STUBS_NAME} {package_version}, already on PyPI")
        return

    if pypi_manager.has_version(package_version):
        package_version = pypi_manager.get_next_version(package_version)

    logger.info(f"Generating {BOTO3_STUBS_NAME} {package_version}")
    process_boto3_stubs(
        session,
        args.output_path,
        service_names,
        generate_setup=not args.installed,
        version=package_version,
    )


def generate_botocore_stubs(args: Namespace) -> None:
    """
    Generate `botocore-stubs` package.
    """
    logger = get_logger()
    pypi_manager = PyPIManager(BOTOCORE_STUBS_NAME)
    package_version = botocore_version
    if args.build_version and Version(args.build_version).is_postrelease:
        post = Version(args.build_version).post or 0
        package_version = Version(botocore_version).bump_postrelease(post).dumps()

    if args.skip_published and pypi_manager.has_version(package_version):
        logger.info(f"Skipping {BOTOCORE_STUBS_NAME} {package_version}, already on PyPI")
        return

    if pypi_manager.has_version(package_version):
        package_version = pypi_manager.get_next_version(package_version)

    JinjaManager.update_globals(
        botocore_build_version=package_version,
    )

    logger.info(f"Generating {BOTOCORE_STUBS_NAME} {package_version}")
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
