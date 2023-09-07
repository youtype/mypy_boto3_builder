# ServicePackageParser

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Parsers](./index.md#parsers) /
ServicePackageParser

> Auto-generated documentation for [mypy_boto3_builder.parsers.service_package_parser](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/service_package_parser.py) module.

## ServicePackageParser

[Show source in service_package_parser.py:25](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/service_package_parser.py#L25)

Parser that produces `structures.ServicePackage`.

#### Arguments

- `session` - boto3 session.
- `service_name` - Target service name.
- `package_data` - Package data.

#### Returns

ServiceModule structure.

#### Signature

```python
class ServicePackageParser:
    def __init__(
        self,
        session: Session,
        service_name: ServiceName,
        package_data: type[BasePackageData],
    ) -> None:
        ...
```

#### See also

- [BasePackageData](../package_data.md#basepackagedata)
- [ServiceName](../service_name.md#servicename)

### ServicePackageParser().parse

[Show source in service_package_parser.py:50](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/service_package_parser.py#L50)

Extract all data from boto3 service package.

#### Signature

```python
def parse(self) -> ServicePackage:
    ...
```

#### See also

- [ServicePackage](../structures/service_package.md#servicepackage)
