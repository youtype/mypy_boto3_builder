# ServicePackage

> Auto-generated documentation for [mypy_boto3_builder.structures.service_package](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py) module.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / ServicePackage
    - [ServicePackage](#servicepackage)
        - [ServicePackage().extract_typed_dicts](#servicepackageextract_typed_dicts)
        - [ServicePackage().get_client_required_import_records](#servicepackageget_client_required_import_records)
        - [ServicePackage().get_init_all_names](#servicepackageget_init_all_names)
        - [ServicePackage().get_init_import_records](#servicepackageget_init_import_records)
        - [ServicePackage().get_paginator_required_import_records](#servicepackageget_paginator_required_import_records)
        - [ServicePackage().get_service_resource_required_import_records](#servicepackageget_service_resource_required_import_records)
        - [ServicePackage().get_type_defs_required_import_records](#servicepackageget_type_defs_required_import_records)
        - [ServicePackage().get_types](#servicepackageget_types)
        - [ServicePackage().get_waiter_required_import_records](#servicepackageget_waiter_required_import_records)

## ServicePackage

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py#L17)

```python
class ServicePackage(Package):
    def __init__(
        name: str,
        pypi_name: str,
        service_name: ServiceName,
        client: Client,
        service_resource: Optional[ServiceResource] = None,
        waiters: Iterable[Waiter] = tuple(),
        paginators: Iterable[Paginator] = tuple(),
        typed_dicts: Iterable[TypeTypedDict] = tuple(),
        helper_functions: Iterable[Function] = tuple(),
    ):
```

#### See also

- [Client](client.md#client)
- [Package](package.md#package)
- [ServiceName](../service_name.md#servicename)

### ServicePackage().extract_typed_dicts

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py#L39)

```python
def extract_typed_dicts() -> List[TypeTypedDict]:
```

### ServicePackage().get_client_required_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py#L137)

```python
def get_client_required_import_records() -> List[ImportRecord]:
```

### ServicePackage().get_init_all_names

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py#L123)

```python
def get_init_all_names() -> List[str]:
```

### ServicePackage().get_init_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py#L82)

```python
def get_init_import_records() -> List[ImportRecord]:
```

### ServicePackage().get_paginator_required_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py#L163)

```python
def get_paginator_required_import_records() -> List[ImportRecord]:
```

### ServicePackage().get_service_resource_required_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py#L150)

```python
def get_service_resource_required_import_records() -> List[ImportRecord]:
```

### ServicePackage().get_type_defs_required_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py#L183)

```python
def get_type_defs_required_import_records() -> List[ImportRecord]:
```

### ServicePackage().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py#L71)

```python
def get_types() -> Set[FakeAnnotation]:
```

### ServicePackage().get_waiter_required_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py#L173)

```python
def get_waiter_required_import_records() -> List[ImportRecord]:
```
