# Client

[mypy-boto3-builder Index](../../README.md#mypy-boto3-builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Structures](./index.md#structures) /
Client

> Auto-generated documentation for [mypy_boto3_builder.structures.client](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/client.py) module.

- [Client](#client)
  - [Client](#client-1)
    - [Client().__hash__](#client()__hash__)
    - [Client().boto3_doc_link](#client()boto3_doc_link)
    - [Client().get_all_names](#client()get_all_names)
    - [Client.get_class_name](#clientget_class_name)
    - [Client().get_example_method](#client()get_example_method)
    - [Client().get_exceptions_property](#client()get_exceptions_property)
    - [Client().get_required_import_records](#client()get_required_import_records)
    - [Client().own_methods](#client()own_methods)

## Client

[Show source in client.py:22](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/client.py#L22)

Boto3 Client.

#### Signature

```python
class Client(ClassRecord):
    def __init__(
        self, name: str, service_name: ServiceName, boto3_client: BaseClient
    ) -> None:
        ...
```

#### See also

- [ClassRecord](./class_record.md#classrecord)
- [ServiceName](../service_name.md#servicename)

### Client().__hash__

[Show source in client.py:58](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/client.py#L58)

Calculate hash from client service name.

#### Signature

```python
def __hash__(self) -> int:
    ...
```

### Client().boto3_doc_link

[Show source in client.py:71](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/client.py#L71)

List to boto3 docs page.

#### Signature

```python
@property
def boto3_doc_link(self) -> str:
    ...
```

### Client().get_all_names

[Show source in client.py:78](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/client.py#L78)

Get a list of names for `__all__` statement.

#### Signature

```python
def get_all_names(self) -> list[str]:
    ...
```

### Client.get_class_name

[Show source in client.py:64](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/client.py#L64)

Get class name for ServiceName.

#### Signature

```python
@staticmethod
def get_class_name(service_name: ServiceName) -> str:
    ...
```

#### See also

- [ServiceName](../service_name.md#servicename)

### Client().get_example_method

[Show source in client.py:120](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/client.py#L120)

Get a nice method with return TypedDict for documentation.

#### Signature

```python
def get_example_method(self) -> Method | None:
    ...
```

### Client().get_exceptions_property

[Show source in client.py:93](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/client.py#L93)

Generate Client exceptions property.

#### Signature

```python
def get_exceptions_property(self) -> Method:
    ...
```

#### See also

- [Method](./method.md#method)

### Client().get_required_import_records

[Show source in client.py:112](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/client.py#L112)

Extract import records from required type annotations.

#### Signature

```python
def get_required_import_records(self) -> set[ImportRecord]:
    ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### Client().own_methods

[Show source in client.py:84](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/client.py#L84)

Get a list of auto-generated methods.

#### Signature

```python
@property
def own_methods(self) -> Iterator[Method]:
    ...
```

#### See also

- [Method](./method.md#method)


