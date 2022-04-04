# BaseGenerator

> Auto-generated documentation for [mypy_boto3_builder.generators.base_generator](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/base_generator.py) module.

Base stubs/docs generator.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Generators](index.md#generators) / BaseGenerator
    - [BaseGenerator](#basegenerator)
        - [BaseGenerator().generate_docs](#basegeneratorgenerate_docs)
        - [BaseGenerator().generate_product](#basegeneratorgenerate_product)
        - [BaseGenerator().generate_service_stubs](#basegeneratorgenerate_service_stubs)
        - [BaseGenerator().generate_stubs](#basegeneratorgenerate_stubs)
        - [BaseGenerator().get_library_version](#basegeneratorget_library_version)

## BaseGenerator

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/base_generator.py#L22)

```python
class BaseGenerator(ABC):
    def __init__(
        service_names: Sequence[ServiceName],
        master_service_names: Sequence[ServiceName],
        session: Session,
        output_path: Path,
        generate_setup: bool,
        skip_published: bool,
        disable_smart_version: bool,
        version: str,
    ):
```

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

#### See also

- [ServiceName](../service_name.md#servicename)

### BaseGenerator().generate_docs

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/base_generator.py#L95)

```python
@abstractmethod
def generate_docs() -> None:
```

Generate service and master docs.

### BaseGenerator().generate_product

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/base_generator.py#L101)

```python
def generate_product(product_type: ProductType) -> None:
```

Run generator for a product type.

#### See also

- [ProductType](../constants.md#producttype)

### BaseGenerator().generate_service_stubs

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/base_generator.py#L200)

```python
def generate_service_stubs() -> None:
```

Generate service stubs.

### BaseGenerator().generate_stubs

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/base_generator.py#L88)

```python
@abstractmethod
def generate_stubs() -> None:
```

Generate main stubs.

### BaseGenerator().get_library_version

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/generators/base_generator.py#L62)

```python
@abstractmethod
def get_library_version() -> str:
```

Get underlying library version.
