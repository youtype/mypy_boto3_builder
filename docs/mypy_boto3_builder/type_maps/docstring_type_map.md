# Docstring Type Map

[mypy-boto3-builder Index](../../README.md#mypy-boto3-builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Type Maps](./index.md#type-maps) /
Docstring Type Map

> Auto-generated documentation for [mypy_boto3_builder.type_maps.docstring_type_map](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_maps/docstring_type_map.py) module.

- [Docstring Type Map](#docstring-type-map)
  - [get_type_from_docstring](#get_type_from_docstring)

## get_type_from_docstring

[Show source in docstring_type_map.py:458](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_maps/docstring_type_map.py#L458)

Get type annotation for a string extracted from docstring.

#### Arguments

- `type_str` - Type name in docstring.

#### Raises

- `ValueError` - If type_str not found in map.

#### Signature

```python
def get_type_from_docstring(type_str: str) -> FakeAnnotation:
    ...
```

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)


