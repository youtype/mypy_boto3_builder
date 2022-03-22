# ClassRecord

> Auto-generated documentation for [mypy_boto3_builder.structures.class_record](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py) module.

Base class for all structures that can be rendered to a class.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / ClassRecord
    - [ClassRecord](#classrecord)
        - [ClassRecord().alias_name](#classrecordalias_name)
        - [ClassRecord().boto3_doc_link](#classrecordboto3_doc_link)
        - [ClassRecord().get_internal_imports](#classrecordget_internal_imports)
        - [ClassRecord().get_method](#classrecordget_method)
        - [ClassRecord().get_required_import_records](#classrecordget_required_import_records)
        - [ClassRecord().get_types](#classrecordget_types)
        - [ClassRecord().method_names](#classrecordmethod_names)
        - [ClassRecord().render_alias](#classrecordrender_alias)
        - [ClassRecord().variable_name](#classrecordvariable_name)

## ClassRecord

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py#L15)

```python
class ClassRecord():
    def __init__(
        name: str,
        methods: Iterable[Method] = tuple(),
        attributes: Iterable[Attribute] = tuple(),
        bases: Iterable[FakeAnnotation] = tuple(),
        use_alias: bool = False,
    ):
```

Base class for all structures that can be rendered to a class.

#### See also

- [Attribute](attribute.md#attribute)
- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)
- [Method](method.md#method)

### ClassRecord().alias_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py#L44)

```python
@property
def alias_name() -> str:
```

Class alias name for safe import.

### ClassRecord().boto3_doc_link

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py#L37)

```python
@property
def boto3_doc_link() -> str:
```

Link to boto3 docs.

### ClassRecord().get_internal_imports

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py#L87)

```python
def get_internal_imports() -> list[InternalImport]:
```

Get internal imports from methods.

#### See also

- [InternalImport](../type_annotations/internal_import.md#internalimport)

### ClassRecord().get_method

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py#L114)

```python
def get_method(name: str) -> Method:
```

Get method by name.

#### See also

- [Method](method.md#method)

### ClassRecord().get_required_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py#L74)

```python
def get_required_import_records() -> set[ImportRecord]:
```

Extract import records from required type annotations.

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### ClassRecord().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py#L61)

```python
def get_types() -> set[FakeAnnotation]:
```

Extract type annotations for methods, attributes and bases.

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)

### ClassRecord().method_names

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py#L107)

```python
@property
def method_names() -> list[str]:
```

Unique method names.

### ClassRecord().render_alias

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py#L55)

```python
def render_alias() -> str:
```

Render alias expression.

### ClassRecord().variable_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py#L100)

```python
@property
def variable_name() -> str:
```

Variable name for an instance of this class.
