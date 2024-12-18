"""
Main entrypoint for builder.

Copyright 2024 Vlad Emelianov
"""

import datetime
import sys
import warnings
from collections.abc import Iterable, Sequence

from mypy_boto3_builder.chat.chat_buddy import ChatBuddy
from mypy_boto3_builder.cli_parser import CLINamespace, parse_args
from mypy_boto3_builder.constants import (
    BUILDER_REPO_URL,
    OUTPUT_PATH_SENTINEL,
    PACKAGE_NAME,
    PROG_NAME,
)
from mypy_boto3_builder.enums.product import Product, ProductLibrary
from mypy_boto3_builder.generators.aioboto3_generator import AioBoto3Generator
from mypy_boto3_builder.generators.aiobotocore_generator import AioBotocoreGenerator
from mypy_boto3_builder.generators.base_generator import BaseGenerator
from mypy_boto3_builder.generators.boto3_generator import Boto3Generator
from mypy_boto3_builder.generators.types_boto3_generator import TypesBoto3Generator
from mypy_boto3_builder.jinja_manager import JinjaManager
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.type_defs import GeneratorKwargs
from mypy_boto3_builder.utils.boto3_utils import get_available_service_names
from mypy_boto3_builder.utils.botocore_changelog import BotocoreChangelog
from mypy_boto3_builder.utils.strings import get_anchor_link, get_copyright, get_md_doc_link
from mypy_boto3_builder.utils.type_checks import (
    is_literal,
    is_type_def,
    is_type_parent,
    is_typed_dict,
    is_union,
)
from mypy_boto3_builder.utils.version import get_builder_version
from mypy_boto3_builder.utils.version_getters import get_botocore_version


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
        updated_service_names = BotocoreChangelog().fetch_updated(botocore_version)
        selected_service_names.extend(
            service_name_str
            for service_name_str in updated_service_names
            if service_name_str in available_map
        )
    if ServiceName.ESSENTIAL in selected_service_names:
        selected_service_names.remove(ServiceName.ESSENTIAL)
        selected_service_names.extend(
            service_name_str
            for service_name_str in available_map
            if service_name_str in ServiceName.ESSENTIAL_NAMES
        )

    for service_name_str in selected_service_names:
        if service_name_str not in available_map:
            logger.info(f"Service {service_name_str} is not provided by botocore, skipping")
            continue
        result.append(available_map[service_name_str])

    return result


def get_generator(product: Product, kwargs: GeneratorKwargs) -> BaseGenerator:
    """
    Get Generator class for a product.
    """
    library = product.get_library()
    match library:
        case ProductLibrary.boto3:
            return TypesBoto3Generator(**kwargs)
        case ProductLibrary.boto3_legacy:
            return Boto3Generator(**kwargs)
        case ProductLibrary.aiobotocore:
            return AioBotocoreGenerator(**kwargs)
        case ProductLibrary.aioboto3:
            return AioBoto3Generator(**kwargs)


def generate_product(
    product: Product,
    args: CLINamespace,
    service_names: Sequence[ServiceName],
    main_service_names: Sequence[ServiceName],
) -> None:
    """
    Generate a selected product.

    Arguments:
        product -- Product to generate
        args -- CLI namespace
        service_names -- Selected service names
        main_service_names -- Service names included in main
    """
    generator = get_generator(
        product,
        {
            "product": product,
            "service_names": service_names,
            "main_service_names": main_service_names,
            "config": args,
            "version": args.build_version,
            "cleanup": True,
        },
    )
    generator.generate_product(product.get_type())
    generator.cleanup_temporary_files()


def initialize_jinja_manager() -> None:
    """
    Initialize Jinja manager with globals.
    """
    jinja_manager = JinjaManager()
    jinja_manager.update_globals(
        get_md_doc_link=get_md_doc_link,
        builder_version=get_builder_version(),
        current_year=str(datetime.datetime.now(datetime.timezone.utc).year),
        get_anchor_link=get_anchor_link,
        len=len,
        sorted=sorted,
        repr=repr,
        builder_prog_name=PROG_NAME,
        builder_package_name=PACKAGE_NAME,
        builder_repo_url=BUILDER_REPO_URL,
        copyright=get_copyright(),
        is_typed_dict=is_typed_dict,
        is_union=is_union,
        is_literal=is_literal,
        is_type_def=is_type_def,
        is_type_parent=is_type_parent,
    )


def run(args: CLINamespace) -> None:
    """
    Run builder.
    """
    # FIXME: suppress botocore endpoint warning
    warnings.filterwarnings("ignore", category=FutureWarning, module="botocore.client")

    if args.output_path == OUTPUT_PATH_SENTINEL:
        ChatBuddy(_run_builder).run()
        return

    _run_builder(args)


def _run_builder(args: CLINamespace) -> None:
    logger = get_logger(level=args.log_level)
    available_service_names = get_available_service_names()
    initialize_jinja_manager()
    args.output_path.mkdir(exist_ok=True, parents=True)

    logger.debug(f"{len(available_service_names)} supported botocore services discovered")
    if args.list_services:
        for service_name in available_service_names:
            sys.stdout.write(
                f"- {service_name.name} : {service_name.class_name}"
                f" {service_name.boto3_doc_link}\n",
            )
        return

    service_names = get_selected_service_names(args.service_names, available_service_names)
    main_service_names = service_names if args.partial_overload else available_service_names

    for product in args.products:
        logger.info(f"Generating {product} product")
        generate_product(product, args, service_names, main_service_names)

    logger.debug("Done!")


def main() -> None:
    """
    CLI entrypoint.
    """
    args = parse_args(sys.argv[1:])
    try:
        run(args)
    except KeyboardInterrupt:
        logger = get_logger()
        logger.warning("Interrupted by user")
        sys.exit(1)


if __name__ == "__main__":
    main()
