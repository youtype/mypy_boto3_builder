# Logger

> Auto-generated documentation for [mypy_boto3_builder.logger](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/logger.py) module.

Logging utils.

- [mypy-boto3-builder](../README.md#mypy_boto3_builder) / [Modules](../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](index.md#mypy-boto3-builder) / Logger
    - [get_logger](#get_logger)

## get_logger

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/logger.py#L44)

```python
def get_logger(verbose: bool = False, panic: bool = False) -> Logger:
```

Get Logger instance.

#### Arguments

- `verbose` - Set log level to DEBUG.
- `panic` - Raise RuntimeError on warning.

#### Returns

Overriden Logger.

#### See also

- [Logger](#logger)
