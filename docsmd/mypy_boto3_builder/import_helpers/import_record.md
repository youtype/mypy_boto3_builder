# ImportRecord

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Import Helpers](./index.md#import-helpers) / ImportRecord

> Auto-generated documentation for [mypy_boto3_builder.import_helpers.import_record](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py) module.

## ImportRecord

[Show source in import_record.py:15](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L15)

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

[Show source in import_record.py:47](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L47)

Whether import record is an empty string.

#### Signature

```python
def __bool__(self) -> bool: ...
```

### ImportRecord().__eq__

[Show source in import_record.py:93](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L93)

Whether two import records produce the same render.

#### Signature

```python
def __eq__(self, other: object) -> bool: ...
```

### ImportRecord().__gt__

[Show source in import_record.py:102](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L102)

Compare two import records for sorting.

Emulates `isort` logic.

#### Signature

```python
def __gt__(self: Self, other: Self) -> bool: ...
```

### ImportRecord().__hash__

[Show source in import_record.py:87](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L87)

Calculate hash value based on source, name and alias.

#### Signature

```python
def __hash__(self) -> int: ...
```

### ImportRecord().__str__

[Show source in import_record.py:81](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L81)

Render as a valid Python import statement.

#### Signature

```python
def __str__(self) -> str: ...
```

### ImportRecord.empty

[Show source in import_record.py:59](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L59)

Whether import record is an empty string.

#### Signature

```python
@classmethod
def empty(cls) -> Self: ...
```

### ImportRecord().get_local_name

[Show source in import_record.py:131](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L131)

Get local import name.

#### Signature

```python
def get_local_name(self) -> str: ...
```

### ImportRecord().is_builtins

[Show source in import_record.py:137](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L137)

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

[Show source in import_record.py:158](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L158)

Whether import is from local module.

#### Signature

```python
def is_local(self) -> bool: ...
```

### ImportRecord().is_third_party

[Show source in import_record.py:149](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L149)

Whether import is from 3rd party module.

#### Signature

```python
def is_third_party(self) -> bool: ...
```

### ImportRecord().is_type_defs

[Show source in import_record.py:143](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L143)

Whether import is from `type_defs` module.

#### Signature

```python
def is_type_defs(self) -> bool: ...
```

### ImportRecord().needs_sys_fallback

[Show source in import_record.py:176](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_record.py#L176)

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
