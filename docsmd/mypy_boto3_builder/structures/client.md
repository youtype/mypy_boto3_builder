# Client

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Structures](./index.md#structures) /
Client

> Auto-generated documentation for [mypy_boto3_builder.structures.client](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/client.py) module.

## Client

[Show source in client.py:20](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/client.py#L20)

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

[Show source in client.py:56](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/client.py#L56)

Calculate hash from client service name.

#### Signature

```python
def __hash__(self) -> int:
    ...
```

### Client().boto3_doc_link

[Show source in client.py:69](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/client.py#L69)

List to boto3 docs page.

#### Signature

```python
@property
def boto3_doc_link(self) -> str:
    ...
```

### Client().get_all_names

[Show source in client.py:76](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/client.py#L76)

Get a list of names for `__all__` statement.

#### Signature

```python
def get_all_names(self) -> list[str]:
    ...
```

### Client.get_class_name

[Show source in client.py:62](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/client.py#L62)

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

[Show source in client.py:118](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/client.py#L118)

Get a nice method with return TypedDict for documentation.

#### Signature

```python
def get_example_method(self) -> Method | None:
    ...
```

### Client().get_exceptions_property

[Show source in client.py:91](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/client.py#L91)

Generate Client exceptions property.

#### Signature

```python
def get_exceptions_property(self) -> Method:
    ...
```

#### See also

- [Method](./method.md#method)

### Client().get_required_import_records

[Show source in client.py:110](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/client.py#L110)

Extract import records from required type annotations.

#### Signature

```python
def get_required_import_records(self) -> set[ImportRecord]:
    ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### Client().own_methods

[Show source in client.py:82](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/client.py#L82)

Get a list of auto-generated methods.

#### Signature

```python
@property
def own_methods(self) -> Iterator[Method]:
    ...
```

#### See also

- [Method](./method.md#method)
