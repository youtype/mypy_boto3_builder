import pytest

from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.type_typed_dict import TypedDictAttribute, TypeTypedDict


class TestTypedDictAttribute:
    result: TypedDictAttribute

    def setup_method(self) -> None:
        self.result = TypedDictAttribute("test", Type.DictStrAny, True)

    def test_init(self) -> None:
        assert self.result.name == "test"
        assert self.result.is_required()

    def test_render(self) -> None:
        assert self.result.render() == '"test": Dict[str, Any]'


class TestTypeTypedDict:
    result: TypeTypedDict

    def setup_method(self):
        self.result = TypeTypedDict(
            "MyDict",
            [
                TypedDictAttribute("required", Type.bool, True),
                TypedDictAttribute("optional", Type.str, False),
            ],
            "documentation",
        )

    def test_init(self) -> None:
        assert self.result.name == "MyDict"
        assert len(self.result.children) == 2
        assert self.result.docstring == "documentation"
        assert self.result.requires_safe_render

    def test_render(self) -> None:
        result = self.result.copy()
        assert result.render() == "MyDict"
        assert result.render("OtherDict") == "MyDict"
        assert result.render("MyDict") == '"MyDict"'
        result.stringify()
        assert result.render() == '"MyDict"'
        result.replace_with_dict.add(result.name)
        assert result.render("MyDict") == "Dict[str, Any]"

    def test_get_import_record(self) -> None:
        assert self.result.get_import_record().render() == "from .type_defs import MyDict"

    def test_get_types(self) -> None:
        assert set(self.result.iterate_types()) == {self.result}

    def test_add_attribute(self) -> None:
        self.result.add_attribute("third", Type.int, False)
        assert len(self.result.children) == 3

    def test_is_dict(self) -> None:
        assert self.result.is_dict()

    def test_is_typed_dict(self) -> None:
        assert self.result.is_typed_dict()

    def test_has_optional(self) -> None:
        assert self.result.has_optional()
        assert not TypeTypedDict(
            "MyDict",
            [TypedDictAttribute("required", Type.bool, True)],
        ).has_optional()
        assert TypeTypedDict(
            "MyDict",
            [TypedDictAttribute("optional", Type.str, False)],
        ).has_optional()
        assert not TypeTypedDict("MyDict", []).has_optional()

    def test_has_required(self) -> None:
        assert self.result.has_required()
        assert TypeTypedDict(
            "MyDict",
            [TypedDictAttribute("required", Type.bool, True)],
        ).has_required()
        assert not TypeTypedDict(
            "MyDict",
            [TypedDictAttribute("optional", Type.str, False)],
        ).has_required()
        assert not TypeTypedDict("MyDict", []).has_required()

    def test_has_both(self) -> None:
        assert self.result.has_both()
        assert not TypeTypedDict(
            "MyDict",
            [TypedDictAttribute("required", Type.bool, True)],
        ).has_both()
        assert not TypeTypedDict(
            "MyDict",
            [TypedDictAttribute("optional", Type.str, False)],
        ).has_both()
        assert not TypeTypedDict("MyDict", []).has_both()

    def test_get_required(self) -> None:
        assert len(self.result.get_required()) == 1
        assert self.result.get_required()[0].name == "required"

    def test_get_optional(self) -> None:
        assert len(self.result.get_optional()) == 1
        assert self.result.get_optional()[0].name == "optional"

    def test_copy(self) -> None:
        assert self.result.copy().name == self.result.name

    def test_is_same(self) -> None:
        assert self.result.is_same(
            TypeTypedDict(
                "OtherDict",
                [
                    TypedDictAttribute("required", Type.bool, True),
                    TypedDictAttribute("optional", Type.str, False),
                ],
            )
        )
        assert not self.result.is_same(
            TypeTypedDict(
                "OtherDict",
                [
                    TypedDictAttribute("required", Type.bool, True),
                    TypedDictAttribute("optional", Type.float, False),
                ],
            )
        )

    def test_get_children_types(self) -> None:
        assert self.result.get_children_types() == {
            Type.str,
            # Type.NotRequired,
            Type.bool,
        }

    def test_get_children_typed_dicts(self) -> None:
        assert len(self.result.get_children_typed_dicts()) == 0

    def test_get_children_literals(self) -> None:
        assert len(self.result.get_children_literals()) == 0
        assert len(self.result.get_children_literals([self.result])) == 0

    def test_replace_self_references(self) -> None:
        self.result.replace_self_references()

    def test_stringify(self) -> None:
        result = self.result.copy()
        assert not result.is_stringified()
        result.stringify()
        assert result.is_stringified()
