# Collection

> Auto-generated documentation for [mypy_boto3_builder.structures.collection](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/collection.py) module.

Boto3 ServiceResource or Resource collection.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / Collection
    - [Collection](#collection)
        - [Collection().get_types](#collectionget_types)

## Collection

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/collection.py#L12)

```python
class Collection(ClassRecord):
    def __init__(
        name: str,
        attribute_name: str,
        parent_name: str,
        type_annotation: FakeAnnotation,
        docstring: str = '',
    ):
```

Boto3 ServiceResource or Resource collection.

#### See also

- [ClassRecord](class_record.md#classrecord)
- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)

### Collection().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/collection.py#L40)

```python
def get_types() -> Set[FakeAnnotation]:
```
