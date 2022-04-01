# ServicePackagePostprocessor

> Auto-generated documentation for [mypy_boto3_builder.parsers.service_package_postprocessor](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/service_package_postprocessor.py) module.

Postprocessor for all classes and methods.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](index.md#parsers) / ServicePackagePostprocessor
    - [ServicePackagePostprocessor](#servicepackagepostprocessor)
        - [ServicePackagePostprocessor().add_contextmanager_methods](#servicepackagepostprocessoradd_contextmanager_methods)
        - [ServicePackagePostprocessor().extend_literals](#servicepackagepostprocessorextend_literals)
        - [ServicePackagePostprocessor().generate_docstrings](#servicepackagepostprocessorgenerate_docstrings)
        - [ServicePackagePostprocessor().make_async](#servicepackagepostprocessormake_async)
        - [ServicePackagePostprocessor().replace_self_ref_typed_dicts](#servicepackagepostprocessorreplace_self_ref_typed_dicts)

## ServicePackagePostprocessor

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/service_package_postprocessor.py#L21)

```python
class ServicePackagePostprocessor():
    def __init__(
        session: Session,
        package: ServicePackage,
        service_names: Sequence[ServiceName],
    ) -> None:
```

Postprocessor for all classes and methods.

#### Arguments

- `package` - Service package

#### See also

- [ServiceName](../service_name.md#servicename)
- [ServicePackage](../structures/service_package.md#servicepackage)

### ServicePackagePostprocessor().add_contextmanager_methods

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/service_package_postprocessor.py#L106)

```python
def add_contextmanager_methods() -> None:
```

Add contextmanager methods.

### ServicePackagePostprocessor().extend_literals

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/service_package_postprocessor.py#L259)

```python
def extend_literals() -> None:
```

Add extra literals.

- `<Class>ServiceName`
- `ServiceName`
- `ResourceServiceName`
- `PaginatorName`
- `WaiterName`
- `RegionName`

### ServicePackagePostprocessor().generate_docstrings

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/service_package_postprocessor.py#L37)

```python
def generate_docstrings() -> None:
```

Generate all docstrings.

### ServicePackagePostprocessor().make_async

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/service_package_postprocessor.py#L48)

```python
def make_async() -> None:
```

Convert all methods to asynchronous.

### ServicePackagePostprocessor().replace_self_ref_typed_dicts

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/service_package_postprocessor.py#L298)

```python
def replace_self_ref_typed_dicts() -> None:
```

Remove self-references from TypedDicts.
