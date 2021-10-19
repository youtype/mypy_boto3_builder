# Client

> Auto-generated documentation for [mypy_boto3_builder.structures.client](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/client.py) module.

Boto3 Client.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / Client
    - [Client](#client)
        - [Client().\_\_hash\_\_](#client__hash__)
        - [Client().boto3_doc_link](#clientboto3_doc_link)
        - [Client().docstring](#clientdocstring)
        - [Client().get_all_names](#clientget_all_names)
        - [Client.get_class_name](#clientget_class_name)
        - [Client().get_exceptions_property](#clientget_exceptions_property)
        - [Client().get_required_import_records](#clientget_required_import_records)
        - [Client().own_methods](#clientown_methods)

## Client

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/client.py#L21)

```python
class Client(ClassRecord):
    def __init__(
        name: str,
        service_name: ServiceName,
        boto3_client: BaseClient,
    ) -> None:
```

Boto3 Client.

#### See also

- [ClassRecord](class_record.md#classrecord)
- [ServiceName](../service_name.md#servicename)

### Client().\_\_hash\_\_

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/client.py#L57)

```python
def __hash__() -> int:
```

Calculate hash from client service name.

### Client().boto3_doc_link

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/client.py#L70)

```python
@property
def boto3_doc_link() -> str:
```

List to boto3 docs page.

### Client().docstring

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/client.py#L77)

```python
@property
def docstring() -> str:
```

Class docstring.

### Client().get_all_names

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/client.py#L89)

```python
def get_all_names() -> list[str]:
```

Get a list of names for `__all__` statement.

### Client.get_class_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/client.py#L63)

```python
@staticmethod
def get_class_name(service_name: ServiceName) -> str:
```

Get class name for ServiceName.

#### See also

- [ServiceName](../service_name.md#servicename)

### Client().get_exceptions_property

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/client.py#L104)

```python
def get_exceptions_property() -> Method:
```

Generate Client exceptions property.

#### See also

- [Method](method.md#method)

### Client().get_required_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/client.py#L123)

```python
def get_required_import_records() -> set[ImportRecord]:
```

Extract import records from required type annotations.

### Client().own_methods

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/client.py#L95)

```python
@property
def own_methods() -> Iterator[Method]:
```

Get a list of auto-generated methods.
