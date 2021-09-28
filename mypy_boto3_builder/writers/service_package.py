"""
Service package writer.
"""
from pathlib import Path

from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.structures.service_package import ServicePackage
from mypy_boto3_builder.utils.markdown import fix_pypi_headers
from mypy_boto3_builder.utils.nice_path import NicePath
from mypy_boto3_builder.writers.utils import (
    blackify,
    format_md,
    insert_md_toc,
    render_jinja2_template,
    sort_imports,
)


def write_service_package(package: ServicePackage, output_path: Path, generate_setup: bool) -> None:
    """
    Create stubs files for service.

    Arguments:
        package -- Service package.
        output_path -- Path to output folder.
        generate_setup -- Generate ready-to-install or to-use package.
    """
    logger = get_logger()
    setup_path = output_path / f"{package.service_name.module_name}_package"
    if generate_setup:
        package_path = setup_path / package.name
    else:
        package_path = output_path / package.name

    package_path.mkdir(exist_ok=True, parents=True)

    templates_path = Path("service")
    module_templates_path = templates_path / "service"
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
            (package_path / "version.py", module_templates_path / "version.py.jinja2"),
            (package_path / "__init__.pyi", module_templates_path / "__init__.pyi.jinja2"),
            (package_path / "__init__.py", module_templates_path / "__init__.pyi.jinja2"),
            (package_path / "__main__.py", module_templates_path / "__main__.py.jinja2"),
            (package_path / "py.typed", module_templates_path / "py.typed.jinja2"),
            (
                package_path / ServiceModuleName.client.stub_file_name,
                module_templates_path / ServiceModuleName.client.template_name,
            ),
            (
                package_path / ServiceModuleName.client.file_name,
                module_templates_path / ServiceModuleName.client.template_name,
            ),
        ]
    )
    if package.service_resource:
        file_paths.extend(
            (
                (
                    package_path / ServiceModuleName.service_resource.stub_file_name,
                    module_templates_path / ServiceModuleName.service_resource.template_name,
                ),
                (
                    package_path / ServiceModuleName.service_resource.file_name,
                    module_templates_path / ServiceModuleName.service_resource.template_name,
                ),
            )
        )
    if package.paginators:
        file_paths.extend(
            (
                (
                    package_path / ServiceModuleName.paginator.stub_file_name,
                    module_templates_path / ServiceModuleName.paginator.template_name,
                ),
                (
                    package_path / ServiceModuleName.paginator.file_name,
                    module_templates_path / ServiceModuleName.paginator.template_name,
                ),
            )
        )
    if package.waiters:
        file_paths.extend(
            (
                (
                    package_path / ServiceModuleName.waiter.stub_file_name,
                    module_templates_path / ServiceModuleName.waiter.template_name,
                ),
                (
                    package_path / ServiceModuleName.waiter.file_name,
                    module_templates_path / ServiceModuleName.waiter.template_name,
                ),
            )
        )
    if package.literals:
        file_paths.extend(
            (
                (
                    package_path / ServiceModuleName.literals.stub_file_name,
                    module_templates_path / ServiceModuleName.literals.template_name,
                ),
                (
                    package_path / ServiceModuleName.literals.file_name,
                    module_templates_path / ServiceModuleName.literals.template_name,
                ),
            )
        )
    if package.typed_dicts:
        file_paths.extend(
            (
                (
                    package_path / ServiceModuleName.type_defs.stub_file_name,
                    module_templates_path / ServiceModuleName.type_defs.template_name,
                ),
                (
                    package_path / ServiceModuleName.type_defs.file_name,
                    module_templates_path / ServiceModuleName.type_defs.template_name,
                ),
            )
        )

    for file_path, template_path in file_paths:
        content = render_jinja2_template(
            template_path,
            package=package,
            service_name=package.service_name,
        )
        if file_path.suffix in [".py", ".pyi"]:
            content = sort_imports(content, package.service_name.module_name, extension="pyi")
            content = blackify(content, file_path)
        if file_path.suffix == ".md":
            content = insert_md_toc(content)
            content = fix_pypi_headers(content)
            content = format_md(content)

        if not file_path.exists() or file_path.read_text() != content:
            file_path.write_text(content)
            logger.debug(f"Updated {NicePath(file_path)}")

    valid_paths = dict(file_paths).keys()
    for unknown_path in NicePath(setup_path if generate_setup else package_path).walk(valid_paths):
        unknown_path.unlink()
        logger.debug(f"Deleted {NicePath(unknown_path)}")


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
