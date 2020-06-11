# TypeTypedDict

> Auto-generated documentation for [mypy_boto3_builder.type_annotations.type_typed_dict](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py) module.

Wrapper for `typing/typing_extensions.TypedDict` type annotations.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Annotations](index.md#type-annotations) / TypeTypedDict
    - [TypeTypedDict](#typetypeddict)
        - [TypeTypedDict().add_attribute](#typetypeddictadd_attribute)
        - [TypeTypedDict().copy](#typetypeddictcopy)
        - [TypeTypedDict().get_attribute](#typetypeddictget_attribute)
        - [TypeTypedDict().get_children_typed_dicts](#typetypeddictget_children_typed_dicts)
        - [TypeTypedDict().get_children_types](#typetypeddictget_children_types)
        - [TypeTypedDict().get_import_record](#typetypeddictget_import_record)
        - [TypeTypedDict().get_optional](#typetypeddictget_optional)
        - [TypeTypedDict().get_required](#typetypeddictget_required)
        - [TypeTypedDict().get_types](#typetypeddictget_types)
        - [TypeTypedDict().has_both](#typetypeddicthas_both)
        - [TypeTypedDict().has_optional](#typetypeddicthas_optional)
        - [TypeTypedDict().has_required](#typetypeddicthas_required)
        - [TypeTypedDict().is_dict](#typetypeddictis_dict)
        - [TypeTypedDict().is_same](#typetypeddictis_same)
        - [TypeTypedDict().render](#typetypeddictrender)
        - [TypeTypedDict().render_class](#typetypeddictrender_class)
        - [TypeTypedDict().replace_self_references](#typetypeddictreplace_self_references)
    - [TypedDictAttribute](#typeddictattribute)
        - [TypedDictAttribute().render](#typeddictattributerender)

## TypeTypedDict

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L38)

```python
class TypeTypedDict(FakeAnnotation):
    def __init__(
        name: str,
        children: Iterable[TypedDictAttribute] = (),
        docstring: str = '',
        stringify: bool = False,
        replace_with_dict: bool = False,
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

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L109)

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

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L171)

```python
def copy() -> 'TypeTypedDict':
```

Create a copy of type annotation wrapper.

### TypeTypedDict().get_attribute

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L64)

```python
def get_attribute(name: str) -> TypedDictAttribute:
```

#### See also

- [TypedDictAttribute](#typeddictattribute)

### TypeTypedDict().get_children_typed_dicts

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L194)

```python
def get_children_typed_dicts() -> Set['TypeTypedDict']:
```

### TypeTypedDict().get_children_types

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L188)

```python
def get_children_types() -> Set[FakeAnnotation]:
```

### TypeTypedDict().get_import_record

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L89)

```python
def get_import_record() -> ImportRecord:
```

Get import record required for using type annotation.

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### TypeTypedDict().get_optional

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L164)

```python
def get_optional() -> List[TypedDictAttribute]:
```

### TypeTypedDict().get_required

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L157)

```python
def get_required() -> List[TypedDictAttribute]:
```

### TypeTypedDict().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L95)

```python
def get_types() -> Set[FakeAnnotation]:
```

Get set with itself.

To get child types, [TypeTypedDict().get_children_types](#typetypeddictget_children_types) has to be used.

#### Returns

A set of type annotations.

### TypeTypedDict().has_both

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L151)

```python
def has_both() -> bool:
```

Whether TypedDict has both optional and required keys.

### TypeTypedDict().has_optional

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L133)

```python
def has_optional() -> bool:
```

Whether TypedDict has optional keys.

### TypeTypedDict().has_required

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L142)

```python
def has_required() -> bool:
```

Whether TypedDict has required keys.

### TypeTypedDict().is_dict

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L120)

```python
def is_dict() -> bool:
```

Always True as it is a TypedDict.

### TypeTypedDict().is_same

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L183)

```python
def is_same(other: 'TypeTypedDict') -> bool:
```

### TypeTypedDict().render

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L71)

```python
def render(parent_name: str = '') -> str:
```

Render type annotation to a valid Python code for local usage.

#### Returns

A string with a valid type annotation.

### TypeTypedDict().render_class

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L126)

```python
def render_class() -> str:
```

Render class-based definition for debugging.

### TypeTypedDict().replace_self_references

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L204)

```python
def replace_self_references() -> None:
```

## TypedDictAttribute

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L13)

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

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/type_annotations/type_typed_dict.py#L28)

```python
def render() -> str:
```

Render attribute to use in class-based TypedDict definition.

#### Returns

A string with argument definition.
