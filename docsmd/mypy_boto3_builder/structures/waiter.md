# Waiter

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](./index.md#structures) / Waiter

> Auto-generated documentation for [mypy_boto3_builder.structures.waiter](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/waiter.py) module.

## Waiter

[Show source in waiter.py:18](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/waiter.py#L18)

Boto3 client Waiter.

#### Signature

```python
class Waiter(ClassRecord):
    def __init__(self, name: str, waiter_name: str, service_name: ServiceName): ...
```

#### See also

- [ClassRecord](./class_record.md#classrecord)
- [ServiceName](../service_name.md#servicename)

### Waiter().boto3_doc_link

[Show source in waiter.py:36](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/waiter.py#L36)

Link to waiter boto3 docs.

#### Signature

```python
@property
def boto3_doc_link(self) -> str: ...
```

### Waiter().get_client_method

[Show source in waiter.py:43](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/waiter.py#L43)

Get `get_waiter` method for `Client`.

#### Signature

```python
def get_client_method(self) -> Method: ...
```

#### See also

- [Method](./method.md#method)
