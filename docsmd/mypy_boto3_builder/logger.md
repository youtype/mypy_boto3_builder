# Logger

[Mypy_boto3_builder Index](../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](./index.md#mypy-boto3-builder) /
Logger

> Auto-generated documentation for [mypy_boto3_builder.logger](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/logger.py) module.

## get_logger

[Show source in logger.py:11](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/logger.py#L11)

Get Logger instance.

#### Arguments

- `verbose` - Set log level to DEBUG.
- `panic` - Raise RuntimeError on warning.

#### Returns

Overriden Logger.

#### Signature

```python
def get_logger(level: int = 0) -> logging.Logger:
    ...
```



