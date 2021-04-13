# ServiceName

> Auto-generated documentation for [mypy_boto3_builder.service_name](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/service_name.py) module.

Description for boto3 service.

- [mypy-boto3-builder](../README.md#mypy_boto3_builder) / [Modules](../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](index.md#mypy-boto3-builder) / ServiceName
    - [ServiceName](#servicename)
        - [ServiceName().boto3_name](#servicenameboto3_name)
        - [ServiceName().doc_link](#servicenamedoc_link)
        - [ServiceName().extras_name](#servicenameextras_name)
        - [ServiceName().import_name](#servicenameimport_name)
        - [ServiceName().is_essential](#servicenameis_essential)
        - [ServiceName().module_name](#servicenamemodule_name)
        - [ServiceName().pypi_link](#servicenamepypi_link)
        - [ServiceName().pypi_name](#servicenamepypi_name)
        - [ServiceName().underscore_name](#servicenameunderscore_name)
    - [ServiceNameCatalog](#servicenamecatalog)
        - [ServiceNameCatalog.create](#servicenamecatalogcreate)
        - [ServiceNameCatalog.find](#servicenamecatalogfind)

## ServiceName

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/service_name.py#L14)

```python
class ServiceName():
    def __init__(name: str, class_name: str) -> None:
```

Description for boto3 service.

### ServiceName().boto3_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/service_name.py#L44)

```python
@property
def boto3_name() -> str:
```

Boto3 package name.

### ServiceName().doc_link

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/service_name.py#L92)

```python
@property
def doc_link() -> str:
```

### ServiceName().extras_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/service_name.py#L82)

```python
@property
def extras_name() -> str:
```

Extras name for subpackage installation.

### ServiceName().import_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/service_name.py#L51)

```python
@property
def import_name() -> str:
```

Safe mudule import name.

### ServiceName().is_essential

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/service_name.py#L89)

```python
def is_essential() -> bool:
```

### ServiceName().module_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/service_name.py#L61)

```python
@property
def module_name() -> str:
```

Package name for given service.

### ServiceName().pypi_link

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/service_name.py#L75)

```python
@property
def pypi_link() -> str:
```

Link to package on PyPI.

### ServiceName().pypi_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/service_name.py#L68)

```python
@property
def pypi_name() -> str:
```

Name of package on PyPI.

### ServiceName().underscore_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/service_name.py#L40)

```python
@property
def underscore_name() -> str:
```

## ServiceNameCatalog

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/service_name.py#L100)

```python
class ServiceNameCatalog():
```

Finder for boto3 services by name.

### ServiceNameCatalog.create

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/service_name.py#L404)

```python
@staticmethod
def create(name: str) -> ServiceName:
```

Create ServiceName for unknown service.

#### See also

- [ServiceName](#servicename)

### ServiceNameCatalog.find

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/service_name.py#L385)

```python
@classmethod
def find(name: str) -> ServiceName:
```

Get [ServiceName](#servicename) by import name.

#### Arguments

- `name` - Service import name.

#### Returns

ServiceName.

#### Raises

- `ValueError` - If ServiceName not found.

#### See also

- [ServiceName](#servicename)
