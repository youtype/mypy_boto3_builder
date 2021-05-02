# Structures for boto3 CloudDirectory module

> [Index](../index.md) > [CloudDirectory](./index.md) > Structures

Auto-generated documentation for [CloudDirectory](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/clouddirectory.html#CloudDirectory)
type annotations stubs module [mypy_boto3_clouddirectory](https://pypi.org/project/mypy-boto3-clouddirectory/).

- [Structures for boto3 CloudDirectory module](#structures-for-boto3-clouddirectory-module)
  - [AttributeKeyAndValueTypeDef](#attributekeyandvaluetypedef)
  - [AttributeKeyTypeDef](#attributekeytypedef)
  - [AttributeNameAndValueTypeDef](#attributenameandvaluetypedef)
  - [BatchAddFacetToObjectTypeDef](#batchaddfacettoobjecttypedef)
  - [BatchAttachObjectResponseTypeDef](#batchattachobjectresponsetypedef)
  - [BatchAttachObjectTypeDef](#batchattachobjecttypedef)
  - [BatchAttachPolicyTypeDef](#batchattachpolicytypedef)
  - [BatchAttachToIndexResponseTypeDef](#batchattachtoindexresponsetypedef)
  - [BatchAttachToIndexTypeDef](#batchattachtoindextypedef)
  - [BatchAttachTypedLinkResponseTypeDef](#batchattachtypedlinkresponsetypedef)
  - [BatchAttachTypedLinkTypeDef](#batchattachtypedlinktypedef)
  - [BatchCreateIndexResponseTypeDef](#batchcreateindexresponsetypedef)
  - [BatchCreateIndexTypeDef](#batchcreateindextypedef)
  - [BatchCreateObjectResponseTypeDef](#batchcreateobjectresponsetypedef)
  - [BatchCreateObjectTypeDef](#batchcreateobjecttypedef)
  - [BatchDeleteObjectTypeDef](#batchdeleteobjecttypedef)
  - [BatchDetachFromIndexResponseTypeDef](#batchdetachfromindexresponsetypedef)
  - [BatchDetachFromIndexTypeDef](#batchdetachfromindextypedef)
  - [BatchDetachObjectResponseTypeDef](#batchdetachobjectresponsetypedef)
  - [BatchDetachObjectTypeDef](#batchdetachobjecttypedef)
  - [BatchDetachPolicyTypeDef](#batchdetachpolicytypedef)
  - [BatchDetachTypedLinkTypeDef](#batchdetachtypedlinktypedef)
  - [BatchGetLinkAttributesResponseTypeDef](#batchgetlinkattributesresponsetypedef)
  - [BatchGetLinkAttributesTypeDef](#batchgetlinkattributestypedef)
  - [BatchGetObjectAttributesResponseTypeDef](#batchgetobjectattributesresponsetypedef)
  - [BatchGetObjectAttributesTypeDef](#batchgetobjectattributestypedef)
  - [BatchGetObjectInformationResponseTypeDef](#batchgetobjectinformationresponsetypedef)
  - [BatchGetObjectInformationTypeDef](#batchgetobjectinformationtypedef)
  - [BatchListAttachedIndicesResponseTypeDef](#batchlistattachedindicesresponsetypedef)
  - [BatchListAttachedIndicesTypeDef](#batchlistattachedindicestypedef)
  - [BatchListIncomingTypedLinksResponseTypeDef](#batchlistincomingtypedlinksresponsetypedef)
  - [BatchListIncomingTypedLinksTypeDef](#batchlistincomingtypedlinkstypedef)
  - [BatchListIndexResponseTypeDef](#batchlistindexresponsetypedef)
  - [BatchListIndexTypeDef](#batchlistindextypedef)
  - [BatchListObjectAttributesResponseTypeDef](#batchlistobjectattributesresponsetypedef)
  - [BatchListObjectAttributesTypeDef](#batchlistobjectattributestypedef)
  - [BatchListObjectChildrenResponseTypeDef](#batchlistobjectchildrenresponsetypedef)
  - [BatchListObjectChildrenTypeDef](#batchlistobjectchildrentypedef)
  - [BatchListObjectParentPathsResponseTypeDef](#batchlistobjectparentpathsresponsetypedef)
  - [BatchListObjectParentPathsTypeDef](#batchlistobjectparentpathstypedef)
  - [BatchListObjectParentsResponseTypeDef](#batchlistobjectparentsresponsetypedef)
  - [BatchListObjectParentsTypeDef](#batchlistobjectparentstypedef)
  - [BatchListObjectPoliciesResponseTypeDef](#batchlistobjectpoliciesresponsetypedef)
  - [BatchListObjectPoliciesTypeDef](#batchlistobjectpoliciestypedef)
  - [BatchListOutgoingTypedLinksResponseTypeDef](#batchlistoutgoingtypedlinksresponsetypedef)
  - [BatchListOutgoingTypedLinksTypeDef](#batchlistoutgoingtypedlinkstypedef)
  - [BatchListPolicyAttachmentsResponseTypeDef](#batchlistpolicyattachmentsresponsetypedef)
  - [BatchListPolicyAttachmentsTypeDef](#batchlistpolicyattachmentstypedef)
  - [BatchLookupPolicyResponseTypeDef](#batchlookuppolicyresponsetypedef)
  - [BatchLookupPolicyTypeDef](#batchlookuppolicytypedef)
  - [BatchReadExceptionTypeDef](#batchreadexceptiontypedef)
  - [BatchReadOperationResponseTypeDef](#batchreadoperationresponsetypedef)
  - [BatchReadSuccessfulResponseTypeDef](#batchreadsuccessfulresponsetypedef)
  - [BatchRemoveFacetFromObjectTypeDef](#batchremovefacetfromobjecttypedef)
  - [BatchUpdateLinkAttributesTypeDef](#batchupdatelinkattributestypedef)
  - [BatchUpdateObjectAttributesResponseTypeDef](#batchupdateobjectattributesresponsetypedef)
  - [BatchUpdateObjectAttributesTypeDef](#batchupdateobjectattributestypedef)
  - [BatchWriteOperationResponseTypeDef](#batchwriteoperationresponsetypedef)
  - [DirectoryTypeDef](#directorytypedef)
  - [FacetAttributeDefinitionTypeDef](#facetattributedefinitiontypedef)
  - [FacetAttributeReferenceTypeDef](#facetattributereferencetypedef)
  - [FacetAttributeTypeDef](#facetattributetypedef)
  - [FacetTypeDef](#facettypedef)
  - [IndexAttachmentTypeDef](#indexattachmenttypedef)
  - [LinkAttributeActionTypeDef](#linkattributeactiontypedef)
  - [LinkAttributeUpdateTypeDef](#linkattributeupdatetypedef)
  - [ObjectAttributeActionTypeDef](#objectattributeactiontypedef)
  - [ObjectAttributeRangeTypeDef](#objectattributerangetypedef)
  - [ObjectAttributeUpdateTypeDef](#objectattributeupdatetypedef)
  - [ObjectIdentifierAndLinkNameTupleTypeDef](#objectidentifierandlinknametupletypedef)
  - [ObjectReferenceTypeDef](#objectreferencetypedef)
  - [PathToObjectIdentifiersTypeDef](#pathtoobjectidentifierstypedef)
  - [PolicyAttachmentTypeDef](#policyattachmenttypedef)
  - [PolicyToPathTypeDef](#policytopathtypedef)
  - [RuleTypeDef](#ruletypedef)
  - [SchemaFacetTypeDef](#schemafacettypedef)
  - [TagTypeDef](#tagtypedef)
  - [TypedAttributeValueRangeTypeDef](#typedattributevaluerangetypedef)
  - [TypedAttributeValueTypeDef](#typedattributevaluetypedef)
  - [TypedLinkAttributeDefinitionTypeDef](#typedlinkattributedefinitiontypedef)
  - [TypedLinkAttributeRangeTypeDef](#typedlinkattributerangetypedef)
  - [TypedLinkSchemaAndFacetNameTypeDef](#typedlinkschemaandfacetnametypedef)
  - [TypedLinkSpecifierTypeDef](#typedlinkspecifiertypedef)
  - [ApplySchemaResponseTypeDef](#applyschemaresponsetypedef)
  - [AttachObjectResponseTypeDef](#attachobjectresponsetypedef)
  - [AttachToIndexResponseTypeDef](#attachtoindexresponsetypedef)
  - [AttachTypedLinkResponseTypeDef](#attachtypedlinkresponsetypedef)
  - [BatchReadOperationTypeDef](#batchreadoperationtypedef)
  - [BatchReadResponseTypeDef](#batchreadresponsetypedef)
  - [BatchWriteOperationTypeDef](#batchwriteoperationtypedef)
  - [BatchWriteResponseTypeDef](#batchwriteresponsetypedef)
  - [CreateDirectoryResponseTypeDef](#createdirectoryresponsetypedef)
  - [CreateIndexResponseTypeDef](#createindexresponsetypedef)
  - [CreateObjectResponseTypeDef](#createobjectresponsetypedef)
  - [CreateSchemaResponseTypeDef](#createschemaresponsetypedef)
  - [DeleteDirectoryResponseTypeDef](#deletedirectoryresponsetypedef)
  - [DeleteSchemaResponseTypeDef](#deleteschemaresponsetypedef)
  - [DetachFromIndexResponseTypeDef](#detachfromindexresponsetypedef)
  - [DetachObjectResponseTypeDef](#detachobjectresponsetypedef)
  - [DisableDirectoryResponseTypeDef](#disabledirectoryresponsetypedef)
  - [EnableDirectoryResponseTypeDef](#enabledirectoryresponsetypedef)
  - [FacetAttributeUpdateTypeDef](#facetattributeupdatetypedef)
  - [GetAppliedSchemaVersionResponseTypeDef](#getappliedschemaversionresponsetypedef)
  - [GetDirectoryResponseTypeDef](#getdirectoryresponsetypedef)
  - [GetFacetResponseTypeDef](#getfacetresponsetypedef)
  - [GetLinkAttributesResponseTypeDef](#getlinkattributesresponsetypedef)
  - [GetObjectAttributesResponseTypeDef](#getobjectattributesresponsetypedef)
  - [GetObjectInformationResponseTypeDef](#getobjectinformationresponsetypedef)
  - [GetSchemaAsJsonResponseTypeDef](#getschemaasjsonresponsetypedef)
  - [GetTypedLinkFacetInformationResponseTypeDef](#gettypedlinkfacetinformationresponsetypedef)
  - [ListAppliedSchemaArnsResponseTypeDef](#listappliedschemaarnsresponsetypedef)
  - [ListAttachedIndicesResponseTypeDef](#listattachedindicesresponsetypedef)
  - [ListDevelopmentSchemaArnsResponseTypeDef](#listdevelopmentschemaarnsresponsetypedef)
  - [ListDirectoriesResponseTypeDef](#listdirectoriesresponsetypedef)
  - [ListFacetAttributesResponseTypeDef](#listfacetattributesresponsetypedef)
  - [ListFacetNamesResponseTypeDef](#listfacetnamesresponsetypedef)
  - [ListIncomingTypedLinksResponseTypeDef](#listincomingtypedlinksresponsetypedef)
  - [ListIndexResponseTypeDef](#listindexresponsetypedef)
  - [ListManagedSchemaArnsResponseTypeDef](#listmanagedschemaarnsresponsetypedef)
  - [ListObjectAttributesResponseTypeDef](#listobjectattributesresponsetypedef)
  - [ListObjectChildrenResponseTypeDef](#listobjectchildrenresponsetypedef)
  - [ListObjectParentPathsResponseTypeDef](#listobjectparentpathsresponsetypedef)
  - [ListObjectParentsResponseTypeDef](#listobjectparentsresponsetypedef)
  - [ListObjectPoliciesResponseTypeDef](#listobjectpoliciesresponsetypedef)
  - [ListOutgoingTypedLinksResponseTypeDef](#listoutgoingtypedlinksresponsetypedef)
  - [ListPolicyAttachmentsResponseTypeDef](#listpolicyattachmentsresponsetypedef)
  - [ListPublishedSchemaArnsResponseTypeDef](#listpublishedschemaarnsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [ListTypedLinkFacetAttributesResponseTypeDef](#listtypedlinkfacetattributesresponsetypedef)
  - [ListTypedLinkFacetNamesResponseTypeDef](#listtypedlinkfacetnamesresponsetypedef)
  - [LookupPolicyResponseTypeDef](#lookuppolicyresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [PublishSchemaResponseTypeDef](#publishschemaresponsetypedef)
  - [PutSchemaFromJsonResponseTypeDef](#putschemafromjsonresponsetypedef)
  - [TypedLinkFacetAttributeUpdateTypeDef](#typedlinkfacetattributeupdatetypedef)
  - [TypedLinkFacetTypeDef](#typedlinkfacettypedef)
  - [UpdateObjectAttributesResponseTypeDef](#updateobjectattributesresponsetypedef)
  - [UpdateSchemaResponseTypeDef](#updateschemaresponsetypedef)
  - [UpgradeAppliedSchemaResponseTypeDef](#upgradeappliedschemaresponsetypedef)
  - [UpgradePublishedSchemaResponseTypeDef](#upgradepublishedschemaresponsetypedef)

## AttributeKeyAndValueTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import AttributeKeyAndValueTypeDef
```


Required fields:
- `Key`: `"AttributeKeyTypeDef"`
- `Value`: `"TypedAttributeValueTypeDef"`




## AttributeKeyTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import AttributeKeyTypeDef
```


Required fields:
- `SchemaArn`: `str`
- `FacetName`: `str`
- `Name`: `str`




## AttributeNameAndValueTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import AttributeNameAndValueTypeDef
```


Required fields:
- `AttributeName`: `str`
- `Value`: `"TypedAttributeValueTypeDef"`




## BatchAddFacetToObjectTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchAddFacetToObjectTypeDef
```


Required fields:
- `SchemaFacet`: `"SchemaFacetTypeDef"`
- `ObjectAttributeList`: `List["AttributeKeyAndValueTypeDef"]`
- `ObjectReference`: `"ObjectReferenceTypeDef"`




## BatchAttachObjectResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchAttachObjectResponseTypeDef
```




Optional fields:
- `attachedObjectIdentifier`: `str`


## BatchAttachObjectTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchAttachObjectTypeDef
```


Required fields:
- `ParentReference`: `"ObjectReferenceTypeDef"`
- `ChildReference`: `"ObjectReferenceTypeDef"`
- `LinkName`: `str`




## BatchAttachPolicyTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchAttachPolicyTypeDef
```


Required fields:
- `PolicyReference`: `"ObjectReferenceTypeDef"`
- `ObjectReference`: `"ObjectReferenceTypeDef"`




## BatchAttachToIndexResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchAttachToIndexResponseTypeDef
```




Optional fields:
- `AttachedObjectIdentifier`: `str`


## BatchAttachToIndexTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchAttachToIndexTypeDef
```


Required fields:
- `IndexReference`: `"ObjectReferenceTypeDef"`
- `TargetReference`: `"ObjectReferenceTypeDef"`




## BatchAttachTypedLinkResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchAttachTypedLinkResponseTypeDef
```




Optional fields:
- `TypedLinkSpecifier`: `"TypedLinkSpecifierTypeDef"`


## BatchAttachTypedLinkTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchAttachTypedLinkTypeDef
```


Required fields:
- `SourceObjectReference`: `"ObjectReferenceTypeDef"`
- `TargetObjectReference`: `"ObjectReferenceTypeDef"`
- `TypedLinkFacet`: `"TypedLinkSchemaAndFacetNameTypeDef"`
- `Attributes`: `List["AttributeNameAndValueTypeDef"]`




## BatchCreateIndexResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchCreateIndexResponseTypeDef
```




Optional fields:
- `ObjectIdentifier`: `str`


## BatchCreateIndexTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchCreateIndexTypeDef
```


Required fields:
- `OrderedIndexedAttributeList`: `List["AttributeKeyTypeDef"]`
- `IsUnique`: `bool`



Optional fields:
- `ParentReference`: `"ObjectReferenceTypeDef"`
- `LinkName`: `str`
- `BatchReferenceName`: `str`


## BatchCreateObjectResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchCreateObjectResponseTypeDef
```




Optional fields:
- `ObjectIdentifier`: `str`


## BatchCreateObjectTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchCreateObjectTypeDef
```


Required fields:
- `SchemaFacet`: `List["SchemaFacetTypeDef"]`
- `ObjectAttributeList`: `List["AttributeKeyAndValueTypeDef"]`



Optional fields:
- `ParentReference`: `"ObjectReferenceTypeDef"`
- `LinkName`: `str`
- `BatchReferenceName`: `str`


## BatchDeleteObjectTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchDeleteObjectTypeDef
```


Required fields:
- `ObjectReference`: `"ObjectReferenceTypeDef"`




## BatchDetachFromIndexResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchDetachFromIndexResponseTypeDef
```




Optional fields:
- `DetachedObjectIdentifier`: `str`


## BatchDetachFromIndexTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchDetachFromIndexTypeDef
```


Required fields:
- `IndexReference`: `"ObjectReferenceTypeDef"`
- `TargetReference`: `"ObjectReferenceTypeDef"`




## BatchDetachObjectResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchDetachObjectResponseTypeDef
```




Optional fields:
- `detachedObjectIdentifier`: `str`


## BatchDetachObjectTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchDetachObjectTypeDef
```


Required fields:
- `ParentReference`: `"ObjectReferenceTypeDef"`
- `LinkName`: `str`



Optional fields:
- `BatchReferenceName`: `str`


## BatchDetachPolicyTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchDetachPolicyTypeDef
```


Required fields:
- `PolicyReference`: `"ObjectReferenceTypeDef"`
- `ObjectReference`: `"ObjectReferenceTypeDef"`




## BatchDetachTypedLinkTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchDetachTypedLinkTypeDef
```


Required fields:
- `TypedLinkSpecifier`: `"TypedLinkSpecifierTypeDef"`




## BatchGetLinkAttributesResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchGetLinkAttributesResponseTypeDef
```




Optional fields:
- `Attributes`: `List["AttributeKeyAndValueTypeDef"]`


## BatchGetLinkAttributesTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchGetLinkAttributesTypeDef
```


Required fields:
- `TypedLinkSpecifier`: `"TypedLinkSpecifierTypeDef"`
- `AttributeNames`: `List[str]`




## BatchGetObjectAttributesResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchGetObjectAttributesResponseTypeDef
```




Optional fields:
- `Attributes`: `List["AttributeKeyAndValueTypeDef"]`


## BatchGetObjectAttributesTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchGetObjectAttributesTypeDef
```


Required fields:
- `ObjectReference`: `"ObjectReferenceTypeDef"`
- `SchemaFacet`: `"SchemaFacetTypeDef"`
- `AttributeNames`: `List[str]`




## BatchGetObjectInformationResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchGetObjectInformationResponseTypeDef
```




Optional fields:
- `SchemaFacets`: `List["SchemaFacetTypeDef"]`
- `ObjectIdentifier`: `str`


## BatchGetObjectInformationTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchGetObjectInformationTypeDef
```


Required fields:
- `ObjectReference`: `"ObjectReferenceTypeDef"`




## BatchListAttachedIndicesResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchListAttachedIndicesResponseTypeDef
```




Optional fields:
- `IndexAttachments`: `List["IndexAttachmentTypeDef"]`
- `NextToken`: `str`


## BatchListAttachedIndicesTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchListAttachedIndicesTypeDef
```


Required fields:
- `TargetReference`: `"ObjectReferenceTypeDef"`



Optional fields:
- `NextToken`: `str`
- `MaxResults`: `int`


## BatchListIncomingTypedLinksResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchListIncomingTypedLinksResponseTypeDef
```




Optional fields:
- `LinkSpecifiers`: `List["TypedLinkSpecifierTypeDef"]`
- `NextToken`: `str`


## BatchListIncomingTypedLinksTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchListIncomingTypedLinksTypeDef
```


Required fields:
- `ObjectReference`: `"ObjectReferenceTypeDef"`



Optional fields:
- `FilterAttributeRanges`: `List["TypedLinkAttributeRangeTypeDef"]`
- `FilterTypedLink`: `"TypedLinkSchemaAndFacetNameTypeDef"`
- `NextToken`: `str`
- `MaxResults`: `int`


## BatchListIndexResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchListIndexResponseTypeDef
```




Optional fields:
- `IndexAttachments`: `List["IndexAttachmentTypeDef"]`
- `NextToken`: `str`


## BatchListIndexTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchListIndexTypeDef
```


Required fields:
- `IndexReference`: `"ObjectReferenceTypeDef"`



Optional fields:
- `RangesOnIndexedValues`: `List["ObjectAttributeRangeTypeDef"]`
- `MaxResults`: `int`
- `NextToken`: `str`


## BatchListObjectAttributesResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchListObjectAttributesResponseTypeDef
```




Optional fields:
- `Attributes`: `List["AttributeKeyAndValueTypeDef"]`
- `NextToken`: `str`


## BatchListObjectAttributesTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchListObjectAttributesTypeDef
```


Required fields:
- `ObjectReference`: `"ObjectReferenceTypeDef"`



Optional fields:
- `NextToken`: `str`
- `MaxResults`: `int`
- `FacetFilter`: `"SchemaFacetTypeDef"`


## BatchListObjectChildrenResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchListObjectChildrenResponseTypeDef
```




Optional fields:
- `Children`: `Dict[str, str]`
- `NextToken`: `str`


## BatchListObjectChildrenTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchListObjectChildrenTypeDef
```


Required fields:
- `ObjectReference`: `"ObjectReferenceTypeDef"`



Optional fields:
- `NextToken`: `str`
- `MaxResults`: `int`


## BatchListObjectParentPathsResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchListObjectParentPathsResponseTypeDef
```




Optional fields:
- `PathToObjectIdentifiersList`: `List["PathToObjectIdentifiersTypeDef"]`
- `NextToken`: `str`


## BatchListObjectParentPathsTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchListObjectParentPathsTypeDef
```


Required fields:
- `ObjectReference`: `"ObjectReferenceTypeDef"`



Optional fields:
- `NextToken`: `str`
- `MaxResults`: `int`


## BatchListObjectParentsResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchListObjectParentsResponseTypeDef
```




Optional fields:
- `ParentLinks`: `List["ObjectIdentifierAndLinkNameTupleTypeDef"]`
- `NextToken`: `str`


## BatchListObjectParentsTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchListObjectParentsTypeDef
```


Required fields:
- `ObjectReference`: `"ObjectReferenceTypeDef"`



Optional fields:
- `NextToken`: `str`
- `MaxResults`: `int`


## BatchListObjectPoliciesResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchListObjectPoliciesResponseTypeDef
```




Optional fields:
- `AttachedPolicyIds`: `List[str]`
- `NextToken`: `str`


## BatchListObjectPoliciesTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchListObjectPoliciesTypeDef
```


Required fields:
- `ObjectReference`: `"ObjectReferenceTypeDef"`



Optional fields:
- `NextToken`: `str`
- `MaxResults`: `int`


## BatchListOutgoingTypedLinksResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchListOutgoingTypedLinksResponseTypeDef
```




Optional fields:
- `TypedLinkSpecifiers`: `List["TypedLinkSpecifierTypeDef"]`
- `NextToken`: `str`


## BatchListOutgoingTypedLinksTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchListOutgoingTypedLinksTypeDef
```


Required fields:
- `ObjectReference`: `"ObjectReferenceTypeDef"`



Optional fields:
- `FilterAttributeRanges`: `List["TypedLinkAttributeRangeTypeDef"]`
- `FilterTypedLink`: `"TypedLinkSchemaAndFacetNameTypeDef"`
- `NextToken`: `str`
- `MaxResults`: `int`


## BatchListPolicyAttachmentsResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchListPolicyAttachmentsResponseTypeDef
```




Optional fields:
- `ObjectIdentifiers`: `List[str]`
- `NextToken`: `str`


## BatchListPolicyAttachmentsTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchListPolicyAttachmentsTypeDef
```


Required fields:
- `PolicyReference`: `"ObjectReferenceTypeDef"`



Optional fields:
- `NextToken`: `str`
- `MaxResults`: `int`


## BatchLookupPolicyResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchLookupPolicyResponseTypeDef
```




Optional fields:
- `PolicyToPathList`: `List["PolicyToPathTypeDef"]`
- `NextToken`: `str`


## BatchLookupPolicyTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchLookupPolicyTypeDef
```


Required fields:
- `ObjectReference`: `"ObjectReferenceTypeDef"`



Optional fields:
- `NextToken`: `str`
- `MaxResults`: `int`


## BatchReadExceptionTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchReadExceptionTypeDef
```




Optional fields:
- `Type`: `BatchReadExceptionType`
- `Message`: `str`


## BatchReadOperationResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchReadOperationResponseTypeDef
```




Optional fields:
- `SuccessfulResponse`: `"BatchReadSuccessfulResponseTypeDef"`
- `ExceptionResponse`: `"BatchReadExceptionTypeDef"`


## BatchReadSuccessfulResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchReadSuccessfulResponseTypeDef
```




Optional fields:
- `ListObjectAttributes`: `"BatchListObjectAttributesResponseTypeDef"`
- `ListObjectChildren`: `"BatchListObjectChildrenResponseTypeDef"`
- `GetObjectInformation`: `"BatchGetObjectInformationResponseTypeDef"`
- `GetObjectAttributes`: `"BatchGetObjectAttributesResponseTypeDef"`
- `ListAttachedIndices`: `"BatchListAttachedIndicesResponseTypeDef"`
- `ListObjectParentPaths`: `"BatchListObjectParentPathsResponseTypeDef"`
- `ListObjectPolicies`: `"BatchListObjectPoliciesResponseTypeDef"`
- `ListPolicyAttachments`: `"BatchListPolicyAttachmentsResponseTypeDef"`
- `LookupPolicy`: `"BatchLookupPolicyResponseTypeDef"`
- `ListIndex`: `"BatchListIndexResponseTypeDef"`
- `ListOutgoingTypedLinks`: `"BatchListOutgoingTypedLinksResponseTypeDef"`
- `ListIncomingTypedLinks`: `"BatchListIncomingTypedLinksResponseTypeDef"`
- `GetLinkAttributes`: `"BatchGetLinkAttributesResponseTypeDef"`
- `ListObjectParents`: `"BatchListObjectParentsResponseTypeDef"`


## BatchRemoveFacetFromObjectTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchRemoveFacetFromObjectTypeDef
```


Required fields:
- `SchemaFacet`: `"SchemaFacetTypeDef"`
- `ObjectReference`: `"ObjectReferenceTypeDef"`




## BatchUpdateLinkAttributesTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchUpdateLinkAttributesTypeDef
```


Required fields:
- `TypedLinkSpecifier`: `"TypedLinkSpecifierTypeDef"`
- `AttributeUpdates`: `List["LinkAttributeUpdateTypeDef"]`




## BatchUpdateObjectAttributesResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchUpdateObjectAttributesResponseTypeDef
```




Optional fields:
- `ObjectIdentifier`: `str`


## BatchUpdateObjectAttributesTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchUpdateObjectAttributesTypeDef
```


Required fields:
- `ObjectReference`: `"ObjectReferenceTypeDef"`
- `AttributeUpdates`: `List["ObjectAttributeUpdateTypeDef"]`




## BatchWriteOperationResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchWriteOperationResponseTypeDef
```




Optional fields:
- `CreateObject`: `"BatchCreateObjectResponseTypeDef"`
- `AttachObject`: `"BatchAttachObjectResponseTypeDef"`
- `DetachObject`: `"BatchDetachObjectResponseTypeDef"`
- `UpdateObjectAttributes`: `"BatchUpdateObjectAttributesResponseTypeDef"`
- `DeleteObject`: `Dict[str, Any]`
- `AddFacetToObject`: `Dict[str, Any]`
- `RemoveFacetFromObject`: `Dict[str, Any]`
- `AttachPolicy`: `Dict[str, Any]`
- `DetachPolicy`: `Dict[str, Any]`
- `CreateIndex`: `"BatchCreateIndexResponseTypeDef"`
- `AttachToIndex`: `"BatchAttachToIndexResponseTypeDef"`
- `DetachFromIndex`: `"BatchDetachFromIndexResponseTypeDef"`
- `AttachTypedLink`: `"BatchAttachTypedLinkResponseTypeDef"`
- `DetachTypedLink`: `Dict[str, Any]`
- `UpdateLinkAttributes`: `Dict[str, Any]`


## DirectoryTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import DirectoryTypeDef
```




Optional fields:
- `Name`: `str`
- `DirectoryArn`: `str`
- `State`: `DirectoryState`
- `CreationDateTime`: `datetime`


## FacetAttributeDefinitionTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import FacetAttributeDefinitionTypeDef
```


Required fields:
- `Type`: `FacetAttributeType`



Optional fields:
- `DefaultValue`: `"TypedAttributeValueTypeDef"`
- `IsImmutable`: `bool`
- `Rules`: `Dict[str, "RuleTypeDef"]`


## FacetAttributeReferenceTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import FacetAttributeReferenceTypeDef
```


Required fields:
- `TargetFacetName`: `str`
- `TargetAttributeName`: `str`




## FacetAttributeTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import FacetAttributeTypeDef
```


Required fields:
- `Name`: `str`



Optional fields:
- `AttributeDefinition`: `"FacetAttributeDefinitionTypeDef"`
- `AttributeReference`: `"FacetAttributeReferenceTypeDef"`
- `RequiredBehavior`: `RequiredAttributeBehavior`


## FacetTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import FacetTypeDef
```




Optional fields:
- `Name`: `str`
- `ObjectType`: `ObjectType`
- `FacetStyle`: `FacetStyle`


## IndexAttachmentTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import IndexAttachmentTypeDef
```




Optional fields:
- `IndexedAttributes`: `List["AttributeKeyAndValueTypeDef"]`
- `ObjectIdentifier`: `str`


## LinkAttributeActionTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import LinkAttributeActionTypeDef
```




Optional fields:
- `AttributeActionType`: `UpdateActionType`
- `AttributeUpdateValue`: `"TypedAttributeValueTypeDef"`


## LinkAttributeUpdateTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import LinkAttributeUpdateTypeDef
```




Optional fields:
- `AttributeKey`: `"AttributeKeyTypeDef"`
- `AttributeAction`: `"LinkAttributeActionTypeDef"`


## ObjectAttributeActionTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import ObjectAttributeActionTypeDef
```




Optional fields:
- `ObjectAttributeActionType`: `UpdateActionType`
- `ObjectAttributeUpdateValue`: `"TypedAttributeValueTypeDef"`


## ObjectAttributeRangeTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import ObjectAttributeRangeTypeDef
```




Optional fields:
- `AttributeKey`: `"AttributeKeyTypeDef"`
- `Range`: `"TypedAttributeValueRangeTypeDef"`


## ObjectAttributeUpdateTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import ObjectAttributeUpdateTypeDef
```




Optional fields:
- `ObjectAttributeKey`: `"AttributeKeyTypeDef"`
- `ObjectAttributeAction`: `"ObjectAttributeActionTypeDef"`


## ObjectIdentifierAndLinkNameTupleTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import ObjectIdentifierAndLinkNameTupleTypeDef
```




Optional fields:
- `ObjectIdentifier`: `str`
- `LinkName`: `str`


## ObjectReferenceTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import ObjectReferenceTypeDef
```




Optional fields:
- `Selector`: `str`


## PathToObjectIdentifiersTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import PathToObjectIdentifiersTypeDef
```




Optional fields:
- `Path`: `str`
- `ObjectIdentifiers`: `List[str]`


## PolicyAttachmentTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import PolicyAttachmentTypeDef
```




Optional fields:
- `PolicyId`: `str`
- `ObjectIdentifier`: `str`
- `PolicyType`: `str`


## PolicyToPathTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import PolicyToPathTypeDef
```




Optional fields:
- `Path`: `str`
- `Policies`: `List["PolicyAttachmentTypeDef"]`


## RuleTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import RuleTypeDef
```




Optional fields:
- `Type`: `RuleType`
- `Parameters`: `Dict[str, str]`


## SchemaFacetTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import SchemaFacetTypeDef
```




Optional fields:
- `SchemaArn`: `str`
- `FacetName`: `str`


## TagTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import TagTypeDef
```




Optional fields:
- `Key`: `str`
- `Value`: `str`


## TypedAttributeValueRangeTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import TypedAttributeValueRangeTypeDef
```


Required fields:
- `StartMode`: `RangeMode`
- `EndMode`: `RangeMode`



Optional fields:
- `StartValue`: `"TypedAttributeValueTypeDef"`
- `EndValue`: `"TypedAttributeValueTypeDef"`


## TypedAttributeValueTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import TypedAttributeValueTypeDef
```




Optional fields:
- `StringValue`: `str`
- `BinaryValue`: `Union[bytes, IO[bytes]]`
- `BooleanValue`: `bool`
- `NumberValue`: `str`
- `DatetimeValue`: `datetime`


## TypedLinkAttributeDefinitionTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import TypedLinkAttributeDefinitionTypeDef
```


Required fields:
- `Name`: `str`
- `Type`: `FacetAttributeType`
- `RequiredBehavior`: `RequiredAttributeBehavior`



Optional fields:
- `DefaultValue`: `"TypedAttributeValueTypeDef"`
- `IsImmutable`: `bool`
- `Rules`: `Dict[str, "RuleTypeDef"]`


## TypedLinkAttributeRangeTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import TypedLinkAttributeRangeTypeDef
```


Required fields:
- `Range`: `"TypedAttributeValueRangeTypeDef"`



Optional fields:
- `AttributeName`: `str`


## TypedLinkSchemaAndFacetNameTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import TypedLinkSchemaAndFacetNameTypeDef
```


Required fields:
- `SchemaArn`: `str`
- `TypedLinkName`: `str`




## TypedLinkSpecifierTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import TypedLinkSpecifierTypeDef
```


Required fields:
- `TypedLinkFacet`: `"TypedLinkSchemaAndFacetNameTypeDef"`
- `SourceObjectReference`: `"ObjectReferenceTypeDef"`
- `TargetObjectReference`: `"ObjectReferenceTypeDef"`
- `IdentityAttributeValues`: `List["AttributeNameAndValueTypeDef"]`




## ApplySchemaResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import ApplySchemaResponseTypeDef
```




Optional fields:
- `AppliedSchemaArn`: `str`
- `DirectoryArn`: `str`


## AttachObjectResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import AttachObjectResponseTypeDef
```




Optional fields:
- `AttachedObjectIdentifier`: `str`


## AttachToIndexResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import AttachToIndexResponseTypeDef
```




Optional fields:
- `AttachedObjectIdentifier`: `str`


## AttachTypedLinkResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import AttachTypedLinkResponseTypeDef
```




Optional fields:
- `TypedLinkSpecifier`: `"TypedLinkSpecifierTypeDef"`


## BatchReadOperationTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchReadOperationTypeDef
```




Optional fields:
- `ListObjectAttributes`: `"BatchListObjectAttributesTypeDef"`
- `ListObjectChildren`: `"BatchListObjectChildrenTypeDef"`
- `ListAttachedIndices`: `"BatchListAttachedIndicesTypeDef"`
- `ListObjectParentPaths`: `"BatchListObjectParentPathsTypeDef"`
- `GetObjectInformation`: `"BatchGetObjectInformationTypeDef"`
- `GetObjectAttributes`: `"BatchGetObjectAttributesTypeDef"`
- `ListObjectParents`: `"BatchListObjectParentsTypeDef"`
- `ListObjectPolicies`: `"BatchListObjectPoliciesTypeDef"`
- `ListPolicyAttachments`: `"BatchListPolicyAttachmentsTypeDef"`
- `LookupPolicy`: `"BatchLookupPolicyTypeDef"`
- `ListIndex`: `"BatchListIndexTypeDef"`
- `ListOutgoingTypedLinks`: `"BatchListOutgoingTypedLinksTypeDef"`
- `ListIncomingTypedLinks`: `"BatchListIncomingTypedLinksTypeDef"`
- `GetLinkAttributes`: `"BatchGetLinkAttributesTypeDef"`


## BatchReadResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchReadResponseTypeDef
```




Optional fields:
- `Responses`: `List["BatchReadOperationResponseTypeDef"]`


## BatchWriteOperationTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchWriteOperationTypeDef
```




Optional fields:
- `CreateObject`: `"BatchCreateObjectTypeDef"`
- `AttachObject`: `"BatchAttachObjectTypeDef"`
- `DetachObject`: `"BatchDetachObjectTypeDef"`
- `UpdateObjectAttributes`: `"BatchUpdateObjectAttributesTypeDef"`
- `DeleteObject`: `"BatchDeleteObjectTypeDef"`
- `AddFacetToObject`: `"BatchAddFacetToObjectTypeDef"`
- `RemoveFacetFromObject`: `"BatchRemoveFacetFromObjectTypeDef"`
- `AttachPolicy`: `"BatchAttachPolicyTypeDef"`
- `DetachPolicy`: `"BatchDetachPolicyTypeDef"`
- `CreateIndex`: `"BatchCreateIndexTypeDef"`
- `AttachToIndex`: `"BatchAttachToIndexTypeDef"`
- `DetachFromIndex`: `"BatchDetachFromIndexTypeDef"`
- `AttachTypedLink`: `"BatchAttachTypedLinkTypeDef"`
- `DetachTypedLink`: `"BatchDetachTypedLinkTypeDef"`
- `UpdateLinkAttributes`: `"BatchUpdateLinkAttributesTypeDef"`


## BatchWriteResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import BatchWriteResponseTypeDef
```




Optional fields:
- `Responses`: `List["BatchWriteOperationResponseTypeDef"]`


## CreateDirectoryResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import CreateDirectoryResponseTypeDef
```


Required fields:
- `DirectoryArn`: `str`
- `Name`: `str`
- `ObjectIdentifier`: `str`
- `AppliedSchemaArn`: `str`




## CreateIndexResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import CreateIndexResponseTypeDef
```




Optional fields:
- `ObjectIdentifier`: `str`


## CreateObjectResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import CreateObjectResponseTypeDef
```




Optional fields:
- `ObjectIdentifier`: `str`


## CreateSchemaResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import CreateSchemaResponseTypeDef
```




Optional fields:
- `SchemaArn`: `str`


## DeleteDirectoryResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import DeleteDirectoryResponseTypeDef
```


Required fields:
- `DirectoryArn`: `str`




## DeleteSchemaResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import DeleteSchemaResponseTypeDef
```




Optional fields:
- `SchemaArn`: `str`


## DetachFromIndexResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import DetachFromIndexResponseTypeDef
```




Optional fields:
- `DetachedObjectIdentifier`: `str`


## DetachObjectResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import DetachObjectResponseTypeDef
```




Optional fields:
- `DetachedObjectIdentifier`: `str`


## DisableDirectoryResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import DisableDirectoryResponseTypeDef
```


Required fields:
- `DirectoryArn`: `str`




## EnableDirectoryResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import EnableDirectoryResponseTypeDef
```


Required fields:
- `DirectoryArn`: `str`




## FacetAttributeUpdateTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import FacetAttributeUpdateTypeDef
```




Optional fields:
- `Attribute`: `"FacetAttributeTypeDef"`
- `Action`: `UpdateActionType`


## GetAppliedSchemaVersionResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import GetAppliedSchemaVersionResponseTypeDef
```




Optional fields:
- `AppliedSchemaArn`: `str`


## GetDirectoryResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import GetDirectoryResponseTypeDef
```


Required fields:
- `Directory`: `"DirectoryTypeDef"`




## GetFacetResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import GetFacetResponseTypeDef
```




Optional fields:
- `Facet`: `"FacetTypeDef"`


## GetLinkAttributesResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import GetLinkAttributesResponseTypeDef
```




Optional fields:
- `Attributes`: `List["AttributeKeyAndValueTypeDef"]`


## GetObjectAttributesResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import GetObjectAttributesResponseTypeDef
```




Optional fields:
- `Attributes`: `List["AttributeKeyAndValueTypeDef"]`


## GetObjectInformationResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import GetObjectInformationResponseTypeDef
```




Optional fields:
- `SchemaFacets`: `List["SchemaFacetTypeDef"]`
- `ObjectIdentifier`: `str`


## GetSchemaAsJsonResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import GetSchemaAsJsonResponseTypeDef
```




Optional fields:
- `Name`: `str`
- `Document`: `str`


## GetTypedLinkFacetInformationResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import GetTypedLinkFacetInformationResponseTypeDef
```




Optional fields:
- `IdentityAttributeOrder`: `List[str]`


## ListAppliedSchemaArnsResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import ListAppliedSchemaArnsResponseTypeDef
```




Optional fields:
- `SchemaArns`: `List[str]`
- `NextToken`: `str`


## ListAttachedIndicesResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import ListAttachedIndicesResponseTypeDef
```




Optional fields:
- `IndexAttachments`: `List["IndexAttachmentTypeDef"]`
- `NextToken`: `str`


## ListDevelopmentSchemaArnsResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import ListDevelopmentSchemaArnsResponseTypeDef
```




Optional fields:
- `SchemaArns`: `List[str]`
- `NextToken`: `str`


## ListDirectoriesResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import ListDirectoriesResponseTypeDef
```


Required fields:
- `Directories`: `List["DirectoryTypeDef"]`



Optional fields:
- `NextToken`: `str`


## ListFacetAttributesResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import ListFacetAttributesResponseTypeDef
```




Optional fields:
- `Attributes`: `List["FacetAttributeTypeDef"]`
- `NextToken`: `str`


## ListFacetNamesResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import ListFacetNamesResponseTypeDef
```




Optional fields:
- `FacetNames`: `List[str]`
- `NextToken`: `str`


## ListIncomingTypedLinksResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import ListIncomingTypedLinksResponseTypeDef
```




Optional fields:
- `LinkSpecifiers`: `List["TypedLinkSpecifierTypeDef"]`
- `NextToken`: `str`


## ListIndexResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import ListIndexResponseTypeDef
```




Optional fields:
- `IndexAttachments`: `List["IndexAttachmentTypeDef"]`
- `NextToken`: `str`


## ListManagedSchemaArnsResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import ListManagedSchemaArnsResponseTypeDef
```




Optional fields:
- `SchemaArns`: `List[str]`
- `NextToken`: `str`


## ListObjectAttributesResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import ListObjectAttributesResponseTypeDef
```




Optional fields:
- `Attributes`: `List["AttributeKeyAndValueTypeDef"]`
- `NextToken`: `str`


## ListObjectChildrenResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import ListObjectChildrenResponseTypeDef
```




Optional fields:
- `Children`: `Dict[str, str]`
- `NextToken`: `str`


## ListObjectParentPathsResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import ListObjectParentPathsResponseTypeDef
```




Optional fields:
- `PathToObjectIdentifiersList`: `List["PathToObjectIdentifiersTypeDef"]`
- `NextToken`: `str`


## ListObjectParentsResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import ListObjectParentsResponseTypeDef
```




Optional fields:
- `Parents`: `Dict[str, str]`
- `NextToken`: `str`
- `ParentLinks`: `List["ObjectIdentifierAndLinkNameTupleTypeDef"]`


## ListObjectPoliciesResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import ListObjectPoliciesResponseTypeDef
```




Optional fields:
- `AttachedPolicyIds`: `List[str]`
- `NextToken`: `str`


## ListOutgoingTypedLinksResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import ListOutgoingTypedLinksResponseTypeDef
```




Optional fields:
- `TypedLinkSpecifiers`: `List["TypedLinkSpecifierTypeDef"]`
- `NextToken`: `str`


## ListPolicyAttachmentsResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import ListPolicyAttachmentsResponseTypeDef
```




Optional fields:
- `ObjectIdentifiers`: `List[str]`
- `NextToken`: `str`


## ListPublishedSchemaArnsResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import ListPublishedSchemaArnsResponseTypeDef
```




Optional fields:
- `SchemaArns`: `List[str]`
- `NextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `Tags`: `List["TagTypeDef"]`
- `NextToken`: `str`


## ListTypedLinkFacetAttributesResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import ListTypedLinkFacetAttributesResponseTypeDef
```




Optional fields:
- `Attributes`: `List["TypedLinkAttributeDefinitionTypeDef"]`
- `NextToken`: `str`


## ListTypedLinkFacetNamesResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import ListTypedLinkFacetNamesResponseTypeDef
```




Optional fields:
- `FacetNames`: `List[str]`
- `NextToken`: `str`


## LookupPolicyResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import LookupPolicyResponseTypeDef
```




Optional fields:
- `PolicyToPathList`: `List["PolicyToPathTypeDef"]`
- `NextToken`: `str`


## PaginatorConfigTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## PublishSchemaResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import PublishSchemaResponseTypeDef
```




Optional fields:
- `PublishedSchemaArn`: `str`


## PutSchemaFromJsonResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import PutSchemaFromJsonResponseTypeDef
```




Optional fields:
- `Arn`: `str`


## TypedLinkFacetAttributeUpdateTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import TypedLinkFacetAttributeUpdateTypeDef
```


Required fields:
- `Attribute`: `"TypedLinkAttributeDefinitionTypeDef"`
- `Action`: `UpdateActionType`




## TypedLinkFacetTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import TypedLinkFacetTypeDef
```


Required fields:
- `Name`: `str`
- `Attributes`: `List["TypedLinkAttributeDefinitionTypeDef"]`
- `IdentityAttributeOrder`: `List[str]`




## UpdateObjectAttributesResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import UpdateObjectAttributesResponseTypeDef
```




Optional fields:
- `ObjectIdentifier`: `str`


## UpdateSchemaResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import UpdateSchemaResponseTypeDef
```




Optional fields:
- `SchemaArn`: `str`


## UpgradeAppliedSchemaResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import UpgradeAppliedSchemaResponseTypeDef
```




Optional fields:
- `UpgradedSchemaArn`: `str`
- `DirectoryArn`: `str`


## UpgradePublishedSchemaResponseTypeDef

```python
from mypy_boto3_clouddirectory.type_defs import UpgradePublishedSchemaResponseTypeDef
```




Optional fields:
- `UpgradedSchemaArn`: `str`

