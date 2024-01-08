# ClassRecord

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](./index.md#structures) / ClassRecord

> Auto-generated documentation for [mypy_boto3_builder.structures.class_record](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/class_record.py) module.

## ClassRecord

[Show source in class_record.py:16](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/class_record.py#L16)

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
    ): ...
```

#### See also

- [Attribute](./attribute.md#attribute)
- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)
- [Method](./method.md#method)

### ClassRecord().alias_name

[Show source in class_record.py:43](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/class_record.py#L43)

Class alias name for safe import.

#### Returns

Name prefixed with underscore.

#### Signature

```python
@property
def alias_name(self) -> str: ...
```

### ClassRecord().boto3_doc_link

[Show source in class_record.py:36](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/class_record.py#L36)

Link to boto3 docs.

#### Signature

```python
@property
def boto3_doc_link(self) -> str: ...
```

### ClassRecord().get_internal_imports

[Show source in class_record.py:77](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/class_record.py#L77)

Get internal imports from methods.

#### Signature

```python
def get_internal_imports(self) -> set[InternalImport]: ...
```

#### See also

- [InternalImport](../type_annotations/internal_import.md#internalimport)

### ClassRecord().get_method

[Show source in class_record.py:104](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/class_record.py#L104)

Get method by name.

#### Signature

```python
def get_method(self, name: str) -> Method: ...
```

#### See also

- [Method](./method.md#method)

### ClassRecord().get_required_import_records

[Show source in class_record.py:67](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/class_record.py#L67)

Extract import records from required type annotations.

#### Signature

```python
def get_required_import_records(self) -> set[ImportRecord]: ...
```

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### ClassRecord().iterate_types

[Show source in class_record.py:56](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/class_record.py#L56)

Iterate over type annotations for methods, attributes and bases.

#### Signature

```python
def iterate_types(self) -> Iterator[FakeAnnotation]: ...
```

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)

### ClassRecord().method_names

[Show source in class_record.py:97](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/class_record.py#L97)

Unique method names.

#### Signature

```python
@property
def method_names(self) -> list[str]: ...
```

### ClassRecord().variable_name

[Show source in class_record.py:90](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/class_record.py#L90)

Variable name for an instance of this class.

#### Signature

```python
@property
def variable_name(self) -> str: ...
```
