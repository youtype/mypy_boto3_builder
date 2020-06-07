"""
Structure for parsed as dict request or response syntax values.
"""
from typing import Any, Dict, List, Optional

from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_annotation import TypeAnnotation
from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.type_typed_dict import TypeTypedDict
from mypy_boto3_builder.type_maps.shape_type_map import get_shape_type_stub
from mypy_boto3_builder.type_maps.syntax_type_map import SYNTAX_TYPE_MAP


class TypeValue:
    """
    Structure for parsed as dict request or response syntax values.
    """

    def __init__(self, service_name: ServiceName, prefix: str, value: Dict[str, Any]) -> None:
        self.service_name = service_name
        self.logger = get_logger()
        self.prefix = prefix
        self.raw: Dict[str, Any] = value
        self.dict_items: Optional[List[Dict[str, Any]]] = value.get("dict_items")
        if value.get("empty_dict"):
            self.dict_items = []
        self.set_items: Optional[List[Any]] = value.get("set_items")
        self.list_items: Optional[List[Any]] = value.get("list_items")
        if value.get("empty_list"):
            self.list_items = []
        self.func_call: Optional[Dict[str, Any]] = value.get("func_call")
        self.union_items: List[Any] = []
        if value.get("union_first_item"):
            self.union_items.append(value["union_first_item"])
            self.union_items.extend(value["union_rest_items"])
        self.literal_items: List[Any] = []
        if value.get("literal_first_item"):
            self.literal_items.append(value["literal_first_item"])
            self.literal_items.extend(value["literal_rest_items"])

        self.value: Optional[str] = value.get("value")

    def is_dict(self) -> bool:
        return self.dict_items is not None

    def is_list(self) -> bool:
        return self.list_items is not None

    def is_literal(self) -> bool:
        return bool(self.literal_items)

    def is_set(self) -> bool:
        return bool(self.set_items)

    def is_union(self) -> bool:
        return bool(self.union_items)

    def is_func_call(self) -> bool:
        return bool(self.func_call)

    def is_plain(self) -> bool:
        return self.value is not None

    def _get_type_dict(self) -> FakeAnnotation:
        if not self.dict_items:
            return Type.DictStrAny

        first_key = self.dict_items[0]["key"]
        if first_key in SYNTAX_TYPE_MAP:
            result = TypeSubscript(Type.Dict)
            result.add_child(SYNTAX_TYPE_MAP[first_key])
            result.add_child(
                TypeValue(self.service_name, self.prefix, self.dict_items[0]["value"]).get_type()
            )
            return result

        typed_dict_name = f"{self.prefix}TypeDef"
        shape_type_stub = get_shape_type_stub(self.service_name, typed_dict_name)
        if shape_type_stub:
            return shape_type_stub

        typed_dict = TypeTypedDict(typed_dict_name)
        for item in self.dict_items:
            key_name = self._parse_constant(item["key"])
            prefix = f"{self.prefix}{key_name}"
            typed_dict.add_attribute(
                key_name,
                TypeValue(self.service_name, prefix, item["value"]).get_type(),
                required=False,
            )
        return typed_dict

    def _get_type_list(self) -> TypeSubscript:
        if not self.list_items:
            return TypeSubscript(Type.List, [Type.Any])

        result = TypeSubscript(Type.List)
        for item_index, item in enumerate(self.list_items):
            prefix = f"{self.prefix}{item_index if item_index else ''}"
            result.add_child(TypeValue(self.service_name, prefix, item).get_type())
        return result

    def _get_type_union(self) -> FakeAnnotation:
        if not self.union_items:
            return Type.Any

        result = TypeSubscript(Type.Union)
        for item_index, item in enumerate(self.union_items):
            prefix = f"{self.prefix}{item_index if item_index else ''}"
            result.add_child(TypeValue(self.service_name, prefix, item).get_type())

        if all(i is result.children[0] for i in result.children):
            return result.children[0]

        return result

    def _get_type_set(self) -> TypeAnnotation:
        if not self.set_items:
            return Type.Any

        plain_values = [i["value"] for i in self.set_items]
        if plain_values == ["'... recursive ...'"]:
            return Type.Any

        self.logger.warning(f"Unknown set: {self.raw}, fallback to Any")
        return Type.Any

    def _get_type_func_call(self) -> FakeAnnotation:
        if not self.func_call:
            raise ValueError(f"Value is not a func call: {self.raw}")

        if self.func_call["name"] == "datetime":
            return ExternalImport(ImportString("datetime"), "datetime")

        if self.func_call["name"] == "StreamingBody":
            return ExternalImport(ImportString("botocore", "response"), "StreamingBody")

        if self.func_call["name"] == "EventStream":
            return ExternalImport(ImportString("botocore", "eventstream"), "EventStream")

        self.logger.warning(f"Unknown function: {self.raw}, fallback to Any")
        return Type.Any

    def _get_type_plain(self) -> FakeAnnotation:
        if not self.value:
            raise ValueError(f"Value is not plain: {self.raw}")

        if self.value in SYNTAX_TYPE_MAP:
            return SYNTAX_TYPE_MAP[self.value]

        if self.value.startswith("'"):
            return Type.str

        self.logger.warning(f"Unknown plain value: {self.raw}, fallback to Any")
        return Type.Any

    def is_literal_item(self) -> bool:
        if self.value is None:
            return False
        return self.value.startswith("'")

    def _get_type_literal(self) -> FakeAnnotation:
        if not self.literal_items:
            raise ValueError(f"Value is not literal: {self.raw}")

        items = [TypeValue(self.service_name, self.prefix, i) for i in self.literal_items]
        if all(i.is_literal_item() for i in items):
            item_constants = [self._parse_constant(i.value or "") for i in items]
            return TypeLiteral(*item_constants)

        item_types = [i.get_type() for i in items]

        if all([i is item_types[0] for i in item_types]):
            return item_types[0]

        return TypeSubscript(Type.Union, item_types)

    @staticmethod
    def _parse_constant(value: str) -> Any:
        if value.startswith("'"):
            return value.replace("'", "")

        if value.isdigit():
            return int(value)

        raise ValueError(f"Invalid constant: {value}")

    def get_type(self) -> FakeAnnotation:
        if self.is_list():
            return self._get_type_list()
        if self.is_dict():
            return self._get_type_dict()
        if self.is_set():
            return self._get_type_set()
        if self.is_func_call():
            return self._get_type_func_call()
        if self.is_union():
            return self._get_type_union()
        if self.is_literal():
            return self._get_type_literal()
        if self.is_plain():
            return self._get_type_plain()

        raise ValueError(f"Unknown value: {self.raw}")
