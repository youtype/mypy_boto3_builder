"""
Generate docs for a package.
"""
from pathlib import Path

from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.structures.package import Package
from mypy_boto3_builder.utils.nice_path import NicePath
from mypy_boto3_builder.writers.utils import format_md, insert_md_toc, render_jinja2_template


def write_docs(package: Package, output_path: Path, templates_path: Path) -> None:
    """
    Generate docs for a package.
    """
    logger = get_logger()
    docs_path = output_path
    docs_path.mkdir(exist_ok=True, parents=True)
    file_paths = []
    for template_path in templates_path.glob("**/*.jinja2"):
        file_name = template_path.name.rsplit(".", 1)[0]
        file_paths.append((docs_path / file_name, template_path))

    for file_path, template_path in file_paths:
        content = render_jinja2_template(
            template_path,
            package=package,
        )
        content = insert_md_toc(content)
        content = format_md(content)
        if not file_path.exists() or file_path.read_text() != content:
            file_path.write_text(content)
            logger.debug(f"Updated {NicePath(file_path)}")
