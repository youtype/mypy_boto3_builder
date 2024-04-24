# Strings

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Utils](./index.md#utils) / Strings

> Auto-generated documentation for [mypy_boto3_builder.utils.strings](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/strings.py) module.

## capitalize

[Show source in strings.py:165](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/strings.py#L165)

Capitalize first letter of a string.

#### Signature

```python
def capitalize(s: str) -> str: ...
```



## clean_artifacts

[Show source in strings.py:87](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/strings.py#L87)

Remove common artifacts in botocre docs.

#### Signature

```python
def clean_artifacts(line: str) -> str: ...
```



## get_anchor_link

[Show source in strings.py:37](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/strings.py#L37)

Convert header to markdown anchor link.

#### Signature

```python
def get_anchor_link(text: str) -> str: ...
```



## get_botocore_class_name

[Show source in strings.py:137](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/strings.py#L137)

Get Botocore class name from Service metadata.

#### Signature

```python
def get_botocore_class_name(metadata: dict[str, str]) -> str: ...
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
def get_class_prefix(func_name: str) -> str: ...
```



## get_short_docstring

[Show source in strings.py:51](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/strings.py#L51)

Create a short docstring from boto3 documentation.

Trims docstring to 300 chars.
Removes double and triple backticks.
Stops on `**Request syntax**` and `::`.
Ensures that backticks are closed.
Replaces `Text <link>` with [Text](link).
Wraps docstring to 80 chars.

#### Signature

```python
def get_short_docstring(doc: str) -> str: ...
```



## get_type_def_name

[Show source in strings.py:148](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/strings.py#L148)

Get a valid Python TypeDef class name from `parts`.

#### Examples

```python
get_type_def_name("MyClass", "my_method")  # MyClassMyMethodTypeDef
```

#### Signature

```python
def get_type_def_name(*parts: str) -> str: ...
```



## is_reserved

[Show source in strings.py:44](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/strings.py#L44)

Check whether varialbe name conflicts with Python reserved names.

#### Signature

```python
def is_reserved(word: str) -> bool: ...
```



## textwrap

[Show source in strings.py:110](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/strings.py#L110)

Wrap text to `width` chars.

#### Signature

```python
def textwrap(text: str, width: int) -> str: ...
```
