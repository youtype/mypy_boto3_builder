# Resource

> Auto-generated documentation for [mypy_boto3_builder.structures.resource](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/resource.py) module.

Boto3 ServiceResource sub-Resource.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / Resource
    - [Resource](#resource)
        - [Resource().boto3_doc_link](#resourceboto3_doc_link)
        - [Resource().get_types](#resourceget_types)

## Resource

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/resource.py#L12)

```python
class Resource(ClassRecord):
    def __init__(name: str, service_name: ServiceName):
```

Boto3 ServiceResource sub-Resource.

#### See also

- [ClassRecord](class_record.md#classrecord)
- [ServiceName](../service_name.md#servicename)

### Resource().boto3_doc_link

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/resource.py#L32)

```python
@property
def boto3_doc_link() -> str:
```

Link to boto3 docs.

### Resource().get_types

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/resource.py#L39)

```python
def get_types() -> set[FakeAnnotation]:
```

Extract type annotations from collections.

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)
