# Structures for boto3 AppRegistry module

> [Index](../index.md) > [AppRegistry](./index.md) > Structures

Auto-generated documentation for [AppRegistry](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/servicecatalog-appregistry.html#AppRegistry)
type annotations stubs module [mypy_boto3_servicecatalog_appregistry](https://pypi.org/project/mypy-boto3-servicecatalog-appregistry/).

- [Structures for boto3 AppRegistry module](#structures-for-boto3-appregistry-module)
  - [ApplicationSummaryTypeDef](#applicationsummarytypedef)
  - [ApplicationTypeDef](#applicationtypedef)
  - [AssociateAttributeGroupResponseTypeDef](#associateattributegroupresponsetypedef)
  - [AssociateResourceResponseTypeDef](#associateresourceresponsetypedef)
  - [AttributeGroupSummaryTypeDef](#attributegroupsummarytypedef)
  - [AttributeGroupTypeDef](#attributegrouptypedef)
  - [CreateApplicationResponseTypeDef](#createapplicationresponsetypedef)
  - [CreateAttributeGroupResponseTypeDef](#createattributegroupresponsetypedef)
  - [DeleteApplicationResponseTypeDef](#deleteapplicationresponsetypedef)
  - [DeleteAttributeGroupResponseTypeDef](#deleteattributegroupresponsetypedef)
  - [DisassociateAttributeGroupResponseTypeDef](#disassociateattributegroupresponsetypedef)
  - [DisassociateResourceResponseTypeDef](#disassociateresourceresponsetypedef)
  - [GetApplicationResponseTypeDef](#getapplicationresponsetypedef)
  - [GetAttributeGroupResponseTypeDef](#getattributegroupresponsetypedef)
  - [ListApplicationsResponseTypeDef](#listapplicationsresponsetypedef)
  - [ListAssociatedAttributeGroupsResponseTypeDef](#listassociatedattributegroupsresponsetypedef)
  - [ListAssociatedResourcesResponseTypeDef](#listassociatedresourcesresponsetypedef)
  - [ListAttributeGroupsResponseTypeDef](#listattributegroupsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [PaginatorConfigTypeDef](#paginatorconfigtypedef)
  - [ResourceInfoTypeDef](#resourceinfotypedef)
  - [SyncResourceResponseTypeDef](#syncresourceresponsetypedef)
  - [UpdateApplicationResponseTypeDef](#updateapplicationresponsetypedef)
  - [UpdateAttributeGroupResponseTypeDef](#updateattributegroupresponsetypedef)

## ApplicationSummaryTypeDef

```python
from mypy_boto3_servicecatalog_appregistry.type_defs import ApplicationSummaryTypeDef
```




Optional fields:
- `id`: `str`
- `arn`: `str`
- `name`: `str`
- `description`: `str`
- `creationTime`: `datetime`
- `lastUpdateTime`: `datetime`


## ApplicationTypeDef

```python
from mypy_boto3_servicecatalog_appregistry.type_defs import ApplicationTypeDef
```




Optional fields:
- `id`: `str`
- `arn`: `str`
- `name`: `str`
- `description`: `str`
- `creationTime`: `datetime`
- `lastUpdateTime`: `datetime`
- `tags`: `Dict[str, str]`


## AssociateAttributeGroupResponseTypeDef

```python
from mypy_boto3_servicecatalog_appregistry.type_defs import AssociateAttributeGroupResponseTypeDef
```




Optional fields:
- `applicationArn`: `str`
- `attributeGroupArn`: `str`


## AssociateResourceResponseTypeDef

```python
from mypy_boto3_servicecatalog_appregistry.type_defs import AssociateResourceResponseTypeDef
```




Optional fields:
- `applicationArn`: `str`
- `resourceArn`: `str`


## AttributeGroupSummaryTypeDef

```python
from mypy_boto3_servicecatalog_appregistry.type_defs import AttributeGroupSummaryTypeDef
```




Optional fields:
- `id`: `str`
- `arn`: `str`
- `name`: `str`
- `description`: `str`
- `creationTime`: `datetime`
- `lastUpdateTime`: `datetime`


## AttributeGroupTypeDef

```python
from mypy_boto3_servicecatalog_appregistry.type_defs import AttributeGroupTypeDef
```




Optional fields:
- `id`: `str`
- `arn`: `str`
- `name`: `str`
- `description`: `str`
- `creationTime`: `datetime`
- `lastUpdateTime`: `datetime`
- `tags`: `Dict[str, str]`


## CreateApplicationResponseTypeDef

```python
from mypy_boto3_servicecatalog_appregistry.type_defs import CreateApplicationResponseTypeDef
```




Optional fields:
- `application`: `"ApplicationTypeDef"`


## CreateAttributeGroupResponseTypeDef

```python
from mypy_boto3_servicecatalog_appregistry.type_defs import CreateAttributeGroupResponseTypeDef
```




Optional fields:
- `attributeGroup`: `"AttributeGroupTypeDef"`


## DeleteApplicationResponseTypeDef

```python
from mypy_boto3_servicecatalog_appregistry.type_defs import DeleteApplicationResponseTypeDef
```




Optional fields:
- `application`: `"ApplicationSummaryTypeDef"`


## DeleteAttributeGroupResponseTypeDef

```python
from mypy_boto3_servicecatalog_appregistry.type_defs import DeleteAttributeGroupResponseTypeDef
```




Optional fields:
- `attributeGroup`: `"AttributeGroupSummaryTypeDef"`


## DisassociateAttributeGroupResponseTypeDef

```python
from mypy_boto3_servicecatalog_appregistry.type_defs import DisassociateAttributeGroupResponseTypeDef
```




Optional fields:
- `applicationArn`: `str`
- `attributeGroupArn`: `str`


## DisassociateResourceResponseTypeDef

```python
from mypy_boto3_servicecatalog_appregistry.type_defs import DisassociateResourceResponseTypeDef
```




Optional fields:
- `applicationArn`: `str`
- `resourceArn`: `str`


## GetApplicationResponseTypeDef

```python
from mypy_boto3_servicecatalog_appregistry.type_defs import GetApplicationResponseTypeDef
```




Optional fields:
- `id`: `str`
- `arn`: `str`
- `name`: `str`
- `description`: `str`
- `creationTime`: `datetime`
- `lastUpdateTime`: `datetime`
- `associatedResourceCount`: `int`
- `tags`: `Dict[str, str]`


## GetAttributeGroupResponseTypeDef

```python
from mypy_boto3_servicecatalog_appregistry.type_defs import GetAttributeGroupResponseTypeDef
```




Optional fields:
- `id`: `str`
- `arn`: `str`
- `name`: `str`
- `description`: `str`
- `attributes`: `str`
- `creationTime`: `datetime`
- `lastUpdateTime`: `datetime`
- `tags`: `Dict[str, str]`


## ListApplicationsResponseTypeDef

```python
from mypy_boto3_servicecatalog_appregistry.type_defs import ListApplicationsResponseTypeDef
```




Optional fields:
- `applications`: `List["ApplicationSummaryTypeDef"]`
- `nextToken`: `str`


## ListAssociatedAttributeGroupsResponseTypeDef

```python
from mypy_boto3_servicecatalog_appregistry.type_defs import ListAssociatedAttributeGroupsResponseTypeDef
```




Optional fields:
- `attributeGroups`: `List[str]`
- `nextToken`: `str`


## ListAssociatedResourcesResponseTypeDef

```python
from mypy_boto3_servicecatalog_appregistry.type_defs import ListAssociatedResourcesResponseTypeDef
```




Optional fields:
- `resources`: `List["ResourceInfoTypeDef"]`
- `nextToken`: `str`


## ListAttributeGroupsResponseTypeDef

```python
from mypy_boto3_servicecatalog_appregistry.type_defs import ListAttributeGroupsResponseTypeDef
```




Optional fields:
- `attributeGroups`: `List["AttributeGroupSummaryTypeDef"]`
- `nextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_servicecatalog_appregistry.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `tags`: `Dict[str, str]`


## PaginatorConfigTypeDef

```python
from mypy_boto3_servicecatalog_appregistry.type_defs import PaginatorConfigTypeDef
```




Optional fields:
- `MaxItems`: `int`
- `PageSize`: `int`
- `StartingToken`: `str`


## ResourceInfoTypeDef

```python
from mypy_boto3_servicecatalog_appregistry.type_defs import ResourceInfoTypeDef
```




Optional fields:
- `name`: `str`
- `arn`: `str`


## SyncResourceResponseTypeDef

```python
from mypy_boto3_servicecatalog_appregistry.type_defs import SyncResourceResponseTypeDef
```




Optional fields:
- `applicationArn`: `str`
- `resourceArn`: `str`
- `actionTaken`: `SyncAction`


## UpdateApplicationResponseTypeDef

```python
from mypy_boto3_servicecatalog_appregistry.type_defs import UpdateApplicationResponseTypeDef
```




Optional fields:
- `application`: `"ApplicationTypeDef"`


## UpdateAttributeGroupResponseTypeDef

```python
from mypy_boto3_servicecatalog_appregistry.type_defs import UpdateAttributeGroupResponseTypeDef
```




Optional fields:
- `attributeGroup`: `"AttributeGroupTypeDef"`

