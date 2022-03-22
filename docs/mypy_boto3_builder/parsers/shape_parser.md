# ShapeParser

> Auto-generated documentation for [mypy_boto3_builder.parsers.shape_parser](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py) module.

Parser for botocore shape files.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](index.md#parsers) / ShapeParser
    - [ShapeParser](#shapeparser)
        - [ShapeParser().get_client_method_map](#shapeparserget_client_method_map)
        - [ShapeParser().get_collection_batch_methods](#shapeparserget_collection_batch_methods)
        - [ShapeParser().get_collection_filter_method](#shapeparserget_collection_filter_method)
        - [ShapeParser().get_paginate_method](#shapeparserget_paginate_method)
        - [ShapeParser().get_paginator_names](#shapeparserget_paginator_names)
        - [ShapeParser().get_resource_method_map](#shapeparserget_resource_method_map)
        - [ShapeParser().get_service_resource_method_map](#shapeparserget_service_resource_method_map)
        - [ShapeParser().get_wait_method](#shapeparserget_wait_method)
        - [ShapeParser().parse_shape](#shapeparserparse_shape)
    - [ShapeParserError](#shapeparsererror)

## ShapeParser

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L50)

```python
class ShapeParser():
    def __init__(session: Session, service_name: ServiceName):
```

Parser for botocore shape files.

#### Arguments

- `session` - Boto3 session.
- `service_name` - ServiceName.

#### See also

- [ServiceName](../service_name.md#servicename)

### ShapeParser().get_client_method_map

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L270)

```python
def get_client_method_map() -> dict[str, Method]:
```

Get client methods from shape.

#### Returns

A map of method name to Method.

#### See also

- [Method](../structures/method.md#method)

### ShapeParser().get_collection_batch_methods

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L736)

```python
def get_collection_batch_methods(
    name: str,
    collection: Collection,
) -> list[Method]:
```

Get batch operations for Resource collection.

#### Arguments

- `name` - Collection record name.
- `collection` - Boto3 Collection.
- `class_type` - Collection self type annotation.

#### Returns

List of Method records.

#### See also

- [Method](../structures/method.md#method)

### ShapeParser().get_collection_filter_method

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L698)

```python
def get_collection_filter_method(
    name: str,
    collection: Collection,
    self_type: FakeAnnotation,
) -> Method:
```

Get `filter` classmethod for Resource collection.

#### Arguments

- `name` - Collection record name.
- `collection` - Boto3 Collection.
- `class_type` - Collection class type annotation.

#### Returns

Filter Method record.

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)
- [Method](../structures/method.md#method)

### ShapeParser().get_paginate_method

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L487)

```python
def get_paginate_method(paginator_name: str) -> Method:
```

Get Paginator `paginate` method.

#### Arguments

- `paginator_name` - Paginator name.

#### Returns

Method.

#### See also

- [Method](../structures/method.md#method)

### ShapeParser().get_paginator_names

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L169)

```python
def get_paginator_names() -> list[str]:
```

Get available paginator names.

#### Returns

A list of paginator names.

### ShapeParser().get_resource_method_map

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L583)

```python
def get_resource_method_map(resource_name: str) -> dict[str, Method]:
```

Get methods for Resource.

#### Arguments

- `resource_name` - Resource name.

#### Returns

A map of method name to Method.

#### See also

- [Method](../structures/method.md#method)

### ShapeParser().get_service_resource_method_map

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L562)

```python
def get_service_resource_method_map() -> dict[str, Method]:
```

Get methods for ServiceResource.

#### Returns

A map of method name to Method.

#### See also

- [Method](../structures/method.md#method)

### ShapeParser().get_wait_method

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L535)

```python
def get_wait_method(waiter_name: str) -> Method:
```

Get Waiter `wait` method.

#### Arguments

- `waiter_name` - Waiter name.

#### Returns

Method.

#### See also

- [Method](../structures/method.md#method)

### ShapeParser().parse_shape

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L425)

```python
def parse_shape(
    shape: Shape,
    output: bool = False,
    output_child: bool = False,
    is_streaming: bool = False,
) -> FakeAnnotation:
```

Parse any botocore shape to TypeAnnotation.

#### Arguments

- `shape` - Botocore shape.
- `output` - Whether shape should use strict output types.
- `output_child` - Whether shape parent is marked as output.
- `is_streaming` - Whether shape should be streaming.

#### Returns

TypeAnnotation or similar class.

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)

## ShapeParserError

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/main/mypy_boto3_builder/parsers/shape_parser.py#L44)

```python
class ShapeParserError(Exception):
```

Main error for ShapeParser.
