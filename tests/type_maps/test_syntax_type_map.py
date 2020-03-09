from mypy_boto3_builder.type_maps.syntax_type_map import SYNTAX_TYPE_MAP


class TestSyntaxTypeMap:
    def test_main(self) -> None:
        assert SYNTAX_TYPE_MAP["b'bytes'"]
