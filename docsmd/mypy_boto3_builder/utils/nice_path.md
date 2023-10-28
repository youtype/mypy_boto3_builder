# NicePath

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Utils](./index.md#utils) /
NicePath

> Auto-generated documentation for [mypy_boto3_builder.utils.nice_path](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/nice_path.py) module.

## NicePath

[Show source in nice_path.py:12](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/nice_path.py#L12)

Path that represents it as relative to workdir.

#### Signature

```python
class NicePath(Path): ...
```

### NicePath().walk

[Show source in nice_path.py:36](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/nice_path.py#L36)

Walk files except for `exclude`.

#### Yields

Existing Path.

#### Signature

```python
def walk(
    self: _R, exclude: Iterable[Path] = (), glob_pattern: str = "**/*"
) -> Iterator[_R]: ...
```
