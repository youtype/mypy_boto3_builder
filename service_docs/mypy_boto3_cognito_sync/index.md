# Type annotations for boto3 CognitoSync module

> [Index](../index.md) > CognitoSync

Auto-generated documentation for [CognitoSync](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync.html#CognitoSync)
type annotations stubs module [mypy_boto3_cognito_sync](https://pypi.org/project/mypy-boto3-cognito-sync/).

```bash
pip install mypy-boto3-cognito-sync
```

- [Type annotations for boto3 CognitoSync module](#type-annotations-for-boto3-cognitosync-module)
  - [CognitoSyncClient](#cognitosyncclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## CognitoSyncClient

Type annotations for  `boto3.client("cognito-sync")` as [CognitoSyncClient](./client.md)

Can be used directly:

```python
from mypy_boto3_cognito_sync.client import CognitoSyncClient
```


CognitoSyncClient [exceptions](./client.md#exceptions)



### Methods
- [bulk_publish](./client.md#bulk-publish)
- [can_paginate](./client.md#can-paginate)
- [delete_dataset](./client.md#delete-dataset)
- [describe_dataset](./client.md#describe-dataset)
- [describe_identity_pool_usage](./client.md#describe-identity-pool-usage)
- [describe_identity_usage](./client.md#describe-identity-usage)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_bulk_publish_details](./client.md#get-bulk-publish-details)
- [get_cognito_events](./client.md#get-cognito-events)
- [get_identity_pool_configuration](./client.md#get-identity-pool-configuration)
- [list_datasets](./client.md#list-datasets)
- [list_identity_pool_usage](./client.md#list-identity-pool-usage)
- [list_records](./client.md#list-records)
- [register_device](./client.md#register-device)
- [set_cognito_events](./client.md#set-cognito-events)
- [set_identity_pool_configuration](./client.md#set-identity-pool-configuration)
- [subscribe_to_dataset](./client.md#subscribe-to-dataset)
- [unsubscribe_from_dataset](./client.md#unsubscribe-from-dataset)
- [update_records](./client.md#update-records)




### Exceptions
- [AlreadyStreamedException](./client.md#alreadystreamedexception)
- [ClientError](./client.md#clienterror)
- [ConcurrentModificationException](./client.md#concurrentmodificationexception)
- [DuplicateRequestException](./client.md#duplicaterequestexception)
- [InternalErrorException](./client.md#internalerrorexception)
- [InvalidConfigurationException](./client.md#invalidconfigurationexception)
- [InvalidLambdaFunctionOutputException](./client.md#invalidlambdafunctionoutputexception)
- [InvalidParameterException](./client.md#invalidparameterexception)
- [LambdaThrottledException](./client.md#lambdathrottledexception)
- [LimitExceededException](./client.md#limitexceededexception)
- [NotAuthorizedException](./client.md#notauthorizedexception)
- [ResourceConflictException](./client.md#resourceconflictexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [TooManyRequestsException](./client.md#toomanyrequestsexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_cognito_sync.literals import BulkPublishStatus, ...
```

- [BulkPublishStatus](./literals.md#bulkpublishstatus)
- [Operation](./literals.md#operation)
- [Platform](./literals.md#platform)
- [StreamingStatus](./literals.md#streamingstatus)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_cognito_sync.type_defs import BulkPublishResponseTypeDef, ...
```

- [BulkPublishResponseTypeDef](./type_defs.md#bulkpublishresponsetypedef)
- [CognitoStreamsTypeDef](./type_defs.md#cognitostreamstypedef)
- [DatasetTypeDef](./type_defs.md#datasettypedef)
- [DeleteDatasetResponseTypeDef](./type_defs.md#deletedatasetresponsetypedef)
- [DescribeDatasetResponseTypeDef](./type_defs.md#describedatasetresponsetypedef)
- [DescribeIdentityPoolUsageResponseTypeDef](./type_defs.md#describeidentitypoolusageresponsetypedef)
- [DescribeIdentityUsageResponseTypeDef](./type_defs.md#describeidentityusageresponsetypedef)
- [GetBulkPublishDetailsResponseTypeDef](./type_defs.md#getbulkpublishdetailsresponsetypedef)
- [GetCognitoEventsResponseTypeDef](./type_defs.md#getcognitoeventsresponsetypedef)
- [GetIdentityPoolConfigurationResponseTypeDef](./type_defs.md#getidentitypoolconfigurationresponsetypedef)
- [IdentityPoolUsageTypeDef](./type_defs.md#identitypoolusagetypedef)
- [IdentityUsageTypeDef](./type_defs.md#identityusagetypedef)
- [ListDatasetsResponseTypeDef](./type_defs.md#listdatasetsresponsetypedef)
- [ListIdentityPoolUsageResponseTypeDef](./type_defs.md#listidentitypoolusageresponsetypedef)
- [ListRecordsResponseTypeDef](./type_defs.md#listrecordsresponsetypedef)
- [PushSyncTypeDef](./type_defs.md#pushsynctypedef)
- [RecordPatchTypeDef](./type_defs.md#recordpatchtypedef)
- [RecordTypeDef](./type_defs.md#recordtypedef)
- [RegisterDeviceResponseTypeDef](./type_defs.md#registerdeviceresponsetypedef)
- [SetIdentityPoolConfigurationResponseTypeDef](./type_defs.md#setidentitypoolconfigurationresponsetypedef)
- [UpdateRecordsResponseTypeDef](./type_defs.md#updaterecordsresponsetypedef)
