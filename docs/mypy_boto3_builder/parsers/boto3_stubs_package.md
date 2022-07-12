# Boto3 Stubs Package

> Auto-generated documentation for [mypy_boto3_builder.parsers.boto3_stubs_package](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/boto3_stubs_package.py) module.

Parser that produces `structures.Boto3StubsPackage`.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](index.md#parsers) / Boto3 Stubs Package
    - [parse_boto3_stubs_package](#parse_boto3_stubs_package)

## parse_boto3_stubs_package

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/boto3_stubs_package.py#L25)

```python
def parse_boto3_stubs_package(
    session: Session,
    service_names: Iterable[ServiceName],
    package_data: type[BasePackageData],
) -> Boto3StubsPackage:
```

Parse data for boto3_stubs package.

#### Arguments

- `session` - boto3 session.
- `service_names` - All available service names.

#### Returns

Boto3StubsPackage structure.

#### See also

- [BasePackageData](../package_data.md#basepackagedata)
- [Boto3StubsPackage](../structures/boto3_stubs_package.md#boto3stubspackage)
- [ServiceName](../service_name.md#servicename)
