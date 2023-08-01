# Typed Dicts

[Mypy_boto3_builder Index](../../README.md#mypy_boto3_builder-index) /
[Mypy Boto3 Builder](../index.md#mypy-boto3-builder) /
[Type Maps](./index.md#type-maps) /
Typed Dicts

> Auto-generated documentation for [mypy_boto3_builder.type_maps.typed_dicts](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_maps/typed_dicts.py) module.

#### Attributes

- `CopySourceTypeDef` - s3: `TypeTypedDict('CopySourceTypeDef', [TypedDictAttribute('Bucket', Type.str, True), TypedDictAttribute('Key', Type.str, True), TypedDictAttribute('VersionId', Type.str, False)])`

- `TagTypeDef` - ec2: `TypeTypedDict('TagTypeDef', [TypedDictAttribute('Key', Type.str, False), TypedDictAttribute('Value', Type.str, False)])`

- `EmptyResponseMetadataTypeDef` - dynamodb: `TypeTypedDict('EmptyResponseMetadataTypeDef', [TypedDictAttribute('ResponseMetadata', ResponseMetadataTypeDef, True)])`

- `GetTemplateOutputTypeDef` - cloudformation: `TypeTypedDict('GetTemplateOutputTypeDef', [TypedDictAttribute('TemplateBody', Type.DictStrAny, True), TypedDictAttribute('StagesAvailable', TypeSubscript(Type.List, [InternalImport(name='TemplateStageType', module_name=ServiceModuleName.literals)]), True), TypedDictAttribute('ResponseMetadata', ResponseMetadataTypeDef, True)])`

- `PolicyDocumentStatementTypeDef` - iam: `TypeTypedDict('PolicyDocumentStatementTypeDef', [TypedDictAttribute('Effect', Type.str, True), TypedDictAttribute('Resource', TypeUnion((Type.str, TypeSubscript(Type.List, [Type.str]))), True), TypedDictAttribute('Sid', Type.str, True), TypedDictAttribute('Action', TypeUnion((Type.str, TypeSubscript(Type.List, [Type.str]))), True)])`
