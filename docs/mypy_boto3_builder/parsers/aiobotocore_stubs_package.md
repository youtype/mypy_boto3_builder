# Aiobotocore Stubs Package

> Auto-generated documentation for [mypy_boto3_builder.parsers.aiobotocore_stubs_package](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/aiobotocore_stubs_package.py) module.

Parser that produces `structures.AioBotocoreStubsPackage`.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](index.md#parsers) / Aiobotocore Stubs Package
    - [parse_aiobotocore_stubs_package](#parse_aiobotocore_stubs_package)

## parse_aiobotocore_stubs_package

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/aiobotocore_stubs_package.py#L24)

```python
def parse_aiobotocore_stubs_package(
    session: Session,
    service_names: Iterable[ServiceName],
) -> AioBotocoreStubsPackage:
```

Parse data for boto3_stubs package.

#### Arguments

- `session` - boto3 session.
- `service_names` - All available service names.

#### Returns

AioBotocoreStubsPackage structure.

#### See also

- [AioBotocoreStubsPackage](../structures/aiobotocore_stubs_package.md#aiobotocorestubspackage)
