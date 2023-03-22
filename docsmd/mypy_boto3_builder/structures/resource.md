# Resource

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Structures](./index.md#structures) /
Resource

> Auto-generated documentation for [mypy_boto3_builder.structures.resource](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/resource.py) module.

## Resource

[Show source in resource.py:15](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/resource.py#L15)

Boto3 ServiceResource sub-Resource.

#### Signature

```python
class Resource(ClassRecord):
    def __init__(self, name: str, service_name: ServiceName):
        ...
```

#### See also

- [ClassRecord](./class_record.md#classrecord)
- [ServiceName](../service_name.md#servicename)

### Resource().boto3_doc_link

[Show source in resource.py:29](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/resource.py#L29)

Link to boto3 docs.

#### Signature

```python
@property
def boto3_doc_link(self) -> str:
    ...
```

### Resource().iterate_types

[Show source in resource.py:36](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/resource.py#L36)

Iterate over all type annotations from collections.

#### Signature

```python
def iterate_types(self) -> Iterator[FakeAnnotation]:
    ...
```

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)
