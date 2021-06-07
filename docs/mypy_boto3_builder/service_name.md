# ServiceName

> Auto-generated documentation for [mypy_boto3_builder.service_name](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/service_name.py) module.

Description for boto3 service.

- [mypy-boto3-builder](../README.md#mypy_boto3_builder) / [Modules](../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](index.md#mypy-boto3-builder) / ServiceName
    - [ServiceName](#servicename)
        - [ServiceName().boto3_doc_link](#servicenameboto3_doc_link)
        - [ServiceName().boto3_name](#servicenameboto3_name)
        - [ServiceName().extras_name](#servicenameextras_name)
        - [ServiceName().get_boto3_doc_link](#servicenameget_boto3_doc_link)
        - [ServiceName().get_doc_link](#servicenameget_doc_link)
        - [ServiceName().get_md_doc_link](#servicenameget_md_doc_link)
        - [ServiceName().import_name](#servicenameimport_name)
        - [ServiceName().is_essential](#servicenameis_essential)
        - [ServiceName().local_doc_link](#servicenamelocal_doc_link)
        - [ServiceName().module_name](#servicenamemodule_name)
        - [ServiceName().pypi_link](#servicenamepypi_link)
        - [ServiceName().pypi_name](#servicenamepypi_name)
        - [ServiceName().underscore_name](#servicenameunderscore_name)
    - [ServiceNameCatalog](#servicenamecatalog)
        - [ServiceNameCatalog.create](#servicenamecatalogcreate)
        - [ServiceNameCatalog.find](#servicenamecatalogfind)

## ServiceName

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/service_name.py#L15)

```python
class ServiceName():
    def __init__(name: str, class_name: str) -> None:
```

Description for boto3 service.

### ServiceName().boto3_doc_link

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/service_name.py#L95)

```python
@property
def boto3_doc_link() -> str:
```

Link to boto3 docs.

### ServiceName().boto3_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/service_name.py#L46)

```python
@property
def boto3_name() -> str:
```

Boto3 package name.

### ServiceName().extras_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/service_name.py#L85)

```python
@property
def extras_name() -> str:
```

Extras name for subpackage installation.

### ServiceName().get_boto3_doc_link

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/service_name.py#L112)

```python
def get_boto3_doc_link(*parts: str) -> str:
```

Get link to boto3 docs with anchor.

#### Arguments

- `parts` - Anchor parts

### ServiceName().get_doc_link

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/service_name.py#L146)

```python
def get_doc_link(
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

Get link to local docs with anchor.

#### Arguments

- `file` - HTML file name
- `parts` - Anchor parts

### ServiceName().get_md_doc_link

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/service_name.py#L121)

```python
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

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/service_name.py#L53)

```python
@property
def import_name() -> str:
```

Safe mudule import name.

### ServiceName().is_essential

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/service_name.py#L92)

```python
def is_essential() -> bool:
```

### ServiceName().local_doc_link

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/service_name.py#L105)

```python
@property
def local_doc_link() -> str:
```

Link to local docs.

### ServiceName().module_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/service_name.py#L64)

```python
@property
def module_name() -> str:
```

Package name for given service.

### ServiceName().pypi_link

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/service_name.py#L78)

```python
@property
def pypi_link() -> str:
```

Link to package on PyPI.

### ServiceName().pypi_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/service_name.py#L71)

```python
@property
def pypi_name() -> str:
```

Name of package on PyPI.

### ServiceName().underscore_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/service_name.py#L42)

```python
@property
def underscore_name() -> str:
```

## ServiceNameCatalog

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/service_name.py#L172)

```python
class ServiceNameCatalog():
```

Finder for boto3 services by name.

### ServiceNameCatalog.create

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/service_name.py#L483)

```python
@staticmethod
def create(name: str) -> ServiceName:
```

Create ServiceName for unknown service.

#### See also

- [ServiceName](#servicename)

### ServiceNameCatalog.find

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/service_name.py#L464)

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
