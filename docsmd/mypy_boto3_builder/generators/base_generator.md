# BaseGenerator

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Generators](./index.md#generators) / BaseGenerator

> Auto-generated documentation for [mypy_boto3_builder.generators.base_generator](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/base_generator.py) module.

## BaseGenerator

[Show source in base_generator.py:23](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/base_generator.py#L23)

Base stubs/docs generator.

#### Arguments

- `service_names` - Selected service names
- `master_service_names` - Service names included in master
- `output_path` - Path to write generated files
- `generate_setup` - Whether to create package or installed module
- `skip_published` - Whether to skip packages that are already published
- `disable_smart_version` - Whether to create a new postrelease based on latest PyPI version
- `version` - Package build version
- `cleanup` - Whether to cleanup generated files

#### Signature

```python
class BaseGenerator(ABC):
    def __init__(
        self,
        service_names: Sequence[ServiceName],
        master_service_names: Sequence[ServiceName],
        output_path: Path,
        generate_setup: bool,
        skip_published: bool,
        disable_smart_version: bool,
        version: str,
        cleanup: bool,
    ): ...
```

#### See also

- [ServiceName](../service_name.md#servicename)

### BaseGenerator().generate_docs

[Show source in base_generator.py:132](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/base_generator.py#L132)

Generate service and master docs.

#### Signature

```python
@abstractmethod
def generate_docs(self) -> None: ...
```

### BaseGenerator().generate_full_stubs

[Show source in base_generator.py:101](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/base_generator.py#L101)

Generate full stubs.

#### Signature

```python
@abstractmethod
def generate_full_stubs(self) -> None: ...
```

### BaseGenerator().generate_product

[Show source in base_generator.py:138](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/base_generator.py#L138)

Run generator for a product type.

#### Signature

```python
def generate_product(self, product_type: ProductType) -> None: ...
```

#### See also

- [ProductType](../enums/product.md#producttype)

### BaseGenerator().generate_service_stubs

[Show source in base_generator.py:220](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/base_generator.py#L220)

Generate service stubs.

#### Signature

```python
def generate_service_stubs(self) -> None: ...
```

### BaseGenerator().generate_stubs

[Show source in base_generator.py:94](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/base_generator.py#L94)

Generate main stubs.

#### Signature

```python
@abstractmethod
def generate_stubs(self) -> None: ...
```

### BaseGenerator().get_library_version

[Show source in base_generator.py:74](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/base_generator.py#L74)

Get underlying library version.

#### Signature

```python
@abstractmethod
def get_library_version(self) -> str: ...
```

### BaseGenerator().get_postprocessor

[Show source in base_generator.py:68](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/base_generator.py#L68)

Get postprocessor for service package.

#### Signature

```python
@abstractmethod
def get_postprocessor(self, service_package: ServicePackage) -> BasePostprocessor: ...
```

#### See also

- [BasePostprocessor](../postprocessors/base.md#basepostprocessor)
- [ServicePackage](../structures/service_package.md#servicepackage)
