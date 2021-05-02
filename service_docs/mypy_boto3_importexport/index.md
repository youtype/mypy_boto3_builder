# Type annotations for boto3 ImportExport module

> [Index](../index.md) > ImportExport

Auto-generated documentation for [ImportExport](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/importexport.html#ImportExport)
type annotations stubs module [mypy_boto3_importexport](https://pypi.org/project/mypy-boto3-importexport/).

```bash
pip install mypy-boto3-importexport
```

- [Type annotations for boto3 ImportExport module](#type-annotations-for-boto3-importexport-module)
  - [ImportExportClient](#importexportclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## ImportExportClient

Type annotations for  `boto3.client("importexport")` as [ImportExportClient](./client.md)

Can be used directly:

```python
from mypy_boto3_importexport.client import ImportExportClient
```


ImportExportClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [cancel_job](./client.md#cancel-job)
- [create_job](./client.md#create-job)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [get_shipping_label](./client.md#get-shipping-label)
- [get_status](./client.md#get-status)
- [list_jobs](./client.md#list-jobs)
- [update_job](./client.md#update-job)




### Exceptions
- [BucketPermissionException](./client.md#bucketpermissionexception)
- [CanceledJobIdException](./client.md#canceledjobidexception)
- [ClientError](./client.md#clienterror)
- [CreateJobQuotaExceededException](./client.md#createjobquotaexceededexception)
- [ExpiredJobIdException](./client.md#expiredjobidexception)
- [InvalidAccessKeyIdException](./client.md#invalidaccesskeyidexception)
- [InvalidAddressException](./client.md#invalidaddressexception)
- [InvalidCustomsException](./client.md#invalidcustomsexception)
- [InvalidFileSystemException](./client.md#invalidfilesystemexception)
- [InvalidJobIdException](./client.md#invalidjobidexception)
- [InvalidManifestFieldException](./client.md#invalidmanifestfieldexception)
- [InvalidParameterException](./client.md#invalidparameterexception)
- [InvalidVersionException](./client.md#invalidversionexception)
- [MalformedManifestException](./client.md#malformedmanifestexception)
- [MissingCustomsException](./client.md#missingcustomsexception)
- [MissingManifestFieldException](./client.md#missingmanifestfieldexception)
- [MissingParameterException](./client.md#missingparameterexception)
- [MultipleRegionsException](./client.md#multipleregionsexception)
- [NoSuchBucketException](./client.md#nosuchbucketexception)
- [UnableToCancelJobIdException](./client.md#unabletocanceljobidexception)
- [UnableToUpdateJobIdException](./client.md#unabletoupdatejobidexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("importexport").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_importexport.paginators import ListJobsPaginator, ...
```

- [ListJobsPaginator](./paginators.md#listjobspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_importexport.literals import JobType, ...
```

- [JobType](./literals.md#jobtype)
- [ListJobsPaginatorName](./literals.md#listjobspaginatorname)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_importexport.type_defs import ArtifactTypeDef, ...
```

- [ArtifactTypeDef](./type_defs.md#artifacttypedef)
- [CancelJobOutputTypeDef](./type_defs.md#canceljoboutputtypedef)
- [CreateJobOutputTypeDef](./type_defs.md#createjoboutputtypedef)
- [GetShippingLabelOutputTypeDef](./type_defs.md#getshippinglabeloutputtypedef)
- [GetStatusOutputTypeDef](./type_defs.md#getstatusoutputtypedef)
- [JobTypeDef](./type_defs.md#jobtypedef)
- [ListJobsOutputTypeDef](./type_defs.md#listjobsoutputtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [UpdateJobOutputTypeDef](./type_defs.md#updatejoboutputtypedef)
