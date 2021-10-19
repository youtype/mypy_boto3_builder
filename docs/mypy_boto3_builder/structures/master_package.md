# MasterPackage

> Auto-generated documentation for [mypy_boto3_builder.structures.master_package](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/master_package.py) module.

Structure for boto3-stubs module.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / MasterPackage
    - [MasterPackage](#masterpackage)
        - [MasterPackage().essential_service_names](#masterpackageessential_service_names)

## MasterPackage

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/master_package.py#L12)

```python
class MasterPackage(Package):
    def __init__(
        name: str = MODULE_NAME,
        pypi_name: str = PYPI_NAME,
        service_names: Iterable[ServiceName] = tuple(),
        service_packages: Iterable[ServicePackage] = tuple(),
    ):
```

Structure for mypy-boto3 package.

#### Arguments

- `name` - Module name.
- `pypi_name` - Module PyPI name.
- `service_names` - List of included service names.
- `service_packages` - List of included service packages.

#### See also

- [MODULE_NAME](../constants.md#module_name)
- [PYPI_NAME](../constants.md#pypi_name)
- [Package](package.md#package)

### MasterPackage().essential_service_names

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/master_package.py#L34)

```python
@property
def essential_service_names() -> list[ServiceName]:
```

List of services maked as essential.
