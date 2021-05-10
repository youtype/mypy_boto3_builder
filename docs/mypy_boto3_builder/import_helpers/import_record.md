# ImportRecord

> Auto-generated documentation for [mypy_boto3_builder.import_helpers.import_record](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/import_helpers/import_record.py) module.

Helper for Python import strings.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Import Helpers](index.md#import-helpers) / ImportRecord
    - [ImportRecord](#importrecord)
        - [ImportRecord.empty](#importrecordempty)
        - [ImportRecord().get_external](#importrecordget_external)
        - [ImportRecord().get_local_name](#importrecordget_local_name)
        - [ImportRecord().is_builtins](#importrecordis_builtins)
        - [ImportRecord().is_local](#importrecordis_local)
        - [ImportRecord().is_standalone](#importrecordis_standalone)
        - [ImportRecord().is_third_party](#importrecordis_third_party)
        - [ImportRecord().is_type_defs](#importrecordis_type_defs)
        - [ImportRecord().render](#importrecordrender)

## ImportRecord

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/import_helpers/import_record.py#L10)

```python
class ImportRecord():
    def __init__(
        source: ImportString,
        name: str = '',
        alias: str = '',
        min_version: Tuple[(int, ...)] = (3, 8),
        fallback: Optional['ImportRecord'] = None,
    ) -> None:
```

Helper for Python import strings.

#### Arguments

- `source` - Source of import.
- `name` - Import name.
- `alias` - Import local name.
- `min_version` - Minimum Python version, used for fallback.
- `fallback` - Fallback ImportRecord.

#### See also

- [ImportString](import_string.md#importstring)

### ImportRecord.empty

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/import_helpers/import_record.py#L45)

```python
@classmethod
def empty() -> 'ImportRecord':
```

### ImportRecord().get_external

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/import_helpers/import_record.py#L149)

```python
def get_external(module_name: str) -> 'ImportRecord':
```

Get itself.

Overriden by `InternalImportRecord`.

### ImportRecord().get_local_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/import_helpers/import_record.py#L106)

```python
def get_local_name() -> str:
```

Get local import name.

### ImportRecord().is_builtins

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/import_helpers/import_record.py#L112)

```python
def is_builtins() -> bool:
```

Whether import is from Python `builtins` module.

### ImportRecord().is_local

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/import_helpers/import_record.py#L134)

```python
def is_local() -> bool:
```

Whether import is from local module.

### ImportRecord().is_standalone

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/import_helpers/import_record.py#L157)

```python
def is_standalone() -> bool:
```

Whether import record should not be grouped.

### ImportRecord().is_third_party

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/import_helpers/import_record.py#L124)

```python
def is_third_party() -> bool:
```

Whether import is from 3rd party module.

### ImportRecord().is_type_defs

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/import_helpers/import_record.py#L118)

```python
def is_type_defs() -> bool:
```

Whether import is from `type_defs` module.

### ImportRecord().render

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/import_helpers/import_record.py#L49)

```python
def render() -> str:
```
