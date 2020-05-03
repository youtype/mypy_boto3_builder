# ServicePackage

> Auto-generated documentation for [mypy_boto3_builder.structures.service_package](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py) module.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / ServicePackage
    - [ServicePackage](#servicepackage)
        - [ServicePackage().extract_typed_dicts](#servicepackageextract_typed_dicts)
        - [ServicePackage().get_client_required_import_record_groups](#servicepackageget_client_required_import_record_groups)
        - [ServicePackage().get_helpers_import_record_groups](#servicepackageget_helpers_import_record_groups)
        - [ServicePackage().get_init_all_names](#servicepackageget_init_all_names)
        - [ServicePackage().get_init_import_record_groups](#servicepackageget_init_import_record_groups)
        - [ServicePackage().get_paginator_required_import_record_groups](#servicepackageget_paginator_required_import_record_groups)
        - [ServicePackage().get_service_resource_required_import_record_groups](#servicepackageget_service_resource_required_import_record_groups)
        - [ServicePackage().get_type_defs_required_import_record_groups](#servicepackageget_type_defs_required_import_record_groups)
        - [ServicePackage().get_types](#servicepackageget_types)
        - [ServicePackage().get_waiter_required_import_record_groups](#servicepackageget_waiter_required_import_record_groups)

## ServicePackage

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py#L20)

```python
dataclass
class ServicePackage(Package):
```

#### See also

- [Package](package.md#package)

### ServicePackage().extract_typed_dicts

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py#L29)

```python
def extract_typed_dicts(
    type_annotations: Iterable[FakeAnnotation],
    added: Dict[str, TypeTypedDict],
) -> List[TypeTypedDict]:
```

### ServicePackage().get_client_required_import_record_groups

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py#L139)

```python
def get_client_required_import_record_groups() -> List[ImportRecordGroup]:
```

### ServicePackage().get_helpers_import_record_groups

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py#L209)

```python
def get_helpers_import_record_groups() -> List[ImportRecordGroup]:
```

### ServicePackage().get_init_all_names

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py#L125)

```python
def get_init_all_names() -> List[str]:
```

### ServicePackage().get_init_import_record_groups

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py#L65)

```python
def get_init_import_record_groups() -> List[ImportRecordGroup]:
```

### ServicePackage().get_paginator_required_import_record_groups

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py#L167)

```python
def get_paginator_required_import_record_groups() -> List[ImportRecordGroup]:
```

### ServicePackage().get_service_resource_required_import_record_groups

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py#L152)

```python
def get_service_resource_required_import_record_groups() -> List[ImportRecordGroup]:
```

### ServicePackage().get_type_defs_required_import_record_groups

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py#L187)

```python
def get_type_defs_required_import_record_groups() -> List[ImportRecordGroup]:
```

### ServicePackage().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py#L54)

```python
def get_types() -> Set[FakeAnnotation]:
```

### ServicePackage().get_waiter_required_import_record_groups

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/service_package.py#L177)

```python
def get_waiter_required_import_record_groups() -> List[ImportRecordGroup]:
```
