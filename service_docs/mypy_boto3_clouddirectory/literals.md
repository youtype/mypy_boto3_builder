# Literals for boto3 CloudDirectory module

> [Index](../index.md) > [CloudDirectory](./index.md) > Literals

Auto-generated documentation for [CloudDirectory](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory)
type annotations stubs module [mypy_boto3_clouddirectory](https://pypi.org/project/mypy-boto3-clouddirectory/).

- [Literals for boto3 CloudDirectory module](#literals-for-boto3-clouddirectory-module)
  - [BatchReadExceptionType](#batchreadexceptiontype)
  - [ConsistencyLevel](#consistencylevel)
  - [DirectoryState](#directorystate)
  - [FacetAttributeType](#facetattributetype)
  - [FacetStyle](#facetstyle)
  - [ListAppliedSchemaArnsPaginatorName](#listappliedschemaarnspaginatorname)
  - [ListAttachedIndicesPaginatorName](#listattachedindicespaginatorname)
  - [ListDevelopmentSchemaArnsPaginatorName](#listdevelopmentschemaarnspaginatorname)
  - [ListDirectoriesPaginatorName](#listdirectoriespaginatorname)
  - [ListFacetAttributesPaginatorName](#listfacetattributespaginatorname)
  - [ListFacetNamesPaginatorName](#listfacetnamespaginatorname)
  - [ListIncomingTypedLinksPaginatorName](#listincomingtypedlinkspaginatorname)
  - [ListIndexPaginatorName](#listindexpaginatorname)
  - [ListManagedSchemaArnsPaginatorName](#listmanagedschemaarnspaginatorname)
  - [ListObjectAttributesPaginatorName](#listobjectattributespaginatorname)
  - [ListObjectParentPathsPaginatorName](#listobjectparentpathspaginatorname)
  - [ListObjectPoliciesPaginatorName](#listobjectpoliciespaginatorname)
  - [ListOutgoingTypedLinksPaginatorName](#listoutgoingtypedlinkspaginatorname)
  - [ListPolicyAttachmentsPaginatorName](#listpolicyattachmentspaginatorname)
  - [ListPublishedSchemaArnsPaginatorName](#listpublishedschemaarnspaginatorname)
  - [ListTagsForResourcePaginatorName](#listtagsforresourcepaginatorname)
  - [ListTypedLinkFacetAttributesPaginatorName](#listtypedlinkfacetattributespaginatorname)
  - [ListTypedLinkFacetNamesPaginatorName](#listtypedlinkfacetnamespaginatorname)
  - [LookupPolicyPaginatorName](#lookuppolicypaginatorname)
  - [ObjectType](#objecttype)
  - [RangeMode](#rangemode)
  - [RequiredAttributeBehavior](#requiredattributebehavior)
  - [RuleType](#ruletype)
  - [UpdateActionType](#updateactiontype)

## BatchReadExceptionType

```python
from mypy_boto3_clouddirectory.literals import BatchReadExceptionType
```

Values:

- `AccessDeniedException`
- `CannotListParentOfRootException`
- `DirectoryNotEnabledException`
- `FacetValidationException`
- `InternalServiceException`
- `InvalidArnException`
- `InvalidNextTokenException`
- `LimitExceededException`
- `NotIndexException`
- `NotNodeException`
- `NotPolicyException`
- `ResourceNotFoundException`
- `ValidationException`

## ConsistencyLevel

```python
from mypy_boto3_clouddirectory.literals import ConsistencyLevel
```

Values:

- `EVENTUAL`
- `SERIALIZABLE`

## DirectoryState

```python
from mypy_boto3_clouddirectory.literals import DirectoryState
```

Values:

- `DELETED`
- `DISABLED`
- `ENABLED`

## FacetAttributeType

```python
from mypy_boto3_clouddirectory.literals import FacetAttributeType
```

Values:

- `BINARY`
- `BOOLEAN`
- `DATETIME`
- `NUMBER`
- `STRING`
- `VARIANT`

## FacetStyle

```python
from mypy_boto3_clouddirectory.literals import FacetStyle
```

Values:

- `DYNAMIC`
- `STATIC`

## ListAppliedSchemaArnsPaginatorName

```python
from mypy_boto3_clouddirectory.literals import ListAppliedSchemaArnsPaginatorName
```

Values:

- `list_applied_schema_arns`

## ListAttachedIndicesPaginatorName

```python
from mypy_boto3_clouddirectory.literals import ListAttachedIndicesPaginatorName
```

Values:

- `list_attached_indices`

## ListDevelopmentSchemaArnsPaginatorName

```python
from mypy_boto3_clouddirectory.literals import ListDevelopmentSchemaArnsPaginatorName
```

Values:

- `list_development_schema_arns`

## ListDirectoriesPaginatorName

```python
from mypy_boto3_clouddirectory.literals import ListDirectoriesPaginatorName
```

Values:

- `list_directories`

## ListFacetAttributesPaginatorName

```python
from mypy_boto3_clouddirectory.literals import ListFacetAttributesPaginatorName
```

Values:

- `list_facet_attributes`

## ListFacetNamesPaginatorName

```python
from mypy_boto3_clouddirectory.literals import ListFacetNamesPaginatorName
```

Values:

- `list_facet_names`

## ListIncomingTypedLinksPaginatorName

```python
from mypy_boto3_clouddirectory.literals import ListIncomingTypedLinksPaginatorName
```

Values:

- `list_incoming_typed_links`

## ListIndexPaginatorName

```python
from mypy_boto3_clouddirectory.literals import ListIndexPaginatorName
```

Values:

- `list_index`

## ListManagedSchemaArnsPaginatorName

```python
from mypy_boto3_clouddirectory.literals import ListManagedSchemaArnsPaginatorName
```

Values:

- `list_managed_schema_arns`

## ListObjectAttributesPaginatorName

```python
from mypy_boto3_clouddirectory.literals import ListObjectAttributesPaginatorName
```

Values:

- `list_object_attributes`

## ListObjectParentPathsPaginatorName

```python
from mypy_boto3_clouddirectory.literals import ListObjectParentPathsPaginatorName
```

Values:

- `list_object_parent_paths`

## ListObjectPoliciesPaginatorName

```python
from mypy_boto3_clouddirectory.literals import ListObjectPoliciesPaginatorName
```

Values:

- `list_object_policies`

## ListOutgoingTypedLinksPaginatorName

```python
from mypy_boto3_clouddirectory.literals import ListOutgoingTypedLinksPaginatorName
```

Values:

- `list_outgoing_typed_links`

## ListPolicyAttachmentsPaginatorName

```python
from mypy_boto3_clouddirectory.literals import ListPolicyAttachmentsPaginatorName
```

Values:

- `list_policy_attachments`

## ListPublishedSchemaArnsPaginatorName

```python
from mypy_boto3_clouddirectory.literals import ListPublishedSchemaArnsPaginatorName
```

Values:

- `list_published_schema_arns`

## ListTagsForResourcePaginatorName

```python
from mypy_boto3_clouddirectory.literals import ListTagsForResourcePaginatorName
```

Values:

- `list_tags_for_resource`

## ListTypedLinkFacetAttributesPaginatorName

```python
from mypy_boto3_clouddirectory.literals import ListTypedLinkFacetAttributesPaginatorName
```

Values:

- `list_typed_link_facet_attributes`

## ListTypedLinkFacetNamesPaginatorName

```python
from mypy_boto3_clouddirectory.literals import ListTypedLinkFacetNamesPaginatorName
```

Values:

- `list_typed_link_facet_names`

## LookupPolicyPaginatorName

```python
from mypy_boto3_clouddirectory.literals import LookupPolicyPaginatorName
```

Values:

- `lookup_policy`

## ObjectType

```python
from mypy_boto3_clouddirectory.literals import ObjectType
```

Values:

- `INDEX`
- `LEAF_NODE`
- `NODE`
- `POLICY`

## RangeMode

```python
from mypy_boto3_clouddirectory.literals import RangeMode
```

Values:

- `EXCLUSIVE`
- `FIRST`
- `INCLUSIVE`
- `LAST`
- `LAST_BEFORE_MISSING_VALUES`

## RequiredAttributeBehavior

```python
from mypy_boto3_clouddirectory.literals import RequiredAttributeBehavior
```

Values:

- `NOT_REQUIRED`
- `REQUIRED_ALWAYS`

## RuleType

```python
from mypy_boto3_clouddirectory.literals import RuleType
```

Values:

- `BINARY_LENGTH`
- `NUMBER_COMPARISON`
- `STRING_FROM_SET`
- `STRING_LENGTH`

## UpdateActionType

```python
from mypy_boto3_clouddirectory.literals import UpdateActionType
```

Values:

- `CREATE_OR_UPDATE`
- `DELETE`
