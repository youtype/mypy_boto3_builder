from mypy_boto3_builder.service_name import ServiceNameCatalog
from mypy_boto3_builder.structures.master_package import MasterPackage
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_constant import TypeConstant


class TestMasterPackage:
    def test_init(self) -> None:
        package = MasterPackage([ServiceNameCatalog.ec2, ServiceNameCatalog.logs], [])
        assert package
        assert package.essential_service_names == [ServiceNameCatalog.ec2]
