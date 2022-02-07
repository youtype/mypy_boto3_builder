"""
Processors for parsing and writing `aiobotocore` modules.
"""
from collections.abc import Iterable
from pathlib import Path

from boto3.session import Session

from mypy_boto3_builder.constants import (
    AIOBOTOCORE_STUBS_LITE_PYPI_NAME,
    AIOBOTOCORE_STUBS_STATIC_PATH,
    TEMPLATES_PATH,
)
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.parsers.aiobotocore_stubs_package import parse_aiobotocore_stubs_package
from mypy_boto3_builder.parsers.service_package import parse_service_package
from mypy_boto3_builder.parsers.service_package_postprocessor import ServicePackagePostprocessor
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.aiobotocore_stubs_package import AioBotocoreStubsPackage
from mypy_boto3_builder.structures.service_package import ServicePackage
from mypy_boto3_builder.utils.nice_path import NicePath
from mypy_boto3_builder.utils.strings import get_aiobotocore_version
from mypy_boto3_builder.writers.package_writer import PackageWriter


def process_aiobotocore_stubs(
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
    generate_setup: bool,
    version: str,
) -> AioBotocoreStubsPackage:
    """
    Parse and write stubs package `aiobotocore-stubs`.

    Arguments:
        session -- boto3 session
        output_path -- Package output path
        service_names -- List of known service names
        generate_setup -- Generate ready-to-install or to-use package
        version -- Package version

    Return:
        Parsed AioBotocoreStubsPackage.
    """
    logger = get_logger()
    logger.debug("Parsing aiobotocore stubs")
    aiobotocore_stubs_package = parse_aiobotocore_stubs_package(
        session=session, service_names=service_names
    )
    aiobotocore_stubs_package.version = version
    aiobotocore_stubs_package.library_name = "aiobotocore"
    aiobotocore_stubs_package.library_version = get_aiobotocore_version()
    logger.debug(f"Writing aiobotocore stubs to {NicePath(output_path)}")

    package_writer = PackageWriter(output_path=output_path, generate_setup=generate_setup)
    package_writer.write_package(
        aiobotocore_stubs_package,
        templates_path=TEMPLATES_PATH / "aiobotocore-stubs",
        static_files_path=AIOBOTOCORE_STUBS_STATIC_PATH,
    )
    return aiobotocore_stubs_package


def process_aiobotocore_stubs_lite(
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
    generate_setup: bool,
    version: str,
) -> AioBotocoreStubsPackage:
    """
    Parse and write stubs package `aiobotocore-stubs-lite`.

    Arguments:
        session -- boto3 session
        output_path -- Package output path
        service_names -- List of known service names
        generate_setup -- Generate ready-to-install or to-use package
        version -- Package version

    Return:
        Parsed AioBotocoreStubsPackage.
    """
    logger = get_logger()
    logger.debug(f"Parsing {AIOBOTOCORE_STUBS_LITE_PYPI_NAME}")
    aiobotocore_stubs_package = parse_aiobotocore_stubs_package(
        session=session, service_names=service_names
    )
    aiobotocore_stubs_package.pypi_name = AIOBOTOCORE_STUBS_LITE_PYPI_NAME
    aiobotocore_stubs_package.version = version
    aiobotocore_stubs_package.library_name = "aiobotocore"
    aiobotocore_stubs_package.library_version = get_aiobotocore_version()
    logger.debug(f"Writing {AIOBOTOCORE_STUBS_LITE_PYPI_NAME} to {NicePath(output_path)}")

    package_writer = PackageWriter(output_path=output_path, generate_setup=generate_setup)
    package_writer.write_package(
        aiobotocore_stubs_package,
        templates_path=TEMPLATES_PATH / "aiobotocore-stubs",
        static_files_path=AIOBOTOCORE_STUBS_STATIC_PATH,
        exclude_template_names=["session.pyi.jinja2"],
    )
    return aiobotocore_stubs_package


