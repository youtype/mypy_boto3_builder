# ImportRecord

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Import Helpers](./index.md#import-helpers) / ImportRecord

> Auto-generated documentation for [mypy_boto3_builder.import_helpers.import_record](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py) module.

## ImportRecord

[Show source in import_record.py:18](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L18)

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
        min_version: tuple[int, ...] | None = None,
        fallback: _R | None = None,
    ) -> None: ...
```

#### See also

- [ImportString](./import_string.md#importstring)

### ImportRecord.empty

[Show source in import_record.py:59](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L59)

Whether import record is an empty string.

#### Signature

```python
@classmethod
def empty(cls) -> Self: ...
```

### ImportRecord().get_local_name

[Show source in import_record.py:117](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L117)

Get local import name.

#### Signature

```python
def get_local_name(self) -> str: ...
```

### ImportRecord().is_builtins

[Show source in import_record.py:123](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L123)

Whether import is from Python `builtins` module.

#### Signature

```python
def is_builtins(self) -> bool: ...
```

### ImportRecord().is_empty

[Show source in import_record.py:53](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L53)

Whether import record is an empty string.

#### Signature

```python
def is_empty(self) -> bool: ...
```

### ImportRecord().is_local

[Show source in import_record.py:144](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L144)

Whether import is from local module.

#### Signature

```python
def is_local(self) -> bool: ...
```

### ImportRecord().is_third_party

[Show source in import_record.py:135](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L135)

Whether import is from 3rd party module.

#### Signature

```python
def is_third_party(self) -> bool: ...
```

### ImportRecord().is_type_defs

[Show source in import_record.py:129](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L129)

Whether import is from `type_defs` module.

#### Signature

```python
def is_type_defs(self) -> bool: ...
```

### ImportRecord().needs_sys_fallback

[Show source in import_record.py:162](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L162)

Whether ImportString requires `sys` module.

#### Signature

```python
def needs_sys_fallback(self) -> bool: ...
```

### ImportRecord().render

[Show source in import_record.py:66](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L66)

Get rendered string.

#### Signature

```python
def render(self) -> str: ...
```
