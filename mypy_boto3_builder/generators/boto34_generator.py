"""
Generator for boto34 package.

Copyright 2025 Vlad Emelianov
"""

import shutil
from pathlib import Path
from typing import NoReturn

from mypy_boto3_builder.constants import TemplatePath
from mypy_boto3_builder.enums.product_library import ProductLibrary
from mypy_boto3_builder.exceptions import BuildInternalError
from mypy_boto3_builder.generators.base_generator import BaseGenerator
from mypy_boto3_builder.package_data import (
    BasePackageData,
    TypesAioBoto3PackageData,
    TypesAioBotocorePackageData,
    TypesBoto3PackageData,
)
from mypy_boto3_builder.parsers.fake_service_package import parse_fake_service_package
from mypy_boto3_builder.structures.packages.boto34_package import Boto34Package
from mypy_boto3_builder.structures.packages.service_package import ServicePackage
from mypy_boto3_builder.utils.jinja2 import render_jinja2_template
from mypy_boto3_builder.utils.path import print_path
from mypy_boto3_builder.utils.strings import progressify


class Boto34Generator(BaseGenerator):
    """
    Generator for boto34 package.
    """

    @property
    def service_package_data(self) -> BasePackageData:
        """
        Service package data.
        """
        library = self.product.get_library()
        match library:
            case ProductLibrary.boto3:
                return TypesBoto3PackageData()
            case ProductLibrary.aiobotocore:
                return TypesAioBotocorePackageData()
            case ProductLibrary.aioboto3:
                return TypesAioBoto3PackageData()
            case _:
                raise BuildInternalError(f"Unsupported library: {library}")

    def _get_boto34_service_template_path(self) -> Path:
        library = self.product.get_library()
        match library:
            case ProductLibrary.boto3:
                return TemplatePath.boto34_boto3_service
            case ProductLibrary.aiobotocore:
                return TemplatePath.boto34_aiobotocore_service
            case ProductLibrary.aioboto3:
                return TemplatePath.boto34_aioboto3_service
            case _:
                raise BuildInternalError(f"Unsupported library: {library}")

    def _get_boto34_session_template_path(self) -> Path:
        library = self.product.get_library()
        match library:
            case ProductLibrary.boto3:
                return TemplatePath.boto34_boto3_session
            case ProductLibrary.aiobotocore:
                return TemplatePath.boto34_aiobotocore_session
            case ProductLibrary.aioboto3:
                return TemplatePath.boto34_aioboto3_session
            case _:
                raise BuildInternalError(f"Unsupported library: {library}")

    def generate_stubs(self) -> None:
        """
        Generate boto34 services.
        """
        service_package_data = self.service_package_data
        main_package = Boto34Package(
            data=service_package_data,
            service_names=self.main_service_names,
            version=self.version,
        )
        library_name = service_package_data.get_library_name()
        output_path = self.output_path / main_package.name / library_name

        self.logger.info(f"Parsing {len(self.service_names)} services")
        services_path = output_path / "services"
        if services_path.exists():
            shutil.rmtree(services_path)

        services_path.mkdir(parents=True, exist_ok=True)
        (services_path / "__init__.py").touch()

        generated_paths: list[Path] = []
        self.logger.info(f"Generating {len(self.service_names)} services")
        for log_counter, service_name in progressify(self.service_names):
            service_path = services_path / f"{service_name.import_name}.py"
            self.logger.debug(f"{log_counter} Writing {print_path(service_path)}")
            package = parse_fake_service_package(service_name, service_package_data, self.version)
            main_package.service_packages.append(package)
            generated_paths.append(service_path)
            service_path.write_text(
                render_jinja2_template(
                    self._get_boto34_service_template_path(),
                    {"package": package, "main_package": main_package},
                )
            )

        if generated_paths:
            self.logger.info(f"Formatting {print_path(services_path)}")
            self.package_writer.format_output(main_package, generated_paths)

        session_path = output_path / "session.py"
        self.logger.info(f"Generating {print_path(session_path)}")
        rendered = render_jinja2_template(
            self._get_boto34_session_template_path(),
            {"package": main_package},
        )
        session_path.write_text(rendered)
        self.package_writer.format_output(main_package, [session_path])

        if self.product.get_library() == ProductLibrary.boto3:
            list_output_path = self.output_path / main_package.name / "services.md"
            self.logger.info(f"Generating {print_path(list_output_path)}")
            list_output_path.write_text(
                render_jinja2_template(
                    TemplatePath.boto34_services,
                    {"package": main_package},
                )
            )
            self.package_writer.format_output(main_package, [list_output_path])

    def _generate_stubs(self) -> None:
        """
        Generate boto34 services.
        """
        service_package_data = self.service_package_data
        main_package = Boto34Package(
            data=service_package_data,
            service_names=self.main_service_names,
            version=self.version,
        )
        library_name = service_package_data.get_library_name()
        output_path = self.output_path / main_package.name / library_name

        self.logger.info(f"Parsing {len(self.service_names)} services")
        for service_name in self.service_names:
            package = parse_fake_service_package(service_name, service_package_data, self.version)
            main_package.service_packages.append(package)

        session_path = output_path / "session.py"
        self.logger.info(f"Generating {print_path(session_path)}")
        rendered = render_jinja2_template(
            self._get_boto34_session_template_path(),
            {"package": main_package},
        )
        session_path.write_text(rendered)
        self.package_writer.format_output(main_package, [session_path])

        if self.product.get_library() == ProductLibrary.boto3:
            list_output_path = self.output_path / main_package.name / "services.md"
            self.logger.info(f"Generating {print_path(list_output_path)}")
            list_output_path.write_text(
                render_jinja2_template(
                    TemplatePath.boto34_services,
                    {"package": main_package},
                )
            )
            self.package_writer.format_output(main_package, [list_output_path])

    def generate_stubs_lite(self) -> NoReturn:
        """
        Not implemented.
        """
        raise NotImplementedError("Should never be called")

    def generate_full_stubs(self) -> NoReturn:
        """
        Not implemented.
        """
        raise NotImplementedError("Should never be called")

    def generate_custom_stubs(self) -> NoReturn:
        """
        Not implemented.
        """
        raise NotImplementedError("Should never be called")

    def generate_docs(self) -> None:
        """
        Not implemented.
        """
        raise NotImplementedError("Should never be called")

    def _get_postprocessor(self, service_package: ServicePackage) -> NoReturn:
        """
        Not implemented.
        """
        raise NotImplementedError("Should never be called")
