# Type annotations for boto3 MQ module

> [Index](../index.md) > MQ

Auto-generated documentation for [MQ](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mq.html#MQ)
type annotations stubs module [mypy_boto3_mq](https://pypi.org/project/mypy-boto3-mq/).

```bash
pip install mypy-boto3-mq
```

- [Type annotations for boto3 MQ module](#type-annotations-for-boto3-mq-module)
  - [MQClient](#mqclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## MQClient

Type annotations for  `boto3.client("mq")` as [MQClient](./client.md)

Can be used directly:

```python
from mypy_boto3_mq.client import MQClient
```


MQClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_broker](./client.md#create-broker)
- [create_configuration](./client.md#create-configuration)
- [create_tags](./client.md#create-tags)
- [create_user](./client.md#create-user)
- [delete_broker](./client.md#delete-broker)
- [delete_tags](./client.md#delete-tags)
- [delete_user](./client.md#delete-user)
- [describe_broker](./client.md#describe-broker)
- [describe_broker_engine_types](./client.md#describe-broker-engine-types)
- [describe_broker_instance_options](./client.md#describe-broker-instance-options)
- [describe_configuration](./client.md#describe-configuration)
- [describe_configuration_revision](./client.md#describe-configuration-revision)
- [describe_user](./client.md#describe-user)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_paginator](./client.md#get-paginator)
- [list_brokers](./client.md#list-brokers)
- [list_configuration_revisions](./client.md#list-configuration-revisions)
- [list_configurations](./client.md#list-configurations)
- [list_tags](./client.md#list-tags)
- [list_users](./client.md#list-users)
- [reboot_broker](./client.md#reboot-broker)
- [update_broker](./client.md#update-broker)
- [update_configuration](./client.md#update-configuration)
- [update_user](./client.md#update-user)




### Exceptions
- [BadRequestException](./client.md#badrequestexception)
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [ForbiddenException](./client.md#forbiddenexception)
- [InternalServerErrorException](./client.md#internalservererrorexception)
- [NotFoundException](./client.md#notfoundexception)
- [UnauthorizedException](./client.md#unauthorizedexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("mq").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_mq.paginators import ListBrokersPaginator, ...
```

- [ListBrokersPaginator](./paginators.md#listbrokerspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_mq.literals import AuthenticationStrategy, ...
```

- [AuthenticationStrategy](./literals.md#authenticationstrategy)
- [BrokerState](./literals.md#brokerstate)
- [BrokerStorageType](./literals.md#brokerstoragetype)
- [ChangeType](./literals.md#changetype)
- [DayOfWeek](./literals.md#dayofweek)
- [DeploymentMode](./literals.md#deploymentmode)
- [EngineType](./literals.md#enginetype)
- [ListBrokersPaginatorName](./literals.md#listbrokerspaginatorname)
- [SanitizationWarningReason](./literals.md#sanitizationwarningreason)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_mq.type_defs import AvailabilityZoneTypeDef, ...
```

- [AvailabilityZoneTypeDef](./type_defs.md#availabilityzonetypedef)
- [BrokerEngineTypeTypeDef](./type_defs.md#brokerenginetypetypedef)
- [BrokerInstanceOptionTypeDef](./type_defs.md#brokerinstanceoptiontypedef)
- [BrokerInstanceTypeDef](./type_defs.md#brokerinstancetypedef)
- [BrokerSummaryTypeDef](./type_defs.md#brokersummarytypedef)
- [ConfigurationIdTypeDef](./type_defs.md#configurationidtypedef)
- [ConfigurationRevisionTypeDef](./type_defs.md#configurationrevisiontypedef)
- [ConfigurationTypeDef](./type_defs.md#configurationtypedef)
- [ConfigurationsTypeDef](./type_defs.md#configurationstypedef)
- [EncryptionOptionsTypeDef](./type_defs.md#encryptionoptionstypedef)
- [EngineVersionTypeDef](./type_defs.md#engineversiontypedef)
- [LdapServerMetadataOutputTypeDef](./type_defs.md#ldapservermetadataoutputtypedef)
- [LogsSummaryTypeDef](./type_defs.md#logssummarytypedef)
- [LogsTypeDef](./type_defs.md#logstypedef)
- [PendingLogsTypeDef](./type_defs.md#pendinglogstypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [SanitizationWarningTypeDef](./type_defs.md#sanitizationwarningtypedef)
- [UserPendingChangesTypeDef](./type_defs.md#userpendingchangestypedef)
- [UserSummaryTypeDef](./type_defs.md#usersummarytypedef)
- [WeeklyStartTimeTypeDef](./type_defs.md#weeklystarttimetypedef)
- [CreateBrokerResponseTypeDef](./type_defs.md#createbrokerresponsetypedef)
- [CreateConfigurationResponseTypeDef](./type_defs.md#createconfigurationresponsetypedef)
- [DeleteBrokerResponseTypeDef](./type_defs.md#deletebrokerresponsetypedef)
- [DescribeBrokerEngineTypesResponseTypeDef](./type_defs.md#describebrokerenginetypesresponsetypedef)
- [DescribeBrokerInstanceOptionsResponseTypeDef](./type_defs.md#describebrokerinstanceoptionsresponsetypedef)
- [DescribeBrokerResponseTypeDef](./type_defs.md#describebrokerresponsetypedef)
- [DescribeConfigurationResponseTypeDef](./type_defs.md#describeconfigurationresponsetypedef)
- [DescribeConfigurationRevisionResponseTypeDef](./type_defs.md#describeconfigurationrevisionresponsetypedef)
- [DescribeUserResponseTypeDef](./type_defs.md#describeuserresponsetypedef)
- [LdapServerMetadataInputTypeDef](./type_defs.md#ldapservermetadatainputtypedef)
- [ListBrokersResponseTypeDef](./type_defs.md#listbrokersresponsetypedef)
- [ListConfigurationRevisionsResponseTypeDef](./type_defs.md#listconfigurationrevisionsresponsetypedef)
- [ListConfigurationsResponseTypeDef](./type_defs.md#listconfigurationsresponsetypedef)
- [ListTagsResponseTypeDef](./type_defs.md#listtagsresponsetypedef)
- [ListUsersResponseTypeDef](./type_defs.md#listusersresponsetypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [UpdateBrokerResponseTypeDef](./type_defs.md#updatebrokerresponsetypedef)
- [UpdateConfigurationResponseTypeDef](./type_defs.md#updateconfigurationresponsetypedef)
- [UserTypeDef](./type_defs.md#usertypedef)
