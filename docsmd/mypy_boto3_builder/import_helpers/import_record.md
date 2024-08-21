# ImportRecord

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Import Helpers](./index.md#import-helpers) / ImportRecord

> Auto-generated documentation for [mypy_boto3_builder.import_helpers.import_record](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py) module.

## ImportRecord

[Show source in import_record.py:16](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L16)

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
        self,
        source: ImportString,
        name: str = "",
        alias: str = "",
        min_version: tuple[int, ...] | None = None,
        fallback: Self | None = None,
    ) -> None: ...
```

#### See also

- [ImportString](./import_string.md#importstring)

### ImportRecord().__bool__

[Show source in import_record.py:48](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L48)

Whether import record is an empty string.

#### Signature

```python
def __bool__(self) -> bool: ...
```

### ImportRecord().__eq__

[Show source in import_record.py:94](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L94)

Whether two import records produce the same render.

#### Signature

```python
def __eq__(self, other: object) -> bool: ...
```

### ImportRecord().__gt__

[Show source in import_record.py:103](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L103)

Compare two import records for sorting.

Emulates `isort` logic.

#### Signature

```python
def __gt__(self: Self, other: Self) -> bool: ...
```

### ImportRecord().__hash__

[Show source in import_record.py:88](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L88)

Calculate hash value based on source, name and alias.

#### Signature

```python
def __hash__(self) -> int: ...
```

### ImportRecord().__str__

[Show source in import_record.py:82](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L82)

Render as a valid Python import statement.

#### Signature

```python
def __str__(self) -> str: ...
```

### ImportRecord.empty

[Show source in import_record.py:60](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L60)

Whether import record is an empty string.

#### Signature

```python
@classmethod
def empty(cls: type[Self]) -> Self: ...
```

### ImportRecord().get_local_name

[Show source in import_record.py:132](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L132)

Get local import name.

#### Signature

```python
def get_local_name(self) -> str: ...
```

### ImportRecord().is_builtins

[Show source in import_record.py:138](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L138)

Whether import is from Python `builtins` module.

#### Signature

```python
def is_builtins(self) -> bool: ...
```

### ImportRecord().is_empty

[Show source in import_record.py:54](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L54)

Whether import record is an empty string.

#### Signature

```python
def is_empty(self) -> bool: ...
```

### ImportRecord().is_local

[Show source in import_record.py:159](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L159)

Whether import is from local module.

#### Signature

```python
def is_local(self) -> bool: ...
```

### ImportRecord().is_third_party

[Show source in import_record.py:150](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L150)

Whether import is from 3rd party module.

#### Signature

```python
def is_third_party(self) -> bool: ...
```

### ImportRecord().is_type_defs

[Show source in import_record.py:144](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L144)

Whether import is from `type_defs` module.

#### Signature

```python
def is_type_defs(self) -> bool: ...
```

### ImportRecord().needs_sys_fallback

[Show source in import_record.py:177](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L177)

Whether ImportString requires `sys` module.

#### Signature

```python
def needs_sys_fallback(self) -> bool: ...
```

### ImportRecord().render

[Show source in import_record.py:67](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L67)

Get rendered string.

#### Signature

```python
def render(self) -> str: ...
```
