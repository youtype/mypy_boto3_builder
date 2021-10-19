import sys
from typing import Any, List, NamedTuple, Pattern

if sys.version_info >= (3, 9):
    from typing import Literal, TypedDict
else:
    from typing_extensions import Literal, TypedDict

ATTR_NAME_REGEX: Pattern[str]

ConditionBaseExpressionType = TypedDict(
    "ConditionBaseExpressionType", {"format": str, "operator": str, "values": List[Any]}
)

class ConditionBase:
    expression_format: str
    expression_operator: str
    has_grouped_values: bool
    def __init__(self, *values: Any) -> None: ...
    def __and__(self, other: ConditionBase) -> "And": ...
    def __or__(self, other: ConditionBase) -> "Or": ...
    def __invert__(self) -> "Not": ...
    def get_expression(self) -> ConditionBaseExpressionType: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...

class AttributeBase(object):
    def __init__(self, name: str) -> None: ...
    def __and__(self, value: Any) -> Any: ...
    def __or__(self, value: Any) -> Any: ...
    def __invert__(self) -> Any: ...
    def eq(self, value: Any) -> "Equals": ...
    def lt(self, value: Any) -> "LessThan": ...
    def lte(self, value: Any) -> "LessThanEquals": ...
    def gt(self, value: Any) -> "GreaterThan": ...
    def gte(self, value: Any) -> "GreaterThanEquals": ...
    def begins_with(self, value: Any) -> "BeginsWith": ...
    def between(self, low_value: Any, high_value: Any) -> "Between": ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...

class ConditionAttributeBase(ConditionBase, AttributeBase):
    def __init__(self, *values: Any) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...

class ComparisonCondition(ConditionBase):
    expression_format: Literal["{0} {operator} {1}"]

class Equals(ComparisonCondition):
    expression_operator: Literal["="]

class NotEquals(ComparisonCondition):
    expression_operator: Literal["<>"]

class LessThan(ComparisonCondition):
    expression_operator: Literal["<"]

class LessThanEquals(ComparisonCondition):
    expression_operator: Literal["<="]

class GreaterThan(ComparisonCondition):
    expression_operator: Literal[">"]

class GreaterThanEquals(ComparisonCondition):
    expression_operator: Literal[">="]

class In(ComparisonCondition):
    expression_operator: Literal["IN"]
    has_grouped_values: bool

class Between(ConditionBase):
    expression_operator: Literal["BETWEEN"]
    expression_format: Literal["{0} {operator} {1} AND {2}"]

class BeginsWith(ConditionBase):
    expression_operator: Literal["begins_with"]
    expression_format: Literal["{operator}({0}, {1})"]

class Contains(ConditionBase):
    expression_operator: Literal["contains"]
    expression_format: Literal["{operator}({0}, {1})"]

class Size(ConditionAttributeBase):
    expression_operator: Literal["size"]
    expression_format: Literal["{operator}({0})"]

class AttributeType(ConditionBase):
    expression_operator: Literal["attribute_type"]
    expression_format: Literal["{operator}({0}, {1})"]

class AttributeExists(ConditionBase):
    expression_operator: Literal["attribute_exists"]
    expression_format: Literal["{operator}({0})"]

class AttributeNotExists(ConditionBase):
    expression_operator: Literal["attribute_not_exists"]
    expression_format: Literal["{operator}({0})"]

class And(ConditionBase):
    expression_operator: Literal["AND"]
    expression_format: Literal["({0} {operator} {1})"]

class Or(ConditionBase):
    expression_operator: Literal["OR"]
    expression_format: Literal["({0} {operator} {1})"]

class Not(ConditionBase):
    expression_operator: Literal["NOT"]
    expression_format: Literal["({operator} {0})"]

class Key(AttributeBase): ...

class Attr(AttributeBase):
    def ne(self, value: Any) -> NotEquals: ...
    def is_in(self, value: Any) -> In: ...
    def exists(self) -> AttributeExists: ...
    def not_exists(self) -> AttributeNotExists: ...
    def contains(self, value: Any) -> Contains: ...
    def size(self) -> Size: ...
    def attribute_type(self, value: Any) -> AttributeType: ...

BuiltConditionExpression = NamedTuple(
    "BuiltConditionExpression",
    [
        ("condition_expression", str),
        ("attribute_name_placeholders", List[str]),
        ("attribute_value_placeholders", List[str]),
    ],
)

class ConditionExpressionBuilder:
    def __init__(self) -> None: ...
    def reset(self) -> None: ...
    def build_expression(
        self, condition: ConditionBase, is_key_condition: bool = ...
    ) -> BuiltConditionExpression: ...
