from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_annotations.type import Type


class TestMethod:
    def test_init(self) -> None:
        method = Method(
            "my_method",
            [
                Argument("self", None),
                Argument("second", Type.str),
                Argument("other", Type.DictStrAny),
            ],
            Type.none,
        )
        assert len(method.call_arguments) == 2
        method = Method(
            "my_method",
            [
                Argument("second", Type.str),
                Argument("other", Type.DictStrAny),
            ],
            Type.none,
        )
        assert len(method.call_arguments) == 2
