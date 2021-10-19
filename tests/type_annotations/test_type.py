from mypy_boto3_builder.type_annotations.type import Type, TypeSubscript


class TestType:
    def test_get_optional(self):
        assert Type.get_optional(Type.DictStrAny).render() == "Optional[Dict[str, Any]]"
        assert (
            Type.get_optional(TypeSubscript(Type.Union, [Type.str])).render() == "Union[str, None]"
        )
