# ServiceResource

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Structures](./index.md#structures) /
ServiceResource

> Auto-generated documentation for [mypy_boto3_builder.structures.service_resource](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_resource.py) module.

## ServiceResource

[Show source in service_resource.py:22](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_resource.py#L22)

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

[Show source in service_resource.py:78](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_resource.py#L78)

Link to boto3 docs.

#### Signature

```python
@property
def boto3_doc_link(self) -> str:
    ...
```

### ServiceResource().get_all_names

[Show source in service_resource.py:96](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_resource.py#L96)

Get names for `__all__` statement.

#### Signature

```python
def get_all_names(self) -> list[str]:
    ...
```

### ServiceResource.get_class_name

[Show source in service_resource.py:58](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_resource.py#L58)

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

[Show source in service_resource.py:107](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_resource.py#L107)

Get a list of Service Resource collections.

#### Signature

```python
def get_collections(self) -> list[Collection]:
    ...
```

#### See also

- [Collection](./collection.md#collection)

### ServiceResource().get_sub_resources

[Show source in service_resource.py:123](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_resource.py#L123)

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

[Show source in service_resource.py:85](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_resource.py#L85)

Iterate over type annotations for collections and sub-resources.

#### Signature

```python
def iterate_types(self) -> Iterator[FakeAnnotation]:
    ...
```

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)
