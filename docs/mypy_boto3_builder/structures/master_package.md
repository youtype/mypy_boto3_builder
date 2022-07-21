# MasterPackage

[mypy-boto3-builder Index](../../README.md#mypy-boto3-builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Structures](./index.md#structures) /
MasterPackage

> Auto-generated documentation for [mypy_boto3_builder.structures.master_package](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/master_package.py) module.

- [MasterPackage](#masterpackage)
  - [MasterPackage](#masterpackage-1)
    - [MasterPackage().essential_service_names](#masterpackage()essential_service_names)

## MasterPackage

[Show source in master_package.py:12](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/master_package.py#L12)

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
        service_names: Iterable[ServiceName] = tuple(),
        service_packages: Iterable[ServicePackage] = tuple(),
    ):
        ...
```

#### See also

- [Package](./package.md#package)
- [ServiceName](../service_name.md#servicename)
- [ServicePackage](./service_package.md#servicepackage)

### MasterPackage().essential_service_names

[Show source in master_package.py:31](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/master_package.py#L31)

List of services maked as essential.

#### Signature

```python
@property
def essential_service_names(self) -> list[ServiceName]:
    ...
```

#### See also

- [ServiceName](../service_name.md#servicename)


