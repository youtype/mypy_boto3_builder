# ServiceResource

> Auto-generated documentation for [mypy_boto3_builder.structures.service_resource](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_resource.py) module.

Boto3 ServiceResource.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / ServiceResource
    - [ServiceResource](#serviceresource)
        - [ServiceResource().get_all_names](#serviceresourceget_all_names)
        - [ServiceResource().get_collections](#serviceresourceget_collections)
        - [ServiceResource().get_sub_resources](#serviceresourceget_sub_resources)
        - [ServiceResource().get_types](#serviceresourceget_types)

## ServiceResource

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_resource.py#L18)

```python
class ServiceResource(ClassRecord):
    def __init__(
        name: str,
        service_name: ServiceName,
        boto3_service_resource: Boto3ServiceResource,
        docstring: str = '',
    ):
```

Boto3 ServiceResource.

#### See also

- [ClassRecord](class_record.md#classrecord)
- [ServiceName](../service_name.md#servicename)

### ServiceResource().get_all_names

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_resource.py#L60)

```python
def get_all_names() -> List[str]:
```

### ServiceResource().get_collections

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_resource.py#L68)

```python
def get_collections() -> List[Collection]:
```

### ServiceResource().get_sub_resources

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_resource.py#L81)

```python
def get_sub_resources() -> List[Resource]:
```

Get sub-resource in safe order.

#### Returns

A list of sub resources.

### ServiceResource().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_resource.py#L51)

```python
def get_types() -> Set[FakeAnnotation]:
```
