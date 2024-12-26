"""
Writer for package static and template files.

Copyright 2024 Vlad Emelianov
"""

import filecmp
import shutil
from collections.abc import Iterable, Sequence
from pathlib import Path
from typing import Final

from mypy_boto3_builder.constants import TEMPLATES_PATH
from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.structures.package import Package
from mypy_boto3_builder.structures.packages.service_package import ServicePackage
from mypy_boto3_builder.utils.markdown import fix_pypi_headers
from mypy_boto3_builder.utils.path import print_path, walk_path
from mypy_boto3_builder.writers.ruff_formatter import RuffFormatter
from mypy_boto3_builder.writers.utils import (
    format_md,
    insert_md_toc,
    render_jinja2_package_template,
)


class TemplateRender:
    """
    Template render target.
    """

    def __init__(
        self,
        template_path: Path,
        path: Path | None = None,
        paths: tuple[Path, ...] = (),
    ) -> None:
        self.template_path = template_path
        self.paths = (*([path] if path else []), *paths)


class PackageWriter:
    """
    Writer for package static and template files.

    Arguments:
        output_path -- Output path
        generate_package -- Whether to generate setup files
        cleanup -- Whether to remove unknown files
        is_typings -- Whether to generate typings without `-stubs` suffix
    """

    _PY_EXTENSIONS: Final = {".py", ".pyi"}
    _MD_EXTENSIONS: Final = {".md"}

    def __init__(
        self,
        output_path: Path,
        *,
        generate_package: bool,
        cleanup: bool,
        is_typings: bool = True,
    ) -> None:
        self.output_path = output_path
        self.is_package = generate_package
        self.is_typings = is_typings
        self.cleanup = cleanup
        self.logger = get_logger()

    def _get_package_path(self, package: Package) -> Path:
        if self.is_package:
            return self.output_path / package.directory_name / package.name

        if self.is_typings:
            return self.output_path / package.library_name

        return self.output_path / package.name

    def _get_service_package_path(self, package: ServicePackage) -> Path:
        if self.is_package:
            return self.output_path / package.directory_name / package.name

        return self.output_path / package.name

    def _get_setup_path(self, package: Package) -> Path:
        return self.output_path / package.directory_name

    def _write_static_paths(
        self,
        static_files_path: Path | None,
        package: Package,
        exclude_paths: Iterable[Path],
    ) -> list[Path]:
        if not static_files_path:
            return []
        package_path = self._get_package_path(package)
        result: list[Path] = []
        for static_path in static_files_path.glob("**/*.pyi"):
            relative_output_path = static_path.relative_to(static_files_path)
            file_path = package_path / relative_output_path
            if file_path in exclude_paths:
                continue
            result.append(file_path)
            file_path.parent.mkdir(exist_ok=True, parents=True)
            if not file_path.exists():
                shutil.copy(static_path, file_path)
                self.logger.debug(f"Created {print_path(file_path)}")
            elif not filecmp.cmp(static_path, file_path):
                shutil.copy(static_path, file_path)
                self.logger.debug(f"Updated {print_path(file_path)}")
        return result

    def _get_setup_template_paths(
        self,
        package: Package,
        templates_path: Path | None,
    ) -> list[TemplateRender]:
        if not templates_path or not self.is_package:
            return []

        result: list[TemplateRender] = []
        setup_path = self._get_setup_path(package)
        template_paths = (
            templates_path / "setup.py.jinja2",
            templates_path / "README.md.jinja2",
            TEMPLATES_PATH / "common" / "LICENSE.jinja2",
        )
        for template_path in template_paths:
            file_name = template_path.stem
            output_file_path = setup_path / file_name
            result.append(TemplateRender(template_path, output_file_path))
        return result

    def _get_package_template_renders(
        self,
        package: Package,
        templates_path: Path | None,
    ) -> list[TemplateRender]:
        if not templates_path or not package.has_main_package():
            return []

        result: list[TemplateRender] = []
        package_path = self._get_package_path(package)
        package_template_path = templates_path / package.name
        for template_path in walk_path(package_template_path, glob_pattern="**/*.jinja2"):
            file_name = template_path.stem
            output_file_path = (
                package_path / template_path.relative_to(package_template_path).parent / file_name
            )
            result.append(TemplateRender(template_path, output_file_path))
        return result

    def _render_template(
        self,
        template_path: Path,
        render_paths: Iterable[Path],
        package: Package,
    ) -> None:
        content = render_jinja2_package_template(template_path, package=package)
        for output_path in render_paths:
            file_suffix = output_path.suffix.lower()
            if file_suffix in self._MD_EXTENSIONS:
                content = insert_md_toc(content)
                content = fix_pypi_headers(content)
                content = format_md(content)
            self._write_template(output_path, content)

    def _render_templates(
        self,
        package: Package,
        template_renders: Iterable[TemplateRender],
    ) -> None:
        for template_render in template_renders:
            self._render_template(template_render.template_path, template_render.paths, package)

    def _write_template(self, path: Path, content: str) -> None:
        if not path.parent.exists():
            path.parent.mkdir(exist_ok=True, parents=True)

        path.write_text(content)
        self.logger.debug(f"Rendered {print_path(path)}")

    def _render_docs_templates(
        self,
        package: Package,
        template_renders: Iterable[TemplateRender],
    ) -> None:
        for template_render in template_renders:
            content = render_jinja2_package_template(template_render.template_path, package=package)
            for output_path in template_render.paths:
                self._write_template(output_path, content)

    def _cleanup(self, valid_paths: Sequence[Path], output_path: Path) -> None:
        if not self.cleanup or not output_path.exists():
            return
        for unknown_path in walk_path(output_path, valid_paths):
            unknown_path.unlink()
            self.logger.debug(f"Deleted {print_path(unknown_path)}")

    def write_package(
        self,
        package: Package,
        template_path: Path | None = None,
        static_files_path: Path | None = None,
        include_template_names: Sequence[str] = (),
        exclude_template_names: Sequence[str] = (),
    ) -> None:
        """
        Generate files for a package.

        Arguments:
            package -- Package to render
            template_path -- Path to Jinja templates for package
            static_files_path -- Path to static files for package
            include_template_names -- Render only templates with these names
            exclude_template_names -- Do not render templates with these names
        """
        self.logger.debug(f"Writing {package.data.pypi_name} to {print_path(self.output_path)}")
        template_renders: list[TemplateRender] = [
            *self._get_setup_template_paths(package, template_path),
            *self._get_package_template_renders(package, template_path),
        ]
        if include_template_names:
            template_renders = list(
                filter(lambda x: x.template_path.name in include_template_names, template_renders)
            )
        if exclude_template_names:
            template_renders = list(
                filter(
                    lambda x: x.template_path.name not in exclude_template_names, template_renders
                )
            )
        exclude_static_paths: set[Path] = set()
        for template_render in template_renders:
            exclude_static_paths.update(template_render.paths)
        static_paths = self._write_static_paths(static_files_path, package, exclude_static_paths)
        self._render_templates(package, template_renders)

        rendered_paths = [path for t in template_renders for path in t.paths]
        valid_paths = (*rendered_paths, *static_paths)

        self._format_output(package, valid_paths)

        cleanup_path = self._get_cleanup_path(package)
        if cleanup_path:
            self._cleanup(valid_paths, cleanup_path)

    def _get_cleanup_path(self, package: Package) -> Path | None:
        if self.is_package:
            return self._get_setup_path(package)

        if package.has_main_package():
            return self._get_package_path(package)

        return None

    def _format_output(self, package: Package, paths: Sequence[Path]) -> None:
        ruff_formatter = RuffFormatter(
            known_first_party=[package.name] if package.has_main_package() else [],
            known_third_party=[
                "boto3",
                "botocore",
                "aioboto3",
                "aiobotocore",
                *[package.data.get_service_package_name(i) for i in package.service_names],
            ],
        )
        existing_paths = [path for path in paths if path.exists()]
        format_python_paths = [
            path for path in existing_paths if path.suffix.lower() in self._PY_EXTENSIONS
        ]
        if format_python_paths:
            ruff_formatter.format_python(format_python_paths)

        format_md_paths = [
            path for path in existing_paths if path.suffix.lower() in self._MD_EXTENSIONS
        ]
        if format_md_paths:
            for path in format_md_paths:
                content = path.read_text()
                content = ruff_formatter.format_markdown(content)
                path.write_text(content)

    def write_docs(self, package: Package, templates_path: Path) -> None:
        """
        Generate docs for a package.
        """
        self.output_path.mkdir(exist_ok=True, parents=True)
        template_renders: list[TemplateRender] = []
        for template_path in templates_path.glob("**/*.jinja2"):
            file_name = template_path.stem
            template_renders.append(TemplateRender(template_path, self.output_path / file_name))

        self._render_docs_templates(package, template_renders)

    def _get_service_package_template_paths(
        self,
        package: ServicePackage,
        templates_path: Path,
    ) -> list[TemplateRender]:
        module_templates_path = templates_path / "service"
        package_path = self._get_service_package_path(package)
        file_paths: list[TemplateRender] = [
            TemplateRender(
                module_templates_path / "version.py.jinja2",
                package_path / "version.py",
            ),
            TemplateRender(
                module_templates_path / "__init__.pyi.jinja2",
                paths=(
                    package_path / "__init__.pyi",
                    package_path / "__init__.py",
                ),
            ),
            TemplateRender(
                module_templates_path / "__main__.py.jinja2",
                package_path / "__main__.py",
            ),
            TemplateRender(module_templates_path / "py.typed.jinja2", package_path / "py.typed"),
            TemplateRender(
                module_templates_path / ServiceModuleName.client.template_name,
                paths=(
                    package_path / ServiceModuleName.client.stub_file_name,
                    package_path / ServiceModuleName.client.file_name,
                ),
            ),
        ]
        if package.service_resource:
            file_paths.append(
                TemplateRender(
                    module_templates_path / ServiceModuleName.service_resource.template_name,
                    paths=(
                        package_path / ServiceModuleName.service_resource.stub_file_name,
                        package_path / ServiceModuleName.service_resource.file_name,
                    ),
                ),
            )
        if package.paginators:
            file_paths.append(
                TemplateRender(
                    module_templates_path / ServiceModuleName.paginator.template_name,
                    paths=(
                        package_path / ServiceModuleName.paginator.stub_file_name,
                        package_path / ServiceModuleName.paginator.file_name,
                    ),
                ),
            )
        if package.waiters:
            file_paths.append(
                TemplateRender(
                    module_templates_path / ServiceModuleName.waiter.template_name,
                    paths=(
                        package_path / ServiceModuleName.waiter.stub_file_name,
                        package_path / ServiceModuleName.waiter.file_name,
                    ),
                ),
            )
        if package.literals:
            file_paths.append(
                TemplateRender(
                    module_templates_path / ServiceModuleName.literals.template_name,
                    paths=(
                        package_path / ServiceModuleName.literals.stub_file_name,
                        package_path / ServiceModuleName.literals.file_name,
                    ),
                ),
            )
        if package.type_defs:
            file_paths.append(
                TemplateRender(
                    module_templates_path / ServiceModuleName.type_defs.template_name,
                    paths=(
                        package_path / ServiceModuleName.type_defs.stub_file_name,
                        package_path / ServiceModuleName.type_defs.file_name,
                    ),
                ),
            )
        return file_paths

    def write_service_package(self, package: ServicePackage, templates_path: Path) -> None:
        """
        Create stubs files for service.

        Arguments:
            package -- Service package.
        """
        template_renders: list[TemplateRender] = [
            *self._get_setup_template_paths(package, templates_path),
            *self._get_service_package_template_paths(package, templates_path),
        ]
        self._render_templates(package, template_renders)

        valid_paths = [path for t in template_renders for path in t.paths]

        self._format_output(package, valid_paths)

        output_path = (
            self._get_setup_path(package)
            if self.is_package
            else self._get_service_package_path(package)
        )
        self._cleanup(valid_paths, output_path)

    def write_service_docs(self, package: ServicePackage, templates_path: Path) -> None:
        """
        Create service docs files.

        Arguments:
            package -- Service package.
            output_path -- Path to output directory.
        """
        docs_path = self.output_path / package.name
        docs_path.mkdir(exist_ok=True, parents=True)
        template_renders: list[TemplateRender] = [
            TemplateRender(templates_path / "README.md.jinja2", docs_path / "README.md"),
            TemplateRender(templates_path / "client.md.jinja2", docs_path / "client.md"),
            TemplateRender(templates_path / "usage.md.jinja2", docs_path / "usage.md"),
        ]

        if package.literals:
            template_renders.append(
                TemplateRender(templates_path / "literals.md.jinja2", docs_path / "literals.md"),
            )

        if package.type_defs:
            template_renders.append(
                TemplateRender(templates_path / "type_defs.md.jinja2", docs_path / "type_defs.md"),
            )

        if package.waiters:
            template_renders.append(
                TemplateRender(templates_path / "waiters.md.jinja2", docs_path / "waiters.md"),
            )

        if package.paginators:
            template_renders.append(
                TemplateRender(
                    templates_path / "paginators.md.jinja2",
                    docs_path / "paginators.md",
                ),
            )

        if package.service_resource:
            template_renders.append(
                TemplateRender(
                    templates_path / "service_resource.md.jinja2",
                    docs_path / "service_resource.md",
                ),
            )

        self._render_docs_templates(package, template_renders)
        valid_paths = [path for t in template_renders for path in t.paths]
        self._cleanup(valid_paths, docs_path)
