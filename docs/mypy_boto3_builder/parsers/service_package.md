# Service Package

> Auto-generated documentation for [mypy_boto3_builder.parsers.service_package](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/service_package.py) module.

Parser that produces `structures.ServiceModule`.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](index.md#parsers) / Service Package
    - [parse_service_package](#parse_service_package)

## parse_service_package

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/service_package.py#L21)

```python
def parse_service_package(
    session: Session,
    service_name: ServiceName,
    package_data: Type[BasePackageData],
) -> ServicePackage:
```

Extract all data from boto3 service package.

#### Arguments

- `session` - boto3 session.
- `service_name` - Target service name.
- `package_data` - Package data.

#### Returns

ServiceModule structure.

#### See also

- [ServiceName](../service_name.md#servicename)
- [ServicePackage](../structures/service_package.md#servicepackage)
