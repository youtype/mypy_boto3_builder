# InternalImportRecord

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Import Helpers](./index.md#import-helpers) /
InternalImportRecord

> Auto-generated documentation for [mypy_boto3_builder.import_helpers.internal_import_record](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/internal_import_record.py) module.

## InternalImportRecord

[Show source in internal_import_record.py:9](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/internal_import_record.py#L9)

Helper for Python import strings with not set master module name.

#### Arguments

- `service_module_name` - Service module name.
- `name` - Import name.
- `alias` - Import local name.

#### Signature

```python
class InternalImportRecord(ImportRecord):
    def __init__(
        self, service_module_name: ServiceModuleName, name: str = "", alias: str = ""
    ):
        ...
```

#### See also

- [ImportRecord](./import_record.md#importrecord)
- [ServiceModuleName](../enums/service_module_name.md#servicemodulename)

### InternalImportRecord().get_external

[Show source in internal_import_record.py:24](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/internal_import_record.py#L24)

Get full import record with `module_name` set as master module.

#### Arguments

- `module_name` - Master module import string.

#### Returns

A new non-internal ImportRecord.

#### Signature

```python
def get_external(self, module_name: str) -> ImportRecord:
    ...
```

#### See also

- [ImportRecord](./import_record.md#importrecord)



