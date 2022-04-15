# NicePath

> Auto-generated documentation for [mypy_boto3_builder.utils.nice_path](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/nice_path.py) module.

Path that represents it as relative to workdir.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Utils](index.md#utils) / NicePath
    - [NicePath](#nicepath)
        - [NicePath().walk](#nicepathwalk)

## NicePath

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/nice_path.py#L11)

```python
class NicePath(Path):
```

Path that represents it as relative to workdir.

### NicePath().walk

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/nice_path.py#L35)

```python
def walk(
    exclude: Iterable[Path] = tuple(),
    glob_pattern: str = '**/*',
) -> Iterator[_R]:
```

Walk files except for `exclude`.

#### Yields

Existing Path.
