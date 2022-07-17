# TypesAioBoto3Package

> Auto-generated documentation for [mypy_boto3_builder.structures.types_aioboto3_package](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/types_aioboto3_package.py) module.

Structure for types-aioboto3 module.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / TypesAioBoto3Package
    - [TypesAioBoto3Package](#typesaioboto3package)
        - [TypesAioBoto3Package().essential_service_names](#typesaioboto3packageessential_service_names)
        - [TypesAioBoto3Package().get_all_names](#typesaioboto3packageget_all_names)
        - [TypesAioBoto3Package().get_session_required_import_records](#typesaioboto3packageget_session_required_import_records)

## TypesAioBoto3Package

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/types_aioboto3_package.py#L17)

```python
class TypesAioBoto3Package(Package):
    def __init__(
        data: type[BasePackageData],
        session_class: ClassRecord | None = None,
        service_names: Iterable[ServiceName] = tuple(),
        service_packages: Iterable[ServicePackage] = tuple(),
    ):
```

Structure for types-aioboto3 module.

#### See also

- [BasePackageData](../package_data.md#basepackagedata)
- [Package](package.md#package)
- [ServiceName](../service_name.md#servicename)
- [ServicePackage](service_package.md#servicepackage)

### TypesAioBoto3Package().essential_service_names

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/types_aioboto3_package.py#L34)

```python
@property
def essential_service_names() -> list[ServiceName]:
```

Service names marked as essential.

#### See also

- [ServiceName](../service_name.md#servicename)

### TypesAioBoto3Package().get_all_names

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/types_aioboto3_package.py#L69)

```python
def get_all_names() -> list[str]:
```

Get names for `__all__` directive.

### TypesAioBoto3Package().get_session_required_import_records

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/types_aioboto3_package.py#L45)

```python
def get_session_required_import_records() -> list[ImportRecord]:
```

Get import reciords for `session.py[i]`.

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)
