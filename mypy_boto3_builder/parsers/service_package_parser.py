"""
Parser that produces `structures.ServicePackage`.

Copyright 2024 Vlad Emelianov
"""

from collections.abc import Iterable

from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.package_data import BasePackageData
from mypy_boto3_builder.parsers.client import parse_client
from mypy_boto3_builder.parsers.service_resource_parser import ServiceResourceParser
from mypy_boto3_builder.parsers.shape_parser import ShapeParser
from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.structures.packages.service_package import ServicePackage
from mypy_boto3_builder.structures.paginator import Paginator
from mypy_boto3_builder.structures.waiter import Waiter
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_def_sortable import TypeDefSortable
from mypy_boto3_builder.type_maps.typed_dicts import CloudwatchEventTypeDef
from mypy_boto3_builder.utils.install_requires import InstallRequiresItem
from mypy_boto3_builder.utils.strings import xform_name
from mypy_boto3_builder.utils.type_checks import is_union
from mypy_boto3_builder.utils.type_def_sorter import TypeDefSorter

UNION_TYPE_MAP = {
    Type.list: Type.List,
    Type.set: Type.Set,
    Type.dict: Type.Dict,
    Type.type: Type.Type,
}


class ServicePackageParser:
    """
    Parser that produces `structures.ServicePackage`.

    Arguments:
        service_name -- Target service name.
        package_data -- Package data.
        version -- Package version.

    Returns:
        ServiceModule structure.
    """

    def __init__(
        self,
        service_name: ServiceName,
        package_data: BasePackageData,
        version: str,
    ) -> None:
        self.service_name = service_name
        self.package_data = package_data
        self.version = version
        self.shape_parser = ShapeParser(self.service_name)
        self._logger = get_logger()

    def parse(self) -> ServicePackage:
        """
        Extract all data from boto3 service package.
        """
        result = self._parse_service_package()
        result.waiters.extend(self._parse_waiters())
        result.waiters.sort()

        result.paginators.extend(self._parse_paginators())
        result.paginators.sort()

        result.client.methods.extend(
            self._get_extra_client_methods(result.paginators, result.waiters),
        )

        self.shape_parser.fix_typed_dict_names()
        self.shape_parser.convert_input_arguments_to_unions(
            [
                *result.client.methods,
                *(result.service_resource.methods if result.service_resource else []),
                *[method for paginator in result.paginators for method in paginator.methods],
                *[method for waiter in result.waiters for method in waiter.methods],
            ],
        )

        type_defs = result.extract_type_defs()

        # Add hardcoded CloudwatchEvent type definitions to cloudwatch service
        if self.service_name == ServiceNameCatalog.cloudwatch:
            type_defs.add(CloudwatchEventTypeDef)

        result.type_defs = self._get_sorted_type_defs(type_defs)
        self.fix_unions_for_py39(result.type_defs)
        result.literals = result.extract_literals()
        result.validate()

        result.install_requires.clear()
        typing_extensions_version = result.get_typing_extensions_fallback_version()
        if typing_extensions_version:
            result.install_requires.add(
                InstallRequiresItem(
                    "typing-extensions",
                    drop_python_version=".".join(str(i) for i in typing_extensions_version),
                )
            )

        return result

    def fix_unions_for_py39(self, type_defs: Iterable[TypeDefSortable]) -> None:
        """
        Fix unions for Python 3.9.

        Python 3.9 does not support new syntax for unions.

        builtins.list -> typing.List
        builtins.set -> typing.Set
        builtins.dict -> typing.Dict
        builtins.type -> typing.Type
        """
        for type_def in type_defs:
            if not is_union(type_def) or not type_def.name:
                continue

            parent_map = type_def.find_type_annotation_parent_map(UNION_TYPE_MAP, shallow=True)
            for old_type_annotation, new_type_annotation in UNION_TYPE_MAP.items():
                parents = parent_map.get(old_type_annotation)
                if not parents:
                    continue
                for parent in parents:
                    parent.replace_child(old_type_annotation, new_type_annotation)

    def _parse_service_package(self) -> ServicePackage:
        client = parse_client(self.service_name, self.shape_parser)
        service_resource_parser = ServiceResourceParser(
            self.service_name,
            self.shape_parser,
        )
        service_resource = service_resource_parser.parse_service_resource()

        return ServicePackage(
            data=self.package_data,
            service_name=self.service_name,
            client=client,
            service_resource=service_resource,
            version=self.version,
        )

    def _parse_waiters(self) -> list[Waiter]:
        waiters: list[Waiter] = []
        for waiter_name in self.shape_parser.get_waiter_names():
            self._logger.debug(f"Parsing Waiter {waiter_name}")
            waiter = Waiter(
                name=f"{waiter_name}Waiter",
                waiter_name=waiter_name,
                attribute_name=xform_name(waiter_name),
                service_name=self.service_name,
            )
            wait_method = self.shape_parser.get_wait_method(waiter_name)
            waiter.methods.append(wait_method)
            waiters.append(waiter)

        return waiters

    def _parse_paginators(self) -> list[Paginator]:
        result: list[Paginator] = []
        for paginator_name in self.shape_parser.get_paginator_names():
            self._logger.debug(f"Parsing Paginator {paginator_name}")
            operation_name = xform_name(paginator_name)
            paginator_record = Paginator(
                name=f"{paginator_name}Paginator",
                paginator_name=paginator_name,
                operation_name=operation_name,
                service_name=self.service_name,
                return_type=self.shape_parser.get_paginator_subscript(paginator_name),
            )

            paginate_method = self.shape_parser.get_paginate_method(paginator_name)
            paginator_record.methods.append(paginate_method)
            result.append(paginator_record)

        return result

    def _get_extra_client_methods(
        self,
        paginators: list[Paginator],
        waiters: list[Waiter],
    ) -> list[Method]:
        result: list[Method] = []
        for paginator in paginators:
            method = paginator.get_client_method()
            if len(paginators) == 1:
                method.decorators.clear()
            result.append(method)

        for waiter in waiters:
            method = waiter.get_client_method()
            if len(waiters) == 1:
                method.decorators.clear()
            result.append(method)

        return result

    def _get_sorted_type_defs(self, type_defs: Iterable[TypeDefSortable]) -> list[TypeDefSortable]:
        type_def_sorter = TypeDefSorter(type_defs)
        return type_def_sorter.sort()
