# MasterPackage

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](./index.md#structures) / MasterPackage

> Auto-generated documentation for [mypy_boto3_builder.structures.master_package](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/master_package.py) module.

## MasterPackage

[Show source in master_package.py:14](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/master_package.py#L14)

Structure for mypy-boto3 package.

#### Arguments

- `name` - Module name.
- `pypi_name` - Module PyPI name.
- `service_names` - List of included service names.
- `service_packages` - List of included service packages.

#### Signature

```python
class MasterPackage(Package):
    def __init__(
        self,
        service_names: Iterable[ServiceName] = (),
        service_packages: Iterable[ServicePackage] = (),
    ): ...
```

#### See also

- [Package](./package.md#package)
- [ServiceName](../service_name.md#servicename)
- [ServicePackage](./service_package.md#servicepackage)

### MasterPackage().essential_service_names

[Show source in master_package.py:34](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/master_package.py#L34)

List of services maked as essential.

#### Signature

```python
@property
def essential_service_names(self) -> list[ServiceName]: ...
```

#### See also

- [ServiceName](../service_name.md#servicename)
