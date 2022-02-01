# TypeValue

> Auto-generated documentation for [mypy_boto3_builder.parsers.docstring_parser.type_value](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/type_value.py) module.

Structure for parsed as dict request or response syntax values.

- [mypy-boto3-builder](../../../README.md#mypy_boto3_builder) / [Modules](../../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../../index.md#mypy-boto3-builder) / [Parsers](../index.md#parsers) / [Docstring Parser](index.md#docstring-parser) / TypeValue
    - [TypeValue](#typevalue)
        - [TypeValue().get_type](#typevalueget_type)
        - [TypeValue().is_dict](#typevalueis_dict)
        - [TypeValue().is_func_call](#typevalueis_func_call)
        - [TypeValue().is_list](#typevalueis_list)
        - [TypeValue().is_literal](#typevalueis_literal)
        - [TypeValue().is_literal_item](#typevalueis_literal_item)
        - [TypeValue().is_plain](#typevalueis_plain)
        - [TypeValue().is_set](#typevalueis_set)
        - [TypeValue().is_union](#typevalueis_union)

## TypeValue

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/type_value.py#L20)

```python
class TypeValue():
    def __init__(
        service_name: ServiceName,
        prefix: str,
        value: dict[(str, Any)],
    ) -> None:
```

Structure for parsed as dict request or response syntax values.

#### See also

- [ServiceName](../../service_name.md#servicename)

### TypeValue().get_type

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/type_value.py#L218)

```python
def get_type() -> FakeAnnotation:
```

Get value type.

#### See also

- [FakeAnnotation](../../type_annotations/fake_annotation.md#fakeannotation)

### TypeValue().is_dict

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/type_value.py#L49)

```python
def is_dict() -> bool:
```

Whether value is Dict.

### TypeValue().is_func_call

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/type_value.py#L79)

```python
def is_func_call() -> bool:
```

Whether value is Callable.

### TypeValue().is_list

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/type_value.py#L55)

```python
def is_list() -> bool:
```

Whether value is List.

### TypeValue().is_literal

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/type_value.py#L61)

```python
def is_literal() -> bool:
```

Whether value is Literal.

### TypeValue().is_literal_item

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/type_value.py#L184)

```python
def is_literal_item() -> bool:
```

Whether value is Literal item.

### TypeValue().is_plain

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/type_value.py#L85)

```python
def is_plain() -> bool:
```

Whether value is not None.

### TypeValue().is_set

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/type_value.py#L67)

```python
def is_set() -> bool:
```

Whether value is Set.

### TypeValue().is_union

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/type_value.py#L73)

```python
def is_union() -> bool:
```

Whether value is Union.
