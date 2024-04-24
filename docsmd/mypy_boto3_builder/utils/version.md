# Version

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Utils](./index.md#utils) / Version

> Auto-generated documentation for [mypy_boto3_builder.utils.version](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/version.py) module.

## get_aioboto3_version

[Show source in version.py:77](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/version.py#L77)

Get aioboto3 package version.

#### Signature

```python
def get_aioboto3_version() -> str: ...
```



## get_aiobotocore_version

[Show source in version.py:66](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/version.py#L66)

Get aiobotocore package version.

#### Signature

```python
def get_aiobotocore_version() -> str: ...
```



## get_boto3_version

[Show source in version.py:55](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/version.py#L55)

Get boto3 package version.

#### Signature

```python
def get_boto3_version() -> str: ...
```



## get_botocore_version

[Show source in version.py:44](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/version.py#L44)

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

[Show source in version.py:37](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/version.py#L37)

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
