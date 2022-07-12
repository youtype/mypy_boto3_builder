# Resource

> Auto-generated documentation for [mypy_boto3_builder.structures.resource](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/resource.py) module.

Boto3 ServiceResource sub-Resource.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / Resource
    - [Resource](#resource)
        - [Resource().boto3_doc_link](#resourceboto3_doc_link)
        - [Resource().iterate_types](#resourceiterate_types)

## Resource

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/resource.py#L14)

```python
class Resource(ClassRecord):
    def __init__(name: str, service_name: ServiceName):
```

Boto3 ServiceResource sub-Resource.

#### See also

- [ClassRecord](class_record.md#classrecord)
- [ServiceName](../service_name.md#servicename)

### Resource().boto3_doc_link

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/resource.py#L34)

```python
@property
def boto3_doc_link() -> str:
```

Link to boto3 docs.

### Resource().iterate_types

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/resource.py#L41)

```python
def iterate_types() -> Iterator[FakeAnnotation]:
```

Iterate over all type annotations from collections.

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)
