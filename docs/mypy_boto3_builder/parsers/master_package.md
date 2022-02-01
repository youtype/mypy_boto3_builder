# Master Package

> Auto-generated documentation for [mypy_boto3_builder.parsers.master_package](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/master_package.py) module.

Parser that produces `structures.MasterPackage`.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](index.md#parsers) / Master Package
    - [parse_master_package](#parse_master_package)

## parse_master_package

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/master_package.py#L13)

```python
def parse_master_package(
    session: Session,
    service_names: Iterable[ServiceName],
) -> MasterPackage:
```

Parse data for master package.

#### Arguments

- `session` - boto3 session.
- `service_names` - All available service names.

#### Returns

MasterPackage structure.

#### See also

- [MasterPackage](../structures/master_package.md#masterpackage)
