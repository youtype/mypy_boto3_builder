from typing import Any, Callable, Dict, List, Optional

from boto3.dynamodb.conditions import ConditionExpressionBuilder
from boto3.dynamodb.types import TypeDeserializer, TypeSerializer
from boto3.resources.model import ResourceModel
from botocore.model import Shape

def register_high_level_interface(base_classes: List[type], **kwargs: Any) -> None: ...
def copy_dynamodb_params(params: Any, **kwargs: Any) -> Any: ...

class DynamoDBHighLevelResource:
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class TransformationInjector:
    def __init__(
        self,
        transformer: Optional[ParameterTransformer] = ...,
        condition_builder: Optional[ConditionExpressionBuilder] = ...,
        serializer: Optional[TypeSerializer] = ...,
        deserializer: Optional[TypeDeserializer] = ...,
    ) -> None: ...
    def inject_condition_expressions(
        self, params: Dict[str, Any], model: ResourceModel
    ) -> None: ...
    def inject_attribute_value_input(
        self, params: Dict[str, Any], model: ResourceModel
    ) -> None: ...
    def inject_attribute_value_output(
        self, parsed: Dict[str, Any], model: ResourceModel
    ) -> None: ...

class ConditionExpressionTransformation:
    def __init__(
        self,
        condition_builder: ConditionExpressionBuilder,
        placeholder_names: List[str],
        placeholder_values: List[str],
        is_key_condition: bool = ...,
    ) -> None: ...
    def __call__(self, value: Any) -> Any: ...

class ParameterTransformer:
    def transform(
        self,
        params: Dict[str, Any],
        model: Shape,
        transformation: Callable[[Any], Any],
        target_shape: str,
    ) -> None: ...
