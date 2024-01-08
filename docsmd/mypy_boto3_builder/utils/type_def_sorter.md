# TypeDefSorter

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Utils](./index.md#utils) / TypeDefSorter

> Auto-generated documentation for [mypy_boto3_builder.utils.type_def_sorter](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/type_def_sorter.py) module.

## TypeDefSorter

[Show source in type_def_sorter.py:12](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/type_def_sorter.py#L12)

Sorter for TypeDefs to prevent import errors.

#### Signature

```python
class TypeDefSorter:
    def __init__(self, type_defs: Iterable[TypeDefSortable]) -> None: ...
```

#### See also

- [TypeDefSortable](../type_annotations/type_def_sortable.md#typedefsortable)

### TypeDefSorter().sort

[Show source in type_def_sorter.py:40](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/type_def_sorter.py#L40)

Sort items with TopologicalSorter or stringify as a fallback.

#### Signature

```python
def sort(self) -> list[TypeDefSortable]: ...
```

#### See also

- [TypeDefSortable](../type_annotations/type_def_sortable.md#typedefsortable)
