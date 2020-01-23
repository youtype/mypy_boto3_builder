# Client

> Auto-generated documentation for [mypy_boto3_builder.parsers.client](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/parsers/client.py) module.

Boto3 client parser, produces `structures.Client`.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Parsers](index.md#parsers) / Client
    - [parse_client](#parse_client)

## parse_client

[[find in source code]](https://github.com/vemel/mypy_boto3_builder/blob/master/mypy_boto3_builder/parsers/client.py#L22)

```python
def parse_client(
    session: Session,
    service_name: ServiceName,
    shape_parser: ShapeParser,
) -> Client:
```

Parse boto3 client to a structure.

#### Arguments

- `session` - boto3 session.
- `service_name` - Target service name.

#### Returns

Client structure.

#### See also

- [Client](../structures/client.md#client)
- [ServiceName](../service_name.md#servicename)
- [ShapeParser](shape_parser.md#shapeparser)
