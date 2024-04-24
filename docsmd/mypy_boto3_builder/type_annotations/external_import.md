# ExternalImport

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Annotations](./index.md#type-annotations) / ExternalImport

> Auto-generated documentation for [mypy_boto3_builder.type_annotations.external_import](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/external_import.py) module.

## ExternalImport

[Show source in external_import.py:14](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/external_import.py#L14)

Wrapper for type annotations imported from 3rd party libraries, like `boto3.service.Service`.

#### Arguments

- `source` - Module import string.
- `name` - Import name.
- `alias` - Import local name.
- `safe` - Whether import is wrapped in try-except.

#### Signature

```python
class ExternalImport(FakeAnnotation):
    def __init__(
        self, source: ImportString, name: str = "", alias: str = "", safe: bool = False
    ) -> None: ...
```

#### See also

- [FakeAnnotation](./fake_annotation.md#fakeannotation)
- [ImportString](../import_helpers/import_string.md#importstring)

### ExternalImport().__copy__

[Show source in external_import.py:95](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/external_import.py#L95)

Create a copy of type annotation wrapper.

#### Signature

```python
def __copy__(self: Self) -> Self: ...
```

### ExternalImport().__hash__

[Show source in external_import.py:74](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/external_import.py#L74)

Calcualte hash value based on import record.

#### Signature

```python
def __hash__(self) -> int: ...
```

### ExternalImport()._get_import_records

[Show source in external_import.py:89](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/external_import.py#L89)

Get import record required for using type annotation.

#### Signature

```python
def _get_import_records(self) -> set[ImportRecord]: ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### ExternalImport().copy_from

[Show source in external_import.py:101](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/external_import.py#L101)

Copy all fileds from another instance.

#### Signature

```python
def copy_from(self: Self, other: Self) -> None: ...
```

### ExternalImport.from_class

[Show source in external_import.py:37](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/external_import.py#L37)

Create an instance from an imported class.

#### Arguments

- `value` - Any Class.
- `alias` - Local name.
- `safe` - Whether import is wrapped in try-except.

#### Signature

```python
@classmethod
def from_class(
    cls: type[Self], obj: type, alias: str = "", safe: bool = False
) -> Self: ...
```

### ExternalImport().import_record

[Show source in external_import.py:59](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/external_import.py#L59)

Get import record required for using type annotation.

#### Signature

```python
@property
def import_record(self) -> ImportRecord: ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### ExternalImport().render

[Show source in external_import.py:80](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/external_import.py#L80)

Get string with local name to use.

#### Returns

Import record local name.

#### Signature

```python
def render(self) -> str: ...
```
