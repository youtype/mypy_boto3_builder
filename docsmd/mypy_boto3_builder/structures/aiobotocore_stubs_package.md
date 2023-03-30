# AioBotocoreStubsPackage

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Structures](./index.md#structures) /
AioBotocoreStubsPackage

> Auto-generated documentation for [mypy_boto3_builder.structures.aiobotocore_stubs_package](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/aiobotocore_stubs_package.py) module.

## AioBotocoreStubsPackage

[Show source in aiobotocore_stubs_package.py:16](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/aiobotocore_stubs_package.py#L16)

Structure for types-aiobotocore module.

#### Signature

```python
class AioBotocoreStubsPackage(Package):
    def __init__(
        self,
        data: type[BasePackageData],
        session_class: ClassRecord | None = None,
        service_names: Iterable[ServiceName] = (),
        service_packages: Iterable[ServicePackage] = (),
        init_functions: Iterable[Function] = (),
    ):
        ...
```

#### See also

- [BasePackageData](../package_data.md#basepackagedata)
- [Function](./function.md#function)
- [Package](./package.md#package)
- [ServiceName](../service_name.md#servicename)
- [ServicePackage](./service_package.md#servicepackage)

### AioBotocoreStubsPackage().essential_service_names

[Show source in aiobotocore_stubs_package.py:35](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/aiobotocore_stubs_package.py#L35)

Service names marked as essential.

#### Signature

```python
@property
def essential_service_names(self) -> list[ServiceName]:
    ...
```

#### See also

- [ServiceName](../service_name.md#servicename)

### AioBotocoreStubsPackage().get_all_names

[Show source in aiobotocore_stubs_package.py:54](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/aiobotocore_stubs_package.py#L54)

Get names for `__all__` directive.

#### Signature

```python
def get_all_names(self) -> list[str]:
    ...
```

### AioBotocoreStubsPackage().get_session_required_import_records

[Show source in aiobotocore_stubs_package.py:46](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/aiobotocore_stubs_package.py#L46)

Get import records for `session.py[i]`.

#### Signature

```python
def get_session_required_import_records(self) -> list[ImportRecord]:
    ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)
