# Fake Service Package

> Auto-generated documentation for [mypy_boto3_builder.parsers.fake_service_package](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/fake_service_package.py) module.

Fake parser that produces `structures.ServiceModule` for master module and stubs.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](index.md#parsers) / Fake Service Package
    - [parse_fake_service_package](#parse_fake_service_package)

## parse_fake_service_package

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/fake_service_package.py#L19)

```python
def parse_fake_service_package(
    session: Session,
    service_name: ServiceName,
    package_data: type[BasePackageData],
) -> ServicePackage:
```

Create fake boto3 service module structure.

Used by stubs and master package.

#### Arguments

- `session` - boto3 session.
- `service_name` - Target service name.
- `package_data` - Package data.

#### Returns

ServiceModule structure.

#### See also

- [BasePackageData](../package_data.md#basepackagedata)
- [ServiceName](../service_name.md#servicename)
- [ServicePackage](../structures/service_package.md#servicepackage)
