# ImportString

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Import Helpers](./index.md#import-helpers) /
ImportString

> Auto-generated documentation for [mypy_boto3_builder.import_helpers.import_string](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py) module.

## ImportString

[Show source in import_string.py:11](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py#L11)

Wrapper for Python import strings.

#### Arguments

- `master` - Master module name
- `parts` - Other import parts

#### Examples

```python
import_string = ImportString("my", "name")

str(import_string)
'my.name'

import_string.render()
'my.name'

import_string.parts.append('test')
import_string.render()
'my.name.test'
```

#### Signature

```python
class ImportString:
    def __init__(self, master_name: str, *parts: str) -> None:
        ...
```

### ImportString.empty

[Show source in import_string.py:49](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py#L49)

Create an empty ImportString.

#### Signature

```python
@classmethod
def empty(cls: type[_R]) -> _R:
    ...
```

### ImportString.from_str

[Show source in import_string.py:42](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py#L42)

Create from string.

#### Signature

```python
@classmethod
def from_str(cls: type[_R], import_string: str) -> _R:
    ...
```

### ImportString().master_name

[Show source in import_string.py:128](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py#L128)

Get first import string part or `builtins`.

#### Signature

```python
@property
def master_name(self) -> str:
    ...
```

### ImportString.parent

[Show source in import_string.py:58](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py#L58)

Get parent ImportString.

#### Signature

```python
@classmethod
def parent(cls: type[_R]) -> _R:
    ...
```

### ImportString().render

[Show source in import_string.py:119](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py#L119)

Render to string.

#### Returns

Ready to use import string.

#### Signature

```python
def render(self) -> str:
    ...
```

### ImportString().startswith

[Show source in import_string.py:87](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py#L87)

Check if import string starts with `other`.

#### Examples

```python
ImportString('my', 'name').startswith(ImportString('my'))
True

ImportString('my_module', 'name').startswith(ImportString('my'))
False

ImportString('my', 'name').startswith(ImportString('my, 'name'))
True

ImportString('my', 'name').startswith(ImportString.empty())
True
```

#### Arguments

- `other` - Other import string.

#### Signature

```python
def startswith(self: _R, other: _R) -> bool:
    ...
```
