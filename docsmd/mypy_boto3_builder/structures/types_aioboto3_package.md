# TypesAioBoto3Package

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Structures](./index.md#structures) /
TypesAioBoto3Package

> Auto-generated documentation for [mypy_boto3_builder.structures.types_aioboto3_package](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/types_aioboto3_package.py) module.

## TypesAioBoto3Package

[Show source in types_aioboto3_package.py:17](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/types_aioboto3_package.py#L17)

Structure for types-aioboto3 module.

#### Signature

```python
class TypesAioBoto3Package(Package):
    def __init__(
        self,
        data: type[BasePackageData],
        session_class: ClassRecord | None = None,
        service_names: Iterable[ServiceName] = (),
        service_packages: Iterable[ServicePackage] = (),
    ):
        ...
```

#### See also

- [BasePackageData](../package_data.md#basepackagedata)
- [Package](./package.md#package)
- [ServiceName](../service_name.md#servicename)
- [ServicePackage](./service_package.md#servicepackage)

### TypesAioBoto3Package().essential_service_names

[Show source in types_aioboto3_package.py:34](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/types_aioboto3_package.py#L34)

Service names marked as essential.

#### Signature

```python
@property
def essential_service_names(self) -> list[ServiceName]:
    ...
```

#### See also

- [ServiceName](../service_name.md#servicename)

### TypesAioBoto3Package().get_all_names

[Show source in types_aioboto3_package.py:70](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/types_aioboto3_package.py#L70)

Get names for `__all__` directive.

#### Signature

```python
def get_all_names(self) -> list[str]:
    ...
```

### TypesAioBoto3Package().get_session_required_import_records

[Show source in types_aioboto3_package.py:45](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/types_aioboto3_package.py#L45)

Get import reciords for `session.py[i]`.

#### Signature

```python
def get_session_required_import_records(self) -> list[ImportRecord]:
    ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)
