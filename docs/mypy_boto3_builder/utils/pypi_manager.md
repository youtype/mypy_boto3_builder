# PyPIManager

> Auto-generated documentation for [mypy_boto3_builder.utils.pypi_manager](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/pypi_manager.py) module.

Version manager for PyPI packages.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Utils](index.md#utils) / PyPIManager
    - [PyPIManager](#pypimanager)
        - [PyPIManager().get_next_version](#pypimanagerget_next_version)
        - [PyPIManager().has_version](#pypimanagerhas_version)

## PyPIManager

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/pypi_manager.py#L11)

```python
class PyPIManager():
    def __init__(package: str) -> None:
```

Version manager for PyPI packages.

#### Arguments

- `package` - PyPI package name

### PyPIManager().get_next_version

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/pypi_manager.py#L34)

```python
def get_next_version(version: str) -> str:
```

Get not existing version or closest not existing post-release.

#### Arguments

- `version` - Target version

### PyPIManager().has_version

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/pypi_manager.py#L25)

```python
def has_version(version: str) -> bool:
```

Check if version is already uploaded to PyPI.

#### Arguments

- `version` - Target version
