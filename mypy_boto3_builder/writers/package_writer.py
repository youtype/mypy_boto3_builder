"""
Writer for package static and template files.
"""

from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path

from mypy_boto3_builder.constants import TEMPLATES_PATH
from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.structures.package import Package
from mypy_boto3_builder.structures.service_package import ServicePackage
from mypy_boto3_builder.utils.markdown import fix_pypi_headers
from mypy_boto3_builder.utils.path import print_path, walk_path
from mypy_boto3_builder.writers.utils import (
    blackify,
    blackify_markdown,
    format_md,
    insert_md_toc,
    render_jinja2_package_template,
    sort_imports,
)


@dataclass
class TemplateRender:
    """
    Template render target.
    """

    template_path: Path
    output_path: Path | tuple[Path, ...]

    @property
    def output_paths(self) -> tuple[Path, ...]:
        """
        Get output paths as a tuple.
        """
        if isinstance(self.output_path, Path):
            return (self.output_path,)
        return self.output_path


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

    def _get_service_package_path(self, package: ServicePackage) -> Path:
        if self.generate_setup:
            return self.output_path / package.directory_name / package.name

        return self.output_path / package.name

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
            file_path.parent.mkdir(exist_ok=True, parents=True)
            content = static_path.read_text()
            if not file_path.exists() or file_path.read_text() != content:
                file_path.write_text(content)
                self.logger.debug(f"Updated {print_path(file_path)}")
        return result

    def _get_setup_template_paths(
        self, package: Package, templates_path: Path | None
    ) -> list[TemplateRender]:
        if not templates_path or not self.generate_setup:
            return []

        result: list[TemplateRender] = []
        setup_path = self._get_setup_path(package)
        template_paths = [
            templates_path / "setup.py.jinja2",
            templates_path / "README.md.jinja2",
            TEMPLATES_PATH / "common" / "LICENSE.jinja2",
        ]
        for template_path in template_paths:
            file_name = template_path.stem
            output_file_path = setup_path / file_name
            result.append(TemplateRender(template_path, output_file_path))
        return result

    def _get_package_template_paths(
        self, package: Package, templates_path: Path | None
    ) -> list[TemplateRender]:
        if not templates_path or not self.generate_setup:
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
        render_paths: Sequence[Path],
        package: Package,
    ) -> None:
        content = render_jinja2_package_template(template_path, package=package)
        for file_path in render_paths:
            file_extension = file_path.suffix.lower().replace(".", "")
            if file_extension in ("py", "pyi"):
                content = sort_imports(
                    content,
                    package.name,
                    extension="py" if file_extension == "py" else "pyi",
                    third_party=[
                        "boto3",
                        "botocore",
                        "aiobotocore",
                        *[package.data.get_service_package_name(i) for i in package.service_names],
                    ],
                )
                content = blackify(content, file_path)
            if file_extension == "md":
                content = insert_md_toc(content)
                content = blackify_markdown(content)
                content = fix_pypi_headers(content)
                content = format_md(content)
            self._write_template(file_path, content)

    def _render_templates(
        self,
        package: Package,
        template_renders: Sequence[TemplateRender],
    ) -> None:
        for template_render in template_renders:
            self._render_template(
                template_render.template_path, template_render.output_paths, package
            )

    def _write_template(self, path: Path, content: str) -> None:
        if not path.parent.exists():
            path.parent.mkdir(exist_ok=True, parents=True)

        path.write_text(content)
        self.logger.debug(f"Rendered {print_path(path)}")

    def _render_md_templates(
        self,
        package: Package,
        template_renders: list[TemplateRender],
    ) -> None:
        for template_render in template_renders:
            content = render_jinja2_package_template(template_render.template_path, package=package)
            # if file_path.suffix == ".md":
            #     content = fix_pypi_headers(content)
            #     content = format_md(content)
            for output_path in template_render.output_paths:
                self._write_template(output_path, content)

    def _cleanup(self, valid_paths: Sequence[Path], output_path: Path) -> None:
        for unknown_path in walk_path(output_path, valid_paths):
            unknown_path.unlink()
            self.logger.debug(f"Deleted {print_path(unknown_path)}")

    def write_package(
        self,
        package: Package,
        templates_path: Path | None = None,
        static_files_path: Path | None = None,
        exclude_template_names: Sequence[str] = (),
    ) -> None:
        """
        Generate files for a package.

        Arguments:
            package -- Package to render
            templates_path -- Path to Jinja templates for package
            static_files_path -- Path to static files for package
            exclude_template_names -- Do not render templates with these names
        """
        package_path = self._get_package_path(package)

        static_paths = self._write_static_paths(static_files_path, package_path)
        template_renders: list[TemplateRender] = [
            *self._get_setup_template_paths(package, templates_path),
            *self._get_package_template_paths(package, templates_path),
        ]
        template_renders = [
            i for i in template_renders if i.template_path.name not in exclude_template_names
        ]
        self._render_templates(package, template_renders)

        rendered_paths = [path for t in template_renders for path in t.output_paths]
        valid_paths = (*rendered_paths, *static_paths)
        output_path = self._get_setup_path(package) if self.generate_setup else package_path
        self._cleanup(valid_paths, output_path)

    def write_docs(self, package: Package, templates_path: Path) -> None:
        """
        Generate docs for a package.
        """
        self.output_path.mkdir(exist_ok=True, parents=True)
        template_renders: list[TemplateRender] = []
        for template_path in templates_path.glob("**/*.jinja2"):
            file_name = template_path.stem
            template_renders.append(TemplateRender(template_path, self.output_path / file_name))

        self._render_md_templates(package, template_renders)

    def _get_service_package_template_paths(
        self, package: ServicePackage, templates_path: Path
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
                (
                    package_path / "__init__.pyi",
                    package_path / "__init__.py",
                ),
            ),
            TemplateRender(
                module_templates_path / "__main__.py.jinja2", package_path / "__main__.py"
            ),
            TemplateRender(module_templates_path / "py.typed.jinja2", package_path / "py.typed"),
            TemplateRender(
                module_templates_path / ServiceModuleName.client.template_name,
                (
                    package_path / ServiceModuleName.client.stub_file_name,
                    package_path / ServiceModuleName.client.file_name,
                ),
            ),
        ]
        if package.service_resource:
            file_paths.append(
                TemplateRender(
                    module_templates_path / ServiceModuleName.service_resource.template_name,
                    (
                        package_path / ServiceModuleName.service_resource.stub_file_name,
                        package_path / ServiceModuleName.service_resource.file_name,
                    ),
                )
            )
        if package.paginators:
            file_paths.append(
                TemplateRender(
                    module_templates_path / ServiceModuleName.paginator.template_name,
                    (
                        package_path / ServiceModuleName.paginator.stub_file_name,
                        package_path / ServiceModuleName.paginator.file_name,
                    ),
                )
            )
        if package.waiters:
            file_paths.append(
                TemplateRender(
                    module_templates_path / ServiceModuleName.waiter.template_name,
                    (
                        package_path / ServiceModuleName.waiter.stub_file_name,
                        package_path / ServiceModuleName.waiter.file_name,
                    ),
                )
            )
        if package.literals:
            file_paths.append(
                TemplateRender(
                    module_templates_path / ServiceModuleName.literals.template_name,
                    (
                        package_path / ServiceModuleName.literals.stub_file_name,
                        package_path / ServiceModuleName.literals.file_name,
                    ),
                )
            )
        if package.type_defs:
            file_paths.append(
                TemplateRender(
                    module_templates_path / ServiceModuleName.type_defs.template_name,
                    (
                        package_path / ServiceModuleName.type_defs.stub_file_name,
                        package_path / ServiceModuleName.type_defs.file_name,
                    ),
                )
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

        valid_paths = [path for t in template_renders for path in t.output_paths]
        output_path = (
            self._get_setup_path(package)
            if self.generate_setup
            else self._get_service_package_path(package)
        )
        self._cleanup(valid_paths, output_path)

    def write_service_docs(self, package: ServicePackage, templates_path: Path) -> None:
        """
        Create service docs files.

        Arguments:
            package -- Service package.
            output_path -- Path to output folder.
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
                TemplateRender(templates_path / "literals.md.jinja2", docs_path / "literals.md")
            )

        if package.type_defs:
            template_renders.append(
                TemplateRender(templates_path / "type_defs.md.jinja2", docs_path / "type_defs.md")
            )

        if package.waiters:
            template_renders.append(
                TemplateRender(templates_path / "waiters.md.jinja2", docs_path / "waiters.md")
            )

        if package.paginators:
            template_renders.append(
                TemplateRender(templates_path / "paginators.md.jinja2", docs_path / "paginators.md")
            )

        if package.service_resource:
            template_renders.append(
                TemplateRender(
                    templates_path / "service_resource.md.jinja2",
                    docs_path / "service_resource.md",
                )
            )

        self._render_md_templates(package, template_renders)
        valid_paths = [path for t in template_renders for path in t.output_paths]
        self._cleanup(valid_paths, docs_path)
