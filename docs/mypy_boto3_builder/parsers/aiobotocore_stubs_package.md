# Aiobotocore Stubs Package

> Auto-generated documentation for [mypy_boto3_builder.parsers.aiobotocore_stubs_package](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/aiobotocore_stubs_package.py) module.

Parser that produces `structures.AioBotocoreStubsPackage`.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](index.md#parsers) / Aiobotocore Stubs Package
    - [parse_aiobotocore_stubs_package](#parse_aiobotocore_stubs_package)

## parse_aiobotocore_stubs_package

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/aiobotocore_stubs_package.py#L23)

```python
def parse_aiobotocore_stubs_package(
    session: Session,
    service_names: Iterable[ServiceName],
    package_data: type[BasePackageData],
) -> AioBotocoreStubsPackage:
```

Parse data for types-aiobotocore package.

#### Arguments

- `session` - boto3 session
- `service_names` - All available service names
- `package_data` - Package data

#### Returns

AioBotocoreStubsPackage structure.

#### See also

- [AioBotocoreStubsPackage](../structures/aiobotocore_stubs_package.md#aiobotocorestubspackage)
- [BasePackageData](../package_data.md#basepackagedata)
- [ServiceName](../service_name.md#servicename)
