# Docstring Type Map

> Auto-generated documentation for [mypy_boto3_builder.type_maps.docstring_type_map](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_maps/docstring_type_map.py) module.

String to type annotation map that find type annotation by argument name and type.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Maps](index.md#type-maps) / Docstring Type Map
    - [get_type_from_docstring](#get_type_from_docstring)

## get_type_from_docstring

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_maps/docstring_type_map.py#L534)

```python
def get_type_from_docstring(type_str: str) -> FakeAnnotation:
```

Get type annotation for a string extracted from docstring.

#### Arguments

- `type_str` - Type name in docstring.

#### Raises

- `ValueError` - If type_str not found in map.

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)
