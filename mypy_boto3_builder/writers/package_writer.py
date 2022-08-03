"""
Writer for package static and template files.
"""
from pathlib import Path
from typing import Sequence

from mypy_boto3_builder.constants import TEMPLATES_PATH
from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.package import Package
from mypy_boto3_builder.structures.service_package import ServicePackage
from mypy_boto3_builder.utils.markdown import fix_pypi_headers
from mypy_boto3_builder.utils.nice_path import NicePath
from mypy_boto3_builder.writers.utils import (
    blackify,
    blackify_markdown,
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
                self.logger.debug(f"Updated {NicePath(file_path)}")
        return result

    def _get_setup_template_paths(
        self, package: Package, templates_path: Path | None
    ) -> list[tuple[Path, Path]]:
        if not templates_path or not self.generate_setup:
            return []

        result: list[tuple[Path, Path]] = []
        setup_path = self._get_setup_path(package)
        template_paths = [
            templates_path / "setup.py.jinja2",
            templates_path / "README.md.jinja2",
            TEMPLATES_PATH / "common" / "LICENSE.jinja2",
        ]
        for template_path in template_paths:
            file_name = template_path.stem
            output_file_path = setup_path / file_name
            result.append((output_file_path, template_path))
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
            file_name = template_path.stem
            output_file_path = (
                package_path / template_path.relative_to(package_template_path).parent / file_name
            )
            result.append((output_file_path, template_path))
        return result

    def _render_templates(
        self,
        package: Package,
        file_paths: list[tuple[Path, Path]],
        service_name: ServiceName | None = None,
    ) -> None:
        for file_path, template_path in file_paths:
            content = render_jinja2_template(
                template_path,
                package=package,
                service_name=service_name,
            )
            if file_path.suffix in [".py", ".pyi"]:
                content = sort_imports(
                    content,
                    package.name,
                    extension="pyi",
                    third_party=[
                        "boto3",
                        "botocore",
                        "aiobotocore",
                        *(
                            [
                                package.data.get_service_package_name(i)
                                for i in package.service_names
                            ]
                            if not service_name
                            else [package.data.get_service_package_name(service_name)]
                        ),
                    ],
                )
                content = blackify(content, file_path)
            if file_path.suffix == ".md":
                content = insert_md_toc(content)
                content = blackify_markdown(content)
                content = fix_pypi_headers(content)
                content = format_md(content)
            if not file_path.parent.exists():
                file_path.parent.mkdir(exist_ok=True, parents=True)
            if not file_path.exists() or file_path.read_text() != content:
                file_path.write_text(content)
                self.logger.debug(f"Rendered {NicePath(file_path)}")

    def _render_md_templates(
        self,
        package: Package,
        file_paths: list[tuple[Path, Path]],
        service_name: ServiceName | None = None,
    ) -> None:
        for file_path, template_path in file_paths:
            content = render_jinja2_template(
                template_path,
                package=package,
                service_name=service_name,
            )
            print(file_path)
            # if file_path.suffix == ".md":
            #     content = fix_pypi_headers(content)
            #     content = format_md(content)
            if not file_path.parent.exists():
                file_path.parent.mkdir(exist_ok=True, parents=True)
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
        exclude_template_names: Sequence[str] = tuple(),
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
        file_paths: list[tuple[Path, Path]] = [
            *self._get_setup_template_paths(package, templates_path),
            *self._get_package_template_paths(package, templates_path),
        ]
        file_paths = [i for i in file_paths if i[1].name not in exclude_template_names]
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
            file_name = template_path.stem
            file_paths.append((self.output_path / file_name, template_path))

        self._render_md_templates(package, file_paths)

    def _get_service_package_template_paths(
        self, package: ServicePackage, templates_path: Path
    ) -> list[tuple[Path, Path]]:
        module_templates_path = templates_path / "service"
        package_path = self._get_service_package_path(package)
        file_paths: list[tuple[Path, Path]] = [
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
        file_paths.extend([])
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
        return file_paths

    def write_service_package(self, package: ServicePackage, templates_path: Path) -> None:
        """
        Create stubs files for service.

        Arguments:
            package -- Service package.
        """
        file_paths: list[tuple[Path, Path]] = [
            *self._get_setup_template_paths(package, templates_path),
            *self._get_service_package_template_paths(package, templates_path),
        ]
        self._render_templates(package, file_paths, service_name=package.service_name)

        valid_paths = list(dict(file_paths).keys())
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
        docs_path = self.output_path / f"{package.name}"
        docs_path.mkdir(exist_ok=True, parents=True)
        file_paths = [
            (docs_path / "README.md", templates_path / "README.md.jinja2"),
            (docs_path / "client.md", templates_path / "client.md.jinja2"),
            (docs_path / "usage.md", templates_path / "usage.md.jinja2"),
        ]

        if package.literals:
            file_paths.append((docs_path / "literals.md", templates_path / "literals.md.jinja2"))

        if package.typed_dicts:
            file_paths.append((docs_path / "type_defs.md", templates_path / "type_defs.md.jinja2"))

        if package.waiters:
            file_paths.append((docs_path / "waiters.md", templates_path / "waiters.md.jinja2"))

        if package.paginators:
            file_paths.append(
                (docs_path / "paginators.md", templates_path / "paginators.md.jinja2")
            )

        if package.service_resource:
            file_paths.append(
                (docs_path / "service_resource.md", templates_path / "service_resource.md.jinja2")
            )

        self._render_md_templates(package, file_paths, service_name=package.service_name)
        valid_paths = list(dict(file_paths).keys())
        self._cleanup(valid_paths, docs_path)