def process_aiobotocore_service(
    session: Session,
    service_name: ServiceName,
    output_path: Path,
    generate_setup: bool,
    service_names: Iterable[ServiceName],
    version: str,
) -> ServicePackage:
    """
    Parse and write service package `types_aiobotocore_*`.

    Arguments:
        session -- boto3 session
        service_name -- Target service name
        output_path -- Package output path
        generate_setup -- Generate ready-to-install or to-use package
        service_names -- List of known service names
        version -- Package version

    Return:
        Parsed ServicePackage.
    """
    logger = get_logger()
    logger.debug(f"Parsing {service_name.boto3_name}")
    service_package = parse_service_package(session, service_name)
    service_package.name = service_name.aiobotocore_module_name
    service_package.pypi_name = service_name.aiobotocore_pypi_name
    service_package.version = version
    service_package.library_name = "aiobotocore"
    service_package.library_version = get_aiobotocore_version()
    service_package.extend_literals(service_names)

    postprocessor = ServicePackagePostprocessor(service_package)
    postprocessor.generate_docstrings()
    postprocessor.make_async()
    postprocessor.add_contextmanager_methods()

    for typed_dict in service_package.typed_dicts:
        typed_dict.replace_self_references()
    logger.debug(f"Writing {service_name.boto3_name} to {NicePath(output_path)}")

    package_writer = PackageWriter(output_path=output_path, generate_setup=generate_setup)
    package_writer.write_service_package(
        service_package,
        templates_path=TEMPLATES_PATH / "aiobotocore_service",
    )
    return service_package


def process_aiobotocore_stubs_docs(
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
) -> AioBotocoreStubsPackage:
    """
    Parse and write master package docs.

    Arguments:
        session -- boto3 session
        output_path -- Package output path
        service_names -- List of known service names

    Return:
        Parsed AioBotocoreStubsPackage.
    """
    logger = get_logger()
    logger.debug("Parsing aiobotocore stubs")
    aiobotocore_stubs_package = parse_aiobotocore_stubs_package(
        session=session, service_names=service_names
    )
    aiobotocore_stubs_package.library_name = "aiobotocore"
    aiobotocore_stubs_package.library_version = get_aiobotocore_version()

    logger.debug(f"Writing aiobotocore stubs to {NicePath(output_path)}")

    package_writer = PackageWriter(output_path=output_path)
    package_writer.write_docs(
        aiobotocore_stubs_package,
        templates_path=TEMPLATES_PATH / "aiobotocore_stubs_docs",
    )

    return aiobotocore_stubs_package


def process_aiobotocore_service_docs(
    session: Session,
    service_name: ServiceName,
    output_path: Path,
    service_names: Iterable[ServiceName],
) -> ServicePackage:
    """
    Parse and write service package docs.

    Arguments:
        session -- boto3 session
        service_name -- Target service name
        output_path -- Package output path
        service_names -- List of known service names

    Return:
        Parsed ServicePackage.
    """
    logger = get_logger()
    logger.debug(f"Parsing {service_name.boto3_name}")
    service_package = parse_service_package(session, service_name)
    service_package.name = service_name.aiobotocore_module_name
    service_package.pypi_name = service_name.aiobotocore_pypi_name
    service_package.library_name = "aiobotocore"
    service_package.library_version = get_aiobotocore_version()
    service_package.extend_literals(service_names)

    postprocessor = ServicePackagePostprocessor(service_package)
    postprocessor.generate_docstrings()
    postprocessor.make_async()
    postprocessor.add_contextmanager_methods()

    for typed_dict in service_package.typed_dicts:
        typed_dict.replace_self_references()

    logger.debug(f"Writing {service_name.boto3_name} to {NicePath(output_path)}")

    package_writer = PackageWriter(output_path=output_path)
    package_writer.write_service_docs(
        service_package,
        templates_path=TEMPLATES_PATH / "aiobotocore_service_docs",
    )
    return service_package
