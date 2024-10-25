from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_constant import TypeConstant


class TestMethod:
    method: Method

    def setup_method(self) -> None:
        self.method = Method(
            name="name",
            arguments=[
                Argument.self(),
                Argument("my_str", Type.str, TypeConstant("test")),
                Argument("lst", Type.ListAny),
            ],
            decorators=[Type.Any],
            return_type=Type.none,
            body_lines=["line1", "line2"],
            docstring="docstring\n\nlong",
        )

    def test_is_kw_only(self) -> None:
        assert self.method.is_kw_only() is False

        self.method.arguments = [
            Argument.self(),
            Argument.kwflag(),
            Argument("lst", Type.ListAny),
        ]
        assert self.method.is_kw_only() is True

        self.method.arguments = [
            Argument.self(),
            Argument("lst", Type.ListAny),
            Argument.kwflag(),
            Argument("lst2", Type.ListAny),
        ]
        assert self.method.is_kw_only() is False

    def test_iterate_call_arguments(self) -> None:
        assert len(list(self.method.iterate_call_arguments())) == 2

        self.method.arguments = [
            Argument("lst", Type.ListAny),
            Argument.kwflag(),
            Argument("lst2", Type.ListAny),
        ]
        assert len(list(self.method.iterate_call_arguments())) == 3

    def test_iterate_packed_arguments(self) -> None:
        assert len(list(self.method.iterate_packed_arguments())) == 3

        self.method.arguments = [
            Argument.self(),
            Argument.kwflag(),
            Argument("lst2", Type.ListAny),
        ]
        assert len(list(self.method.iterate_packed_arguments())) == 3
        self.method.create_request_type_annotation("RequestType")
        assert len(list(self.method.iterate_packed_arguments())) == 2

    def test_has_arguments(self) -> None:
        assert self.method.has_arguments() is True

        self.method.arguments = [Argument.self()]
        assert self.method.has_arguments() is False

        self.method.arguments = [Argument("other", Type.str)]
        assert self.method.has_arguments() is True
