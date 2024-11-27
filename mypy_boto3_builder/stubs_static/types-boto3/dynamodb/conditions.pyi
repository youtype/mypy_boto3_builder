import sys
from typing import Any, Dict, List, NamedTuple, Pattern

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

ATTR_NAME_REGEX: Pattern[str]

_ConditionBaseExpressionType = TypedDict(
    "_ConditionBaseExpressionType", {"format": str, "operator": str, "values": List[Any]}
)

class ConditionBase:
    expression_format: str
    expression_operator: str
    has_grouped_values: bool
    def __init__(self, *values: Any) -> None: ...
    def __and__(self, other: ConditionBase) -> "And": ...
    def __or__(self, other: ConditionBase) -> "Or": ...
    def __invert__(self) -> "Not": ...
    def get_expression(self) -> _ConditionBaseExpressionType: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...

class AttributeBase:
    def __init__(self, name: str) -> None:
        self.name: str = ...

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
    expression_format: Literal["{0} {operator} {1}"]  # type: ignore [override]

class Equals(ComparisonCondition):
    expression_operator: Literal["="]  # type: ignore [override]

class NotEquals(ComparisonCondition):
    expression_operator: Literal["<>"]  # type: ignore [override]

class LessThan(ComparisonCondition):
    expression_operator: Literal["<"]  # type: ignore [override]

class LessThanEquals(ComparisonCondition):
    expression_operator: Literal["<="]  # type: ignore [override]

class GreaterThan(ComparisonCondition):
    expression_operator: Literal[">"]  # type: ignore [override]

class GreaterThanEquals(ComparisonCondition):
    expression_operator: Literal[">="]  # type: ignore [override]

class In(ComparisonCondition):
    expression_operator: Literal["IN"]  # type: ignore [override]
    has_grouped_values: bool

class Between(ConditionBase):
    expression_operator: Literal["BETWEEN"]  # type: ignore [override]
    expression_format: Literal["{0} {operator} {1} AND {2}"]  # type: ignore [override]

class BeginsWith(ConditionBase):
    expression_operator: Literal["begins_with"]  # type: ignore [override]
    expression_format: Literal["{operator}({0}, {1})"]  # type: ignore [override]

class Contains(ConditionBase):
    expression_operator: Literal["contains"]  # type: ignore [override]
    expression_format: Literal["{operator}({0}, {1})"]  # type: ignore [override]

class Size(ConditionAttributeBase):
    expression_operator: Literal["size"]  # type: ignore [override]
    expression_format: Literal["{operator}({0})"]  # type: ignore [override]

class AttributeType(ConditionBase):
    expression_operator: Literal["attribute_type"]  # type: ignore [override]
    expression_format: Literal["{operator}({0}, {1})"]  # type: ignore [override]

class AttributeExists(ConditionBase):
    expression_operator: Literal["attribute_exists"]  # type: ignore [override]
    expression_format: Literal["{operator}({0})"]  # type: ignore [override]

class AttributeNotExists(ConditionBase):
    expression_operator: Literal["attribute_not_exists"]  # type: ignore [override]
    expression_format: Literal["{operator}({0})"]  # type: ignore [override]

class And(ConditionBase):
    expression_operator: Literal["AND"]  # type: ignore [override]
    expression_format: Literal["({0} {operator} {1})"]  # type: ignore [override]

class Or(ConditionBase):
    expression_operator: Literal["OR"]  # type: ignore [override]
    expression_format: Literal["({0} {operator} {1})"]  # type: ignore [override]

class Not(ConditionBase):
    expression_operator: Literal["NOT"]  # type: ignore [override]
    expression_format: Literal["({operator} {0})"]  # type: ignore [override]

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
        ("attribute_name_placeholders", Dict[str, str]),
        ("attribute_value_placeholders", Dict[str, Any]),
    ],
)

class ConditionExpressionBuilder:
    def __init__(self) -> None: ...
    def reset(self) -> None: ...
    def build_expression(
        self, condition: ConditionBase, is_key_condition: bool = ...
    ) -> BuiltConditionExpression: ...
