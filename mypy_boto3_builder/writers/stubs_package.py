"""
Stubs package writer.
"""
from pathlib import Path

from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.structures.package import Package
from mypy_boto3_builder.utils.markdown import fix_pypi_headers
from mypy_boto3_builder.utils.nice_path import NicePath
from mypy_boto3_builder.writers.utils import (
    blackify,
    format_md,
    insert_md_toc,
    render_jinja2_template,
    sort_imports,
)


def write_stubs_package(
    package: Package,
    output_path: Path,
    generate_setup: bool,
    templates_path: Path | None = None,
    static_files_path: Path | None = None,
) -> None:
    """
    Generate files for a package.

    Arguments:
        package -- Package to render
        output_path -- Output path
        generate_setup -- Whether to generate setup files
        templates_path -- Path to Jinja templates for package
        static_path -- Path to static files for package.
    """
    logger = get_logger()
    setup_path = NicePath(output_path) / package.directory_name

    if generate_setup:
        package_path = setup_path / package.name
    else:
        package_path = output_path / package.non_stubs_name

    file_paths: list[tuple[Path, Path]] = []

    static_paths: list[Path] = []
    if static_files_path:
        for static_path in static_files_path.glob("**/*.pyi"):
            relative_output_path = static_path.relative_to(static_files_path)
            file_path = package_path / relative_output_path
            static_paths.append(file_path)
            file_path.parent.mkdir(exist_ok=True)
            content = static_path.read_text()
            if not file_path.exists() or file_path.read_text() != content:
                file_path.write_text(content)
                logger.debug(f"Updated {NicePath(file_path)}")

    if templates_path:
        module_templates_path = templates_path / package.name
        for template_path in NicePath(templates_path).walk(glob_pattern="**/*.jinja2"):
            relative_template_path = Path(package.name) / template_path.relative_to(templates_path)
            file_name = relative_template_path.name.rsplit(".", 1)[0]
            output_file_path = setup_path / relative_template_path.parent.parent / file_name

            is_setup_file = len(relative_template_path.parts) == 2
            if is_setup_file and not generate_setup:
                continue

            dir_name = relative_template_path.parts[0]
            if dir_name == package.name and not generate_setup:
                output_file_path = (
                    setup_path
                    / package.non_stubs_name
                    / template_path.relative_to(module_templates_path).parent
                    / file_name
                )

            file_paths.append((output_file_path, relative_template_path))

    for file_path, template_path in file_paths:
        content = render_jinja2_template(template_path, package=package)
        if file_path.suffix in [".py", ".pyi"]:
            content = sort_imports(
                content,
                package.name,
                extension="pyi",
                third_party=[
                    "boto3",
                    "botocore",
                    "aiobotocore",
                    *[i.module_name for i in package.service_names],
                ],
            )
            content = blackify(content, file_path)
        if file_path.suffix == ".md":
            content = insert_md_toc(content)
            content = fix_pypi_headers(content)
            content = format_md(content)
        if not file_path.parent.exists():
            file_path.parent.mkdir(parents=True, exist_ok=True)
        if not file_path.exists() or file_path.read_text() != content:
            file_path.write_text(content)
            logger.debug(f"Updated {NicePath(file_path)}")

    valid_paths = (*dict(file_paths).keys(), *static_paths)
    for unknown_path in NicePath(setup_path if generate_setup else package_path).walk(valid_paths):
        unknown_path.unlink()
        logger.debug(f"Deleted {NicePath(unknown_path)}")
