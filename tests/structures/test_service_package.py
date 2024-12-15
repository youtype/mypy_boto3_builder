from unittest.mock import Mock

import pytest

from mypy_boto3_builder.exceptions import StructureError
from mypy_boto3_builder.package_data import Boto3StubsPackageData
from mypy_boto3_builder.service_name import ServiceNameCatalog
from mypy_boto3_builder.structures.client import Client
from mypy_boto3_builder.structures.paginator import Paginator
from mypy_boto3_builder.structures.service_package import ServicePackage
from mypy_boto3_builder.structures.service_resource import ServiceResource
from mypy_boto3_builder.structures.waiter import Waiter
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral
from mypy_boto3_builder.type_annotations.type_typed_dict import TypeTypedDict


class TestServicePackage:
    service_package: ServicePackage

    def setup_method(self) -> None:
        service_name = ServiceNameCatalog.s3
        self.service_package = ServicePackage(
            data=Boto3StubsPackageData(),
            service_name=service_name,
            version="1.2.3",
            client=Client("Client", service_name),
            service_resource=ServiceResource("ServiceResource", service_name),
            waiters=[Waiter("waiter", "waiter", "waiter", service_name)],
            paginators=[Paginator("Paginator", "Paginator", "paginate", service_name)],
            type_defs=[TypeTypedDict("MyTypedDict", [])],
            literals=[TypeLiteral("MyLiteral", ["value"])],
            helper_functions=[Mock()],
        )

    def test_init(self) -> None:
        assert self.service_package.name == "mypy_boto3_s3"
        assert self.service_package.pypi_name == "mypy-boto3-s3"

    def test_client(self) -> None:
        assert self.service_package.client.name == "Client"

        self.service_package._client = None  # type: ignore[attr-defined]
        with pytest.raises(StructureError):
            _ = self.service_package.client

    def test_extract_literals(self) -> None:
        assert self.service_package.extract_literals() == []

    def test_extract_type_defs(self) -> None:
        assert self.service_package.extract_type_defs() == set()

    def test_get_init_import_records(self) -> None:
        assert len(list(self.service_package.get_init_import_records())) == 4

    def test_get_init_all_names(self) -> None:
        assert len(self.service_package.get_init_all_names()) == 4

    def test_get_client_required_import_records(self) -> None:
        assert list(self.service_package.get_client_required_import_records()) == [
            "from typing import Any, Dict",
            "from botocore.client import BaseClient",
        ]

    def test_get_service_resource_required_import_records(self) -> None:
        assert list(self.service_package.get_service_resource_required_import_records()) == [
            "from .client import S3Client",
            "from boto3.resources.base import ResourceMeta, ServiceResource",
        ]

        self.service_package.service_resource = None
        assert list(self.service_package.get_service_resource_required_import_records()) == []

    def test_get_paginator_required_import_records(self) -> None:
        assert list(self.service_package.get_paginator_required_import_records()) == [
            "from botocore.paginate import Paginator",
        ]

    def test_get_waiter_required_import_records(self) -> None:
        assert list(self.service_package.get_waiter_required_import_records()) == [
            "from botocore.waiter import Waiter",
        ]

    def test_get_type_defs_required_import_records(self) -> None:
        assert list(self.service_package.get_type_defs_required_import_records()) == [
            "import sys",
            (
                "if sys.version_info >= (3, 12):"
                "\n    from typing import TypedDict"
                "\nelse:"
                "\n    from typing_extensions import TypedDict"
            ),
        ]

        self.service_package.type_defs = []
        assert list(self.service_package.get_type_defs_required_import_records()) == []

    def test_get_literals_required_import_records(self) -> None:
        assert list(self.service_package.get_literals_required_import_records()) == [
            "import sys",
            (
                "if sys.version_info >= (3, 12):"
                "\n    from typing import Literal"
                "\nelse:"
                "\n    from typing_extensions import Literal"
            ),
        ]

    def test_validate(self) -> None:
        self.service_package.validate()

        service_package = self.service_package
        service_package.literals[0].name = "Literal"
        with pytest.raises(StructureError):
            service_package.validate()

        service_package = self.service_package
        service_package.literals[0].name = "MyTypedDict"
        with pytest.raises(StructureError):
            service_package.validate()

    def test_get_doc_link(self) -> None:
        assert (
            self.service_package.get_doc_link("client")
            == "https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/"
        )
        assert (
            self.service_package.get_doc_link("client", "extra", "parts")
            == "https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/client/#extraparts"
        )

    def test_get_local_doc_link(self) -> None:
        assert (
            self.service_package.get_local_doc_link()
            == "https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/"
        )
