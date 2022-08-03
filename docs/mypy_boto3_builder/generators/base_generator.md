# BaseGenerator

[mypy-boto3-builder Index](../../README.md#mypy-boto3-builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Generators](./index.md#generators) /
BaseGenerator

> Auto-generated documentation for [mypy_boto3_builder.generators.base_generator](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/base_generator.py) module.

- [BaseGenerator](#basegenerator)
  - [BaseGenerator](#basegenerator-1)
    - [BaseGenerator().generate_docs](#basegenerator()generate_docs)
    - [BaseGenerator().generate_product](#basegenerator()generate_product)
    - [BaseGenerator().generate_service_stubs](#basegenerator()generate_service_stubs)
    - [BaseGenerator().generate_stubs](#basegenerator()generate_stubs)
    - [BaseGenerator().get_library_version](#basegenerator()get_library_version)
    - [BaseGenerator().get_postprocessor](#basegenerator()get_postprocessor)

## BaseGenerator

[Show source in base_generator.py:22](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/base_generator.py#L22)

Base stubs/docs generator.

#### Arguments

- `service_names` - Selected service names
- `master_service_names` - Service names included in master
- `session` - Botocore session
- `output_path` - Path to write generated files
- `generate_setup` - Whether to create package or installed module
- `skip_published` - Whether to skip packages that are already published
- `disable_smart_version` - Whether to create a new postrelease if version is already published
- `version` - Package build version

#### Signature

```python
class BaseGenerator(ABC):
    def __init__(
        self,
        service_names: Sequence[ServiceName],
        master_service_names: Sequence[ServiceName],
        session: Session,
        output_path: Path,
        generate_setup: bool,
        skip_published: bool,
        disable_smart_version: bool,
        version: str,
    ):
        ...
```

#### See also

- [ServiceName](../service_name.md#servicename)

### BaseGenerator().generate_docs

[Show source in base_generator.py:101](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/base_generator.py#L101)

Generate service and master docs.

#### Signature

```python
@abstractmethod
def generate_docs(self) -> None:
    ...
```

### BaseGenerator().generate_product

[Show source in base_generator.py:107](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/base_generator.py#L107)

Run generator for a product type.

#### Signature

```python
def generate_product(self, product_type: ProductType) -> None:
    ...
```

#### See also

- [ProductType](../constants.md#producttype)

### BaseGenerator().generate_service_stubs

[Show source in base_generator.py:201](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/base_generator.py#L201)

Generate service stubs.

#### Signature

```python
def generate_service_stubs(self) -> None:
    ...
```

### BaseGenerator().generate_stubs

[Show source in base_generator.py:94](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/base_generator.py#L94)

Generate main stubs.

#### Signature

```python
@abstractmethod
def generate_stubs(self) -> None:
    ...
```

### BaseGenerator().get_library_version

[Show source in base_generator.py:68](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/base_generator.py#L68)

Get underlying library version.

#### Signature

```python
@abstractmethod
def get_library_version(self) -> str:
    ...
```

### BaseGenerator().get_postprocessor

[Show source in base_generator.py:62](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/base_generator.py#L62)

Get postprocessor for service package.

#### Signature

```python
@abstractmethod
def get_postprocessor(self, service_package: ServicePackage) -> BasePostprocessor:
    ...
```

#### See also

- [BasePostprocessor](../postprocessors/base.md#basepostprocessor)
- [ServicePackage](../structures/service_package.md#servicepackage)

