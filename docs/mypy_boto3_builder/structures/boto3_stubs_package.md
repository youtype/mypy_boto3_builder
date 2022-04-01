# Boto3StubsPackage

> Auto-generated documentation for [mypy_boto3_builder.structures.boto3_stubs_package](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/boto3_stubs_package.py) module.

Structure for boto3-stubs module.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / Boto3StubsPackage
    - [Boto3StubsPackage](#boto3stubspackage)
        - [Boto3StubsPackage().essential_service_names](#boto3stubspackageessential_service_names)
        - [Boto3StubsPackage().get_all_names](#boto3stubspackageget_all_names)
        - [Boto3StubsPackage().get_init_required_import_records](#boto3stubspackageget_init_required_import_records)
        - [Boto3StubsPackage().get_session_required_import_records](#boto3stubspackageget_session_required_import_records)

## Boto3StubsPackage

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/boto3_stubs_package.py#L18)

```python
class Boto3StubsPackage(Package):
    def __init__(
        data: type[BasePackageData],
        session_class: ClassRecord | None = None,
        service_names: Iterable[ServiceName] = tuple(),
        service_packages: Iterable[ServicePackage] = tuple(),
        init_functions: Iterable[Function] = tuple(),
        literals: Iterable[TypeLiteral] = tuple(),
    ):
```

Structure for boto3-stubs module.

#### See also

- [BasePackageData](../package_data.md#basepackagedata)
- [Function](function.md#function)
- [Package](package.md#package)
- [ServiceName](../service_name.md#servicename)
- [ServicePackage](service_package.md#servicepackage)
- [TypeLiteral](../type_annotations/type_literal.md#typeliteral)

### Boto3StubsPackage().essential_service_names

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/boto3_stubs_package.py#L39)

```python
@property
def essential_service_names() -> list[ServiceName]:
```

Service names marked as essential.

#### See also

- [ServiceName](../service_name.md#servicename)

### Boto3StubsPackage().get_all_names

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/boto3_stubs_package.py#L113)

```python
def get_all_names() -> list[str]:
```

Get names for `__all__` directive.

### Boto3StubsPackage().get_init_required_import_records

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/boto3_stubs_package.py#L50)

```python
def get_init_required_import_records() -> list[ImportRecord]:
```

Get import records for `__init__.py[i]`.

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### Boto3StubsPackage().get_session_required_import_records

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/boto3_stubs_package.py#L70)

```python
def get_session_required_import_records() -> list[ImportRecord]:
```

Get import reciords for `session.py[i]`.

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)
