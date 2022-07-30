# Strings

[mypy-boto3-builder Index](../../README.md#mypy-boto3-builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Utils](./index.md#utils) /
Strings

> Auto-generated documentation for [mypy_boto3_builder.utils.strings](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/strings.py) module.

- [Strings](#strings)
  - [get_anchor_link](#get_anchor_link)
  - [get_botocore_class_name](#get_botocore_class_name)
  - [get_class_prefix](#get_class_prefix)
  - [get_line_with_indented](#get_line_with_indented)
  - [get_short_docstring](#get_short_docstring)
  - [is_reserved](#is_reserved)

## get_anchor_link

[Show source in strings.py:96](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/strings.py#L96)

Convert header to markdown anchor link.

#### Signature

```python
def get_anchor_link(text: str) -> str:
    ...
```



## get_botocore_class_name

[Show source in strings.py:156](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/strings.py#L156)

Get Botocore class name from Service metadata.

#### Signature

```python
def get_botocore_class_name(metadata: dict[str, str]) -> str:
    ...
```



## get_class_prefix

[Show source in strings.py:23](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/strings.py#L23)

Get a valid Python class prefix from `func_name`.

#### Arguments

- `func_name` - Any string.

#### Returns

String with a class prefix.

#### Signature

```python
def get_class_prefix(func_name: str) -> str:
    ...
```



## get_line_with_indented

[Show source in strings.py:37](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/strings.py#L37)

Get first line of the string with all indented lines.

Fixes invalid unindent.

#### Arguments

- `input_string` - Input string.

#### Returns

A string with first line and following indented lines.

#### Signature

```python
def get_line_with_indented(input_string: str, multi_first_line: bool = False) -> str:
    ...
```



## get_short_docstring

[Show source in strings.py:110](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/strings.py#L110)

Create a short docstring from boto3 documentation.

Trims docstring to 300 chars.
Removes double and triple backticks.
Stops on `**Request syntax**` and `::`.
Ensures that backticks are closed.
Replaces `Text <link>` with [Text](link).
Wraps docstring to 80 chars.

#### Signature

```python
def get_short_docstring(doc: str) -> str:
    ...
```



## is_reserved

[Show source in strings.py:103](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/strings.py#L103)

Check whether varialbe name conflicts with Python reserved names.

#### Signature

```python
def is_reserved(word: str) -> bool:
    ...
```


