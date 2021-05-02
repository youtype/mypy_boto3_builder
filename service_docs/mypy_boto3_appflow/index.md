# Type annotations for boto3 Appflow module

> [Index](../index.md) > Appflow

Auto-generated documentation for [Appflow](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow)
type annotations stubs module [mypy_boto3_appflow](https://pypi.org/project/mypy-boto3-appflow/).

```bash
pip install mypy-boto3-appflow
```

- [Type annotations for boto3 Appflow module](#type-annotations-for-boto3-appflow-module)
  - [AppflowClient](#appflowclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## AppflowClient

Type annotations for  `boto3.client("appflow")` as [AppflowClient](./client.md)

Can be used directly:

```python
from mypy_boto3_appflow.client import AppflowClient
```


AppflowClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_connector_profile](./client.md#create-connector-profile)
- [create_flow](./client.md#create-flow)
- [delete_connector_profile](./client.md#delete-connector-profile)
- [delete_flow](./client.md#delete-flow)
- [describe_connector_entity](./client.md#describe-connector-entity)
- [describe_connector_profiles](./client.md#describe-connector-profiles)
- [describe_connectors](./client.md#describe-connectors)
- [describe_flow](./client.md#describe-flow)
- [describe_flow_execution_records](./client.md#describe-flow-execution-records)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [list_connector_entities](./client.md#list-connector-entities)
- [list_flows](./client.md#list-flows)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [start_flow](./client.md#start-flow)
- [stop_flow](./client.md#stop-flow)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_connector_profile](./client.md#update-connector-profile)
- [update_flow](./client.md#update-flow)




### Exceptions
- [ClientError](./client.md#clienterror)
- [ConflictException](./client.md#conflictexception)
- [ConnectorAuthenticationException](./client.md#connectorauthenticationexception)
- [ConnectorServerException](./client.md#connectorserverexception)
- [InternalServerException](./client.md#internalserverexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ServiceQuotaExceededException](./client.md#servicequotaexceededexception)
- [UnsupportedOperationException](./client.md#unsupportedoperationexception)
- [ValidationException](./client.md#validationexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_appflow.literals import AggregationType, ...
```

- [AggregationType](./literals.md#aggregationtype)
- [AmplitudeConnectorOperator](./literals.md#amplitudeconnectoroperator)
- [ConnectionMode](./literals.md#connectionmode)
- [ConnectorType](./literals.md#connectortype)
- [DataPullMode](./literals.md#datapullmode)
- [DatadogConnectorOperator](./literals.md#datadogconnectoroperator)
- [DynatraceConnectorOperator](./literals.md#dynatraceconnectoroperator)
- [ExecutionStatus](./literals.md#executionstatus)
- [FileType](./literals.md#filetype)
- [FlowStatus](./literals.md#flowstatus)
- [GoogleAnalyticsConnectorOperator](./literals.md#googleanalyticsconnectoroperator)
- [InforNexusConnectorOperator](./literals.md#infornexusconnectoroperator)
- [MarketoConnectorOperator](./literals.md#marketoconnectoroperator)
- [Operator](./literals.md#operator)
- [OperatorPropertiesKeys](./literals.md#operatorpropertieskeys)
- [PrefixFormat](./literals.md#prefixformat)
- [PrefixType](./literals.md#prefixtype)
- [S3ConnectorOperator](./literals.md#s3connectoroperator)
- [SalesforceConnectorOperator](./literals.md#salesforceconnectoroperator)
- [ScheduleFrequencyType](./literals.md#schedulefrequencytype)
- [ServiceNowConnectorOperator](./literals.md#servicenowconnectoroperator)
- [SingularConnectorOperator](./literals.md#singularconnectoroperator)
- [SlackConnectorOperator](./literals.md#slackconnectoroperator)
- [TaskType](./literals.md#tasktype)
- [TrendmicroConnectorOperator](./literals.md#trendmicroconnectoroperator)
- [TriggerType](./literals.md#triggertype)
- [VeevaConnectorOperator](./literals.md#veevaconnectoroperator)
- [WriteOperationType](./literals.md#writeoperationtype)
- [ZendeskConnectorOperator](./literals.md#zendeskconnectoroperator)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_appflow.type_defs import AggregationConfigTypeDef, ...
```

- [AggregationConfigTypeDef](./type_defs.md#aggregationconfigtypedef)
- [AmplitudeConnectorProfileCredentialsTypeDef](./type_defs.md#amplitudeconnectorprofilecredentialstypedef)
- [AmplitudeSourcePropertiesTypeDef](./type_defs.md#amplitudesourcepropertiestypedef)
- [ConnectorConfigurationTypeDef](./type_defs.md#connectorconfigurationtypedef)
- [ConnectorEntityFieldTypeDef](./type_defs.md#connectorentityfieldtypedef)
- [ConnectorEntityTypeDef](./type_defs.md#connectorentitytypedef)
- [ConnectorMetadataTypeDef](./type_defs.md#connectormetadatatypedef)
- [ConnectorOAuthRequestTypeDef](./type_defs.md#connectoroauthrequesttypedef)
- [ConnectorOperatorTypeDef](./type_defs.md#connectoroperatortypedef)
- [ConnectorProfileConfigTypeDef](./type_defs.md#connectorprofileconfigtypedef)
- [ConnectorProfileCredentialsTypeDef](./type_defs.md#connectorprofilecredentialstypedef)
- [ConnectorProfilePropertiesTypeDef](./type_defs.md#connectorprofilepropertiestypedef)
- [ConnectorProfileTypeDef](./type_defs.md#connectorprofiletypedef)
- [CreateConnectorProfileResponseTypeDef](./type_defs.md#createconnectorprofileresponsetypedef)
- [CreateFlowResponseTypeDef](./type_defs.md#createflowresponsetypedef)
- [CustomerProfilesDestinationPropertiesTypeDef](./type_defs.md#customerprofilesdestinationpropertiestypedef)
- [DatadogConnectorProfileCredentialsTypeDef](./type_defs.md#datadogconnectorprofilecredentialstypedef)
- [DatadogConnectorProfilePropertiesTypeDef](./type_defs.md#datadogconnectorprofilepropertiestypedef)
- [DatadogSourcePropertiesTypeDef](./type_defs.md#datadogsourcepropertiestypedef)
- [DescribeConnectorEntityResponseTypeDef](./type_defs.md#describeconnectorentityresponsetypedef)
- [DescribeConnectorProfilesResponseTypeDef](./type_defs.md#describeconnectorprofilesresponsetypedef)
- [DescribeConnectorsResponseTypeDef](./type_defs.md#describeconnectorsresponsetypedef)
- [DescribeFlowExecutionRecordsResponseTypeDef](./type_defs.md#describeflowexecutionrecordsresponsetypedef)
- [DescribeFlowResponseTypeDef](./type_defs.md#describeflowresponsetypedef)
- [DestinationConnectorPropertiesTypeDef](./type_defs.md#destinationconnectorpropertiestypedef)
- [DestinationFieldPropertiesTypeDef](./type_defs.md#destinationfieldpropertiestypedef)
- [DestinationFlowConfigTypeDef](./type_defs.md#destinationflowconfigtypedef)
- [DynatraceConnectorProfileCredentialsTypeDef](./type_defs.md#dynatraceconnectorprofilecredentialstypedef)
- [DynatraceConnectorProfilePropertiesTypeDef](./type_defs.md#dynatraceconnectorprofilepropertiestypedef)
- [DynatraceSourcePropertiesTypeDef](./type_defs.md#dynatracesourcepropertiestypedef)
- [ErrorHandlingConfigTypeDef](./type_defs.md#errorhandlingconfigtypedef)
- [ErrorInfoTypeDef](./type_defs.md#errorinfotypedef)
- [EventBridgeDestinationPropertiesTypeDef](./type_defs.md#eventbridgedestinationpropertiestypedef)
- [ExecutionDetailsTypeDef](./type_defs.md#executiondetailstypedef)
- [ExecutionRecordTypeDef](./type_defs.md#executionrecordtypedef)
- [ExecutionResultTypeDef](./type_defs.md#executionresulttypedef)
- [FieldTypeDetailsTypeDef](./type_defs.md#fieldtypedetailstypedef)
- [FlowDefinitionTypeDef](./type_defs.md#flowdefinitiontypedef)
- [GoogleAnalyticsConnectorProfileCredentialsTypeDef](./type_defs.md#googleanalyticsconnectorprofilecredentialstypedef)
- [GoogleAnalyticsMetadataTypeDef](./type_defs.md#googleanalyticsmetadatatypedef)
- [GoogleAnalyticsSourcePropertiesTypeDef](./type_defs.md#googleanalyticssourcepropertiestypedef)
- [HoneycodeConnectorProfileCredentialsTypeDef](./type_defs.md#honeycodeconnectorprofilecredentialstypedef)
- [HoneycodeDestinationPropertiesTypeDef](./type_defs.md#honeycodedestinationpropertiestypedef)
- [HoneycodeMetadataTypeDef](./type_defs.md#honeycodemetadatatypedef)
- [IncrementalPullConfigTypeDef](./type_defs.md#incrementalpullconfigtypedef)
- [InforNexusConnectorProfileCredentialsTypeDef](./type_defs.md#infornexusconnectorprofilecredentialstypedef)
- [InforNexusConnectorProfilePropertiesTypeDef](./type_defs.md#infornexusconnectorprofilepropertiestypedef)
- [InforNexusSourcePropertiesTypeDef](./type_defs.md#infornexussourcepropertiestypedef)
- [ListConnectorEntitiesResponseTypeDef](./type_defs.md#listconnectorentitiesresponsetypedef)
- [ListFlowsResponseTypeDef](./type_defs.md#listflowsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [MarketoConnectorProfileCredentialsTypeDef](./type_defs.md#marketoconnectorprofilecredentialstypedef)
- [MarketoConnectorProfilePropertiesTypeDef](./type_defs.md#marketoconnectorprofilepropertiestypedef)
- [MarketoSourcePropertiesTypeDef](./type_defs.md#marketosourcepropertiestypedef)
- [PrefixConfigTypeDef](./type_defs.md#prefixconfigtypedef)
- [RedshiftConnectorProfileCredentialsTypeDef](./type_defs.md#redshiftconnectorprofilecredentialstypedef)
- [RedshiftConnectorProfilePropertiesTypeDef](./type_defs.md#redshiftconnectorprofilepropertiestypedef)
- [RedshiftDestinationPropertiesTypeDef](./type_defs.md#redshiftdestinationpropertiestypedef)
- [S3DestinationPropertiesTypeDef](./type_defs.md#s3destinationpropertiestypedef)
- [S3OutputFormatConfigTypeDef](./type_defs.md#s3outputformatconfigtypedef)
- [S3SourcePropertiesTypeDef](./type_defs.md#s3sourcepropertiestypedef)
- [SalesforceConnectorProfileCredentialsTypeDef](./type_defs.md#salesforceconnectorprofilecredentialstypedef)
- [SalesforceConnectorProfilePropertiesTypeDef](./type_defs.md#salesforceconnectorprofilepropertiestypedef)
- [SalesforceDestinationPropertiesTypeDef](./type_defs.md#salesforcedestinationpropertiestypedef)
- [SalesforceMetadataTypeDef](./type_defs.md#salesforcemetadatatypedef)
- [SalesforceSourcePropertiesTypeDef](./type_defs.md#salesforcesourcepropertiestypedef)
- [ScheduledTriggerPropertiesTypeDef](./type_defs.md#scheduledtriggerpropertiestypedef)
- [ServiceNowConnectorProfileCredentialsTypeDef](./type_defs.md#servicenowconnectorprofilecredentialstypedef)
- [ServiceNowConnectorProfilePropertiesTypeDef](./type_defs.md#servicenowconnectorprofilepropertiestypedef)
- [ServiceNowSourcePropertiesTypeDef](./type_defs.md#servicenowsourcepropertiestypedef)
- [SingularConnectorProfileCredentialsTypeDef](./type_defs.md#singularconnectorprofilecredentialstypedef)
- [SingularSourcePropertiesTypeDef](./type_defs.md#singularsourcepropertiestypedef)
- [SlackConnectorProfileCredentialsTypeDef](./type_defs.md#slackconnectorprofilecredentialstypedef)
- [SlackConnectorProfilePropertiesTypeDef](./type_defs.md#slackconnectorprofilepropertiestypedef)
- [SlackMetadataTypeDef](./type_defs.md#slackmetadatatypedef)
- [SlackSourcePropertiesTypeDef](./type_defs.md#slacksourcepropertiestypedef)
- [SnowflakeConnectorProfileCredentialsTypeDef](./type_defs.md#snowflakeconnectorprofilecredentialstypedef)
- [SnowflakeConnectorProfilePropertiesTypeDef](./type_defs.md#snowflakeconnectorprofilepropertiestypedef)
- [SnowflakeDestinationPropertiesTypeDef](./type_defs.md#snowflakedestinationpropertiestypedef)
- [SnowflakeMetadataTypeDef](./type_defs.md#snowflakemetadatatypedef)
- [SourceConnectorPropertiesTypeDef](./type_defs.md#sourceconnectorpropertiestypedef)
- [SourceFieldPropertiesTypeDef](./type_defs.md#sourcefieldpropertiestypedef)
- [SourceFlowConfigTypeDef](./type_defs.md#sourceflowconfigtypedef)
- [StartFlowResponseTypeDef](./type_defs.md#startflowresponsetypedef)
- [StopFlowResponseTypeDef](./type_defs.md#stopflowresponsetypedef)
- [SupportedFieldTypeDetailsTypeDef](./type_defs.md#supportedfieldtypedetailstypedef)
- [TaskTypeDef](./type_defs.md#tasktypedef)
- [TrendmicroConnectorProfileCredentialsTypeDef](./type_defs.md#trendmicroconnectorprofilecredentialstypedef)
- [TrendmicroSourcePropertiesTypeDef](./type_defs.md#trendmicrosourcepropertiestypedef)
- [TriggerConfigTypeDef](./type_defs.md#triggerconfigtypedef)
- [TriggerPropertiesTypeDef](./type_defs.md#triggerpropertiestypedef)
- [UpdateConnectorProfileResponseTypeDef](./type_defs.md#updateconnectorprofileresponsetypedef)
- [UpdateFlowResponseTypeDef](./type_defs.md#updateflowresponsetypedef)
- [UpsolverDestinationPropertiesTypeDef](./type_defs.md#upsolverdestinationpropertiestypedef)
- [UpsolverS3OutputFormatConfigTypeDef](./type_defs.md#upsolvers3outputformatconfigtypedef)
- [VeevaConnectorProfileCredentialsTypeDef](./type_defs.md#veevaconnectorprofilecredentialstypedef)
- [VeevaConnectorProfilePropertiesTypeDef](./type_defs.md#veevaconnectorprofilepropertiestypedef)
- [VeevaSourcePropertiesTypeDef](./type_defs.md#veevasourcepropertiestypedef)
- [ZendeskConnectorProfileCredentialsTypeDef](./type_defs.md#zendeskconnectorprofilecredentialstypedef)
- [ZendeskConnectorProfilePropertiesTypeDef](./type_defs.md#zendeskconnectorprofilepropertiestypedef)
- [ZendeskDestinationPropertiesTypeDef](./type_defs.md#zendeskdestinationpropertiestypedef)
- [ZendeskMetadataTypeDef](./type_defs.md#zendeskmetadatatypedef)
- [ZendeskSourcePropertiesTypeDef](./type_defs.md#zendesksourcepropertiestypedef)
