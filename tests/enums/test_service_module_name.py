from mypy_boto3_builder.enums.service_module_name import ServiceModuleName


class TestServiceModuleName:
    def test_properties(self) -> None:
        assert ServiceModuleName.paginator.file_name == "paginator.py"
        assert ServiceModuleName.paginator.template_name == "paginator.py.jinja2"
