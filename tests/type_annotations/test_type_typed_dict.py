from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral
from mypy_boto3_builder.type_annotations.type_typed_dict import TypedDictAttribute, TypeTypedDict


class TestTypedDictAttribute:
    result: TypedDictAttribute

    def setup_method(self) -> None:
        self.result = TypedDictAttribute("test", Type.DictStrAny, required=True)

    def test_init(self) -> None:
        assert self.result.name == "test"
        assert self.result.is_required()

    def test_render(self) -> None:
        assert self.result.render() == '"test": dict[str, Any]'

    def test_mark_as_required(self) -> None:
        self.result.required = False
        assert not self.result.is_required()
        self.result.mark_as_required()
        assert self.result.is_required()


class TestTypeTypedDict:
    result: TypeTypedDict

    def setup_method(self) -> None:
        self.result = TypeTypedDict(
            "MyDict",
            [
                TypedDictAttribute("required", Type.bool, required=True),
                TypedDictAttribute("optional", Type.str, required=False),
            ],
            "documentation",
        )

    def test_init(self) -> None:
        assert self.result.name == "MyDict"
        assert len(self.result.children) == 2
        assert self.result.docstring == "documentation"

    def test_render(self) -> None:
        result = self.result.copy()
        assert result.render() == "MyDict"
        result.stringify()
        assert result.render() == '"MyDict"'

    def test_render_definition(self) -> None:
        result = self.result.copy()
        assert result.render_definition() == (
            "class MyDict(TypedDict):\n    required: bool\n    optional: NotRequired[str]\n"
        )

        typed_dict = TypeTypedDict(
            "MyDict",
            [
                TypedDictAttribute("required", Type.str, required=True),
                TypedDictAttribute("Type", Type.str, required=False),
            ],
        )
        typed_dict.is_safe_as_class = False
        assert (
            typed_dict.render_definition()
            == 'MyDict = TypedDict("MyDict", {"required": str, "Type": NotRequired[str], })'
        )

    def test_get_import_records(self) -> None:
        import_records = sorted(self.result.get_import_records())
        assert len(import_records) == 1
        assert import_records[0].render() == "from .type_defs import MyDict"

    def test_get_types(self) -> None:
        assert set(self.result.iterate_types()) == {self.result}

    def test_add_attribute(self) -> None:
        self.result.add_attribute("third", Type.int, required=False)
        assert len(self.result.children) == 3

    def test_is_dict(self) -> None:
        assert self.result.is_dict()

    def test_has_optional(self) -> None:
        assert self.result.has_optional()
        assert not TypeTypedDict(
            "MyDict",
            [TypedDictAttribute("required", Type.bool, required=True)],
        ).has_optional()
        assert TypeTypedDict(
            "MyDict",
            [TypedDictAttribute("optional", Type.str, required=False)],
        ).has_optional()
        assert not TypeTypedDict("MyDict", []).has_optional()

    def test_has_required(self) -> None:
        assert self.result.has_required()
        assert TypeTypedDict(
            "MyDict",
            [TypedDictAttribute("required", Type.bool, required=True)],
        ).has_required()
        assert not TypeTypedDict(
            "MyDict",
            [TypedDictAttribute("optional", Type.str, required=False)],
        ).has_required()
        assert not TypeTypedDict("MyDict", []).has_required()

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
                "MyDict",
                [
                    TypedDictAttribute("required", Type.bool, required=True),
                    TypedDictAttribute("optional", Type.str, required=False),
                ],
            ),
        )
        assert not self.result.is_same(
            TypeTypedDict(
                "MyDict",
                [
                    TypedDictAttribute("required", Type.bool, required=True),
                    TypedDictAttribute("optional", Type.float, required=False),
                ],
            ),
        )

    def test_get_children_types(self) -> None:
        assert self.result.get_children_types() == {
            Type.str,
            # Type.NotRequired,
            Type.bool,
        }

    def test_get_children_literals(self) -> None:
        clone = self.result.copy()
        assert len(clone.get_children_literals()) == 0
        clone.add_attribute("literal", TypeLiteral("test", ["asd"]), required=True)
        assert len(clone.get_children_literals()) == 1
        assert len(clone.get_children_literals(["other"])) == 1
        assert len(clone.get_children_literals([clone.name])) == 0

    def test_stringify(self) -> None:
        result = self.result.copy()
        assert not result.is_stringified()
        result.stringify()
        assert result.is_stringified()

    def test_replace_self_references(self) -> None:
        typed_dict = TypeTypedDict(
            "MyDict",
            [
                TypedDictAttribute("required", Type.str, required=True),
            ],
        )
        typed_dict.is_safe_as_class = False
        typed_dict.add_attribute("self_one", typed_dict, required=True)
        typed_dict.add_attribute("Type", typed_dict, required=False)
        assert typed_dict.replace_self_references(Type.DictStrAny)
        assert typed_dict.render_definition() == (
            'MyDict = TypedDict("MyDict",'
            ' {"required": str, "self_one": dict[str, Any],'
            ' "Type": NotRequired[dict[str, Any]], })'
        )
        assert not self.result.replace_self_references(Type.DictStrAny)
