# Boto3StubsPackage

[mypy-boto3-builder Index](../../README.md#mypy-boto3-builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Structures](./index.md#structures) /
Boto3StubsPackage

> Auto-generated documentation for [mypy_boto3_builder.structures.boto3_stubs_package](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/boto3_stubs_package.py) module.

- [Boto3StubsPackage](#boto3stubspackage)
  - [Boto3StubsPackage](#boto3stubspackage-1)
    - [Boto3StubsPackage().essential_service_names](#boto3stubspackage()essential_service_names)
    - [Boto3StubsPackage().get_all_names](#boto3stubspackage()get_all_names)
    - [Boto3StubsPackage().get_init_required_import_records](#boto3stubspackage()get_init_required_import_records)
    - [Boto3StubsPackage().get_session_required_import_records](#boto3stubspackage()get_session_required_import_records)

## Boto3StubsPackage

[Show source in boto3_stubs_package.py:18](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/boto3_stubs_package.py#L18)

Structure for boto3-stubs module.

#### Signature

```python
class Boto3StubsPackage(Package):
    def __init__(
        self,
        data: type[BasePackageData],
        session_class: ClassRecord | None = None,
        service_names: Iterable[ServiceName] = tuple(),
        service_packages: Iterable[ServicePackage] = tuple(),
        init_functions: Iterable[Function] = tuple(),
        literals: Iterable[TypeLiteral] = tuple(),
    ):
        ...
```

#### See also

- [BasePackageData](../package_data.md#basepackagedata)
- [Function](./function.md#function)
- [Package](./package.md#package)
- [ServiceName](../service_name.md#servicename)
- [ServicePackage](./service_package.md#servicepackage)
- [TypeLiteral](../type_annotations/type_literal.md#typeliteral)

### Boto3StubsPackage().essential_service_names

[Show source in boto3_stubs_package.py:39](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/boto3_stubs_package.py#L39)

Service names marked as essential.

#### Signature

```python
@property
def essential_service_names(self) -> list[ServiceName]:
    ...
```

#### See also

- [ServiceName](../service_name.md#servicename)

### Boto3StubsPackage().get_all_names

[Show source in boto3_stubs_package.py:113](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/boto3_stubs_package.py#L113)

Get names for `__all__` directive.

#### Signature

```python
def get_all_names(self) -> list[str]:
    ...
```

### Boto3StubsPackage().get_init_required_import_records

[Show source in boto3_stubs_package.py:50](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/boto3_stubs_package.py#L50)

Get import records for `__init__.py[i]`.

#### Signature

```python
def get_init_required_import_records(self) -> list[ImportRecord]:
    ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### Boto3StubsPackage().get_session_required_import_records

[Show source in boto3_stubs_package.py:70](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/boto3_stubs_package.py#L70)

Get import reciords for `session.py[i]`.

#### Signature

```python
def get_session_required_import_records(self) -> list[ImportRecord]:
    ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)


