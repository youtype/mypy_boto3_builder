from mypy_boto3_builder.structures.attribute import Attribute
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_constant import TypeConstant


class TestAttribute:
    def test_init(self) -> None:
        assert Attribute("attr", Type.DictStrAny)
        assert Attribute("attr", Type.DictStrAny, TypeConstant("abc"))
        assert Attribute("attr", Type.DictStrAny, TypeConstant("abc"), True)

    def test_render(self) -> None:
        assert Attribute("attr", Type.DictStrAny).render() == "attr: Dict[str, Any]"
        assert (
            Attribute("attr", Type.DictStrAny, TypeConstant("abc")).render()
            == "attr: Dict[str, Any]"
        )
        assert (
            Attribute("attr", Type.DictStrAny, TypeConstant("abc"), True).render()
            == "attr: Dict[str, Any]  # type: ignore"
        )

    def test_is_autoload_property(self) -> None:
        assert Attribute("attr", Type.DictStrAny).is_autoload_property()
        assert Attribute("attr", Type.DictStrAny, is_reference=True).is_autoload_property() is False
        assert (
            Attribute("attr", Type.DictStrAny, is_identifier=True).is_autoload_property() is False
        )
        assert (
            Attribute("attr", Type.DictStrAny, is_collection=True).is_autoload_property() is False
        )
        assert Attribute("meta", Type.DictStrAny).is_autoload_property() is False
