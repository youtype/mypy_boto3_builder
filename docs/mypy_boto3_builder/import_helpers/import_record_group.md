# ImportRecordGroup

> Auto-generated documentation for [mypy_boto3_builder.import_helpers.import_record_group](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/import_helpers/import_record_group.py) module.

Grouped by `source` import records for nicer rendering.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Import Helpers](index.md#import-helpers) / ImportRecordGroup
    - [ImportRecordGroup](#importrecordgroup)
        - [ImportRecordGroup.from_import_records](#importrecordgroupfrom_import_records)
        - [ImportRecordGroup().is_builtins](#importrecordgroupis_builtins)
        - [ImportRecordGroup().render](#importrecordgrouprender)

## ImportRecordGroup

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/import_helpers/import_record_group.py#L10)

```python
class ImportRecordGroup():
    def __init__(
        source: ImportString,
        import_records: Iterable[ImportRecord],
    ) -> None:
```

Grouped by `source` import records for nicer rendering.

#### Arguments

- `source` - Common source for import records.
- `import_records` - Grouped import records.

#### See also

- [ImportString](import_string.md#importstring)

### ImportRecordGroup.from_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/import_helpers/import_record_group.py#L25)

```python
@classmethod
def from_import_records(
    import_records: Iterable[ImportRecord],
) -> List['ImportRecordGroup']:
```

Get groups from `ImportRecord` list.

#### Arguments

- `import_records` - Import records list.

#### Returns

A list of generated [ImportRecordGroup](#importrecordgroup).

### ImportRecordGroup().is_builtins

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/import_helpers/import_record_group.py#L63)

```python
def is_builtins() -> bool:
```

Whether imports are from builtins.

### ImportRecordGroup().render

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/import_helpers/import_record_group.py#L69)

```python
def render() -> str:
```

Render to string.

#### Returns

A valid Python import records group.
