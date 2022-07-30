# Type

[mypy-boto3-builder Index](../../README.md#mypy-boto3-builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Type Annotations](./index.md#type-annotations) /
Type

> Auto-generated documentation for [mypy_boto3_builder.type_annotations.type](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type.py) module.

- [Type](#type)
  - [Type](#type-1)
    - [Type.get_optional](#typeget_optional)

## Type

[Show source in type.py:15](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type.py#L15)

Predefined FakeAnnotation instances.

#### Signature

```python
class Type:
    ...
```

### Type.get_optional

[Show source in type.py:55](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type.py#L55)

Get Optional type annotation.

#### Signature

```python
@classmethod
def get_optional(cls, wrapped: FakeAnnotation) -> FakeAnnotation:
    ...
```

#### See also

- [FakeAnnotation](./fake_annotation.md#fakeannotation)


