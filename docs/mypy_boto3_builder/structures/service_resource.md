# ServiceResource

> Auto-generated documentation for [mypy_boto3_builder.structures.service_resource](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_resource.py) module.

Boto3 ServiceResource.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / ServiceResource
    - [ServiceResource](#serviceresource)
        - [ServiceResource().boto3_doc_link](#serviceresourceboto3_doc_link)
        - [ServiceResource().get_all_names](#serviceresourceget_all_names)
        - [ServiceResource.get_class_name](#serviceresourceget_class_name)
        - [ServiceResource().get_collections](#serviceresourceget_collections)
        - [ServiceResource().get_sub_resources](#serviceresourceget_sub_resources)
        - [ServiceResource().iterate_types](#serviceresourceiterate_types)

## ServiceResource

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_resource.py#L21)

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

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_resource.py#L87)

```python
@property
def boto3_doc_link() -> str:
```

Link to boto3 docs.

### ServiceResource().get_all_names

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_resource.py#L105)

```python
def get_all_names() -> list[str]:
```

Get names for `__all__` statement.

### ServiceResource.get_class_name

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_resource.py#L62)

```python
@staticmethod
def get_class_name(service_name: ServiceName) -> str:
```

Get class name for ServiceName.

#### See also

- [ServiceName](../service_name.md#servicename)

### ServiceResource().get_collections

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_resource.py#L116)

```python
def get_collections() -> list[Collection]:
```

Get a list of Service Resource collections.

#### See also

- [Collection](collection.md#collection)

### ServiceResource().get_sub_resources

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_resource.py#L132)

```python
def get_sub_resources() -> list[Resource]:
```

Get sub-resource in safe order.

#### Returns

A list of sub resources.

#### See also

- [Resource](resource.md#resource)

### ServiceResource().iterate_types

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_resource.py#L94)

```python
def iterate_types() -> Iterator[FakeAnnotation]:
```

Iterate over type annotations for collections and sub-resources.

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)
