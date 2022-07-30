# Boto3 Stubs Package

[mypy-boto3-builder Index](../../README.md#mypy-boto3-builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Parsers](./index.md#parsers) /
Boto3 Stubs Package

> Auto-generated documentation for [mypy_boto3_builder.parsers.boto3_stubs_package](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/boto3_stubs_package.py) module.

- [Boto3 Stubs Package](#boto3-stubs-package)
  - [parse_boto3_stubs_package](#parse_boto3_stubs_package)

## parse_boto3_stubs_package

[Show source in boto3_stubs_package.py:25](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/boto3_stubs_package.py#L25)

Parse data for boto3-stubs package.

#### Arguments

- `session` - boto3 session
- `service_names` - All available service names
- `package_data` - Package data

#### Returns

Boto3StubsPackage structure.

#### Signature

```python
def parse_boto3_stubs_package(
    session: Session,
    service_names: Iterable[ServiceName],
    package_data: type[BasePackageData],
) -> Boto3StubsPackage:
    ...
```

#### See also

- [BasePackageData](../package_data.md#basepackagedata)
- [Boto3StubsPackage](../structures/boto3_stubs_package.md#boto3stubspackage)
- [ServiceName](../service_name.md#servicename)


