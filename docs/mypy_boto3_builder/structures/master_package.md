# MasterPackage

> Auto-generated documentation for [mypy_boto3_builder.structures.master_package](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/master_package.py) module.

Structure for boto3-stubs module.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / MasterPackage
    - [MasterPackage](#masterpackage)
        - [MasterPackage().essential_service_names](#masterpackageessential_service_names)

## MasterPackage

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/master_package.py#L15)

```python
dataclass
class MasterPackage(Package):
```

Structure for mypy-boto3 package.

#### See also

- [Package](package.md#package)

### MasterPackage().essential_service_names

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/master_package.py#L25)

```python
@property
def essential_service_names() -> List[ServiceName]:
```
