"""
botocore-stubs package writer.
"""
from pathlib import Path

from mypy_boto3_builder.constants import BOTOCORE_STUBS_NAME, BOTOCORE_STUBS_STATIC_PATH
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.utils.markdown import fix_pypi_headers
from mypy_boto3_builder.utils.nice_path import NicePath
from mypy_boto3_builder.writers.utils import (
    blackify,
    format_md,
    insert_md_toc,
    render_jinja2_template,
    sort_imports,
)


def write_botocore_stubs_package(output_path: Path, generate_setup: bool) -> None:
    """
    Generate botocore-stubs stub files.

    Arguments:
        output_path -- Path to output folder.
        generate_setup -- Generate ready-to-install or to-use package.
    """
    logger = get_logger()
    setup_path = output_path / "botocore_stubs_package"
    if generate_setup:
        package_path = setup_path / BOTOCORE_STUBS_NAME
    else:
        package_path = output_path / "botocore"

    package_path.mkdir(exist_ok=True, parents=True)

    templates_path = Path("botocore-stubs")
    module_templates_path = templates_path / "botocore-stubs"
    file_paths: list[tuple[Path, Path]] = []
    if generate_setup:
        file_paths.extend(
            [
                (setup_path / "setup.py", templates_path / "setup.py.jinja2"),
                (setup_path / "README.md", templates_path / "README.md.jinja2"),
            ]
        )

    file_paths.extend(
        [
            (package_path / "py.typed", module_templates_path / "py.typed.jinja2"),
            (package_path / "__main__.py", module_templates_path / "__main__.py.jinja2"),
            (package_path / "version.py", module_templates_path / "version.py.jinja2"),
        ]
    )

    for file_path, template_path in file_paths:
        content = render_jinja2_template(template_path)
        if file_path.suffix in [".py", ".pyi"]:
            content = sort_imports(
                content,
                "boto3_stubs",
                extension="pyi",
            )
            content = blackify(content, file_path)
        if file_path.suffix == ".md":
            content = insert_md_toc(content)
            content = fix_pypi_headers(content)
            content = format_md(content)
        if not file_path.exists() or file_path.read_text() != content:
            file_path.write_text(content)
            logger.debug(f"Updated {NicePath(file_path)}")

    static_paths = []
    for static_path in BOTOCORE_STUBS_STATIC_PATH.glob("**/*.pyi"):
        relative_output_path = static_path.relative_to(BOTOCORE_STUBS_STATIC_PATH)
        file_path = package_path / relative_output_path
        static_paths.append(file_path)
        file_path.parent.mkdir(exist_ok=True)
        content = static_path.read_text()
        if not file_path.exists() or file_path.read_text() != content:
            file_path.write_text(content)
            logger.debug(f"Updated {NicePath(file_path)}")

    valid_paths = (*dict(file_paths).keys(), *static_paths)
    for unknown_path in NicePath(setup_path if generate_setup else package_path).walk(valid_paths):
        unknown_path.unlink()
        logger.debug(f"Deleted {NicePath(unknown_path)}")
