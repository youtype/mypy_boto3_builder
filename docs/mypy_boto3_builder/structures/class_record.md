# ClassRecord

> Auto-generated documentation for [mypy_boto3_builder.structures.class_record](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py) module.

Base class for all structures that can be rendered to a class.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / ClassRecord
    - [ClassRecord](#classrecord)
        - [ClassRecord().get_required_import_records](#classrecordget_required_import_records)
        - [ClassRecord().get_types](#classrecordget_types)

## ClassRecord

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py#L14)

```python
dataclass
class ClassRecord():
```

Base class for all structures that can be rendered to a class.

### ClassRecord().get_required_import_records

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py#L36)

```python
def get_required_import_records() -> Set[ImportRecord]:
```

### ClassRecord().get_types

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/structures/class_record.py#L26)

```python
def get_types() -> Set[FakeAnnotation]:
```
