from mypy_boto3_builder.type_annotations.internal_import import InternalImport


class TestInternalImport:
    def setup_method(self) -> None:
        self.result = InternalImport("MyClass")

    def test_init(self) -> None:
        assert self.result.name == "MyClass"

    def test_render(self) -> None:
        assert self.result.render() == "MyClass"
        self.result.use_alias = True
        assert self.result.render() == "_MyClass"

    def test_get_import_records(self) -> None:
        assert len(self.result.get_import_records()) == 0

    def test_copy(self) -> None:
        assert self.result.copy().name == "MyClass"
