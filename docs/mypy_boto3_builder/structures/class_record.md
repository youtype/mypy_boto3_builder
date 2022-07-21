# ClassRecord

[mypy-boto3-builder Index](../../README.md#mypy-boto3-builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Structures](./index.md#structures) /
ClassRecord

> Auto-generated documentation for [mypy_boto3_builder.structures.class_record](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/class_record.py) module.

- [ClassRecord](#classrecord)
  - [ClassRecord](#classrecord-1)
    - [ClassRecord().alias_name](#classrecord()alias_name)
    - [ClassRecord().boto3_doc_link](#classrecord()boto3_doc_link)
    - [ClassRecord().get_internal_imports](#classrecord()get_internal_imports)
    - [ClassRecord().get_method](#classrecord()get_method)
    - [ClassRecord().get_required_import_records](#classrecord()get_required_import_records)
    - [ClassRecord().iterate_types](#classrecord()iterate_types)
    - [ClassRecord().method_names](#classrecord()method_names)
    - [ClassRecord().render_alias](#classrecord()render_alias)
    - [ClassRecord().variable_name](#classrecord()variable_name)

## ClassRecord

[Show source in class_record.py:16](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/class_record.py#L16)

Base class for all structures that can be rendered to a class.

#### Signature

```python
class ClassRecord:
    def __init__(
        self,
        name: str,
        methods: Iterable[Method] = tuple(),
        attributes: Iterable[Attribute] = tuple(),
        bases: Iterable[FakeAnnotation] = tuple(),
        use_alias: bool = False,
    ):
        ...
```

#### See also

- [Attribute](./attribute.md#attribute)
- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)
- [Method](./method.md#method)

### ClassRecord().alias_name

[Show source in class_record.py:45](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/class_record.py#L45)

Class alias name for safe import.

#### Signature

```python
@property
def alias_name(self) -> str:
    ...
```

### ClassRecord().boto3_doc_link

[Show source in class_record.py:38](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/class_record.py#L38)

Link to boto3 docs.

#### Signature

```python
@property
def boto3_doc_link(self) -> str:
    ...
```

### ClassRecord().get_internal_imports

[Show source in class_record.py:86](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/class_record.py#L86)

Get internal imports from methods.

#### Signature

```python
def get_internal_imports(self) -> set[InternalImport]:
    ...
```

#### See also

- [InternalImport](../type_annotations/internal_import.md#internalimport)

### ClassRecord().get_method

[Show source in class_record.py:113](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/class_record.py#L113)

Get method by name.

#### Signature

```python
def get_method(self, name: str) -> Method:
    ...
```

#### See also

- [Method](./method.md#method)

### ClassRecord().get_required_import_records

[Show source in class_record.py:73](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/class_record.py#L73)

Extract import records from required type annotations.

#### Signature

```python
def get_required_import_records(self) -> set[ImportRecord]:
    ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### ClassRecord().iterate_types

[Show source in class_record.py:62](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/class_record.py#L62)

Iterate over type annotations for methods, attributes and bases.

#### Signature

```python
def iterate_types(self) -> Iterator[FakeAnnotation]:
    ...
```

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)

### ClassRecord().method_names

[Show source in class_record.py:106](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/class_record.py#L106)

Unique method names.

#### Signature

```python
@property
def method_names(self) -> list[str]:
    ...
```

### ClassRecord().render_alias

[Show source in class_record.py:56](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/class_record.py#L56)

Render alias expression.

#### Signature

```python
def render_alias(self) -> str:
    ...
```

### ClassRecord().variable_name

[Show source in class_record.py:99](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/class_record.py#L99)

Variable name for an instance of this class.

#### Signature

```python
@property
def variable_name(self) -> str:
    ...
```


