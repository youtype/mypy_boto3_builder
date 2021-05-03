# Client

> Auto-generated documentation for [mypy_boto3_builder.structures.client](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/client.py) module.

Boto3 Client.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / Client
    - [Client](#client)
        - [Client().boto3_doc_link](#clientboto3_doc_link)
        - [Client().docstring](#clientdocstring)
        - [Client().get_all_names](#clientget_all_names)
        - [Client().own_methods](#clientown_methods)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/client.py#L18)

```python
class Client(ClassRecord):
    def __init__(
        name: str,
        service_name: ServiceName,
        boto3_client: BaseClient,
    ):
```

Boto3 Client.

#### See also

- [ClassRecord](class_record.md#classrecord)
- [ServiceName](../service_name.md#servicename)

### Client().boto3_doc_link

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/client.py#L56)

```python
@property
def boto3_doc_link() -> str:
```

### Client().docstring

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/client.py#L60)

```python
@property
def docstring() -> str:
```

### Client().get_all_names

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/client.py#L68)

```python
def get_all_names() -> List[str]:
```

### Client().own_methods

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/client.py#L71)

```python
@property
def own_methods() -> Iterator[Method]:
```
