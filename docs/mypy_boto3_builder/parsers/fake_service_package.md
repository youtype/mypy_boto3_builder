# Fake Service Package

[mypy-boto3-builder Index](../../README.md#mypy-boto3-builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Parsers](./index.md#parsers) /
Fake Service Package

> Auto-generated documentation for [mypy_boto3_builder.parsers.fake_service_package](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/fake_service_package.py) module.

- [Fake Service Package](#fake-service-package)
  - [parse_fake_service_package](#parse_fake_service_package)

## parse_fake_service_package

[Show source in fake_service_package.py:19](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/fake_service_package.py#L19)

Create fake boto3 service module structure.

Used by stubs and master package.

#### Arguments

- `session` - boto3 session.
- `service_name` - Target service name.
- `package_data` - Package data.

#### Returns

ServiceModule structure.

#### Signature

```python
def parse_fake_service_package(
    session: Session, service_name: ServiceName, package_data: type[BasePackageData]
) -> ServicePackage:
    ...
```

#### See also

- [BasePackageData](../package_data.md#basepackagedata)
- [ServiceName](../service_name.md#servicename)
- [ServicePackage](../structures/service_package.md#servicepackage)


