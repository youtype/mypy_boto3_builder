# Type annotations for boto3 Mobile module

> [Index](../index.md) > Mobile

Auto-generated documentation for [Mobile](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mobile.html#Mobile)
type annotations stubs module [mypy_boto3_mobile](https://pypi.org/project/mypy-boto3-mobile/).

```bash
pip install mypy-boto3-mobile
```

- [Type annotations for boto3 Mobile module](#type-annotations-for-boto3-mobile-module)
  - [MobileClient](#mobileclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## MobileClient

Type annotations for  `boto3.client("mobile")` as [MobileClient](./client.md)

Can be used directly:

```python
from mypy_boto3_mobile.client import MobileClient
```


MobileClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_project](./client.md#create-project)
- [delete_project](./client.md#delete-project)
- [describe_bundle](./client.md#describe-bundle)
- [describe_project](./client.md#describe-project)
- [export_bundle](./client.md#export-bundle)
- [export_project](./client.md#export-project)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [list_bundles](./client.md#list-bundles)
- [list_projects](./client.md#list-projects)
- [update_project](./client.md#update-project)




### Exceptions
- [AccountActionRequiredException](./client.md#accountactionrequiredexception)
- [BadRequestException](./client.md#badrequestexception)
- [ClientError](./client.md#clienterror)
- [InternalFailureException](./client.md#internalfailureexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [NotFoundException](./client.md#notfoundexception)
- [ServiceUnavailableException](./client.md#serviceunavailableexception)
- [TooManyRequestsException](./client.md#toomanyrequestsexception)
- [UnauthorizedException](./client.md#unauthorizedexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("mobile").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_mobile.paginators import ListBundlesPaginator, ...
```

- [ListBundlesPaginator](./paginators.md#listbundlespaginator)
- [ListProjectsPaginator](./paginators.md#listprojectspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_mobile.literals import ListBundlesPaginatorName, ...
```

- [ListBundlesPaginatorName](./literals.md#listbundlespaginatorname)
- [ListProjectsPaginatorName](./literals.md#listprojectspaginatorname)
- [Platform](./literals.md#platform)
- [ProjectState](./literals.md#projectstate)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_mobile.type_defs import BundleDetailsTypeDef, ...
```

- [BundleDetailsTypeDef](./type_defs.md#bundledetailstypedef)
- [ProjectDetailsTypeDef](./type_defs.md#projectdetailstypedef)
- [ProjectSummaryTypeDef](./type_defs.md#projectsummarytypedef)
- [ResourceTypeDef](./type_defs.md#resourcetypedef)
- [CreateProjectResultTypeDef](./type_defs.md#createprojectresulttypedef)
- [DeleteProjectResultTypeDef](./type_defs.md#deleteprojectresulttypedef)
- [DescribeBundleResultTypeDef](./type_defs.md#describebundleresulttypedef)
- [DescribeProjectResultTypeDef](./type_defs.md#describeprojectresulttypedef)
- [ExportBundleResultTypeDef](./type_defs.md#exportbundleresulttypedef)
- [ExportProjectResultTypeDef](./type_defs.md#exportprojectresulttypedef)
- [ListBundlesResultTypeDef](./type_defs.md#listbundlesresulttypedef)
- [ListProjectsResultTypeDef](./type_defs.md#listprojectsresulttypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [UpdateProjectResultTypeDef](./type_defs.md#updateprojectresulttypedef)
