# ServicePackagePostprocessor

> Auto-generated documentation for [mypy_boto3_builder.parsers.service_package_postprocessor](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/service_package_postprocessor.py) module.

Postprocessor for all classes and methods.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](index.md#parsers) / ServicePackagePostprocessor
    - [ServicePackagePostprocessor](#servicepackagepostprocessor)
        - [ServicePackagePostprocessor().add_contextmanager_methods](#servicepackagepostprocessoradd_contextmanager_methods)
        - [ServicePackagePostprocessor().generate_docstrings](#servicepackagepostprocessorgenerate_docstrings)
        - [ServicePackagePostprocessor().make_async](#servicepackagepostprocessormake_async)

## ServicePackagePostprocessor

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/service_package_postprocessor.py#L13)

```python
class ServicePackagePostprocessor():
    def __init__(package: ServicePackage) -> None:
```

Postprocessor for all classes and methods.

#### Arguments

- `package` - Service package

#### See also

- [ServicePackage](../structures/service_package.md#servicepackage)

### ServicePackagePostprocessor().add_contextmanager_methods

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/service_package_postprocessor.py#L76)

```python
def add_contextmanager_methods() -> None:
```

Add contextmanager methods.

### ServicePackagePostprocessor().generate_docstrings

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/service_package_postprocessor.py#L25)

```python
def generate_docstrings() -> None:
```

Generate all docstrings.

### ServicePackagePostprocessor().make_async

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/service_package_postprocessor.py#L36)

```python
def make_async() -> None:
```

Convert all methods to asynchronous.
