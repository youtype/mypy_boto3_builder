# Master Package

> Auto-generated documentation for [mypy_boto3_builder.writers.master_package](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/writers/master_package.py) module.

Master package writer.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Writers](index.md#writers) / Master Package
    - [write_master_package](#write_master_package)

## write_master_package

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/writers/master_package.py#L19)

```python
def write_master_package(
    package: MasterPackage,
    output_path: Path,
    generate_setup: bool,
) -> List[Path]:
```

Create mypy-boto3 stubs.

#### Arguments

- `package` - Master package.
- `output_path` - Path to output folder.
- `generate_setup` - Generate ready-to-install or to-use package.

#### See also

- [MasterPackage](../structures/master_package.md#masterpackage)
