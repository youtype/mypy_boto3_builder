# Constants

> Auto-generated documentation for [mypy_boto3_builder.constants](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/constants.py) module.

Constants and paths.

- [mypy-boto3-builder](../README.md#mypy_boto3_builder) / [Modules](../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](index.md#mypy-boto3-builder) / Constants
    - [Product](#product)
        - [Product().get_library](#productget_library)
        - [Product().get_type](#productget_type)
    - [ProductLibrary](#productlibrary)
    - [ProductType](#producttype)

#### Attributes

- `DUMMY_REGION` - Random region to initialize services: `'us-west-2'`
- `TEMPLATES_PATH` - Jinja2 templates for boto3-stubs: `Path(__file__).parent / 'templates'`
- `BOTO3_STUBS_STATIC_PATH` - Static *.pyi files for boto3-stubs: `Path(__file__).parent / 'boto3_stubs_static'`
- `BOTOCORE_STUBS_STATIC_PATH` - Static *.pyi files for botocore-stubs: `Path(__file__).parent / 'botocore_stubs_static'`
- `AIOBOTOCORE_STUBS_STATIC_PATH` - Static *.pyi files for aiobotocore-stubs: `Path(__file__).parent / 'aiobotocore_stubs_static'`
- `LINE_LENGTH` - Max line length for boto3 docs: `100`
- `LOGGER_NAME` - Main logger name: `'mypy_boto3_builder'`
- `PROG_NAME` - builder CLI entrypoint name: `'mypy_boto3_builder'`
- `PACKAGE_NAME` - builder package name: `'mypy-boto3-builder'`

## Product

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/constants.py#L55)

```python
class Product(Enum):
```

Product choice for CLI.

### Product().get_library

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/constants.py#L70)

```python
def get_library() -> ProductLibrary:
```

Get library name.

#### See also

- [ProductLibrary](#productlibrary)

### Product().get_type

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/constants.py#L79)

```python
def get_type() -> ProductType:
```

Get product type.

#### See also

- [ProductType](#producttype)

## ProductLibrary

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/constants.py#L36)

```python
class ProductLibrary(Enum):
```

Product library for Generator.

## ProductType

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/constants.py#L45)

```python
class ProductType(Enum):
```

Product type for Generator.
