# ServiceResource

> Auto-generated documentation for [mypy_boto3_builder.structures.service_resource](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_resource.py) module.

Boto3 ServiceResource.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / ServiceResource
    - [ServiceResource](#serviceresource)
        - [ServiceResource().boto3_doc_link](#serviceresourceboto3_doc_link)
        - [ServiceResource().get_all_names](#serviceresourceget_all_names)
        - [ServiceResource.get_class_name](#serviceresourceget_class_name)
        - [ServiceResource().get_collections](#serviceresourceget_collections)
        - [ServiceResource().get_sub_resources](#serviceresourceget_sub_resources)
        - [ServiceResource().get_types](#serviceresourceget_types)

## ServiceResource

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_resource.py#L20)

```python
class ServiceResource(ClassRecord):
    def __init__(
        name: str,
        service_name: ServiceName,
        boto3_service_resource: Boto3ServiceResource,
    ):
```

Boto3 ServiceResource.

#### See also

- [ClassRecord](class_record.md#classrecord)
- [ServiceName](../service_name.md#servicename)

### ServiceResource().boto3_doc_link

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_resource.py#L91)

```python
@property
def boto3_doc_link() -> str:
```

Link to boto3 docs.

### ServiceResource().get_all_names

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_resource.py#L111)

```python
def get_all_names() -> list[str]:
```

Get names for `__all__` statement.

### ServiceResource.get_class_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_resource.py#L62)

```python
@staticmethod
def get_class_name(service_name: ServiceName) -> str:
```

Get class name for ServiceName.

#### See also

- [ServiceName](../service_name.md#servicename)

### ServiceResource().get_collections

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_resource.py#L122)

```python
def get_collections() -> list[Collection]:
```

Get a list of Service Resource collections.

### ServiceResource().get_sub_resources

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_resource.py#L138)

```python
def get_sub_resources() -> list[Resource]:
```

Get sub-resource in safe order.

#### Returns

A list of sub resources.

### ServiceResource().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_resource.py#L98)

```python
def get_types() -> set[FakeAnnotation]:
```

Extract type annotations for collections and sub-resources.
