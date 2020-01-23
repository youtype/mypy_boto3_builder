# Boto3StubsPackage

> Auto-generated documentation for [mypy_boto3_builder.structures.boto3_stubs_package](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/boto3_stubs_package.py) module.

Structure for boto3-stubs module.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / Boto3StubsPackage
    - [Boto3StubsPackage](#boto3stubspackage)
        - [Boto3StubsPackage().essential_service_names](#boto3stubspackageessential_service_names)

## Boto3StubsPackage

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/boto3_stubs_package.py#L13)

```python
dataclass
class Boto3StubsPackage(Package):
```

Structure for boto3-stubs module.

#### See also

- [Package](package.md#package)

### Boto3StubsPackage().essential_service_names

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/boto3_stubs_package.py#L23)

```python
@property
def essential_service_names() -> List[ServiceName]:
```
