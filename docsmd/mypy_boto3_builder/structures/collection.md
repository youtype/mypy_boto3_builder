# Collection

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Structures](./index.md#structures) /
Collection

> Auto-generated documentation for [mypy_boto3_builder.structures.collection](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/collection.py) module.

## Collection

[Show source in collection.py:15](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/collection.py#L15)

Boto3 ServiceResource or Resource collection.

#### Signature

```python
class Collection(ClassRecord):
    def __init__(
        self,
        name: str,
        attribute_name: str,
        parent_name: str,
        service_name: ServiceName,
        type_annotation: FakeAnnotation,
        object_class_name: str,
    ): ...
```

#### See also

- [ClassRecord](./class_record.md#classrecord)
- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)
- [ServiceName](../service_name.md#servicename)

### Collection().boto3_doc_link

[Show source in collection.py:40](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/collection.py#L40)

Link to boto3 docs.

#### Signature

```python
@property
def boto3_doc_link(self) -> str: ...
```

### Collection().iterate_types

[Show source in collection.py:47](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/collection.py#L47)

Iterate over all type annotations.

#### Signature

```python
def iterate_types(self) -> Iterator[FakeAnnotation]: ...
```

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)
