# InternalImport

> Auto-generated documentation for [mypy_boto3_builder.type_annotations.internal_import](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/internal_import.py) module.

Wrapper for simple type annotations from this module.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Annotations](index.md#type-annotations) / InternalImport
    - [AliasInternalImport](#aliasinternalimport)
    - [InternalImport](#internalimport)
        - [InternalImport().copy](#internalimportcopy)
        - [InternalImport.get_alias](#internalimportget_alias)
        - [InternalImport().get_import_record](#internalimportget_import_record)
        - [InternalImport().render](#internalimportrender)

## AliasInternalImport

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/internal_import.py#L84)

```python
class AliasInternalImport(InternalImport):
    def __init__(name: str, service_name: ServiceName | None = None) -> None:
```

Internal import for safe local usages.

#### Arguments

- `name` - Import name.
- `service_name` - Service that import belongs to.

#### See also

- [InternalImport](#internalimport)

## InternalImport

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/internal_import.py#L10)

```python
class InternalImport(FakeAnnotation):
    def __init__(
        name: str,
        service_name: ServiceName | None = None,
        module_name: ServiceModuleName = ServiceModuleName.service_resource,
        stringify: bool = True,
        use_alias: bool = False,
    ) -> None:
```

Wrapper for simple type annotations from this module.

#### Arguments

- `name` - Import name.
- `service_name` - Service that import belongs to.
- `module_name` - Service module name.
- `stringify` - Convert type annotation to string to avoid circular deps.
- `use_alias` - Use name alias.

#### See also

- [FakeAnnotation](fake_annotation.md#fakeannotation)
- [ServiceModuleName](../enums/service_module_name.md#servicemodulename)

### InternalImport().copy

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/internal_import.py#L71)

```python
def copy() -> 'InternalImport':
```

Create a copy of type annotation wrapper.

### InternalImport.get_alias

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/internal_import.py#L36)

```python
@staticmethod
def get_alias(name: str) -> str:
```

Get import name alias.

#### Arguments

- `name` - Original name.

#### Returns

Name prefixed with underscore.

### InternalImport().get_import_record

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/internal_import.py#L65)

```python
def get_import_record() -> ImportRecord:
```

Get import record required for using type annotation.

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### InternalImport().render

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/internal_import.py#L49)

```python
def render(parent_name: str = '') -> str:
```

Render type annotation to a valid Python code for local usage.

#### Returns

A string with a valid type annotation.
