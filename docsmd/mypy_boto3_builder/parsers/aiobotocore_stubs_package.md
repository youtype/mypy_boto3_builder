# Aiobotocore Stubs Package

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Parsers](./index.md#parsers) /
Aiobotocore Stubs Package

> Auto-generated documentation for [mypy_boto3_builder.parsers.aiobotocore_stubs_package](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/aiobotocore_stubs_package.py) module.

## parse_aiobotocore_stubs_package

[Show source in aiobotocore_stubs_package.py:26](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/aiobotocore_stubs_package.py#L26)

Parse data for types-aiobotocore package.

#### Arguments

- `session` - boto3 session
- `service_names` - All available service names
- `package_data` - Package data

#### Returns

AioBotocoreStubsPackage structure.

#### Signature

```python
def parse_aiobotocore_stubs_package(
    session: Session,
    service_names: Iterable[ServiceName],
    package_data: type[BasePackageData],
) -> AioBotocoreStubsPackage: ...
```

#### See also

- [AioBotocoreStubsPackage](../structures/aiobotocore_stubs_package.md#aiobotocorestubspackage)
- [BasePackageData](../package_data.md#basepackagedata)
- [ServiceName](../service_name.md#servicename)
