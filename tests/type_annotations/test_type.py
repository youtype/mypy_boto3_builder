from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_union import TypeUnion


class TestType:
    def test_get_optional(self):
        assert Type.get_optional(Type.DictStrAny).render() == "Optional[Dict[str, Any]]"
        assert (
            Type.get_optional(TypeUnion([Type.str, Type.bool])).render() == "Union[str, bool, None]"
        )
