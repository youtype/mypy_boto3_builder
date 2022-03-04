# ServicePackage

> Auto-generated documentation for [mypy_boto3_builder.structures.service_package](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_package.py) module.

Parsed Service package.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / ServicePackage
    - [ServicePackage](#servicepackage)
        - [ServicePackage().extend_literals](#servicepackageextend_literals)
        - [ServicePackage().extract_literals](#servicepackageextract_literals)
        - [ServicePackage().extract_typed_dicts](#servicepackageextract_typed_dicts)
        - [ServicePackage().get_client_required_import_records](#servicepackageget_client_required_import_records)
        - [ServicePackage().get_doc_link](#servicepackageget_doc_link)
        - [ServicePackage().get_init_all_names](#servicepackageget_init_all_names)
        - [ServicePackage().get_init_import_records](#servicepackageget_init_import_records)
        - [ServicePackage().get_literals_required_import_records](#servicepackageget_literals_required_import_records)
        - [ServicePackage().get_local_doc_link](#servicepackageget_local_doc_link)
        - [ServicePackage().get_paginator_required_import_records](#servicepackageget_paginator_required_import_records)
        - [ServicePackage().get_service_resource_required_import_records](#servicepackageget_service_resource_required_import_records)
        - [ServicePackage().get_type_defs_required_import_records](#servicepackageget_type_defs_required_import_records)
        - [ServicePackage().get_types](#servicepackageget_types)
        - [ServicePackage().get_waiter_required_import_records](#servicepackageget_waiter_required_import_records)
        - [ServicePackage().validate](#servicepackagevalidate)

## ServicePackage

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_package.py#L24)

```python
class ServicePackage(Package):
    def __init__(
        data: type[BasePackageData],
        service_name: ServiceName,
        client: Client,
        service_resource: ServiceResource | None = None,
        waiters: Iterable[Waiter] = tuple(),
        paginators: Iterable[Paginator] = tuple(),
        typed_dicts: Iterable[TypeTypedDict] = tuple(),
        literals: Iterable[TypeLiteral] = tuple(),
        helper_functions: Iterable[Function] = tuple(),
    ):
```

Parsed Service package.

#### See also

- [Client](client.md#client)
- [Package](package.md#package)
- [ServiceName](../service_name.md#servicename)

### ServicePackage().extend_literals

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_package.py#L338)

```python
def extend_literals(service_names: Iterable[ServiceName]) -> None:
```

Add extra literals.

- `<Class>ServiceName`
- `ServiceName`
- `ResourceServiceName`
- `PaginatorName`
- `WaiterName`

### ServicePackage().extract_literals

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_package.py#L53)

```python
def extract_literals() -> list[TypeLiteral]:
```

Extract literals from children.

### ServicePackage().extract_typed_dicts

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_package.py#L99)

```python
def extract_typed_dicts() -> list[TypeTypedDict]:
```

Extract typed dicts from children.

Attempts to resolve circular typed dicts.

### ServicePackage().get_client_required_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_package.py#L200)

```python
def get_client_required_import_records() -> list[ImportRecord]:
```

Get import records for `client.py[i]`.

### ServicePackage().get_doc_link

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_package.py#L369)

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

### ServicePackage().get_init_all_names

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_package.py#L183)

```python
def get_init_all_names() -> list[str]:
```

Get `__all__` statement names for `__init__.py[i]`.

### ServicePackage().get_init_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_package.py#L148)

```python
def get_init_import_records() -> list[ImportRecord]:
```

Get import records for `__init__.py[i]`.

### ServicePackage().get_literals_required_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_package.py#L303)

```python
def get_literals_required_import_records() -> list[ImportRecord]:
```

Get import records for `literals.py[i]`.

### ServicePackage().get_local_doc_link

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_package.py#L394)

```python
def get_local_doc_link(service_name: ServiceName | None = None) -> str:
```

Get link to local docs.

### ServicePackage().get_paginator_required_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_package.py#L232)

```python
def get_paginator_required_import_records() -> list[ImportRecord]:
```

Get import records for `paginator.py[i]`.

### ServicePackage().get_service_resource_required_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_package.py#L216)

```python
def get_service_resource_required_import_records() -> list[ImportRecord]:
```

Get import records for `service_resource.py[i]`.

### ServicePackage().get_type_defs_required_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_package.py#L267)

```python
def get_type_defs_required_import_records() -> list[ImportRecord]:
```

Get import records for `type_defs.py[i]`.

### ServicePackage().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_package.py#L133)

```python
def get_types() -> set[FakeAnnotation]:
```

Extract type annotations from Client, ServiceResource, waiters and paginators.

### ServicePackage().get_waiter_required_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_package.py#L252)

```python
def get_waiter_required_import_records() -> list[ImportRecord]:
```

Get import records for `waiter.py[i]`.

### ServicePackage().validate

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/service_package.py#L312)

```python
def validate() -> None:
```

Validate parsed module.

Finds duplicated names.
Finds conflicts with reserved Python words.
