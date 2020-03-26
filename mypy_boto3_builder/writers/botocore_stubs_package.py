"""
botocore-stubs package writer.
"""
from pathlib import Path
import shutil
from typing import List
import filecmp

from mypy_boto3_builder.writers.utils import render_jinja2_template, blackify
from mypy_boto3_builder.constants import BOTOCORE_STUBS_STATIC_PATH, BOTOCORE_STUBS_NAME


def write_botocore_stubs_package(output_path: Path) -> List[Path]:
    """
    Generate output files for `botocore-stubs` package.

    Arguments:
        output_path -- Path to output directory.

    Returns:
        A list of changed paths.
    """
    modified_paths: List[Path] = []
    package_path = output_path / BOTOCORE_STUBS_NAME

    output_path.mkdir(exist_ok=True)
    package_path.mkdir(exist_ok=True)

    templates_path = Path(BOTOCORE_STUBS_NAME)
    module_templates_path = templates_path / BOTOCORE_STUBS_NAME
    file_paths = [
        (output_path / "setup.py", templates_path / "setup.py.jinja2"),
        (output_path / "README.md", templates_path / "README.md.jinja2"),
        (package_path / "py.typed", module_templates_path / "py.typed.jinja2"),
        (package_path / "__init__.py", module_templates_path / "__init__.py.jinja2"),
        (package_path / "version.py", module_templates_path / "version.py.jinja2"),
    ]

    for file_path, template_path in file_paths:
        content = render_jinja2_template(template_path)
        content = blackify(content, file_path)
        if not file_path.exists() or file_path.read_text() != content:
            modified_paths.append(file_path)
            file_path.write_text(content)

    for static_path in BOTOCORE_STUBS_STATIC_PATH.glob("**/*.pyi"):
        relative_output_path = static_path.relative_to(BOTOCORE_STUBS_STATIC_PATH)
        file_path = package_path / relative_output_path
        file_path.parent.mkdir(exist_ok=True, parents=True)
        if file_path.exists() and filecmp.cmp(
            static_path.as_posix(), file_path.as_posix()
        ):
            continue

        shutil.copy(static_path, file_path)
        modified_paths.append(file_path)

    return modified_paths
