# TypeTypedDict

> Auto-generated documentation for [mypy_boto3_builder.type_annotations.type_typed_dict](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py) module.

Wrapper for `typing/typing_extensions.TypedDict` type annotations.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Annotations](index.md#type-annotations) / TypeTypedDict
    - [TypeTypedDict](#typetypeddict)
        - [TypeTypedDict().add_attribute](#typetypeddictadd_attribute)
        - [TypeTypedDict().copy](#typetypeddictcopy)
        - [TypeTypedDict().get_attribute](#typetypeddictget_attribute)
        - [TypeTypedDict().get_children_literals](#typetypeddictget_children_literals)
        - [TypeTypedDict().get_children_typed_dicts](#typetypeddictget_children_typed_dicts)
        - [TypeTypedDict().get_children_types](#typetypeddictget_children_types)
        - [TypeTypedDict().get_import_record](#typetypeddictget_import_record)
        - [TypeTypedDict().get_optional](#typetypeddictget_optional)
        - [TypeTypedDict().get_required](#typetypeddictget_required)
        - [TypeTypedDict().get_sort_key](#typetypeddictget_sort_key)
        - [TypeTypedDict().has_both](#typetypeddicthas_both)
        - [TypeTypedDict().has_optional](#typetypeddicthas_optional)
        - [TypeTypedDict().has_required](#typetypeddicthas_required)
        - [TypeTypedDict().is_dict](#typetypeddictis_dict)
        - [TypeTypedDict().is_same](#typetypeddictis_same)
        - [TypeTypedDict().is_typed_dict](#typetypeddictis_typed_dict)
        - [TypeTypedDict().render](#typetypeddictrender)
        - [TypeTypedDict().render_class](#typetypeddictrender_class)
        - [TypeTypedDict().replace_self_references](#typetypeddictreplace_self_references)
        - [TypeTypedDict().requires_safe_render](#typetypeddictrequires_safe_render)
    - [TypedDictAttribute](#typeddictattribute)
        - [TypedDictAttribute().render](#typeddictattributerender)

## TypeTypedDict

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L39)

```python
class TypeTypedDict(FakeAnnotation):
    def __init__(
        name: str,
        children: Iterable[TypedDictAttribute] = (),
        docstring: str = '',
        stringify: bool = False,
        replace_with_dict: Iterable[str] = tuple(),
    ) -> None:
```

Wrapper for `typing/typing_extensions.TypedDict` type annotations.

#### Arguments

- `name` - Type name.
- `children` - Typed dict attributes.
- `docstring` - Docstring for render.
- `stringify` - Convert type annotation to string to avoid circular deps.
- `replace_with_dict` - Render Dict[str, Any] instead to avoid circular dependencies.

#### See also

- [FakeAnnotation](fake_annotation.md#fakeannotation)

### TypeTypedDict().add_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L116)

```python
def add_attribute(
    name: str,
    type_annotation: FakeAnnotation,
    required: bool,
) -> None:
```

Add new attribute to a dictionary.

#### Arguments

- `name` - Argument name.
- `type_annotation` - Argument type annotation.
- `required` - Whether argument has to be set.

#### See also

- [FakeAnnotation](fake_annotation.md#fakeannotation)

### TypeTypedDict().copy

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L190)

```python
def copy() -> 'TypeTypedDict':
```

Create a copy of type annotation wrapper.

### TypeTypedDict().get_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L76)

```python
def get_attribute(name: str) -> TypedDictAttribute:
```

Find attribute by `name`.

#### Arguments

- `name` - Attribute name.

#### Returns

Found attribute.

#### See also

- [TypedDictAttribute](#typeddictattribute)

### TypeTypedDict().get_children_literals

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L232)

```python
def get_children_literals(
    processed: Iterable['TypeTypedDict'] = tuple(),
) -> Set[TypeLiteral]:
```

Extract required TypeLiteral list from attributes.

### TypeTypedDict().get_children_typed_dicts

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L219)

```python
def get_children_typed_dicts() -> Set['TypeTypedDict']:
```

Extract required TypeTypedDict list from attributes.

### TypeTypedDict().get_children_types

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L210)

```python
def get_children_types() -> Set[FakeAnnotation]:
```

Extract required type annotatyions from attributes.

### TypeTypedDict().get_import_record

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L110)

```python
def get_import_record() -> ImportRecord:
```

Get import record required for using type annotation.

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### TypeTypedDict().get_optional

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L180)

```python
def get_optional() -> List[TypedDictAttribute]:
```

Get a list of optional attributes.

### TypeTypedDict().get_required

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L170)

```python
def get_required() -> List[TypedDictAttribute]:
```

Get a list of required attributes.

### TypeTypedDict().get_sort_key

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L65)

```python
def get_sort_key() -> str:
```

Sort Typed Dicts by name.

### TypeTypedDict().has_both

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L164)

```python
def has_both() -> bool:
```

Whether TypedDict has both optional and required keys.

### TypeTypedDict().has_optional

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L146)

```python
def has_optional() -> bool:
```

Whether TypedDict has optional keys.

### TypeTypedDict().has_required

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L155)

```python
def has_required() -> bool:
```

Whether TypedDict has required keys.

### TypeTypedDict().is_dict

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L127)

```python
def is_dict() -> bool:
```

Always True as it is a TypedDict.

### TypeTypedDict().is_same

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L202)

```python
def is_same(other: 'TypeTypedDict') -> bool:
```

Check whether typed dict attributes are the same as `other`.

### TypeTypedDict().is_typed_dict

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L133)

```python
def is_typed_dict() -> bool:
```

Always True as it is a TypedDict.

### TypeTypedDict().render

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L92)

```python
def render(parent_name: str = '') -> str:
```

Render type annotation to a valid Python code for local usage.

#### Returns

A string with a valid type annotation.

### TypeTypedDict().render_class

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L139)

```python
def render_class() -> str:
```

Render class-based definition for debugging.

### TypeTypedDict().replace_self_references

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L249)

```python
def replace_self_references() -> None:
```

Replace self refenrences with `Dict[str, Any]` to avoid circular dependencies.

### TypeTypedDict().requires_safe_render

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L264)

```python
@property
def requires_safe_render() -> bool:
```

Whether TypedDict has reserved words and has to be rendered safely.

## TypedDictAttribute

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L14)

```python
class TypedDictAttribute():
    def __init__(name: str, type_annotation: FakeAnnotation, required: bool):
```

TypedDict attribute wrapper.

#### Arguments

- `name` - Attribute name.
- `type_annotation` - Attribute type annotation.
- `required` - Whether the attribute has to be set.

#### See also

- [FakeAnnotation](fake_annotation.md#fakeannotation)

### TypedDictAttribute().render

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L29)

```python
def render() -> str:
```

Render attribute to use in class-based TypedDict definition.

#### Returns

A string with argument definition.
