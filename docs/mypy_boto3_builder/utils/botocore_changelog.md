# BotocoreChangelog

> Auto-generated documentation for [mypy_boto3_builder.utils.botocore_changelog](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/utils/botocore_changelog.py) module.

Parser for boto3 changelog.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Utils](index.md#utils) / BotocoreChangelog
    - [BotocoreChangelog](#botocorechangelog)
        - [BotocoreChangelog().get_updated_service_names](#botocorechangelogget_updated_service_names)

## BotocoreChangelog

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/utils/botocore_changelog.py#L10)

```python
class BotocoreChangelog():
```

Parser for boto3 changelog.

### BotocoreChangelog().get_updated_service_names

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/utils/botocore_changelog.py#L36)

```python
def get_updated_service_names(version: str) -> list[str]:
```

Get a list of service names updated in `version` release.
