# Base

> Auto-generated documentation for [mypy_boto3_builder.postprocessors.base](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/postprocessors/base.py) module.

Base postprocessor for classes and methods.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Postprocessors](index.md#postprocessors) / Base
    - [BasePostprocessor](#basepostprocessor)
        - [BasePostprocessor().extend_literals](#basepostprocessorextend_literals)
        - [BasePostprocessor().generate_docstrings](#basepostprocessorgenerate_docstrings)
        - [BasePostprocessor().process_package](#basepostprocessorprocess_package)
        - [BasePostprocessor().replace_self_ref_typed_dicts](#basepostprocessorreplace_self_ref_typed_dicts)

## BasePostprocessor

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/postprocessors/base.py#L15)

```python
class BasePostprocessor(ABC):
    def __init__(
        session: Session,
        package: ServicePackage,
        service_names: Sequence[ServiceName],
    ) -> None:
```

Base postprocessor for classes and methods.

#### Arguments

- `session` - Boto3 session
- `package` - Service package
- `service_names` - Available service names

#### See also

- [ServiceName](../service_name.md#servicename)
- [ServicePackage](../structures/service_package.md#servicepackage)

### BasePostprocessor().extend_literals

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/postprocessors/base.py#L173)

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

### BasePostprocessor().generate_docstrings

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/postprocessors/base.py#L33)

```python
def generate_docstrings() -> None:
```

Generate all docstrings.

### BasePostprocessor().process_package

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/postprocessors/base.py#L44)

```python
@abstractmethod
def process_package() -> None:
```

Postprocess built package.

### BasePostprocessor().replace_self_ref_typed_dicts

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/postprocessors/base.py#L212)

```python
def replace_self_ref_typed_dicts() -> None:
```

Remove self-references from TypedDicts.
