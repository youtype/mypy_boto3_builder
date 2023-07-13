# PyPIManager

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Utils](./index.md#utils) /
PyPIManager

> Auto-generated documentation for [mypy_boto3_builder.utils.pypi_manager](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/pypi_manager.py) module.

## PyPIManager

[Show source in pypi_manager.py:11](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/pypi_manager.py#L11)

Version manager for PyPI packages.

#### Arguments

- `package` - PyPI package name

#### Signature

```python
class PyPIManager:
    def __init__(self, package: str) -> None:
        ...
```

### PyPIManager().get_next_version

[Show source in pypi_manager.py:35](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/pypi_manager.py#L35)

Get not existing version or closest not existing post-release.

#### Arguments

- `version` - Target version

#### Signature

```python
def get_next_version(self, version: str) -> str:
    ...
```

### PyPIManager().has_version

[Show source in pypi_manager.py:26](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/pypi_manager.py#L26)

Check if version is already uploaded to PyPI.

#### Arguments

- `version` - Target version

#### Signature

```python
def has_version(self, version: str) -> bool:
    ...
```
