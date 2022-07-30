# ImportRecord

[mypy-boto3-builder Index](../../README.md#mypy-boto3-builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Import Helpers](./index.md#import-helpers) /
ImportRecord

> Auto-generated documentation for [mypy_boto3_builder.import_helpers.import_record](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py) module.

- [ImportRecord](#importrecord)
  - [ImportRecord](#importrecord-1)
    - [ImportRecord.empty](#importrecordempty)
    - [ImportRecord().get_external](#importrecord()get_external)
    - [ImportRecord().get_local_name](#importrecord()get_local_name)
    - [ImportRecord().is_builtins](#importrecord()is_builtins)
    - [ImportRecord().is_local](#importrecord()is_local)
    - [ImportRecord().is_standalone](#importrecord()is_standalone)
    - [ImportRecord().is_third_party](#importrecord()is_third_party)
    - [ImportRecord().is_type_defs](#importrecord()is_type_defs)
    - [ImportRecord().needs_sys_fallback](#importrecord()needs_sys_fallback)
    - [ImportRecord().render](#importrecord()render)

## ImportRecord

[Show source in import_record.py:13](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L13)

Helper for Python import strings.

#### Arguments

- `source` - Source of import.
- `name` - Import name.
- `alias` - Import local name.
- `min_version` - Minimum Python version, used for fallback.
- `fallback` - Fallback ImportRecord.

#### Signature

```python
class ImportRecord:
    def __init__(
        self: _R,
        source: ImportString,
        name: str = "",
        alias: str = "",
        min_version: tuple[int, ...] | None = (3, 8),
        fallback: _R | None = None,
    ) -> None:
        ...
```

#### See also

- [ImportString](./import_string.md#importstring)

### ImportRecord.empty

[Show source in import_record.py:48](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L48)

Whether import record is an empty string.

#### Signature

```python
@classmethod
def empty(cls: type[_R]) -> _R:
    ...
```

### ImportRecord().get_external

[Show source in import_record.py:161](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L161)

Get itself.

Overriden by `InternalImportRecord`.

#### Signature

```python
def get_external(self, module_name: str) -> "ImportRecord":
    ...
```

### ImportRecord().get_local_name

[Show source in import_record.py:115](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L115)

Get local import name.

#### Signature

```python
def get_local_name(self) -> str:
    ...
```

### ImportRecord().is_builtins

[Show source in import_record.py:121](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L121)

Whether import is from Python `builtins` module.

#### Signature

```python
def is_builtins(self) -> bool:
    ...
```

### ImportRecord().is_local

[Show source in import_record.py:143](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L143)

Whether import is from local module.

#### Signature

```python
def is_local(self) -> bool:
    ...
```

### ImportRecord().is_standalone

[Show source in import_record.py:169](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L169)

Whether import record should not be grouped.

#### Signature

```python
def is_standalone(self) -> bool:
    ...
```

### ImportRecord().is_third_party

[Show source in import_record.py:133](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L133)

Whether import is from 3rd party module.

#### Signature

```python
def is_third_party(self) -> bool:
    ...
```

### ImportRecord().is_type_defs

[Show source in import_record.py:127](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L127)

Whether import is from `type_defs` module.

#### Signature

```python
def is_type_defs(self) -> bool:
    ...
```

### ImportRecord().needs_sys_fallback

[Show source in import_record.py:178](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L178)

Whether ImportString requires `sys` module.

#### Signature

```python
def needs_sys_fallback(self) -> bool:
    ...
```

### ImportRecord().render

[Show source in import_record.py:55](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L55)

Get rendered string.

#### Signature

```python
def render(self) -> str:
    ...
```


