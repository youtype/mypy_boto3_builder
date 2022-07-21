# InternalImport

[mypy-boto3-builder Index](../../README.md#mypy-boto3-builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Type Annotations](./index.md#type-annotations) /
InternalImport

> Auto-generated documentation for [mypy_boto3_builder.type_annotations.internal_import](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/internal_import.py) module.

- [InternalImport](#internalimport)
  - [AliasInternalImport](#aliasinternalimport)
  - [InternalImport](#internalimport-1)
    - [InternalImport().copy](#internalimport()copy)
    - [InternalImport.get_alias](#internalimportget_alias)
    - [InternalImport().get_import_record](#internalimport()get_import_record)
    - [InternalImport().render](#internalimport()render)

## AliasInternalImport

[Show source in internal_import.py:84](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/internal_import.py#L84)

Internal import for safe local usages.

#### Arguments

- `name` - Import name.
- `service_name` - Service that import belongs to.

#### Signature

```python
class AliasInternalImport(InternalImport):
    def __init__(self, name: str, service_name: ServiceName | None = None) -> None:
        ...
```

#### See also

- [InternalImport](#internalimport)



## InternalImport

[Show source in internal_import.py:10](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/internal_import.py#L10)

Wrapper for simple type annotations from this module.

#### Arguments

- `name` - Import name.
- `service_name` - Service that import belongs to.
- `module_name` - Service module name.
- `stringify` - Convert type annotation to string to avoid circular deps.
- `use_alias` - Use name alias.

#### Signature

```python
class InternalImport(FakeAnnotation):
    def __init__(
        self,
        name: str,
        service_name: ServiceName | None = None,
        module_name: ServiceModuleName = ServiceModuleName.service_resource,
        stringify: bool = True,
        use_alias: bool = False,
    ) -> None:
        ...
```

#### See also

- [FakeAnnotation](./fake_annotation.md#fakeannotation)
- [ServiceModuleName](../enums/service_module_name.md#servicemodulename)

### InternalImport().copy

[Show source in internal_import.py:71](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/internal_import.py#L71)

Create a copy of type annotation wrapper.

#### Signature

```python
def copy(self) -> "InternalImport":
    ...
```

### InternalImport.get_alias

[Show source in internal_import.py:36](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/internal_import.py#L36)

Get import name alias.

#### Arguments

- `name` - Original name.

#### Returns

Name prefixed with underscore.

#### Signature

```python
@staticmethod
def get_alias(name: str) -> str:
    ...
```

### InternalImport().get_import_record

[Show source in internal_import.py:65](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/internal_import.py#L65)

Get import record required for using type annotation.

#### Signature

```python
def get_import_record(self) -> ImportRecord:
    ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### InternalImport().render

[Show source in internal_import.py:49](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/internal_import.py#L49)

Render type annotation to a valid Python code for local usage.

#### Returns

A string with a valid type annotation.

#### Signature

```python
def render(self, parent_name: str = "") -> str:
    ...
```


