# TypeValue

[Mypy_boto3_builder Index](../../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../../index.md#mypy-boto3-builder) /
[Parsers](../index.md#parsers) /
[Docstring Parser](./index.md#docstring-parser) /
TypeValue

> Auto-generated documentation for [mypy_boto3_builder.parsers.docstring_parser.type_value](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/type_value.py) module.

## TypeValue

[Show source in type_value.py:20](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/type_value.py#L20)

Structure for parsed as dict request or response syntax values.

#### Signature

```python
class TypeValue:
    def __init__(
        self, service_name: ServiceName, prefix: str, value: dict[str, Any]
    ) -> None:
        ...
```

#### See also

- [ServiceName](../../service_name.md#servicename)

### TypeValue().get_type

[Show source in type_value.py:218](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/type_value.py#L218)

Get value type.

#### Signature

```python
def get_type(self) -> FakeAnnotation:
    ...
```

#### See also

- [FakeAnnotation](../../type_annotations/fake_annotation.md#fakeannotation)

### TypeValue().is_dict

[Show source in type_value.py:49](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/type_value.py#L49)

Whether value is Dict.

#### Signature

```python
def is_dict(self) -> bool:
    ...
```

### TypeValue().is_func_call

[Show source in type_value.py:79](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/type_value.py#L79)

Whether value is Callable.

#### Signature

```python
def is_func_call(self) -> bool:
    ...
```

### TypeValue().is_list

[Show source in type_value.py:55](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/type_value.py#L55)

Whether value is List.

#### Signature

```python
def is_list(self) -> bool:
    ...
```

### TypeValue().is_literal

[Show source in type_value.py:61](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/type_value.py#L61)

Whether value is Literal.

#### Signature

```python
def is_literal(self) -> bool:
    ...
```

### TypeValue().is_literal_item

[Show source in type_value.py:184](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/type_value.py#L184)

Whether value is Literal item.

#### Signature

```python
def is_literal_item(self) -> bool:
    ...
```

### TypeValue().is_plain

[Show source in type_value.py:85](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/type_value.py#L85)

Whether value is not None.

#### Signature

```python
def is_plain(self) -> bool:
    ...
```

### TypeValue().is_set

[Show source in type_value.py:67](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/type_value.py#L67)

Whether value is Set.

#### Signature

```python
def is_set(self) -> bool:
    ...
```

### TypeValue().is_union

[Show source in type_value.py:73](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/docstring_parser/type_value.py#L73)

Whether value is Union.

#### Signature

```python
def is_union(self) -> bool:
    ...
```
