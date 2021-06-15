# Botocore Stubs Package

> Auto-generated documentation for [mypy_boto3_builder.writers.botocore_stubs_package](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/writers/botocore_stubs_package.py) module.

botocore-stubs package writer.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Writers](index.md#writers) / Botocore Stubs Package
    - [write_botocore_stubs_package](#write_botocore_stubs_package)

## write_botocore_stubs_package

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/writers/botocore_stubs_package.py#L20)

```python
def write_botocore_stubs_package(
    output_path: Path,
    generate_setup: bool,
) -> List[Path]:
```

Generate botocore-stubs stub files.

#### Arguments

- `output_path` - Path to output folder.
- `generate_setup` - Generate ready-to-install or to-use package.
