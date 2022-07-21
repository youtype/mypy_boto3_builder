# ExternalImport

[mypy-boto3-builder Index](../../README.md#mypy-boto3-builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Type Annotations](./index.md#type-annotations) /
ExternalImport

> Auto-generated documentation for [mypy_boto3_builder.type_annotations.external_import](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/external_import.py) module.

- [ExternalImport](#externalimport)
  - [ExternalImport](#externalimport-1)
    - [ExternalImport().copy](#externalimport()copy)
    - [ExternalImport().get_import_record](#externalimport()get_import_record)
    - [ExternalImport().import_record](#externalimport()import_record)
    - [ExternalImport().render](#externalimport()render)

## ExternalImport

[Show source in external_import.py:9](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/external_import.py#L9)

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
    ) -> None:
        ...
```

#### See also

- [FakeAnnotation](./fake_annotation.md#fakeannotation)
- [ImportString](../import_helpers/import_string.md#importstring)

### ExternalImport().copy

[Show source in external_import.py:65](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/external_import.py#L65)

Create a copy of type annotation wrapper.

#### Signature

```python
def copy(self) -> "ExternalImport":
    ...
```

### ExternalImport().get_import_record

[Show source in external_import.py:59](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/external_import.py#L59)

Get import record required for using type annotation.

#### Signature

```python
def get_import_record(self) -> ImportRecord:
    ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### ExternalImport().import_record

[Show source in external_import.py:32](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/external_import.py#L32)

Get import record required for using type annotation.

#### Signature

```python
@property
def import_record(self) -> ImportRecord:
    ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### ExternalImport().render

[Show source in external_import.py:50](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/external_import.py#L50)

Get string with local name to use.

#### Returns

Import record local name.

#### Signature

```python
def render(self, parent_name: str = "") -> str:
    ...
```


