"""
Service package writer.
"""
from pathlib import Path

from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.structures.service_package import ServicePackage
from mypy_boto3_builder.utils.nice_path import NicePath
from mypy_boto3_builder.writers.utils import format_md, insert_md_toc, render_jinja2_template


def write_service_docs(package: ServicePackage, output_path: Path) -> None:
    """
    Create service docs files.

    Arguments:
        package -- Service package.
        output_path -- Path to output folder.
    """
    logger = get_logger()
    docs_path = output_path / f"{package.service_name.module_name}"
    docs_path.mkdir(exist_ok=True)
    templates_path = Path("service_docs")
    file_paths = [
        (docs_path / "README.md", templates_path / "README.md.jinja2"),
        (docs_path / "client.md", templates_path / "client.md.jinja2"),
    ]

    if package.literals:
        file_paths.append((docs_path / "literals.md", templates_path / "literals.md.jinja2"))

    if package.typed_dicts:
        file_paths.append((docs_path / "type_defs.md", templates_path / "type_defs.md.jinja2"))

    if package.waiters:
        file_paths.append((docs_path / "waiters.md", templates_path / "waiters.md.jinja2"))

    if package.paginators:
        file_paths.append((docs_path / "paginators.md", templates_path / "paginators.md.jinja2"))

    if package.service_resource:
        file_paths.append(
            (docs_path / "service_resource.md", templates_path / "service_resource.md.jinja2")
        )

    for file_path, template_path in file_paths:
        content = render_jinja2_template(
            template_path,
            package=package,
            service_name=package.service_name,
        )
        content = insert_md_toc(content)
        content = format_md(content)
        if not file_path.exists() or file_path.read_text() != content:
            file_path.write_text(content)
            logger.debug(f"Updated {NicePath(file_path)}")

    valid_paths = dict(file_paths).keys()
    for unknown_path in NicePath(docs_path).walk(valid_paths):
        unknown_path.unlink()
        logger.debug(f"Deleted {NicePath(unknown_path)}")
