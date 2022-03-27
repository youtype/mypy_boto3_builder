# ServicePackage

> Auto-generated documentation for [mypy_boto3_builder.structures.service_package](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py) module.

Parsed Service package.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / ServicePackage
    - [ServicePackage](#servicepackage)
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

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py#L25)

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

- [BasePackageData](../package_data.md#basepackagedata)
- [Client](client.md#client)
- [Function](function.md#function)
- [Package](package.md#package)
- [Paginator](paginator.md#paginator)
- [ServiceName](../service_name.md#servicename)
- [TypeLiteral](../type_annotations/type_literal.md#typeliteral)
- [TypeTypedDict](../type_annotations/type_typed_dict.md#typetypeddict)
- [Waiter](waiter.md#waiter)

### ServicePackage().extract_literals

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py#L54)

```python
def extract_literals() -> list[TypeLiteral]:
```

Extract literals from children.

#### See also

- [TypeLiteral](../type_annotations/type_literal.md#typeliteral)

### ServicePackage().extract_typed_dicts

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py#L108)

```python
def extract_typed_dicts() -> list[TypeTypedDict]:
```

Extract typed dicts from children.

Attempts to resolve circular typed dicts.

#### See also

- [TypeTypedDict](../type_annotations/type_typed_dict.md#typetypeddict)

### ServicePackage().get_client_required_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py#L209)

```python
def get_client_required_import_records() -> list[ImportRecord]:
```

Get import records for `client.py[i]`.

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### ServicePackage().get_doc_link

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py#L347)

```python
def get_doc_link(
    file: Literal[
        'client',
        'service_resource',
        'waiters',
        'paginators',
        'type_defs',
        'literals',
    ],
    *parts: str,
) -> str:
```

Get link to local docs with anchor.

#### Arguments

- `file` - HTML file name
- `parts` - Anchor parts

### ServicePackage().get_init_all_names

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py#L192)

```python
def get_init_all_names() -> list[str]:
```

Get `__all__` statement names for `__init__.py[i]`.

### ServicePackage().get_init_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py#L157)

```python
def get_init_import_records() -> list[ImportRecord]:
```

Get import records for `__init__.py[i]`.

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### ServicePackage().get_literals_required_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py#L312)

```python
def get_literals_required_import_records() -> list[ImportRecord]:
```

Get import records for `literals.py[i]`.

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### ServicePackage().get_local_doc_link

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py#L372)

```python
def get_local_doc_link(service_name: ServiceName | None = None) -> str:
```

Get link to local docs.

### ServicePackage().get_paginator_required_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py#L241)

```python
def get_paginator_required_import_records() -> list[ImportRecord]:
```

Get import records for `paginator.py[i]`.

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### ServicePackage().get_service_resource_required_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py#L225)

```python
def get_service_resource_required_import_records() -> list[ImportRecord]:
```

Get import records for `service_resource.py[i]`.

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### ServicePackage().get_type_defs_required_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py#L276)

```python
def get_type_defs_required_import_records() -> list[ImportRecord]:
```

Get import records for `type_defs.py[i]`.

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### ServicePackage().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py#L142)

```python
def get_types() -> set[FakeAnnotation]:
```

Extract type annotations from Client, ServiceResource, waiters and paginators.

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)

### ServicePackage().get_waiter_required_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py#L261)

```python
def get_waiter_required_import_records() -> list[ImportRecord]:
```

Get import records for `waiter.py[i]`.

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### ServicePackage().validate

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py#L321)

```python
def validate() -> None:
```

Validate parsed module.

Finds duplicated names.
Finds conflicts with reserved Python words.
