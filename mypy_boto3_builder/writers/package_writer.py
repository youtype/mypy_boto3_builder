"""
Writer for package static and template files.
"""
from pathlib import Path
from typing import Sequence

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


class PackageWriter:
    """
    Writer for package static and template files.

    Arguments:
        output_path -- Output path
        generate_setup -- Whether to generate setup files
    """

    def __init__(self, output_path: Path, generate_setup: bool = True) -> None:
        self.output_path = output_path
        self.generate_setup = generate_setup
        self.logger = get_logger()

    def _get_package_path(self, package: Package) -> Path:
        if self.generate_setup:
            return self.output_path / package.directory_name / package.name

        return self.output_path / package.library_name

    def _get_setup_path(self, package: Package) -> Path:
        return self.output_path / package.directory_name

    def _write_static_paths(self, static_files_path: Path | None, package_path: Path) -> list[Path]:
        if not static_files_path:
            return []
        result: list[Path] = []
        for static_path in static_files_path.glob("**/*.pyi"):
            relative_output_path = static_path.relative_to(static_files_path)
            file_path = package_path / relative_output_path
            result.append(file_path)
            file_path.parent.mkdir(exist_ok=True)
            content = static_path.read_text()
            if not file_path.exists() or file_path.read_text() != content:
                file_path.write_text(content)
                self.logger.debug(f"Updated {NicePath(file_path)}")
        return result

    def _get_setup_template_paths(
        self, package: Package, templates_path: Path | None
    ) -> list[tuple[Path, Path]]:
        if not templates_path or not self.generate_setup:
            return []

        result: list[tuple[Path, Path]] = []
        setup_path = self._get_setup_path(package)
        for template_path in NicePath(templates_path).walk(glob_pattern="*.jinja2"):
            relative_template_path = template_path.relative_to(templates_path)
            file_name = relative_template_path.name.rsplit(".", 1)[0]
            output_file_path = setup_path / file_name
            result.append((output_file_path, template_path.relative_to(templates_path.parent)))
        return result

    def _get_package_template_paths(
        self, package: Package, templates_path: Path | None
    ) -> list[tuple[Path, Path]]:
        if not templates_path or not self.generate_setup:
            return []

        result: list[tuple[Path, Path]] = []
        package_path = self._get_package_path(package)
        package_template_path = templates_path / package.name
        for template_path in NicePath(package_template_path).walk(glob_pattern="**/*.jinja2"):
            relative_template_path = template_path.relative_to(templates_path)
            file_name = relative_template_path.name.rsplit(".", 1)[0]
            output_file_path = (
                package_path / template_path.relative_to(package_template_path).parent / file_name
            )
            result.append((output_file_path, template_path.relative_to(templates_path.parent)))
        return result

    def _render_templates(self, package: Package, file_paths: list[tuple[Path, Path]]) -> None:
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
                self.logger.debug(f"Rendered {NicePath(file_path)}")

    def _cleanup(self, valid_paths: Sequence[Path], output_path: Path) -> None:
        for unknown_path in NicePath(output_path).walk(valid_paths):
            unknown_path.unlink()
            self.logger.debug(f"Deleted {NicePath(unknown_path)}")

    def write_package(
        self,
        package: Package,
        templates_path: Path | None = None,
        static_files_path: Path | None = None,
    ) -> None:
        """
        Generate files for a package.

        Arguments:
            package -- Package to render
            templates_path -- Path to Jinja templates for package
            static_files_path -- Path to static files for package
        """
        package_path = self._get_package_path(package)

        static_paths = self._write_static_paths(static_files_path, package_path)
        file_paths: list[tuple[Path, Path]] = [
            *self._get_setup_template_paths(package, templates_path),
            *self._get_package_template_paths(package, templates_path),
        ]
        self._render_templates(package, file_paths)

        valid_paths = (*dict(file_paths).keys(), *static_paths)
        output_path = self._get_setup_path(package) if self.generate_setup else package_path
        self._cleanup(valid_paths, output_path)

    def write_docs(self, package: Package, templates_path: Path) -> None:
        """
        Generate docs for a package.
        """
        self.output_path.mkdir(exist_ok=True, parents=True)
        file_paths = []
        for template_path in templates_path.glob("**/*.jinja2"):
            file_name = template_path.name.rsplit(".", 1)[0]
            file_paths.append(
                (self.output_path / file_name, template_path.relative_to(templates_path.parent))
            )

        for file_path, template_path in file_paths:
            content = render_jinja2_template(
                template_path,
                package=package,
            )
            content = insert_md_toc(content)
            content = format_md(content)
            if not file_path.exists() or file_path.read_text() != content:
                file_path.write_text(content)
                self.logger.debug(f"Updated {NicePath(file_path)}")
