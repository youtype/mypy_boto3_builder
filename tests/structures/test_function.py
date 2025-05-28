import pytest

from mypy_boto3_builder.exceptions import BuildInternalError
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.function import Function
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_constant import TypeConstant
from mypy_boto3_builder.type_annotations.type_typed_dict import TypedDictAttribute, TypeTypedDict


class TestFunction:
    function: Function

    def setup_method(self) -> None:
        self.function = Function(
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

    def test_init(self) -> None:
        assert self.function.name == "name"
        assert len(self.function.arguments) == 3
        assert self.function.body == "line1\nline2"
        assert self.function.docstring == "docstring\n\nlong"
        assert self.function.short_docstring == "docstring"
        assert repr(self.function) == "def name(self, my_str: str = 'test', lst: list[Any]) -> None"

        self.function.docstring = ""
        assert not self.function.short_docstring

    def test_set_boto3_doc_link(self) -> None:
        with pytest.raises(BuildInternalError):
            _link = self.function.boto3_doc_link

        assert not self.function.has_boto3_doc_link()
        self.function.set_boto3_doc_link("link")
        assert self.function.boto3_doc_link == "link"
        assert self.function.has_boto3_doc_link()

    def test_short_docstring(self) -> None:
        self.function.docstring = "docstring\n\nlong"
        assert self.function.short_docstring == "docstring"

        self.function.docstring = "[text](link)"
        assert not self.function.short_docstring

        self.function.docstring = ""
        assert not self.function.short_docstring

    def test_returns_none(self) -> None:
        self.function.return_type = Type.none
        assert self.function.returns_none is True

        self.function.return_type = Type.str
        assert self.function.returns_none is False

    def test_is_kw_only(self) -> None:
        assert self.function.is_kw_only() is False

        self.function.arguments = [
            Argument.kwflag(),
            Argument("lst", Type.ListAny),
        ]
        assert self.function.is_kw_only() is True

        self.function.arguments = [
            Argument("lst", Type.ListAny),
            Argument.kwflag(),
        ]
        assert self.function.is_kw_only() is False

    def test_type_hint_annotations(self) -> None:
        assert self.function.type_hint_annotations == []

        my_typed_dict = TypeTypedDict(
            "MyTypedDict",
            [TypedDictAttribute("key", Type.str, required=False)],
        )
        self.function.arguments = [
            Argument.self(),
            Argument("my_str", Type.str, TypeConstant("test")),
            Argument("dct", my_typed_dict),
        ]
        self.function.return_type = my_typed_dict
        assert self.function.type_hint_annotations == [my_typed_dict, my_typed_dict]

    def test_get_types(self) -> None:
        assert set(self.function.iterate_types()) == {
            Type.Any,
            Type.none,
            Type.List,
            Type.str,
            TypeConstant("test"),
        }

    def test_get_required_import_records(self) -> None:
        rendered = [i.render() for i in sorted(self.function.get_required_import_records())]
        assert rendered == [
            "from typing import Any",
        ]

    def test_remove_argument(self) -> None:
        test_function = self.function.copy()
        test_function.remove_argument("unknown")
        assert len(test_function.arguments) == 3

        test_function = self.function.copy()
        test_function.remove_argument("my_str")
        assert len(test_function.arguments) == 2

        test_function = self.function.copy()
        test_function.remove_argument("my_str", "lst")
        assert len(test_function.arguments) == 1
