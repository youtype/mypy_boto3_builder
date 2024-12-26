from mypy_boto3_builder.service_name import ServiceNameCatalog
from mypy_boto3_builder.structures.packages.mypy_boto3_package import MypyBoto3Package


class TestMypyBoto3Package:
    def test_init(self) -> None:
        package = MypyBoto3Package([ServiceNameCatalog.ec2, ServiceNameCatalog.logs], [], "1.2.3")
        assert package
        assert package.essential_service_names == [ServiceNameCatalog.ec2]
        assert package.literals == []
