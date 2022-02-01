# Boto3Changelog

> Auto-generated documentation for [mypy_boto3_builder.utils.boto3_changelog](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/boto3_changelog.py) module.

Parser for boto3 changelog.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Utils](index.md#utils) / Boto3Changelog
    - [Boto3Changelog](#boto3changelog)
        - [Boto3Changelog().get_updated_service_names](#boto3changelogget_updated_service_names)

## Boto3Changelog

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/boto3_changelog.py#L10)

```python
class Boto3Changelog():
```

Parser for boto3 changelog.

### Boto3Changelog().get_updated_service_names

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/boto3_changelog.py#L36)

```python
def get_updated_service_names(version: str) -> list[str]:
```

Get a list of service names updated in `version` release.
