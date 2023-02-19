from mypy_boto3_builder.package_data import Boto3StubsPackageData
from mypy_boto3_builder.service_name import ServiceNameCatalog
from mypy_boto3_builder.structures.package import Package


class TestPackage:
    def test_init(self) -> None:
        package = Package(Boto3StubsPackageData, [ServiceNameCatalog.s3])
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
        assert (
            package.get_service_pypi_link(ServiceNameCatalog.s3)
            == "https://pypi.org/project/mypy-boto3-s3/"
        )
