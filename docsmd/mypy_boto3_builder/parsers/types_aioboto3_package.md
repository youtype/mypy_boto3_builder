# Types Aioboto3 Package

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Parsers](./index.md#parsers) /
Types Aioboto3 Package

> Auto-generated documentation for [mypy_boto3_builder.parsers.types_aioboto3_package](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/types_aioboto3_package.py) module.

## parse_types_aioboto3_package

[Show source in types_aioboto3_package.py:24](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/types_aioboto3_package.py#L24)

Parse data for types-aioboto3 package.

#### Arguments

- `session` - boto3 session
- `service_names` - All available service names
- `package_data` - Package data

#### Returns

AioBotocoreStubsPackage structure.

#### Signature

```python
def parse_types_aioboto3_package(
    session: Session,
    service_names: Iterable[ServiceName],
    package_data: type[BasePackageData],
) -> TypesAioBoto3Package:
    ...
```

#### See also

- [BasePackageData](../package_data.md#basepackagedata)
- [ServiceName](../service_name.md#servicename)
- [TypesAioBoto3Package](../structures/types_aioboto3_package.md#typesaioboto3package)
