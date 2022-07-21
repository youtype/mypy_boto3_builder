# TypedDictSorter

[mypy-boto3-builder Index](../../README.md#mypy-boto3-builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Utils](./index.md#utils) /
TypedDictSorter

> Auto-generated documentation for [mypy_boto3_builder.utils.typed_dict_sorter](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/typed_dict_sorter.py) module.

- [TypedDictSorter](#typeddictsorter)
  - [TypedDictSorter](#typeddictsorter-1)
    - [TypedDictSorter().sort](#typeddictsorter()sort)

## TypedDictSorter

[Show source in typed_dict_sorter.py:11](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/typed_dict_sorter.py#L11)

Sorter for TypeTypedDict to prevent import errors.

#### Signature

```python
class TypedDictSorter:
    def __init__(self, typed_dicts: Iterable[TypeTypedDict]):
        ...
```

#### See also

- [TypeTypedDict](../type_annotations/type_typed_dict.md#typetypeddict)

### TypedDictSorter().sort

[Show source in typed_dict_sorter.py:38](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/typed_dict_sorter.py#L38)

Sort items with TopologicalSorter or stringify as a fallback.

#### Signature

```python
def sort(self) -> list[TypeTypedDict]:
    ...
```

#### See also

- [TypeTypedDict](../type_annotations/type_typed_dict.md#typetypeddict)


