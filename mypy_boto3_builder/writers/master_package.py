"""
Master package writer.
"""
import shutil
from pathlib import Path
from typing import List, Tuple

from mypy_boto3_builder.structures.master_package import MasterPackage
from mypy_boto3_builder.utils.markdown import fix_pypi_headers
from mypy_boto3_builder.writers.utils import (
    blackify,
    format_md,
    insert_md_toc,
    render_jinja2_template,
    sort_imports,
)


def write_master_package(
    package: MasterPackage, output_path: Path, generate_setup: bool
) -> List[Path]:
    setup_path = output_path / "master_package"
    if not generate_setup:
        setup_path = output_path

    modified_paths: List[Path] = []
    package_path = setup_path / package.name

    if setup_path.exists():
        shutil.rmtree(setup_path)

    setup_path.mkdir(exist_ok=True)
    package_path.mkdir(exist_ok=True)

    templates_path = Path("master")
    module_templates_path = templates_path / "master"
    file_paths: List[Tuple[Path, Path]] = []
    if generate_setup:
        file_paths.extend(
            [
                (setup_path / "setup.py", templates_path / "setup.py.jinja2"),
                (setup_path / "README.md", templates_path / "README.md.jinja2"),
            ]
        )

    file_paths.extend(
        [
            (package_path / "__init__.py", module_templates_path / "__init__.py.jinja2"),
            (package_path / "__main__.py", module_templates_path / "__main__.py.jinja2"),
            (package_path / "py.typed", module_templates_path / "py.typed.jinja2"),
            (package_path / "version.py", module_templates_path / "version.py.jinja2"),
            (package_path / "main.py", module_templates_path / "main.py.jinja2"),
            (package_path / "boto3_init.py", module_templates_path / "boto3_init.py.jinja2"),
            (package_path / "boto3_session.py", module_templates_path / "boto3_session.py.jinja2"),
            (
                package_path / "boto3_init_gen.py",
                module_templates_path / "boto3_init_stub.py.jinja2",
            ),
            (
                package_path / "boto3_session_gen.py",
                module_templates_path / "boto3_session_stub.py.jinja2",
            ),
            (
                package_path / "boto3_init_stub.py",
                module_templates_path / "boto3_init_stub.py.jinja2",
            ),
            (
                package_path / "boto3_session_stub.py",
                module_templates_path / "boto3_session_stub.py.jinja2",
            ),
            (package_path / "submodules.py", module_templates_path / "submodules.py.jinja2"),
        ]
    )

    for file_path, template_path in file_paths:
        content = render_jinja2_template(template_path, package=package)
        if file_path.suffix in [".py", ".pyi"]:
            content = sort_imports(content, "mypy_boto3", extension=file_path.suffix[1:])
            content = blackify(content, file_path)
        if file_path.suffix == ".md":
            content = insert_md_toc(content)
            content = fix_pypi_headers(content)
            content = format_md(content)

        if not file_path.exists() or file_path.read_text() != content:
            modified_paths.append(file_path)
            file_path.write_text(content)

    return modified_paths
