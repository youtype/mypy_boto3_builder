# Structures for boto3 Appflow module

> [Index](../index.md) > [Appflow](./index.md) > Structures

Auto-generated documentation for [Appflow](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appflow.html#Appflow)
type annotations stubs module [mypy_boto3_appflow](https://pypi.org/project/mypy-boto3-appflow/).

- [Structures for boto3 Appflow module](#structures-for-boto3-appflow-module)
  - [AggregationConfigTypeDef](#aggregationconfigtypedef)
  - [AmplitudeConnectorProfileCredentialsTypeDef](#amplitudeconnectorprofilecredentialstypedef)
  - [AmplitudeSourcePropertiesTypeDef](#amplitudesourcepropertiestypedef)
  - [ConnectorConfigurationTypeDef](#connectorconfigurationtypedef)
  - [ConnectorEntityFieldTypeDef](#connectorentityfieldtypedef)
  - [ConnectorEntityTypeDef](#connectorentitytypedef)
  - [ConnectorMetadataTypeDef](#connectormetadatatypedef)
  - [ConnectorOAuthRequestTypeDef](#connectoroauthrequesttypedef)
  - [ConnectorOperatorTypeDef](#connectoroperatortypedef)
  - [ConnectorProfileCredentialsTypeDef](#connectorprofilecredentialstypedef)
  - [ConnectorProfilePropertiesTypeDef](#connectorprofilepropertiestypedef)
  - [ConnectorProfileTypeDef](#connectorprofiletypedef)
  - [CustomerProfilesDestinationPropertiesTypeDef](#customerprofilesdestinationpropertiestypedef)
  - [DatadogConnectorProfileCredentialsTypeDef](#datadogconnectorprofilecredentialstypedef)
  - [DatadogConnectorProfilePropertiesTypeDef](#datadogconnectorprofilepropertiestypedef)
  - [DatadogSourcePropertiesTypeDef](#datadogsourcepropertiestypedef)
  - [DestinationConnectorPropertiesTypeDef](#destinationconnectorpropertiestypedef)
  - [DestinationFieldPropertiesTypeDef](#destinationfieldpropertiestypedef)
  - [DestinationFlowConfigTypeDef](#destinationflowconfigtypedef)
  - [DynatraceConnectorProfileCredentialsTypeDef](#dynatraceconnectorprofilecredentialstypedef)
  - [DynatraceConnectorProfilePropertiesTypeDef](#dynatraceconnectorprofilepropertiestypedef)
  - [DynatraceSourcePropertiesTypeDef](#dynatracesourcepropertiestypedef)
  - [ErrorHandlingConfigTypeDef](#errorhandlingconfigtypedef)
  - [ErrorInfoTypeDef](#errorinfotypedef)
  - [EventBridgeDestinationPropertiesTypeDef](#eventbridgedestinationpropertiestypedef)
  - [ExecutionDetailsTypeDef](#executiondetailstypedef)
  - [ExecutionRecordTypeDef](#executionrecordtypedef)
  - [ExecutionResultTypeDef](#executionresulttypedef)
  - [FieldTypeDetailsTypeDef](#fieldtypedetailstypedef)
  - [FlowDefinitionTypeDef](#flowdefinitiontypedef)
  - [GoogleAnalyticsConnectorProfileCredentialsTypeDef](#googleanalyticsconnectorprofilecredentialstypedef)
  - [GoogleAnalyticsMetadataTypeDef](#googleanalyticsmetadatatypedef)
  - [GoogleAnalyticsSourcePropertiesTypeDef](#googleanalyticssourcepropertiestypedef)
  - [HoneycodeConnectorProfileCredentialsTypeDef](#honeycodeconnectorprofilecredentialstypedef)
  - [HoneycodeDestinationPropertiesTypeDef](#honeycodedestinationpropertiestypedef)
  - [HoneycodeMetadataTypeDef](#honeycodemetadatatypedef)
  - [IncrementalPullConfigTypeDef](#incrementalpullconfigtypedef)
  - [InforNexusConnectorProfileCredentialsTypeDef](#infornexusconnectorprofilecredentialstypedef)
  - [InforNexusConnectorProfilePropertiesTypeDef](#infornexusconnectorprofilepropertiestypedef)
  - [InforNexusSourcePropertiesTypeDef](#infornexussourcepropertiestypedef)
  - [MarketoConnectorProfileCredentialsTypeDef](#marketoconnectorprofilecredentialstypedef)
  - [MarketoConnectorProfilePropertiesTypeDef](#marketoconnectorprofilepropertiestypedef)
  - [MarketoSourcePropertiesTypeDef](#marketosourcepropertiestypedef)
  - [PrefixConfigTypeDef](#prefixconfigtypedef)
  - [RedshiftConnectorProfileCredentialsTypeDef](#redshiftconnectorprofilecredentialstypedef)
  - [RedshiftConnectorProfilePropertiesTypeDef](#redshiftconnectorprofilepropertiestypedef)
  - [RedshiftDestinationPropertiesTypeDef](#redshiftdestinationpropertiestypedef)
  - [S3DestinationPropertiesTypeDef](#s3destinationpropertiestypedef)
  - [S3OutputFormatConfigTypeDef](#s3outputformatconfigtypedef)
  - [S3SourcePropertiesTypeDef](#s3sourcepropertiestypedef)
  - [SalesforceConnectorProfileCredentialsTypeDef](#salesforceconnectorprofilecredentialstypedef)
  - [SalesforceConnectorProfilePropertiesTypeDef](#salesforceconnectorprofilepropertiestypedef)
  - [SalesforceDestinationPropertiesTypeDef](#salesforcedestinationpropertiestypedef)
  - [SalesforceMetadataTypeDef](#salesforcemetadatatypedef)
  - [SalesforceSourcePropertiesTypeDef](#salesforcesourcepropertiestypedef)
  - [ScheduledTriggerPropertiesTypeDef](#scheduledtriggerpropertiestypedef)
  - [ServiceNowConnectorProfileCredentialsTypeDef](#servicenowconnectorprofilecredentialstypedef)
  - [ServiceNowConnectorProfilePropertiesTypeDef](#servicenowconnectorprofilepropertiestypedef)
  - [ServiceNowSourcePropertiesTypeDef](#servicenowsourcepropertiestypedef)
  - [SingularConnectorProfileCredentialsTypeDef](#singularconnectorprofilecredentialstypedef)
  - [SingularSourcePropertiesTypeDef](#singularsourcepropertiestypedef)
  - [SlackConnectorProfileCredentialsTypeDef](#slackconnectorprofilecredentialstypedef)
  - [SlackConnectorProfilePropertiesTypeDef](#slackconnectorprofilepropertiestypedef)
  - [SlackMetadataTypeDef](#slackmetadatatypedef)
  - [SlackSourcePropertiesTypeDef](#slacksourcepropertiestypedef)
  - [SnowflakeConnectorProfileCredentialsTypeDef](#snowflakeconnectorprofilecredentialstypedef)
  - [SnowflakeConnectorProfilePropertiesTypeDef](#snowflakeconnectorprofilepropertiestypedef)
  - [SnowflakeDestinationPropertiesTypeDef](#snowflakedestinationpropertiestypedef)
  - [SnowflakeMetadataTypeDef](#snowflakemetadatatypedef)
  - [SourceConnectorPropertiesTypeDef](#sourceconnectorpropertiestypedef)
  - [SourceFieldPropertiesTypeDef](#sourcefieldpropertiestypedef)
  - [SourceFlowConfigTypeDef](#sourceflowconfigtypedef)
  - [SupportedFieldTypeDetailsTypeDef](#supportedfieldtypedetailstypedef)
  - [TaskTypeDef](#tasktypedef)
  - [TrendmicroConnectorProfileCredentialsTypeDef](#trendmicroconnectorprofilecredentialstypedef)
  - [TrendmicroSourcePropertiesTypeDef](#trendmicrosourcepropertiestypedef)
  - [TriggerConfigTypeDef](#triggerconfigtypedef)
  - [TriggerPropertiesTypeDef](#triggerpropertiestypedef)
  - [UpsolverDestinationPropertiesTypeDef](#upsolverdestinationpropertiestypedef)
  - [UpsolverS3OutputFormatConfigTypeDef](#upsolvers3outputformatconfigtypedef)
  - [VeevaConnectorProfileCredentialsTypeDef](#veevaconnectorprofilecredentialstypedef)
  - [VeevaConnectorProfilePropertiesTypeDef](#veevaconnectorprofilepropertiestypedef)
  - [VeevaSourcePropertiesTypeDef](#veevasourcepropertiestypedef)
  - [ZendeskConnectorProfileCredentialsTypeDef](#zendeskconnectorprofilecredentialstypedef)
  - [ZendeskConnectorProfilePropertiesTypeDef](#zendeskconnectorprofilepropertiestypedef)
  - [ZendeskDestinationPropertiesTypeDef](#zendeskdestinationpropertiestypedef)
  - [ZendeskMetadataTypeDef](#zendeskmetadatatypedef)
  - [ZendeskSourcePropertiesTypeDef](#zendesksourcepropertiestypedef)
  - [ConnectorProfileConfigTypeDef](#connectorprofileconfigtypedef)
  - [CreateConnectorProfileResponseTypeDef](#createconnectorprofileresponsetypedef)
  - [CreateFlowResponseTypeDef](#createflowresponsetypedef)
  - [DescribeConnectorEntityResponseTypeDef](#describeconnectorentityresponsetypedef)
  - [DescribeConnectorProfilesResponseTypeDef](#describeconnectorprofilesresponsetypedef)
  - [DescribeConnectorsResponseTypeDef](#describeconnectorsresponsetypedef)
  - [DescribeFlowExecutionRecordsResponseTypeDef](#describeflowexecutionrecordsresponsetypedef)
  - [DescribeFlowResponseTypeDef](#describeflowresponsetypedef)
  - [ListConnectorEntitiesResponseTypeDef](#listconnectorentitiesresponsetypedef)
  - [ListFlowsResponseTypeDef](#listflowsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [StartFlowResponseTypeDef](#startflowresponsetypedef)
  - [StopFlowResponseTypeDef](#stopflowresponsetypedef)
  - [UpdateConnectorProfileResponseTypeDef](#updateconnectorprofileresponsetypedef)
  - [UpdateFlowResponseTypeDef](#updateflowresponsetypedef)

## AggregationConfigTypeDef

```python
from mypy_boto3_appflow.type_defs import AggregationConfigTypeDef
```




Optional fields:
- `aggregationType`: `AggregationType`


## AmplitudeConnectorProfileCredentialsTypeDef

```python
from mypy_boto3_appflow.type_defs import AmplitudeConnectorProfileCredentialsTypeDef
```


Required fields:
- `apiKey`: `str`
- `secretKey`: `str`




## AmplitudeSourcePropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import AmplitudeSourcePropertiesTypeDef
```


Required fields:
- `object`: `str`




## ConnectorConfigurationTypeDef

```python
from mypy_boto3_appflow.type_defs import ConnectorConfigurationTypeDef
```




Optional fields:
- `canUseAsSource`: `bool`
- `canUseAsDestination`: `bool`
- `supportedDestinationConnectors`: `List[ConnectorType]`
- `supportedSchedulingFrequencies`: `List[ScheduleFrequencyType]`
- `isPrivateLinkEnabled`: `bool`
- `isPrivateLinkEndpointUrlRequired`: `bool`
- `supportedTriggerTypes`: `List[TriggerType]`
- `connectorMetadata`: `"ConnectorMetadataTypeDef"`


## ConnectorEntityFieldTypeDef

```python
from mypy_boto3_appflow.type_defs import ConnectorEntityFieldTypeDef
```


Required fields:
- `identifier`: `str`



Optional fields:
- `label`: `str`
- `supportedFieldTypeDetails`: `"SupportedFieldTypeDetailsTypeDef"`
- `description`: `str`
- `sourceProperties`: `"SourceFieldPropertiesTypeDef"`
- `destinationProperties`: `"DestinationFieldPropertiesTypeDef"`


## ConnectorEntityTypeDef

```python
from mypy_boto3_appflow.type_defs import ConnectorEntityTypeDef
```


Required fields:
- `name`: `str`



Optional fields:
- `label`: `str`
- `hasNestedEntities`: `bool`


## ConnectorMetadataTypeDef

```python
from mypy_boto3_appflow.type_defs import ConnectorMetadataTypeDef
```




Optional fields:
- `Amplitude`: `Dict[str, Any]`
- `Datadog`: `Dict[str, Any]`
- `Dynatrace`: `Dict[str, Any]`
- `GoogleAnalytics`: `"GoogleAnalyticsMetadataTypeDef"`
- `InforNexus`: `Dict[str, Any]`
- `Marketo`: `Dict[str, Any]`
- `Redshift`: `Dict[str, Any]`
- `S3`: `Dict[str, Any]`
- `Salesforce`: `"SalesforceMetadataTypeDef"`
- `ServiceNow`: `Dict[str, Any]`
- `Singular`: `Dict[str, Any]`
- `Slack`: `"SlackMetadataTypeDef"`
- `Snowflake`: `"SnowflakeMetadataTypeDef"`
- `Trendmicro`: `Dict[str, Any]`
- `Veeva`: `Dict[str, Any]`
- `Zendesk`: `"ZendeskMetadataTypeDef"`
- `EventBridge`: `Dict[str, Any]`
- `Upsolver`: `Dict[str, Any]`
- `CustomerProfiles`: `Dict[str, Any]`
- `Honeycode`: `"HoneycodeMetadataTypeDef"`


## ConnectorOAuthRequestTypeDef

```python
from mypy_boto3_appflow.type_defs import ConnectorOAuthRequestTypeDef
```




Optional fields:
- `authCode`: `str`
- `redirectUri`: `str`


## ConnectorOperatorTypeDef

```python
from mypy_boto3_appflow.type_defs import ConnectorOperatorTypeDef
```




Optional fields:
- `Amplitude`: `AmplitudeConnectorOperator`
- `Datadog`: `DatadogConnectorOperator`
- `Dynatrace`: `DynatraceConnectorOperator`
- `GoogleAnalytics`: `GoogleAnalyticsConnectorOperator`
- `InforNexus`: `InforNexusConnectorOperator`
- `Marketo`: `MarketoConnectorOperator`
- `S3`: `S3ConnectorOperator`
- `Salesforce`: `SalesforceConnectorOperator`
- `ServiceNow`: `ServiceNowConnectorOperator`
- `Singular`: `SingularConnectorOperator`
- `Slack`: `SlackConnectorOperator`
- `Trendmicro`: `TrendmicroConnectorOperator`
- `Veeva`: `VeevaConnectorOperator`
- `Zendesk`: `ZendeskConnectorOperator`


## ConnectorProfileCredentialsTypeDef

```python
from mypy_boto3_appflow.type_defs import ConnectorProfileCredentialsTypeDef
```




Optional fields:
- `Amplitude`: `"AmplitudeConnectorProfileCredentialsTypeDef"`
- `Datadog`: `"DatadogConnectorProfileCredentialsTypeDef"`
- `Dynatrace`: `"DynatraceConnectorProfileCredentialsTypeDef"`
- `GoogleAnalytics`: `"GoogleAnalyticsConnectorProfileCredentialsTypeDef"`
- `Honeycode`: `"HoneycodeConnectorProfileCredentialsTypeDef"`
- `InforNexus`: `"InforNexusConnectorProfileCredentialsTypeDef"`
- `Marketo`: `"MarketoConnectorProfileCredentialsTypeDef"`
- `Redshift`: `"RedshiftConnectorProfileCredentialsTypeDef"`
- `Salesforce`: `"SalesforceConnectorProfileCredentialsTypeDef"`
- `ServiceNow`: `"ServiceNowConnectorProfileCredentialsTypeDef"`
- `Singular`: `"SingularConnectorProfileCredentialsTypeDef"`
- `Slack`: `"SlackConnectorProfileCredentialsTypeDef"`
- `Snowflake`: `"SnowflakeConnectorProfileCredentialsTypeDef"`
- `Trendmicro`: `"TrendmicroConnectorProfileCredentialsTypeDef"`
- `Veeva`: `"VeevaConnectorProfileCredentialsTypeDef"`
- `Zendesk`: `"ZendeskConnectorProfileCredentialsTypeDef"`


## ConnectorProfilePropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import ConnectorProfilePropertiesTypeDef
```




Optional fields:
- `Amplitude`: `Dict[str, Any]`
- `Datadog`: `"DatadogConnectorProfilePropertiesTypeDef"`
- `Dynatrace`: `"DynatraceConnectorProfilePropertiesTypeDef"`
- `GoogleAnalytics`: `Dict[str, Any]`
- `Honeycode`: `Dict[str, Any]`
- `InforNexus`: `"InforNexusConnectorProfilePropertiesTypeDef"`
- `Marketo`: `"MarketoConnectorProfilePropertiesTypeDef"`
- `Redshift`: `"RedshiftConnectorProfilePropertiesTypeDef"`
- `Salesforce`: `"SalesforceConnectorProfilePropertiesTypeDef"`
- `ServiceNow`: `"ServiceNowConnectorProfilePropertiesTypeDef"`
- `Singular`: `Dict[str, Any]`
- `Slack`: `"SlackConnectorProfilePropertiesTypeDef"`
- `Snowflake`: `"SnowflakeConnectorProfilePropertiesTypeDef"`
- `Trendmicro`: `Dict[str, Any]`
- `Veeva`: `"VeevaConnectorProfilePropertiesTypeDef"`
- `Zendesk`: `"ZendeskConnectorProfilePropertiesTypeDef"`


## ConnectorProfileTypeDef

```python
from mypy_boto3_appflow.type_defs import ConnectorProfileTypeDef
```




Optional fields:
- `connectorProfileArn`: `str`
- `connectorProfileName`: `str`
- `connectorType`: `ConnectorType`
- `connectionMode`: `ConnectionMode`
- `credentialsArn`: `str`
- `connectorProfileProperties`: `"ConnectorProfilePropertiesTypeDef"`
- `createdAt`: `datetime`
- `lastUpdatedAt`: `datetime`


## CustomerProfilesDestinationPropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import CustomerProfilesDestinationPropertiesTypeDef
```


Required fields:
- `domainName`: `str`



Optional fields:
- `objectTypeName`: `str`


## DatadogConnectorProfileCredentialsTypeDef

```python
from mypy_boto3_appflow.type_defs import DatadogConnectorProfileCredentialsTypeDef
```


Required fields:
- `apiKey`: `str`
- `applicationKey`: `str`




## DatadogConnectorProfilePropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import DatadogConnectorProfilePropertiesTypeDef
```


Required fields:
- `instanceUrl`: `str`




## DatadogSourcePropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import DatadogSourcePropertiesTypeDef
```


Required fields:
- `object`: `str`




## DestinationConnectorPropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import DestinationConnectorPropertiesTypeDef
```




Optional fields:
- `Redshift`: `"RedshiftDestinationPropertiesTypeDef"`
- `S3`: `"S3DestinationPropertiesTypeDef"`
- `Salesforce`: `"SalesforceDestinationPropertiesTypeDef"`
- `Snowflake`: `"SnowflakeDestinationPropertiesTypeDef"`
- `EventBridge`: `"EventBridgeDestinationPropertiesTypeDef"`
- `LookoutMetrics`: `Dict[str, Any]`
- `Upsolver`: `"UpsolverDestinationPropertiesTypeDef"`
- `Honeycode`: `"HoneycodeDestinationPropertiesTypeDef"`
- `CustomerProfiles`: `"CustomerProfilesDestinationPropertiesTypeDef"`
- `Zendesk`: `"ZendeskDestinationPropertiesTypeDef"`


## DestinationFieldPropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import DestinationFieldPropertiesTypeDef
```




Optional fields:
- `isCreatable`: `bool`
- `isNullable`: `bool`
- `isUpsertable`: `bool`
- `isUpdatable`: `bool`
- `supportedWriteOperations`: `List[WriteOperationType]`


## DestinationFlowConfigTypeDef

```python
from mypy_boto3_appflow.type_defs import DestinationFlowConfigTypeDef
```


Required fields:
- `connectorType`: `ConnectorType`
- `destinationConnectorProperties`: `"DestinationConnectorPropertiesTypeDef"`



Optional fields:
- `connectorProfileName`: `str`


## DynatraceConnectorProfileCredentialsTypeDef

```python
from mypy_boto3_appflow.type_defs import DynatraceConnectorProfileCredentialsTypeDef
```


Required fields:
- `apiToken`: `str`




## DynatraceConnectorProfilePropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import DynatraceConnectorProfilePropertiesTypeDef
```


Required fields:
- `instanceUrl`: `str`




## DynatraceSourcePropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import DynatraceSourcePropertiesTypeDef
```


Required fields:
- `object`: `str`




## ErrorHandlingConfigTypeDef

```python
from mypy_boto3_appflow.type_defs import ErrorHandlingConfigTypeDef
```




Optional fields:
- `failOnFirstDestinationError`: `bool`
- `bucketPrefix`: `str`
- `bucketName`: `str`


## ErrorInfoTypeDef

```python
from mypy_boto3_appflow.type_defs import ErrorInfoTypeDef
```




Optional fields:
- `putFailuresCount`: `int`
- `executionMessage`: `str`


## EventBridgeDestinationPropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import EventBridgeDestinationPropertiesTypeDef
```


Required fields:
- `object`: `str`



Optional fields:
- `errorHandlingConfig`: `"ErrorHandlingConfigTypeDef"`


## ExecutionDetailsTypeDef

```python
from mypy_boto3_appflow.type_defs import ExecutionDetailsTypeDef
```




Optional fields:
- `mostRecentExecutionMessage`: `str`
- `mostRecentExecutionTime`: `datetime`
- `mostRecentExecutionStatus`: `ExecutionStatus`


## ExecutionRecordTypeDef

```python
from mypy_boto3_appflow.type_defs import ExecutionRecordTypeDef
```




Optional fields:
- `executionId`: `str`
- `executionStatus`: `ExecutionStatus`
- `executionResult`: `"ExecutionResultTypeDef"`
- `startedAt`: `datetime`
- `lastUpdatedAt`: `datetime`
- `dataPullStartTime`: `datetime`
- `dataPullEndTime`: `datetime`


## ExecutionResultTypeDef

```python
from mypy_boto3_appflow.type_defs import ExecutionResultTypeDef
```




Optional fields:
- `errorInfo`: `"ErrorInfoTypeDef"`
- `bytesProcessed`: `int`
- `bytesWritten`: `int`
- `recordsProcessed`: `int`


## FieldTypeDetailsTypeDef

```python
from mypy_boto3_appflow.type_defs import FieldTypeDetailsTypeDef
```


Required fields:
- `fieldType`: `str`
- `filterOperators`: `List[Operator]`



Optional fields:
- `supportedValues`: `List[str]`


## FlowDefinitionTypeDef

```python
from mypy_boto3_appflow.type_defs import FlowDefinitionTypeDef
```




Optional fields:
- `flowArn`: `str`
- `description`: `str`
- `flowName`: `str`
- `flowStatus`: `FlowStatus`
- `sourceConnectorType`: `ConnectorType`
- `destinationConnectorType`: `ConnectorType`
- `triggerType`: `TriggerType`
- `createdAt`: `datetime`
- `lastUpdatedAt`: `datetime`
- `createdBy`: `str`
- `lastUpdatedBy`: `str`
- `tags`: `Dict[str, str]`
- `lastRunExecutionDetails`: `"ExecutionDetailsTypeDef"`


## GoogleAnalyticsConnectorProfileCredentialsTypeDef

```python
from mypy_boto3_appflow.type_defs import GoogleAnalyticsConnectorProfileCredentialsTypeDef
```


Required fields:
- `clientId`: `str`
- `clientSecret`: `str`



Optional fields:
- `accessToken`: `str`
- `refreshToken`: `str`
- `oAuthRequest`: `"ConnectorOAuthRequestTypeDef"`


## GoogleAnalyticsMetadataTypeDef

```python
from mypy_boto3_appflow.type_defs import GoogleAnalyticsMetadataTypeDef
```




Optional fields:
- `oAuthScopes`: `List[str]`


## GoogleAnalyticsSourcePropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import GoogleAnalyticsSourcePropertiesTypeDef
```


Required fields:
- `object`: `str`




## HoneycodeConnectorProfileCredentialsTypeDef

```python
from mypy_boto3_appflow.type_defs import HoneycodeConnectorProfileCredentialsTypeDef
```




Optional fields:
- `accessToken`: `str`
- `refreshToken`: `str`
- `oAuthRequest`: `"ConnectorOAuthRequestTypeDef"`


## HoneycodeDestinationPropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import HoneycodeDestinationPropertiesTypeDef
```


Required fields:
- `object`: `str`



Optional fields:
- `errorHandlingConfig`: `"ErrorHandlingConfigTypeDef"`


## HoneycodeMetadataTypeDef

```python
from mypy_boto3_appflow.type_defs import HoneycodeMetadataTypeDef
```




Optional fields:
- `oAuthScopes`: `List[str]`


## IncrementalPullConfigTypeDef

```python
from mypy_boto3_appflow.type_defs import IncrementalPullConfigTypeDef
```




Optional fields:
- `datetimeTypeFieldName`: `str`


## InforNexusConnectorProfileCredentialsTypeDef

```python
from mypy_boto3_appflow.type_defs import InforNexusConnectorProfileCredentialsTypeDef
```


Required fields:
- `accessKeyId`: `str`
- `userId`: `str`
- `secretAccessKey`: `str`
- `datakey`: `str`




## InforNexusConnectorProfilePropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import InforNexusConnectorProfilePropertiesTypeDef
```


Required fields:
- `instanceUrl`: `str`




## InforNexusSourcePropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import InforNexusSourcePropertiesTypeDef
```


Required fields:
- `object`: `str`




## MarketoConnectorProfileCredentialsTypeDef

```python
from mypy_boto3_appflow.type_defs import MarketoConnectorProfileCredentialsTypeDef
```


Required fields:
- `clientId`: `str`
- `clientSecret`: `str`



Optional fields:
- `accessToken`: `str`
- `oAuthRequest`: `"ConnectorOAuthRequestTypeDef"`


## MarketoConnectorProfilePropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import MarketoConnectorProfilePropertiesTypeDef
```


Required fields:
- `instanceUrl`: `str`




## MarketoSourcePropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import MarketoSourcePropertiesTypeDef
```


Required fields:
- `object`: `str`




## PrefixConfigTypeDef

```python
from mypy_boto3_appflow.type_defs import PrefixConfigTypeDef
```




Optional fields:
- `prefixType`: `PrefixType`
- `prefixFormat`: `PrefixFormat`


## RedshiftConnectorProfileCredentialsTypeDef

```python
from mypy_boto3_appflow.type_defs import RedshiftConnectorProfileCredentialsTypeDef
```


Required fields:
- `username`: `str`
- `password`: `str`




## RedshiftConnectorProfilePropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import RedshiftConnectorProfilePropertiesTypeDef
```


Required fields:
- `databaseUrl`: `str`
- `bucketName`: `str`
- `roleArn`: `str`



Optional fields:
- `bucketPrefix`: `str`


## RedshiftDestinationPropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import RedshiftDestinationPropertiesTypeDef
```


Required fields:
- `object`: `str`
- `intermediateBucketName`: `str`



Optional fields:
- `bucketPrefix`: `str`
- `errorHandlingConfig`: `"ErrorHandlingConfigTypeDef"`


## S3DestinationPropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import S3DestinationPropertiesTypeDef
```


Required fields:
- `bucketName`: `str`



Optional fields:
- `bucketPrefix`: `str`
- `s3OutputFormatConfig`: `"S3OutputFormatConfigTypeDef"`


## S3OutputFormatConfigTypeDef

```python
from mypy_boto3_appflow.type_defs import S3OutputFormatConfigTypeDef
```




Optional fields:
- `fileType`: `FileType`
- `prefixConfig`: `"PrefixConfigTypeDef"`
- `aggregationConfig`: `"AggregationConfigTypeDef"`


## S3SourcePropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import S3SourcePropertiesTypeDef
```


Required fields:
- `bucketName`: `str`



Optional fields:
- `bucketPrefix`: `str`


## SalesforceConnectorProfileCredentialsTypeDef

```python
from mypy_boto3_appflow.type_defs import SalesforceConnectorProfileCredentialsTypeDef
```




Optional fields:
- `accessToken`: `str`
- `refreshToken`: `str`
- `oAuthRequest`: `"ConnectorOAuthRequestTypeDef"`
- `clientCredentialsArn`: `str`


## SalesforceConnectorProfilePropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import SalesforceConnectorProfilePropertiesTypeDef
```




Optional fields:
- `instanceUrl`: `str`
- `isSandboxEnvironment`: `bool`


## SalesforceDestinationPropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import SalesforceDestinationPropertiesTypeDef
```


Required fields:
- `object`: `str`



Optional fields:
- `idFieldNames`: `List[str]`
- `errorHandlingConfig`: `"ErrorHandlingConfigTypeDef"`
- `writeOperationType`: `WriteOperationType`


## SalesforceMetadataTypeDef

```python
from mypy_boto3_appflow.type_defs import SalesforceMetadataTypeDef
```




Optional fields:
- `oAuthScopes`: `List[str]`


## SalesforceSourcePropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import SalesforceSourcePropertiesTypeDef
```


Required fields:
- `object`: `str`



Optional fields:
- `enableDynamicFieldUpdate`: `bool`
- `includeDeletedRecords`: `bool`


## ScheduledTriggerPropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import ScheduledTriggerPropertiesTypeDef
```


Required fields:
- `scheduleExpression`: `str`



Optional fields:
- `dataPullMode`: `DataPullMode`
- `scheduleStartTime`: `datetime`
- `scheduleEndTime`: `datetime`
- `timezone`: `str`
- `scheduleOffset`: `int`
- `firstExecutionFrom`: `datetime`


## ServiceNowConnectorProfileCredentialsTypeDef

```python
from mypy_boto3_appflow.type_defs import ServiceNowConnectorProfileCredentialsTypeDef
```


Required fields:
- `username`: `str`
- `password`: `str`




## ServiceNowConnectorProfilePropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import ServiceNowConnectorProfilePropertiesTypeDef
```


Required fields:
- `instanceUrl`: `str`




## ServiceNowSourcePropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import ServiceNowSourcePropertiesTypeDef
```


Required fields:
- `object`: `str`




## SingularConnectorProfileCredentialsTypeDef

```python
from mypy_boto3_appflow.type_defs import SingularConnectorProfileCredentialsTypeDef
```


Required fields:
- `apiKey`: `str`




## SingularSourcePropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import SingularSourcePropertiesTypeDef
```


Required fields:
- `object`: `str`




## SlackConnectorProfileCredentialsTypeDef

```python
from mypy_boto3_appflow.type_defs import SlackConnectorProfileCredentialsTypeDef
```


Required fields:
- `clientId`: `str`
- `clientSecret`: `str`



Optional fields:
- `accessToken`: `str`
- `oAuthRequest`: `"ConnectorOAuthRequestTypeDef"`


## SlackConnectorProfilePropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import SlackConnectorProfilePropertiesTypeDef
```


Required fields:
- `instanceUrl`: `str`




## SlackMetadataTypeDef

```python
from mypy_boto3_appflow.type_defs import SlackMetadataTypeDef
```




Optional fields:
- `oAuthScopes`: `List[str]`


## SlackSourcePropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import SlackSourcePropertiesTypeDef
```


Required fields:
- `object`: `str`




## SnowflakeConnectorProfileCredentialsTypeDef

```python
from mypy_boto3_appflow.type_defs import SnowflakeConnectorProfileCredentialsTypeDef
```


Required fields:
- `username`: `str`
- `password`: `str`




## SnowflakeConnectorProfilePropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import SnowflakeConnectorProfilePropertiesTypeDef
```


Required fields:
- `warehouse`: `str`
- `stage`: `str`
- `bucketName`: `str`



Optional fields:
- `bucketPrefix`: `str`
- `privateLinkServiceName`: `str`
- `accountName`: `str`
- `region`: `str`


## SnowflakeDestinationPropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import SnowflakeDestinationPropertiesTypeDef
```


Required fields:
- `object`: `str`
- `intermediateBucketName`: `str`



Optional fields:
- `bucketPrefix`: `str`
- `errorHandlingConfig`: `"ErrorHandlingConfigTypeDef"`


## SnowflakeMetadataTypeDef

```python
from mypy_boto3_appflow.type_defs import SnowflakeMetadataTypeDef
```




Optional fields:
- `supportedRegions`: `List[str]`


## SourceConnectorPropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import SourceConnectorPropertiesTypeDef
```




Optional fields:
- `Amplitude`: `"AmplitudeSourcePropertiesTypeDef"`
- `Datadog`: `"DatadogSourcePropertiesTypeDef"`
- `Dynatrace`: `"DynatraceSourcePropertiesTypeDef"`
- `GoogleAnalytics`: `"GoogleAnalyticsSourcePropertiesTypeDef"`
- `InforNexus`: `"InforNexusSourcePropertiesTypeDef"`
- `Marketo`: `"MarketoSourcePropertiesTypeDef"`
- `S3`: `"S3SourcePropertiesTypeDef"`
- `Salesforce`: `"SalesforceSourcePropertiesTypeDef"`
- `ServiceNow`: `"ServiceNowSourcePropertiesTypeDef"`
- `Singular`: `"SingularSourcePropertiesTypeDef"`
- `Slack`: `"SlackSourcePropertiesTypeDef"`
- `Trendmicro`: `"TrendmicroSourcePropertiesTypeDef"`
- `Veeva`: `"VeevaSourcePropertiesTypeDef"`
- `Zendesk`: `"ZendeskSourcePropertiesTypeDef"`


## SourceFieldPropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import SourceFieldPropertiesTypeDef
```




Optional fields:
- `isRetrievable`: `bool`
- `isQueryable`: `bool`


## SourceFlowConfigTypeDef

```python
from mypy_boto3_appflow.type_defs import SourceFlowConfigTypeDef
```


Required fields:
- `connectorType`: `ConnectorType`
- `sourceConnectorProperties`: `"SourceConnectorPropertiesTypeDef"`



Optional fields:
- `connectorProfileName`: `str`
- `incrementalPullConfig`: `"IncrementalPullConfigTypeDef"`


## SupportedFieldTypeDetailsTypeDef

```python
from mypy_boto3_appflow.type_defs import SupportedFieldTypeDetailsTypeDef
```


Required fields:
- `v1`: `"FieldTypeDetailsTypeDef"`




## TaskTypeDef

```python
from mypy_boto3_appflow.type_defs import TaskTypeDef
```


Required fields:
- `sourceFields`: `List[str]`
- `taskType`: `TaskType`



Optional fields:
- `connectorOperator`: `"ConnectorOperatorTypeDef"`
- `destinationField`: `str`
- `taskProperties`: `Dict[OperatorPropertiesKeys, str]`


## TrendmicroConnectorProfileCredentialsTypeDef

```python
from mypy_boto3_appflow.type_defs import TrendmicroConnectorProfileCredentialsTypeDef
```


Required fields:
- `apiSecretKey`: `str`




## TrendmicroSourcePropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import TrendmicroSourcePropertiesTypeDef
```


Required fields:
- `object`: `str`




## TriggerConfigTypeDef

```python
from mypy_boto3_appflow.type_defs import TriggerConfigTypeDef
```


Required fields:
- `triggerType`: `TriggerType`



Optional fields:
- `triggerProperties`: `"TriggerPropertiesTypeDef"`


## TriggerPropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import TriggerPropertiesTypeDef
```




Optional fields:
- `Scheduled`: `"ScheduledTriggerPropertiesTypeDef"`


## UpsolverDestinationPropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import UpsolverDestinationPropertiesTypeDef
```


Required fields:
- `bucketName`: `str`
- `s3OutputFormatConfig`: `"UpsolverS3OutputFormatConfigTypeDef"`



Optional fields:
- `bucketPrefix`: `str`


## UpsolverS3OutputFormatConfigTypeDef

```python
from mypy_boto3_appflow.type_defs import UpsolverS3OutputFormatConfigTypeDef
```


Required fields:
- `prefixConfig`: `"PrefixConfigTypeDef"`



Optional fields:
- `fileType`: `FileType`
- `aggregationConfig`: `"AggregationConfigTypeDef"`


## VeevaConnectorProfileCredentialsTypeDef

```python
from mypy_boto3_appflow.type_defs import VeevaConnectorProfileCredentialsTypeDef
```


Required fields:
- `username`: `str`
- `password`: `str`




## VeevaConnectorProfilePropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import VeevaConnectorProfilePropertiesTypeDef
```


Required fields:
- `instanceUrl`: `str`




## VeevaSourcePropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import VeevaSourcePropertiesTypeDef
```


Required fields:
- `object`: `str`




## ZendeskConnectorProfileCredentialsTypeDef

```python
from mypy_boto3_appflow.type_defs import ZendeskConnectorProfileCredentialsTypeDef
```


Required fields:
- `clientId`: `str`
- `clientSecret`: `str`



Optional fields:
- `accessToken`: `str`
- `oAuthRequest`: `"ConnectorOAuthRequestTypeDef"`


## ZendeskConnectorProfilePropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import ZendeskConnectorProfilePropertiesTypeDef
```


Required fields:
- `instanceUrl`: `str`




## ZendeskDestinationPropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import ZendeskDestinationPropertiesTypeDef
```


Required fields:
- `object`: `str`



Optional fields:
- `idFieldNames`: `List[str]`
- `errorHandlingConfig`: `"ErrorHandlingConfigTypeDef"`
- `writeOperationType`: `WriteOperationType`


## ZendeskMetadataTypeDef

```python
from mypy_boto3_appflow.type_defs import ZendeskMetadataTypeDef
```




Optional fields:
- `oAuthScopes`: `List[str]`


## ZendeskSourcePropertiesTypeDef

```python
from mypy_boto3_appflow.type_defs import ZendeskSourcePropertiesTypeDef
```


Required fields:
- `object`: `str`




## ConnectorProfileConfigTypeDef

```python
from mypy_boto3_appflow.type_defs import ConnectorProfileConfigTypeDef
```


Required fields:
- `connectorProfileProperties`: `"ConnectorProfilePropertiesTypeDef"`
- `connectorProfileCredentials`: `"ConnectorProfileCredentialsTypeDef"`




## CreateConnectorProfileResponseTypeDef

```python
from mypy_boto3_appflow.type_defs import CreateConnectorProfileResponseTypeDef
```




Optional fields:
- `connectorProfileArn`: `str`


## CreateFlowResponseTypeDef

```python
from mypy_boto3_appflow.type_defs import CreateFlowResponseTypeDef
```




Optional fields:
- `flowArn`: `str`
- `flowStatus`: `FlowStatus`


## DescribeConnectorEntityResponseTypeDef

```python
from mypy_boto3_appflow.type_defs import DescribeConnectorEntityResponseTypeDef
```


Required fields:
- `connectorEntityFields`: `List["ConnectorEntityFieldTypeDef"]`




## DescribeConnectorProfilesResponseTypeDef

```python
from mypy_boto3_appflow.type_defs import DescribeConnectorProfilesResponseTypeDef
```




Optional fields:
- `connectorProfileDetails`: `List["ConnectorProfileTypeDef"]`
- `nextToken`: `str`


## DescribeConnectorsResponseTypeDef

```python
from mypy_boto3_appflow.type_defs import DescribeConnectorsResponseTypeDef
```




Optional fields:
- `connectorConfigurations`: `Dict[ConnectorType, "ConnectorConfigurationTypeDef"]`
- `nextToken`: `str`


## DescribeFlowExecutionRecordsResponseTypeDef

```python
from mypy_boto3_appflow.type_defs import DescribeFlowExecutionRecordsResponseTypeDef
```




Optional fields:
- `flowExecutions`: `List["ExecutionRecordTypeDef"]`
- `nextToken`: `str`


## DescribeFlowResponseTypeDef

```python
from mypy_boto3_appflow.type_defs import DescribeFlowResponseTypeDef
```




Optional fields:
- `flowArn`: `str`
- `description`: `str`
- `flowName`: `str`
- `kmsArn`: `str`
- `flowStatus`: `FlowStatus`
- `flowStatusMessage`: `str`
- `sourceFlowConfig`: `"SourceFlowConfigTypeDef"`
- `destinationFlowConfigList`: `List["DestinationFlowConfigTypeDef"]`
- `lastRunExecutionDetails`: `"ExecutionDetailsTypeDef"`
- `triggerConfig`: `"TriggerConfigTypeDef"`
- `tasks`: `List["TaskTypeDef"]`
- `createdAt`: `datetime`
- `lastUpdatedAt`: `datetime`
- `createdBy`: `str`
- `lastUpdatedBy`: `str`
- `tags`: `Dict[str, str]`


## ListConnectorEntitiesResponseTypeDef

```python
from mypy_boto3_appflow.type_defs import ListConnectorEntitiesResponseTypeDef
```


Required fields:
- `connectorEntityMap`: `Dict[str, List["ConnectorEntityTypeDef"]]`




## ListFlowsResponseTypeDef

```python
from mypy_boto3_appflow.type_defs import ListFlowsResponseTypeDef
```




Optional fields:
- `flows`: `List["FlowDefinitionTypeDef"]`
- `nextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_appflow.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `tags`: `Dict[str, str]`


## StartFlowResponseTypeDef

```python
from mypy_boto3_appflow.type_defs import StartFlowResponseTypeDef
```




Optional fields:
- `flowArn`: `str`
- `flowStatus`: `FlowStatus`
- `executionId`: `str`


## StopFlowResponseTypeDef

```python
from mypy_boto3_appflow.type_defs import StopFlowResponseTypeDef
```




Optional fields:
- `flowArn`: `str`
- `flowStatus`: `FlowStatus`


## UpdateConnectorProfileResponseTypeDef

```python
from mypy_boto3_appflow.type_defs import UpdateConnectorProfileResponseTypeDef
```




Optional fields:
- `connectorProfileArn`: `str`


## UpdateFlowResponseTypeDef

```python
from mypy_boto3_appflow.type_defs import UpdateFlowResponseTypeDef
```




Optional fields:
- `flowStatus`: `FlowStatus`

