# Master Package

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](./index.md#parsers) / Master Package

> Auto-generated documentation for [mypy_boto3_builder.parsers.master_package](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/master_package.py) module.

## parse_master_package

[Show source in master_package.py:17](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/master_package.py#L17)

Parse data for master package.

#### Arguments

- `session` - boto3 session.
- `service_names` - All available service names.

#### Returns

MasterPackage structure.

#### Signature

```python
def parse_master_package(
    session: Session, service_names: Iterable[ServiceName]
) -> MasterPackage: ...
```

#### See also

- [MasterPackage](../structures/master_package.md#masterpackage)
- [ServiceName](../service_name.md#servicename)
