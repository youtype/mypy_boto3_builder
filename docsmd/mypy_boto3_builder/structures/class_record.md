# ClassRecord

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Structures](./index.md#structures) /
ClassRecord

> Auto-generated documentation for [mypy_boto3_builder.structures.class_record](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/class_record.py) module.

## ClassRecord

[Show source in class_record.py:15](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/class_record.py#L15)

Base class for all structures that can be rendered to a class.

#### Signature

```python
class ClassRecord:
    def __init__(
        self,
        name: str,
        methods: Iterable[Method] = (),
        attributes: Iterable[Attribute] = (),
        bases: Iterable[FakeAnnotation] = (),
        use_alias: bool = False,
    ):
        ...
```

#### See also

- [Attribute](./attribute.md#attribute)
- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)
- [Method](./method.md#method)

### ClassRecord().alias_name

[Show source in class_record.py:44](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/class_record.py#L44)

Class alias name for safe import.

#### Signature

```python
@property
def alias_name(self) -> str:
    ...
```

### ClassRecord().boto3_doc_link

[Show source in class_record.py:37](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/class_record.py#L37)

Link to boto3 docs.

#### Signature

```python
@property
def boto3_doc_link(self) -> str:
    ...
```

### ClassRecord().get_internal_imports

[Show source in class_record.py:85](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/class_record.py#L85)

Get internal imports from methods.

#### Signature

```python
def get_internal_imports(self) -> set[InternalImport]:
    ...
```

#### See also

- [InternalImport](../type_annotations/internal_import.md#internalimport)

### ClassRecord().get_method

[Show source in class_record.py:112](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/class_record.py#L112)

Get method by name.

#### Signature

```python
def get_method(self, name: str) -> Method:
    ...
```

#### See also

- [Method](./method.md#method)

### ClassRecord().get_required_import_records

[Show source in class_record.py:72](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/class_record.py#L72)

Extract import records from required type annotations.

#### Signature

```python
def get_required_import_records(self) -> set[ImportRecord]:
    ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### ClassRecord().iterate_types

[Show source in class_record.py:61](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/class_record.py#L61)

Iterate over type annotations for methods, attributes and bases.

#### Signature

```python
def iterate_types(self) -> Iterator[FakeAnnotation]:
    ...
```

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)

### ClassRecord().method_names

[Show source in class_record.py:105](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/class_record.py#L105)

Unique method names.

#### Signature

```python
@property
def method_names(self) -> list[str]:
    ...
```

### ClassRecord().render_alias

[Show source in class_record.py:55](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/class_record.py#L55)

Render alias expression.

#### Signature

```python
def render_alias(self) -> str:
    ...
```

### ClassRecord().variable_name

[Show source in class_record.py:98](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/class_record.py#L98)

Variable name for an instance of this class.

#### Signature

```python
@property
def variable_name(self) -> str:
    ...
```
