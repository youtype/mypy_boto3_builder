# ServiceResource

[mypy-boto3-builder Index](../../README.md#mypy-boto3-builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Structures](./index.md#structures) /
ServiceResource

> Auto-generated documentation for [mypy_boto3_builder.structures.service_resource](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_resource.py) module.

- [ServiceResource](#serviceresource)
  - [ServiceResource](#serviceresource-1)
    - [ServiceResource().boto3_doc_link](#serviceresource()boto3_doc_link)
    - [ServiceResource().get_all_names](#serviceresource()get_all_names)
    - [ServiceResource.get_class_name](#serviceresourceget_class_name)
    - [ServiceResource().get_collections](#serviceresource()get_collections)
    - [ServiceResource().get_sub_resources](#serviceresource()get_sub_resources)
    - [ServiceResource().iterate_types](#serviceresource()iterate_types)

## ServiceResource

[Show source in service_resource.py:21](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_resource.py#L21)

Boto3 ServiceResource.

#### Signature

```python
class ServiceResource(ClassRecord):
    def __init__(
        self,
        name: str,
        service_name: ServiceName,
        boto3_service_resource: Boto3ServiceResource,
    ):
        ...
```

#### See also

- [ClassRecord](./class_record.md#classrecord)
- [ServiceName](../service_name.md#servicename)

### ServiceResource().boto3_doc_link

[Show source in service_resource.py:87](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_resource.py#L87)

Link to boto3 docs.

#### Signature

```python
@property
def boto3_doc_link(self) -> str:
    ...
```

### ServiceResource().get_all_names

[Show source in service_resource.py:105](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_resource.py#L105)

Get names for `__all__` statement.

#### Signature

```python
def get_all_names(self) -> list[str]:
    ...
```

### ServiceResource.get_class_name

[Show source in service_resource.py:62](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_resource.py#L62)

Get class name for ServiceName.

#### Signature

```python
@staticmethod
def get_class_name(service_name: ServiceName) -> str:
    ...
```

#### See also

- [ServiceName](../service_name.md#servicename)

### ServiceResource().get_collections

[Show source in service_resource.py:116](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_resource.py#L116)

Get a list of Service Resource collections.

#### Signature

```python
def get_collections(self) -> list[Collection]:
    ...
```

#### See also

- [Collection](./collection.md#collection)

### ServiceResource().get_sub_resources

[Show source in service_resource.py:132](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_resource.py#L132)

Get sub-resource in safe order.

#### Returns

A list of sub resources.

#### Signature

```python
def get_sub_resources(self) -> list[Resource]:
    ...
```

#### See also

- [Resource](./resource.md#resource)

### ServiceResource().iterate_types

[Show source in service_resource.py:94](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_resource.py#L94)

Iterate over type annotations for collections and sub-resources.

#### Signature

```python
def iterate_types(self) -> Iterator[FakeAnnotation]:
    ...
```

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)


