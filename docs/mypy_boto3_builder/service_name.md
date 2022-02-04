# ServiceName

> Auto-generated documentation for [mypy_boto3_builder.service_name](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/service_name.py) module.

Description for boto3 service.

- [mypy-boto3-builder](../README.md#mypy_boto3_builder) / [Modules](../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](index.md#mypy-boto3-builder) / ServiceName
    - [ServiceName](#servicename)
        - [ServiceName().aiobotocore_module_name](#servicenameaiobotocore_module_name)
        - [ServiceName().aiobotocore_pypi_name](#servicenameaiobotocore_pypi_name)
        - [ServiceName().boto3_doc_link](#servicenameboto3_doc_link)
        - [ServiceName().boto3_name](#servicenameboto3_name)
        - [ServiceName().extras_name](#servicenameextras_name)
        - [ServiceName().get_boto3_doc_link](#servicenameget_boto3_doc_link)
        - [ServiceName.get_md_doc_link](#servicenameget_md_doc_link)
        - [ServiceName().import_name](#servicenameimport_name)
        - [ServiceName().is_conda_forge_available](#servicenameis_conda_forge_available)
        - [ServiceName().is_essential](#servicenameis_essential)
        - [ServiceName().module_name](#servicenamemodule_name)
        - [ServiceName().pypi_name](#servicenamepypi_name)
        - [ServiceName().underscore_name](#servicenameunderscore_name)
    - [ServiceNameCatalog](#servicenamecatalog)
        - [ServiceNameCatalog.add](#servicenamecatalogadd)

## ServiceName

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/service_name.py#L20)

```python
class ServiceName():
    def __init__(name: str, class_name: str) -> None:
```

Description for boto3 service.

### ServiceName().aiobotocore_module_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/service_name.py#L90)

```python
@property
def aiobotocore_module_name() -> str:
```

Package name for given service for aiobotocore.

### ServiceName().aiobotocore_pypi_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/service_name.py#L104)

```python
@property
def aiobotocore_pypi_name() -> str:
```

Name of aiobotocore package on PyPI.

### ServiceName().boto3_doc_link

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/service_name.py#L130)

```python
@property
def boto3_doc_link() -> str:
```

Link to boto3 docs.

### ServiceName().boto3_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/service_name.py#L65)

```python
@property
def boto3_name() -> str:
```

Boto3 package name.

### ServiceName().extras_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/service_name.py#L111)

```python
@property
def extras_name() -> str:
```

Extras name for subpackage installation.

### ServiceName().get_boto3_doc_link

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/service_name.py#L140)

```python
def get_boto3_doc_link(*parts: str) -> str:
```

Get link to boto3 docs with anchor.

#### Arguments

- `parts` - Anchor parts

### ServiceName.get_md_doc_link

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/service_name.py#L149)

```python
@staticmethod
def get_md_doc_link(
    file: Literal[(
        'client',
        'service_resource',
        'waiters',
        'paginators',
        'type_defs',
        'literals',
    )],
    *parts: str,
) -> str:
```

Get link to MD docs with anchor.

#### Arguments

- `file` - HTML file name
- `parts` - Anchor parts

### ServiceName().import_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/service_name.py#L72)

```python
@property
def import_name() -> str:
```

Safe mudule import name.

### ServiceName().is_conda_forge_available

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/service_name.py#L124)

```python
def is_conda_forge_available() -> bool:
```

Whether service is available for `conda-forge`.

### ServiceName().is_essential

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/service_name.py#L118)

```python
def is_essential() -> bool:
```

Whether service is included to `boto3-stubs[essential]`.

### ServiceName().module_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/service_name.py#L83)

```python
@property
def module_name() -> str:
```

Package name for given service for boto3.

### ServiceName().pypi_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/service_name.py#L97)

```python
@property
def pypi_name() -> str:
```

Name of boto3 package on PyPI.

### ServiceName().underscore_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/service_name.py#L58)

```python
@property
def underscore_name() -> str:
```

Python-friendly service name.

## ServiceNameCatalog

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/service_name.py#L175)

```python
class ServiceNameCatalog():
```

Finder for boto3 services by name.

### ServiceNameCatalog.add

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/service_name.py#L210)

```python
@classmethod
def add(name: str, class_name: str) -> ServiceName:
```

Add new ServiceName to catalog or modify existing one.

#### Returns

New ServiceName or modified if it exists.

#### See also

- [ServiceName](#servicename)
