# ServiceName

[Mypy_boto3_builder Index](../README.md#mypy_boto3_builder-index) / [Mypy Boto3 Builder](./index.md#mypy-boto3-builder) / ServiceName

> Auto-generated documentation for [mypy_boto3_builder.service_name](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/service_name.py) module.

## ServiceName

[Show source in service_name.py:15](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/service_name.py#L15)

Description for boto3 service.

#### Signature

```python
class ServiceName:
    def __init__(
        self, name: str, class_name: str, override_boto3_name: str = ""
    ) -> None: ...
```

### ServiceName().__hash__

[Show source in service_name.py:48](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/service_name.py#L48)

Calculate hash value based on service name.

#### Signature

```python
def __hash__(self) -> int: ...
```

### ServiceName().__str__

[Show source in service_name.py:54](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/service_name.py#L54)

Represent as string for debugging.

#### Signature

```python
def __str__(self) -> str: ...
```

### ServiceName().boto3_doc_link

[Show source in service_name.py:104](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/service_name.py#L104)

Link to boto3 docs.

#### Signature

```python
@property
def boto3_doc_link(self) -> str: ...
```

### ServiceName().boto3_name

[Show source in service_name.py:67](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/service_name.py#L67)

Boto3 package name.

#### Signature

```python
@property
def boto3_name(self) -> str: ...
```

### ServiceName().extras_name

[Show source in service_name.py:85](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/service_name.py#L85)

Extras name for subpackage installation.

#### Signature

```python
@property
def extras_name(self) -> str: ...
```

### ServiceName().get_boto3_doc_link

[Show source in service_name.py:114](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/service_name.py#L114)

Get link to boto3 docs with anchor.

#### Arguments

- `parts` - Anchor parts

#### Signature

```python
def get_boto3_doc_link(self, *parts: str) -> str: ...
```

### ServiceName.get_md_doc_link

[Show source in service_name.py:123](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/service_name.py#L123)

Get link to MD docs with anchor.

#### Arguments

- `file` - HTML file name
- `parts` - Anchor parts

#### Signature

```python
@staticmethod
def get_md_doc_link(
    file: Literal[
        "client", "service_resource", "waiters", "paginators", "type_defs", "literals"
    ],
    *parts: str
) -> str: ...
```

### ServiceName().import_name

[Show source in service_name.py:74](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/service_name.py#L74)

Safe mudule import name.

#### Signature

```python
@property
def import_name(self) -> str: ...
```

### ServiceName().is_conda_forge_available

[Show source in service_name.py:98](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/service_name.py#L98)

Whether service is available for `conda-forge`.

#### Signature

```python
def is_conda_forge_available(self) -> bool: ...
```

### ServiceName().is_essential

[Show source in service_name.py:92](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/service_name.py#L92)

Whether service is included to `boto3-stubs[essential]`.

#### Signature

```python
def is_essential(self) -> bool: ...
```

### ServiceName().underscore_name

[Show source in service_name.py:60](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/service_name.py#L60)

Python-friendly service name.

#### Signature

```python
@property
def underscore_name(self) -> str: ...
```



## ServiceNameCatalog

[Show source in service_name.py:149](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/service_name.py#L149)

Finder for boto3 services by name.

#### Signature

```python
class ServiceNameCatalog: ...
```

### ServiceNameCatalog.add

[Show source in service_name.py:193](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/service_name.py#L193)

Add new ServiceName to catalog or modify existing one.

#### Returns

New ServiceName or modified if it exists.

#### Signature

```python
@classmethod
def add(cls, name: str, class_name: str) -> ServiceName: ...
```

#### See also

- [ServiceName](#servicename)
