# Version

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Utils](./index.md#utils) / Version

> Auto-generated documentation for [mypy_boto3_builder.utils.version](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/version.py) module.

## bump_postrelease

[Show source in version.py:46](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/version.py#L46)

Bump postrelease version.

#### Signature

```python
def bump_postrelease(version: str) -> str: ...
```



## get_aioboto3_version

[Show source in version.py:89](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/version.py#L89)

Get aioboto3 package version.

#### Signature

```python
def get_aioboto3_version() -> str: ...
```



## get_aiobotocore_version

[Show source in version.py:78](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/version.py#L78)

Get aiobotocore package version.

#### Signature

```python
def get_aiobotocore_version() -> str: ...
```



## get_boto3_version

[Show source in version.py:67](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/version.py#L67)

Get boto3 package version.

#### Signature

```python
def get_boto3_version() -> str: ...
```



## get_botocore_version

[Show source in version.py:56](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/version.py#L56)

Get botocore package version.

#### Signature

```python
def get_botocore_version() -> str: ...
```



## get_builder_version

[Show source in version.py:13](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/version.py#L13)

Get program version.

#### Signature

```python
def get_builder_version() -> str: ...
```



## get_max_build_version

[Show source in version.py:38](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/version.py#L38)

Get min version build version by bumping minor.

#### Signature

```python
def get_max_build_version(version: str) -> str: ...
```



## get_min_build_version

[Show source in version.py:30](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/version.py#L30)

Get min version build version by setting micro to 0.

#### Signature

```python
def get_min_build_version(version: str) -> str: ...
```



## get_supported_python_versions

[Show source in version.py:23](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/version.py#L23)

Get supported python versions.

#### Signature

```python
def get_supported_python_versions() -> tuple[str, ...]: ...
```
