# ServiceModuleName

> Auto-generated documentation for [mypy_boto3_builder.enums.service_module_name](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/enums/service_module_name.py) module.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Enums](index.md#enums) / ServiceModuleName
    - [ServiceModuleName](#servicemodulename)
        - [ServiceModuleName().file_name](#servicemodulenamefile_name)
        - [ServiceModuleName().stub_file_name](#servicemodulenamestub_file_name)
        - [ServiceModuleName().template_name](#servicemodulenametemplate_name)

## ServiceModuleName

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/enums/service_module_name.py#L4)

```python
class ServiceModuleName(enum.Enum):
```

Enum for service modules.

### ServiceModuleName().file_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/enums/service_module_name.py#L22)

```python
@property
def file_name() -> str:
```

Module file name.

### ServiceModuleName().stub_file_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/enums/service_module_name.py#L15)

```python
@property
def stub_file_name() -> str:
```

Module file name.

### ServiceModuleName().template_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/enums/service_module_name.py#L29)

```python
@property
def template_name() -> str:
```

Module template file name.
