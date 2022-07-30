# BotocoreChangelog

[mypy-boto3-builder Index](../../README.md#mypy-boto3-builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Utils](./index.md#utils) /
BotocoreChangelog

> Auto-generated documentation for [mypy_boto3_builder.utils.botocore_changelog](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/botocore_changelog.py) module.

- [BotocoreChangelog](#botocorechangelog)
  - [BotocoreChangelog](#botocorechangelog-1)
    - [BotocoreChangelog().get_updated_service_names](#botocorechangelog()get_updated_service_names)

## BotocoreChangelog

[Show source in botocore_changelog.py:10](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/botocore_changelog.py#L10)

Parser for boto3 changelog.

#### Signature

```python
class BotocoreChangelog:
    ...
```

### BotocoreChangelog().get_updated_service_names

[Show source in botocore_changelog.py:37](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/botocore_changelog.py#L37)

Get a list of service names updated in `version` release.

#### Signature

```python
def get_updated_service_names(self, version: str) -> list[str]:
    ...
```


