# Base

[mypy-boto3-builder Index](../../README.md#mypy-boto3-builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Postprocessors](./index.md#postprocessors) /
Base

> Auto-generated documentation for [mypy_boto3_builder.postprocessors.base](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/postprocessors/base.py) module.

- [Base](#base)
  - [BasePostprocessor](#basepostprocessor)
    - [BasePostprocessor().extend_literals](#basepostprocessor()extend_literals)
    - [BasePostprocessor().generate_docstrings](#basepostprocessor()generate_docstrings)
    - [BasePostprocessor().process_package](#basepostprocessor()process_package)
    - [BasePostprocessor().replace_self_ref_typed_dicts](#basepostprocessor()replace_self_ref_typed_dicts)

## BasePostprocessor

[Show source in base.py:15](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/postprocessors/base.py#L15)

Base postprocessor for classes and methods.

#### Arguments

- `session` - Boto3 session
- `package` - Service package
- `service_names` - Available service names

#### Signature

```python
class BasePostprocessor(ABC):
    def __init__(
        self,
        session: Session,
        package: ServicePackage,
        service_names: Sequence[ServiceName],
    ) -> None:
        ...
```

#### See also

- [ServiceName](../service_name.md#servicename)
- [ServicePackage](../structures/service_package.md#servicepackage)

### BasePostprocessor().extend_literals

[Show source in base.py:173](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/postprocessors/base.py#L173)

Add extra literals.

- `<Class>ServiceName`
- `ServiceName`
- `ResourceServiceName`
- `PaginatorName`
- `WaiterName`
- `RegionName`

#### Signature

```python
def extend_literals(self) -> None:
    ...
```

### BasePostprocessor().generate_docstrings

[Show source in base.py:33](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/postprocessors/base.py#L33)

Generate all docstrings.

#### Signature

```python
def generate_docstrings(self) -> None:
    ...
```

### BasePostprocessor().process_package

[Show source in base.py:44](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/postprocessors/base.py#L44)

Postprocess built package.

#### Signature

```python
@abstractmethod
def process_package(self) -> None:
    ...
```

### BasePostprocessor().replace_self_ref_typed_dicts

[Show source in base.py:212](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/postprocessors/base.py#L212)

Remove self-references from TypedDicts.

#### Signature

```python
def replace_self_ref_typed_dicts(self) -> None:
    ...
```

