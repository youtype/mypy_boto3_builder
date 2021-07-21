# ServiceResource

> Auto-generated documentation for [mypy_boto3_builder.structures.service_resource](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_resource.py) module.

Boto3 ServiceResource.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / ServiceResource
    - [ServiceResource](#serviceresource)
        - [ServiceResource().boto3_doc_link](#serviceresourceboto3_doc_link)
        - [ServiceResource().docstring](#serviceresourcedocstring)
        - [ServiceResource().get_all_names](#serviceresourceget_all_names)
        - [ServiceResource.get_class_name](#serviceresourceget_class_name)
        - [ServiceResource().get_collections](#serviceresourceget_collections)
        - [ServiceResource().get_sub_resources](#serviceresourceget_sub_resources)
        - [ServiceResource().get_types](#serviceresourceget_types)

## ServiceResource

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_resource.py#L22)

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

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_resource.py#L93)

```python
@property
def boto3_doc_link() -> str:
```

Link to boto3 docs.

### ServiceResource().docstring

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_resource.py#L100)

```python
@property
def docstring() -> str:
```

Class docstring.

### ServiceResource().get_all_names

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_resource.py#L125)

```python
def get_all_names() -> List[str]:
```

Get names for `__all__` statement.

### ServiceResource.get_class_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_resource.py#L64)

```python
@staticmethod
def get_class_name(service_name: ServiceName) -> str:
```

Get class name for ServiceName.

#### See also

- [ServiceName](../service_name.md#servicename)

### ServiceResource().get_collections

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_resource.py#L136)

```python
def get_collections() -> List[Collection]:
```

Get a list of Service Resource collections.

### ServiceResource().get_sub_resources

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_resource.py#L152)

```python
def get_sub_resources() -> List[Resource]:
```

Get sub-resource in safe order.

#### Returns

A list of sub resources.

### ServiceResource().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_resource.py#L112)

```python
def get_types() -> Set[FakeAnnotation]:
```

Extract type annotations for collections and sub-resources.
