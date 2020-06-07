"""
Main entrypoint for builder.
"""
from typing import List

from boto3 import __version__ as boto3_version
from boto3.session import Session

from mypy_boto3_builder.cli_parser import get_cli_parser
from mypy_boto3_builder.constants import BOTO3_STUBS_NAME, DUMMY_REGION, MODULE_NAME, PYPI_NAME
from mypy_boto3_builder.jinja_manager import JinjaManager
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.version import __version__ as version
from mypy_boto3_builder.writers.processors import (
    process_boto3_stubs,
    process_master,
    process_service,
)


def main() -> None:
    """
    Main entrypoint for builder.
    """
    parser = get_cli_parser()
    args = parser.parse_args()
    logger = get_logger(verbose=args.debug, panic=args.panic)
    session = Session(region_name=DUMMY_REGION)
    args.output_path.mkdir(exist_ok=True)
    service_names: List[ServiceName] = []
    master_service_names = []
    available_services = session.get_available_services()

    for available_service in available_services:
        try:
            service_name = ServiceNameCatalog.find(available_service)
            master_service_names.append(service_name)
        except ValueError:
            logger.info(f"Service {available_service} is not supported, skipping.")

    for service_name in args.service_names:
        if service_name.name not in available_services:
            logger.warning(f"Service {service_name.name} is not available, skipping.")
            continue

        service_name.boto3_version = boto3_version
        service_names.append(service_name)

    build_version = args.build_version or boto3_version
    JinjaManager.update_globals(
        master_pypi_name=PYPI_NAME,
        master_module_name=MODULE_NAME,
        boto3_stubs_name=BOTO3_STUBS_NAME,
        boto3_version=boto3_version,
        build_version=build_version,
        builder_version=version,
    )

    logger.info(f"Bulding version {build_version}")

    if not args.skip_services:
        for index, service_name in enumerate(service_names):
            logger.info(
                f"[{index + 1}/{len(service_names)}] Generating {service_name.module_name} module"
            )
            output_path = args.output_path / f"{service_name.module_name}_package"
            process_service(session=session, output_path=output_path, service_name=service_name)

    if not args.skip_master:
        logger.info(f"Generating {MODULE_NAME} module")
        output_path = args.output_path / "master_package"
        process_master(session, output_path, master_service_names)

        logger.info(f"Generating {BOTO3_STUBS_NAME} module")
        output_path = args.output_path / "boto3_stubs_package"
        process_boto3_stubs(output_path, master_service_names)

    logger.info("Completed")


if __name__ == "__main__":
    main()
