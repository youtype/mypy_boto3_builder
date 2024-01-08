# Constants

[Mypy_boto3_builder Index](../README.md#mypy_boto3_builder-index) / [Mypy Boto3 Builder](./index.md#mypy-boto3-builder) / Constants

> Auto-generated documentation for [mypy_boto3_builder.constants](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/constants.py) module.

#### Attributes

- `DUMMY_REGION` - Random region to initialize services: 'us-west-2'

- `TEMPLATES_PATH` - Jinja2 templates for boto3-stubs: Path(__file__).parent / 'templates'

- `BOTO3_STUBS_STATIC_PATH` - Static *.pyi files for boto3-stubs: Path(__file__).parent / 'stubs_static' / 'boto3'

- `AIOBOTOCORE_STUBS_STATIC_PATH` - Static *.pyi files for types-aiobotocore: Path(__file__).parent / 'stubs_static' / 'aiobotocore'

- `AIOBOTO3_STUBS_STATIC_PATH` - Static *.pyi files for types-aioboto3: Path(__file__).parent / 'stubs_static' / 'aioboto3'

- `LINE_LENGTH` - Max line length for boto3 docs: 100

- `BUILDER_REPO_URL` - mypy-boto3-builder GitHub link: 'https://github.com/youtype/mypy_boto3_builder'

- `LOGGER_NAME` - Main logger name: 'mypy_boto3_builder'

- `PROG_NAME` - builder CLI entrypoint name: 'mypy_boto3_builder'

- `PACKAGE_NAME` - builder package name: 'mypy-boto3-builder'

- `ALL` - universal mask for all resources: '*'


## Product

[Show source in constants.py:63](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/constants.py#L63)

Product choice for CLI.

#### Signature

```python
class Product(Enum): ...
```

### Product().get_library

[Show source in constants.py:80](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/constants.py#L80)

Get library name.

#### Signature

```python
def get_library(self) -> ProductLibrary: ...
```

#### See also

- [ProductLibrary](#productlibrary)

### Product().get_type

[Show source in constants.py:89](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/constants.py#L89)

Get product type.

#### Signature

```python
def get_type(self) -> ProductType: ...
```

#### See also

- [ProductType](#producttype)



## ProductLibrary

[Show source in constants.py:43](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/constants.py#L43)

Product library for Generator.

#### Signature

```python
class ProductLibrary(Enum): ...
```



## ProductType

[Show source in constants.py:53](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/constants.py#L53)

Product type for Generator.

#### Signature

```python
class ProductType(Enum): ...
```
