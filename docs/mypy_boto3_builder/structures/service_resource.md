# ServiceResource

> Auto-generated documentation for [mypy_boto3_builder.structures.service_resource](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_resource.py) module.

Boto3 ServiceResource.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / ServiceResource
    - [ServiceResource](#serviceresource)
        - [ServiceResource().get_all_names](#serviceresourceget_all_names)
        - [ServiceResource().get_collections](#serviceresourceget_collections)
        - [ServiceResource().get_types](#serviceresourceget_types)

## ServiceResource

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_resource.py#L18)

```python
dataclass
class ServiceResource(ClassRecord):
```

Boto3 ServiceResource.

#### See also

- [ClassRecord](class_record.md#classrecord)

### ServiceResource().get_all_names

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_resource.py#L52)

```python
def get_all_names() -> List[str]:
```

### ServiceResource().get_collections

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_resource.py#L60)

```python
def get_collections() -> List[Collection]:
```

### ServiceResource().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_resource.py#L43)

```python
def get_types() -> Set[FakeAnnotation]:
```
