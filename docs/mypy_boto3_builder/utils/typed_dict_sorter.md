# TypedDictSorter

> Auto-generated documentation for [mypy_boto3_builder.utils.typed_dict_sorter](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/typed_dict_sorter.py) module.

Sorter for TypeTypedDict to prevent import errors.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Utils](index.md#utils) / TypedDictSorter
    - [TypedDictSorter](#typeddictsorter)
        - [TypedDictSorter().sort](#typeddictsortersort)

## TypedDictSorter

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/typed_dict_sorter.py#L11)

```python
class TypedDictSorter():
    def __init__(typed_dicts: Iterable[TypeTypedDict]):
```

Sorter for TypeTypedDict to prevent import errors.

#### See also

- [TypeTypedDict](../type_annotations/type_typed_dict.md#typetypeddict)

### TypedDictSorter().sort

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/typed_dict_sorter.py#L38)

```python
def sort() -> list[TypeTypedDict]:
```

Sort items with TopologicalSorter or stringify as a fallback.

#### See also

- [TypeTypedDict](../type_annotations/type_typed_dict.md#typetypeddict)
