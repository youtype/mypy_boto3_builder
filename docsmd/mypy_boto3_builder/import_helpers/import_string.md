# ImportString

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Import Helpers](./index.md#import-helpers) /
ImportString

> Auto-generated documentation for [mypy_boto3_builder.import_helpers.import_string](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py) module.

## ImportString

[Show source in import_string.py:9](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py#L9)

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

[Show source in import_string.py:47](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py#L47)

Create an empty ImportString.

#### Signature

```python
@classmethod
def empty(cls: type[_R]) -> _R:
    ...
```

### ImportString.from_str

[Show source in import_string.py:40](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py#L40)

Create from string.

#### Signature

```python
@classmethod
def from_str(cls, import_string: str) -> "ImportString":
    ...
```

### ImportString().master_name

[Show source in import_string.py:126](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py#L126)

Get first import string part or `builtins`.

#### Signature

```python
@property
def master_name(self) -> str:
    ...
```

### ImportString.parent

[Show source in import_string.py:56](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py#L56)

Get parent ImportString.

#### Signature

```python
@classmethod
def parent(cls: type[_R]) -> _R:
    ...
```

### ImportString().render

[Show source in import_string.py:117](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py#L117)

Render to string.

#### Returns

Ready to use import string.

#### Signature

```python
def render(self) -> str:
    ...
```

### ImportString().startswith

[Show source in import_string.py:85](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/import_helpers/import_string.py#L85)

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
