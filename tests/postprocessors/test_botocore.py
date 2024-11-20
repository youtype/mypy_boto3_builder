from unittest.mock import Mock

from mypy_boto3_builder.postprocessors.botocore import BotocorePostprocessor
from mypy_boto3_builder.service_name import ServiceNameCatalog
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_typed_dict import TypedDictAttribute, TypeTypedDict
from mypy_boto3_builder.type_annotations.type_union import TypeUnion


class TestBotocorePostprocessor:
    def test_replace_self_ref_typed_dicts(self) -> None:
        package = Mock()
        self_ref_typed_dict = TypeTypedDict(
            "TestTypeDef",
            [
                TypedDictAttribute("test", Type.str, required=False),
            ],
        )
        other_typed_dict = TypeTypedDict(
            "OtherTypeDef",
            [
                TypedDictAttribute("test", Type.str, required=False),
            ],
        )
        deep_self_ref_typed_dict = TypeTypedDict(
            "DeepSelfRefTypeDef",
            [
                TypedDictAttribute("test", Type.str, required=False),
                TypedDictAttribute(
                    "deep_self_ref",
                    TypeUnion([self_ref_typed_dict, Type.str]),
                    required=False,
                ),
            ],
        )
        self_ref_typed_dict.add_attribute("self_ref", self_ref_typed_dict, required=False)
        self_ref_typed_dict.add_attribute("other_ref", other_typed_dict, required=False)
        self_ref_typed_dict.add_attribute("deep_self_ref", deep_self_ref_typed_dict, required=False)

        package.type_defs = [self_ref_typed_dict]
        postprocessor = BotocorePostprocessor(
            package=package,
            service_names=[ServiceNameCatalog.s3],
        )
        postprocessor.replace_self_ref_typed_dicts()
        assert self_ref_typed_dict.children[0].type_annotation == Type.str
        assert self_ref_typed_dict.children[1].type_annotation == Type.DictStrAny
        assert self_ref_typed_dict.children[2].type_annotation == other_typed_dict
        assert self_ref_typed_dict.children[3].type_annotation == deep_self_ref_typed_dict
        assert (
            deep_self_ref_typed_dict.children[1].type_annotation.render()
            == "Union[Dict[str, Any], str]"
        )
