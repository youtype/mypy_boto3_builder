# ClassRecord

> Auto-generated documentation for [mypy_boto3_builder.structures.class_record](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py) module.

Base class for all structures that can be rendered to a class.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / ClassRecord
    - [ClassRecord](#classrecord)
        - [ClassRecord().alias_name](#classrecordalias_name)
        - [ClassRecord().boto3_doc_link](#classrecordboto3_doc_link)
        - [ClassRecord().docstring](#classrecorddocstring)
        - [ClassRecord().get_internal_imports](#classrecordget_internal_imports)
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

### ClassRecord().alias_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py#L44)

```python
@property
def alias_name() -> str:
```

### ClassRecord().boto3_doc_link

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py#L36)

```python
@property
def boto3_doc_link() -> str:
```

### ClassRecord().docstring

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py#L40)

```python
@property
def docstring() -> str:
```

### ClassRecord().get_internal_imports

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py#L75)

```python
def get_internal_imports() -> List[InternalImport]:
```

### ClassRecord().get_required_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py#L65)

```python
def get_required_import_records() -> Set[ImportRecord]:
```

### ClassRecord().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py#L55)

```python
def get_types() -> Set[FakeAnnotation]:
```

### ClassRecord().method_names

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py#L92)

```python
@property
def method_names() -> List[str]:
```

Unique method names.

### ClassRecord().render_alias

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py#L52)

```python
def render_alias() -> str:
```

### ClassRecord().variable_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py#L85)

```python
@property
def variable_name() -> str:
```

Get a proper variable name for an instance of this class.
