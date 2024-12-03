import pytest

from mypy_boto3_builder.exceptions import StructureError
from mypy_boto3_builder.package_data import Boto3StubsPackageData
from mypy_boto3_builder.service_name import ServiceNameCatalog
from mypy_boto3_builder.structures.package import Package


class TestPackage:
    def test_init(self) -> None:
        package = Package(
            data=Boto3StubsPackageData(),
            service_names=[ServiceNameCatalog.s3],
            version="2.3.4",
        )
        assert package.directory_name == "boto3_stubs_package"
        assert package.min_library_version
        assert package.max_library_version
        assert package.get_local_doc_link() == "https://youtype.github.io/boto3_stubs_docs/"
        assert (
            package.get_local_doc_link(ServiceNameCatalog.s3)
            == "https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3/"
        )
        assert package.get_module_name(ServiceNameCatalog.s3) == "mypy_boto3_s3"
        assert package.get_service_pypi_name(ServiceNameCatalog.s3) == "mypy-boto3-s3"
        assert package.essential_service_names == [ServiceNameCatalog.s3]
        assert package.min_python_version
        assert str(package) == "boto3-stubs 2.3.4 (boto3 1.2.3)"

    def test_service_name(self) -> None:
        package = Package(Boto3StubsPackageData(), [ServiceNameCatalog.s3])
        assert package.service_name == ServiceNameCatalog.s3

        package.service_names = (*package.service_names, ServiceNameCatalog.ec2)
        with pytest.raises(StructureError):
            _ = package.service_name

    def test_get_classifiers(self) -> None:
        package = Package(Boto3StubsPackageData(), [ServiceNameCatalog.s3])
        classifiers = package.get_classifiers()
        assert "Programming Language :: Python :: 3" in classifiers
        assert "Programming Language :: Python :: 3.13" in classifiers
        assert "Programming Language :: Python :: 3 :: Only" in classifiers
