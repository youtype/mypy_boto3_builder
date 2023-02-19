# Paginator

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Structures](./index.md#structures) /
Paginator

> Auto-generated documentation for [mypy_boto3_builder.structures.paginator](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/paginator.py) module.

## Paginator

[Show source in paginator.py:16](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/paginator.py#L16)

Boto3 client Paginator.

#### Signature

```python
class Paginator(ClassRecord):
    def __init__(
        self,
        name: str,
        paginator_name: str,
        operation_name: str,
        service_name: ServiceName,
    ):
        ...
```

#### See also

- [ClassRecord](./class_record.md#classrecord)
- [ServiceName](../service_name.md#servicename)

### Paginator().boto3_doc_link

[Show source in paginator.py:36](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/paginator.py#L36)

Link to boto3 docs.

#### Signature

```python
@property
def boto3_doc_link(self) -> str:
    ...
```

### Paginator().get_client_method

[Show source in paginator.py:43](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/paginator.py#L43)

Get `get_paginator` method for `Client`.

#### Signature

```python
def get_client_method(self) -> Method:
    ...
```

#### See also

- [Method](./method.md#method)
