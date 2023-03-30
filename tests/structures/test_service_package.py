import pytest

from mypy_boto3_builder.package_data import Boto3StubsPackageData
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.client import Client
from mypy_boto3_builder.structures.paginator import Paginator
from mypy_boto3_builder.structures.service_package import ServicePackage
from mypy_boto3_builder.structures.service_resource import ServiceResource
from mypy_boto3_builder.structures.waiter import Waiter
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral
from mypy_boto3_builder.type_annotations.type_typed_dict import TypeTypedDict


class TestServicePackage:
    @property
    def service_package(self) -> ServicePackage:
        service_name = ServiceName("service", "Service")
        return ServicePackage(
            Boto3StubsPackageData,
            service_name=service_name,
            client=Client("Client", service_name, "base"),
            service_resource=ServiceResource("ServiceResource", service_name, "base"),
            waiters=[Waiter("waiter", "waiter", service_name)],
            paginators=[Paginator("Paginator", "Paginator", "paginate", service_name)],
            typed_dicts=[TypeTypedDict("MyTypedDict", [])],
            literals=[TypeLiteral("MyLiteral", ["value"])],
            helper_functions=["helper_function"],
        )

    def test_init(self) -> None:
        assert self.service_package

    def test_extract_literals(self) -> None:
        assert self.service_package.extract_literals() == []

    def test_extract_typed_dicts(self) -> None:
        assert self.service_package.extract_typed_dicts() == []

    def test_get_init_import_records(self) -> None:
        assert len(self.service_package.get_init_import_records()) == 4

    def test_get_init_all_names(self) -> None:
        assert len(self.service_package.get_init_all_names()) == 4

    def test_get_client_required_import_records(self) -> None:
        assert len(self.service_package.get_client_required_import_records()) == 2

    def test_get_service_resource_required_import_records(self) -> None:
        assert len(self.service_package.get_service_resource_required_import_records()) == 3

    def test_get_paginator_required_import_records(self) -> None:
        assert len(self.service_package.get_paginator_required_import_records()) == 1

    def test_get_waiter_required_import_records(self) -> None:
        assert len(self.service_package.get_waiter_required_import_records()) == 1

    def test_get_type_defs_required_import_records(self) -> None:
        assert len(self.service_package.get_type_defs_required_import_records()) == 2

    def test_get_literals_required_import_records(self) -> None:
        assert len(self.service_package.get_literals_required_import_records()) == 2

    def test_validate(self) -> None:
        self.service_package.validate()
        with pytest.raises(ValueError):
            service_package = self.service_package
            service_package.literals[0].name = "Literal"
            service_package.validate()
        with pytest.raises(ValueError):
            service_package = self.service_package
            service_package.literals[0].name = "MyTypedDict"
            service_package.validate()
