# Waiter

> Auto-generated documentation for [mypy_boto3_builder.structures.waiter](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/waiter.py) module.

Boto3 client Waiter.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / Waiter
    - [Waiter](#waiter)
        - [Waiter().boto3_doc_link](#waiterboto3_doc_link)
        - [Waiter().get_client_method](#waiterget_client_method)

## Waiter

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/waiter.py#L18)

```python
class Waiter(ClassRecord):
    def __init__(name: str, waiter_name: str, service_name: ServiceName):
```

Boto3 client Waiter.

#### See also

- [ClassRecord](class_record.md#classrecord)
- [ServiceName](../service_name.md#servicename)

### Waiter().boto3_doc_link

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/waiter.py#L36)

```python
@property
def boto3_doc_link() -> str:
```

Link to waiter boto3 docs.

### Waiter().get_client_method

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/waiter.py#L43)

```python
def get_client_method() -> Method:
```

Get `get_waiter` method for `Client`.

#### See also

- [Method](method.md#method)
