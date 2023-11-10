# TypeConstant

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Type Annotations](./index.md#type-annotations) /
TypeConstant

> Auto-generated documentation for [mypy_boto3_builder.type_annotations.type_constant](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_constant.py) module.

## EllipsisType

[Show source in type_constant.py:12](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_constant.py#L12)

Placeholder for `...`.

#### Signature

```python
class EllipsisType: ...
```



## TypeConstant

[Show source in type_constant.py:21](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_constant.py#L21)

Wrapper for constant like `False` or `"test"`.

#### Arguments

- `value` - Constant value.

#### Signature

```python
class TypeConstant(FakeAnnotation):
    def __init__(self, value: ValueType) -> None: ...
```

#### See also

- [FakeAnnotation](./fake_annotation.md#fakeannotation)
- [ValueType](#valuetype)

### TypeConstant().__copy__

[Show source in type_constant.py:46](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_constant.py#L46)

Create a copy of type annotation wrapper.

#### Signature

```python
def __copy__(self: _R) -> _R: ...
```

### TypeConstant().render

[Show source in type_constant.py:34](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_constant.py#L34)

Render type annotation to a valid Python code for local usage.

#### Returns

A string with a valid type annotation.

#### Signature

```python
def render(self) -> str: ...
```
