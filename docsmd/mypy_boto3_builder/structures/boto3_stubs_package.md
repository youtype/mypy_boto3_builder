# Boto3StubsPackage

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Structures](./index.md#structures) /
Boto3StubsPackage

> Auto-generated documentation for [mypy_boto3_builder.structures.boto3_stubs_package](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/boto3_stubs_package.py) module.

## Boto3StubsPackage

[Show source in boto3_stubs_package.py:17](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/boto3_stubs_package.py#L17)

Structure for boto3-stubs module.

#### Signature

```python
class Boto3StubsPackage(Package):
    def __init__(
        self,
        data: type[BasePackageData],
        session_class: ClassRecord | None = None,
        service_names: Iterable[ServiceName] = (),
        service_packages: Iterable[ServicePackage] = (),
        init_functions: Iterable[Function] = (),
        literals: Iterable[TypeLiteral] = (),
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

[Show source in boto3_stubs_package.py:38](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/boto3_stubs_package.py#L38)

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

[Show source in boto3_stubs_package.py:66](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/boto3_stubs_package.py#L66)

Get names for `__all__` directive.

#### Signature

```python
def get_all_names(self) -> list[str]:
    ...
```

### Boto3StubsPackage().get_init_required_import_records

[Show source in boto3_stubs_package.py:49](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/boto3_stubs_package.py#L49)

Get import records for `__init__.py[i]`.

#### Signature

```python
def get_init_required_import_records(self) -> list[ImportRecord]:
    ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### Boto3StubsPackage().get_session_required_import_records

[Show source in boto3_stubs_package.py:59](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/boto3_stubs_package.py#L59)

Get import records for `session.py[i]`.

#### Signature

```python
def get_session_required_import_records(self) -> list[ImportRecord]:
    ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)
