# ShapeParser

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](./index.md#parsers) / ShapeParser

> Auto-generated documentation for [mypy_boto3_builder.parsers.shape_parser](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py) module.

## ShapeParser

[Show source in shape_parser.py:112](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L112)

Parser for botocore shape files.

#### Arguments

- `session` - Boto3 session.
- `service_name` - ServiceName.

#### Signature

```python
class ShapeParser:
    def __init__(self, session: Session, service_name: ServiceName): ...
```

#### See also

- [ServiceName](../service_name.md#servicename)

### ShapeParser._get_streaming_body

[Show source in shape_parser.py:489](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L489)

Get the streaming member's shape if any; or None otherwise.

#### Signature

```python
@staticmethod
def _get_streaming_body(shape: Shape) -> Shape | None: ...
```

### ShapeParser().fix_method_arguments_for_mypy

[Show source in shape_parser.py:1024](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L1024)

Accept both input and output shapes in method arguments.

mypy does not compare TypedDicts, so we need to accept both input and output shapes.
https://github.com/youtype/mypy_boto3_builder/issues/209

#### Signature

```python
def fix_method_arguments_for_mypy(self, methods: Sequence[Method]) -> None: ...
```

#### See also

- [Method](../structures/method.md#method)

### ShapeParser().fix_typed_dict_names

[Show source in shape_parser.py:963](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L963)

Fix typed dict names to avoid duplicates.

#### Signature

```python
def fix_typed_dict_names(self) -> None: ...
```

### ShapeParser().get_client_method_map

[Show source in shape_parser.py:276](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L276)

Get client methods from shape.

#### Returns

A map of method name to Method.

#### Signature

```python
def get_client_method_map(self) -> dict[str, Method]: ...
```

#### See also

- [Method](../structures/method.md#method)

### ShapeParser().get_collection_batch_methods

[Show source in shape_parser.py:883](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L883)

Get batch operations for Resource collection.

#### Arguments

- `name` - Collection record name.
- `collection` - Boto3 Collection.
- `class_type` - Collection self type annotation.

#### Returns

List of Method records.

#### Signature

```python
def get_collection_batch_methods(
    self, name: str, collection: Collection
) -> list[Method]: ...
```

#### See also

- [Method](../structures/method.md#method)

### ShapeParser().get_collection_filter_method

[Show source in shape_parser.py:845](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L845)

Get `filter` classmethod for Resource collection.

#### Arguments

- `name` - Collection record name.
- `collection` - Boto3 Collection.
- `class_type` - Collection class type annotation.

#### Returns

Filter Method record.

#### Signature

```python
def get_collection_filter_method(
    self, name: str, collection: Collection, self_type: FakeAnnotation
) -> Method: ...
```

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)
- [Method](../structures/method.md#method)

### ShapeParser().get_paginate_method

[Show source in shape_parser.py:585](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L585)

Get Paginator `paginate` method.

#### Arguments

- `paginator_name` - Paginator name.

#### Returns

Method.

#### Signature

```python
def get_paginate_method(self, paginator_name: str) -> Method: ...
```

#### See also

- [Method](../structures/method.md#method)

### ShapeParser().get_paginator_names

[Show source in shape_parser.py:194](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L194)

Get available paginator names.

#### Returns

A list of paginator names.

#### Signature

```python
def get_paginator_names(self) -> list[str]: ...
```

### ShapeParser().get_resource_method_map

[Show source in shape_parser.py:709](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L709)

Get methods for Resource.

#### Arguments

- [ShapeParser().resource_name](#shapeparserresource_name) - Resource name.

#### Returns

A map of method name to Method.

#### Signature

```python
def get_resource_method_map(self, resource_name: str) -> dict[str, Method]: ...
```

#### See also

- [Method](../structures/method.md#method)

### ShapeParser().get_service_resource_method_map

[Show source in shape_parser.py:674](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L674)

Get methods for ServiceResource.

#### Returns

A map of method name to Method.

#### Signature

```python
def get_service_resource_method_map(self) -> dict[str, Method]: ...
```

#### See also

- [Method](../structures/method.md#method)

### ShapeParser().get_wait_method

[Show source in shape_parser.py:641](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L641)

Get Waiter `wait` method.

#### Arguments

- `waiter_name` - Waiter name.

#### Returns

Method.

#### Signature

```python
def get_wait_method(self, waiter_name: str) -> Method: ...
```

#### See also

- [Method](../structures/method.md#method)

### ShapeParser().parse_shape

[Show source in shape_parser.py:503](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L503)

Parse any botocore shape to TypeAnnotation.

#### Arguments

- `shape` - Botocore shape.
- `output` - Whether shape should use strict output types.
- `output_child` - Whether shape parent is marked as output.
- `is_streaming` - Whether shape should be streaming.

#### Returns

TypeAnnotation or similar class.

#### Signature

```python
def parse_shape(
    self,
    shape: Shape,
    output: bool = False,
    output_child: bool = False,
    is_streaming: bool = False,
) -> FakeAnnotation: ...
```

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)

### ShapeParser().resource_name

[Show source in shape_parser.py:152](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L152)

Parsed resource name.

#### Signature

```python
@property
def resource_name(self) -> str: ...
```



## ShapeParserError

[Show source in shape_parser.py:67](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L67)

Main error for ShapeParser.

#### Signature

```python
class ShapeParserError(Exception): ...
```



## TypedDictMap

[Show source in shape_parser.py:73](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L73)

Wrapper for TypedDict maps.

#### Signature

```python
class TypedDictMap(dict[str, TypeTypedDict]): ...
```

#### See also

- [TypeTypedDict](../type_annotations/type_typed_dict.md#typetypeddict)

### TypedDictMap().add

[Show source in shape_parser.py:78](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L78)

Add new item.

#### Signature

```python
def add(self, item: TypeTypedDict) -> None: ...
```

#### See also

- [TypeTypedDict](../type_annotations/type_typed_dict.md#typetypeddict)

### TypedDictMap().get_sorted_names

[Show source in shape_parser.py:103](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L103)

Get real TypedDict names topologically sorted.

#### Signature

```python
def get_sorted_names(self) -> list[str]: ...
```

### TypedDictMap().iterate_pairs

[Show source in shape_parser.py:84](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L84)

Iterate over pairs mathed by real dict name.

#### Signature

```python
def iterate_pairs(self, name: str) -> Iterator[tuple[str, TypeTypedDict]]: ...
```

#### See also

- [TypeTypedDict](../type_annotations/type_typed_dict.md#typetypeddict)

### TypedDictMap().rename

[Show source in shape_parser.py:92](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L92)

Rename item and change mapping.

#### Signature

```python
def rename(self, item: TypeTypedDict, new_name: str) -> None: ...
```

#### See also

- [TypeTypedDict](../type_annotations/type_typed_dict.md#typetypeddict)
