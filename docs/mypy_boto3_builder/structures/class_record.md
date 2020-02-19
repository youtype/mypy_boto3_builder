# ClassRecord

> Auto-generated documentation for [mypy_boto3_builder.structures.class_record](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py) module.

Base class for all structures that can be rendered to a class.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / ClassRecord
    - [ClassRecord](#classrecord)
        - [ClassRecord().alias_name](#classrecordalias_name)
        - [ClassRecord().get_required_import_records](#classrecordget_required_import_records)
        - [ClassRecord().get_types](#classrecordget_types)
        - [ClassRecord().render_alias](#classrecordrender_alias)
        - [ClassRecord().render_type_var](#classrecordrender_type_var)
        - [ClassRecord().type_name](#classrecordtype_name)

## ClassRecord

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py#L15)

```python
dataclass
class ClassRecord():
```

Base class for all structures that can be rendered to a class.

### ClassRecord().alias_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py#L37)

```python
@property
def alias_name() -> str:
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

### ClassRecord().render_alias

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py#L52)

```python
def render_alias() -> str:
```

### ClassRecord().render_type_var

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py#L43)

```python
def render_type_var() -> str:
```

### ClassRecord().type_name

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py#L29)

```python
@property
def type_name() -> str:
```
