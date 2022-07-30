# Resource

[mypy-boto3-builder Index](../../README.md#mypy-boto3-builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Structures](./index.md#structures) /
Resource

> Auto-generated documentation for [mypy_boto3_builder.structures.resource](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/resource.py) module.

- [Resource](#resource)
  - [Resource](#resource-1)
    - [Resource().boto3_doc_link](#resource()boto3_doc_link)
    - [Resource().iterate_types](#resource()iterate_types)

## Resource

[Show source in resource.py:14](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/resource.py#L14)

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

[Show source in resource.py:33](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/resource.py#L33)

Link to boto3 docs.

#### Signature

```python
@property
def boto3_doc_link(self) -> str:
    ...
```

### Resource().iterate_types

[Show source in resource.py:40](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/resource.py#L40)

Iterate over all type annotations from collections.

#### Signature

```python
def iterate_types(self) -> Iterator[FakeAnnotation]:
    ...
```

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)


