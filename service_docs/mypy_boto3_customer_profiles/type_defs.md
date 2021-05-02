# Structures for boto3 CustomerProfiles module

> [Index](../index.md) > [CustomerProfiles](./index.md) > Structures

Auto-generated documentation for [CustomerProfiles](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles)
type annotations stubs module [mypy_boto3_customer_profiles](https://pypi.org/project/mypy-boto3-customer-profiles/).

- [Structures for boto3 CustomerProfiles module](#structures-for-boto3-customerprofiles-module)
  - [AddressTypeDef](#addresstypedef)
  - [ConnectorOperatorTypeDef](#connectoroperatortypedef)
  - [DomainStatsTypeDef](#domainstatstypedef)
  - [IncrementalPullConfigTypeDef](#incrementalpullconfigtypedef)
  - [ListDomainItemTypeDef](#listdomainitemtypedef)
  - [ListIntegrationItemTypeDef](#listintegrationitemtypedef)
  - [ListProfileObjectTypeItemTypeDef](#listprofileobjecttypeitemtypedef)
  - [ListProfileObjectTypeTemplateItemTypeDef](#listprofileobjecttypetemplateitemtypedef)
  - [ListProfileObjectsItemTypeDef](#listprofileobjectsitemtypedef)
  - [MarketoSourcePropertiesTypeDef](#marketosourcepropertiestypedef)
  - [MatchItemTypeDef](#matchitemtypedef)
  - [MatchingResponseTypeDef](#matchingresponsetypedef)
  - [ObjectTypeFieldTypeDef](#objecttypefieldtypedef)
  - [ObjectTypeKeyTypeDef](#objecttypekeytypedef)
  - [ProfileTypeDef](#profiletypedef)
  - [S3SourcePropertiesTypeDef](#s3sourcepropertiestypedef)
  - [SalesforceSourcePropertiesTypeDef](#salesforcesourcepropertiestypedef)
  - [ScheduledTriggerPropertiesTypeDef](#scheduledtriggerpropertiestypedef)
  - [ServiceNowSourcePropertiesTypeDef](#servicenowsourcepropertiestypedef)
  - [SourceConnectorPropertiesTypeDef](#sourceconnectorpropertiestypedef)
  - [SourceFlowConfigTypeDef](#sourceflowconfigtypedef)
  - [TaskTypeDef](#tasktypedef)
  - [TriggerConfigTypeDef](#triggerconfigtypedef)
  - [TriggerPropertiesTypeDef](#triggerpropertiestypedef)
  - [ZendeskSourcePropertiesTypeDef](#zendesksourcepropertiestypedef)
  - [AddProfileKeyResponseTypeDef](#addprofilekeyresponsetypedef)
  - [CreateDomainResponseTypeDef](#createdomainresponsetypedef)
  - [CreateProfileResponseTypeDef](#createprofileresponsetypedef)
  - [DeleteDomainResponseTypeDef](#deletedomainresponsetypedef)
  - [DeleteIntegrationResponseTypeDef](#deleteintegrationresponsetypedef)
  - [DeleteProfileKeyResponseTypeDef](#deleteprofilekeyresponsetypedef)
  - [DeleteProfileObjectResponseTypeDef](#deleteprofileobjectresponsetypedef)
  - [DeleteProfileObjectTypeResponseTypeDef](#deleteprofileobjecttyperesponsetypedef)
  - [DeleteProfileResponseTypeDef](#deleteprofileresponsetypedef)
  - [FieldSourceProfileIdsTypeDef](#fieldsourceprofileidstypedef)
  - [FlowDefinitionTypeDef](#flowdefinitiontypedef)
  - [GetDomainResponseTypeDef](#getdomainresponsetypedef)
  - [GetIntegrationResponseTypeDef](#getintegrationresponsetypedef)
  - [GetMatchesResponseTypeDef](#getmatchesresponsetypedef)
  - [GetProfileObjectTypeResponseTypeDef](#getprofileobjecttyperesponsetypedef)
  - [GetProfileObjectTypeTemplateResponseTypeDef](#getprofileobjecttypetemplateresponsetypedef)
  - [ListAccountIntegrationsResponseTypeDef](#listaccountintegrationsresponsetypedef)
  - [ListDomainsResponseTypeDef](#listdomainsresponsetypedef)
  - [ListIntegrationsResponseTypeDef](#listintegrationsresponsetypedef)
  - [ListProfileObjectTypeTemplatesResponseTypeDef](#listprofileobjecttypetemplatesresponsetypedef)
  - [ListProfileObjectTypesResponseTypeDef](#listprofileobjecttypesresponsetypedef)
  - [ListProfileObjectsResponseTypeDef](#listprofileobjectsresponsetypedef)
  - [ListTagsForResourceResponseTypeDef](#listtagsforresourceresponsetypedef)
  - [MatchingRequestTypeDef](#matchingrequesttypedef)
  - [MergeProfilesResponseTypeDef](#mergeprofilesresponsetypedef)
  - [PutIntegrationResponseTypeDef](#putintegrationresponsetypedef)
  - [PutProfileObjectResponseTypeDef](#putprofileobjectresponsetypedef)
  - [PutProfileObjectTypeResponseTypeDef](#putprofileobjecttyperesponsetypedef)
  - [SearchProfilesResponseTypeDef](#searchprofilesresponsetypedef)
  - [UpdateAddressTypeDef](#updateaddresstypedef)
  - [UpdateDomainResponseTypeDef](#updatedomainresponsetypedef)
  - [UpdateProfileResponseTypeDef](#updateprofileresponsetypedef)

## AddressTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import AddressTypeDef
```




Optional fields:
- `Address1`: `str`
- `Address2`: `str`
- `Address3`: `str`
- `Address4`: `str`
- `City`: `str`
- `County`: `str`
- `State`: `str`
- `Province`: `str`
- `Country`: `str`
- `PostalCode`: `str`


## ConnectorOperatorTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import ConnectorOperatorTypeDef
```




Optional fields:
- `Marketo`: `MarketoConnectorOperator`
- `S3`: `S3ConnectorOperator`
- `Salesforce`: `SalesforceConnectorOperator`
- `ServiceNow`: `ServiceNowConnectorOperator`
- `Zendesk`: `ZendeskConnectorOperator`


## DomainStatsTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import DomainStatsTypeDef
```




Optional fields:
- `ProfileCount`: `int`
- `MeteringProfileCount`: `int`
- `ObjectCount`: `int`
- `TotalSize`: `int`


## IncrementalPullConfigTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import IncrementalPullConfigTypeDef
```




Optional fields:
- `DatetimeTypeFieldName`: `str`


## ListDomainItemTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import ListDomainItemTypeDef
```


Required fields:
- `DomainName`: `str`
- `CreatedAt`: `datetime`
- `LastUpdatedAt`: `datetime`



Optional fields:
- `Tags`: `Dict[str, str]`


## ListIntegrationItemTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import ListIntegrationItemTypeDef
```


Required fields:
- `DomainName`: `str`
- `Uri`: `str`
- `ObjectTypeName`: `str`
- `CreatedAt`: `datetime`
- `LastUpdatedAt`: `datetime`



Optional fields:
- `Tags`: `Dict[str, str]`


## ListProfileObjectTypeItemTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import ListProfileObjectTypeItemTypeDef
```


Required fields:
- `ObjectTypeName`: `str`
- `Description`: `str`



Optional fields:
- `CreatedAt`: `datetime`
- `LastUpdatedAt`: `datetime`
- `Tags`: `Dict[str, str]`


## ListProfileObjectTypeTemplateItemTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import ListProfileObjectTypeTemplateItemTypeDef
```




Optional fields:
- `TemplateId`: `str`
- `SourceName`: `str`
- `SourceObject`: `str`


## ListProfileObjectsItemTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import ListProfileObjectsItemTypeDef
```




Optional fields:
- `ObjectTypeName`: `str`
- `ProfileObjectUniqueKey`: `str`
- `Object`: `str`


## MarketoSourcePropertiesTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import MarketoSourcePropertiesTypeDef
```


Required fields:
- `Object`: `str`




## MatchItemTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import MatchItemTypeDef
```




Optional fields:
- `MatchId`: `str`
- `ProfileIds`: `List[str]`


## MatchingResponseTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import MatchingResponseTypeDef
```




Optional fields:
- `Enabled`: `bool`


## ObjectTypeFieldTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import ObjectTypeFieldTypeDef
```




Optional fields:
- `Source`: `str`
- `Target`: `str`
- `ContentType`: `FieldContentType`


## ObjectTypeKeyTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import ObjectTypeKeyTypeDef
```




Optional fields:
- `StandardIdentifiers`: `List[StandardIdentifier]`
- `FieldNames`: `List[str]`


## ProfileTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import ProfileTypeDef
```




Optional fields:
- `ProfileId`: `str`
- `AccountNumber`: `str`
- `AdditionalInformation`: `str`
- `PartyType`: `PartyType`
- `BusinessName`: `str`
- `FirstName`: `str`
- `MiddleName`: `str`
- `LastName`: `str`
- `BirthDate`: `str`
- `Gender`: `Gender`
- `PhoneNumber`: `str`
- `MobilePhoneNumber`: `str`
- `HomePhoneNumber`: `str`
- `BusinessPhoneNumber`: `str`
- `EmailAddress`: `str`
- `PersonalEmailAddress`: `str`
- `BusinessEmailAddress`: `str`
- `Address`: `"AddressTypeDef"`
- `ShippingAddress`: `"AddressTypeDef"`
- `MailingAddress`: `"AddressTypeDef"`
- `BillingAddress`: `"AddressTypeDef"`
- `Attributes`: `Dict[str, str]`


## S3SourcePropertiesTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import S3SourcePropertiesTypeDef
```


Required fields:
- `BucketName`: `str`



Optional fields:
- `BucketPrefix`: `str`


## SalesforceSourcePropertiesTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import SalesforceSourcePropertiesTypeDef
```


Required fields:
- `Object`: `str`



Optional fields:
- `EnableDynamicFieldUpdate`: `bool`
- `IncludeDeletedRecords`: `bool`


## ScheduledTriggerPropertiesTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import ScheduledTriggerPropertiesTypeDef
```


Required fields:
- `ScheduleExpression`: `str`



Optional fields:
- `DataPullMode`: `DataPullMode`
- `ScheduleStartTime`: `datetime`
- `ScheduleEndTime`: `datetime`
- `Timezone`: `str`
- `ScheduleOffset`: `int`
- `FirstExecutionFrom`: `datetime`


## ServiceNowSourcePropertiesTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import ServiceNowSourcePropertiesTypeDef
```


Required fields:
- `Object`: `str`




## SourceConnectorPropertiesTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import SourceConnectorPropertiesTypeDef
```




Optional fields:
- `Marketo`: `"MarketoSourcePropertiesTypeDef"`
- `S3`: `"S3SourcePropertiesTypeDef"`
- `Salesforce`: `"SalesforceSourcePropertiesTypeDef"`
- `ServiceNow`: `"ServiceNowSourcePropertiesTypeDef"`
- `Zendesk`: `"ZendeskSourcePropertiesTypeDef"`


## SourceFlowConfigTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import SourceFlowConfigTypeDef
```


Required fields:
- `ConnectorType`: `SourceConnectorType`
- `SourceConnectorProperties`: `"SourceConnectorPropertiesTypeDef"`



Optional fields:
- `ConnectorProfileName`: `str`
- `IncrementalPullConfig`: `"IncrementalPullConfigTypeDef"`


## TaskTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import TaskTypeDef
```


Required fields:
- `SourceFields`: `List[str]`
- `TaskType`: `TaskType`



Optional fields:
- `ConnectorOperator`: `"ConnectorOperatorTypeDef"`
- `DestinationField`: `str`
- `TaskProperties`: `Dict[OperatorPropertiesKeys, str]`


## TriggerConfigTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import TriggerConfigTypeDef
```


Required fields:
- `TriggerType`: `TriggerType`



Optional fields:
- `TriggerProperties`: `"TriggerPropertiesTypeDef"`


## TriggerPropertiesTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import TriggerPropertiesTypeDef
```




Optional fields:
- `Scheduled`: `"ScheduledTriggerPropertiesTypeDef"`


## ZendeskSourcePropertiesTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import ZendeskSourcePropertiesTypeDef
```


Required fields:
- `Object`: `str`




## AddProfileKeyResponseTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import AddProfileKeyResponseTypeDef
```




Optional fields:
- `KeyName`: `str`
- `Values`: `List[str]`


## CreateDomainResponseTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import CreateDomainResponseTypeDef
```


Required fields:
- `DomainName`: `str`
- `DefaultExpirationDays`: `int`
- `CreatedAt`: `datetime`
- `LastUpdatedAt`: `datetime`



Optional fields:
- `DefaultEncryptionKey`: `str`
- `DeadLetterQueueUrl`: `str`
- `Matching`: `"MatchingResponseTypeDef"`
- `Tags`: `Dict[str, str]`


## CreateProfileResponseTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import CreateProfileResponseTypeDef
```


Required fields:
- `ProfileId`: `str`




## DeleteDomainResponseTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import DeleteDomainResponseTypeDef
```


Required fields:
- `Message`: `str`




## DeleteIntegrationResponseTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import DeleteIntegrationResponseTypeDef
```


Required fields:
- `Message`: `str`




## DeleteProfileKeyResponseTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import DeleteProfileKeyResponseTypeDef
```




Optional fields:
- `Message`: `str`


## DeleteProfileObjectResponseTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import DeleteProfileObjectResponseTypeDef
```




Optional fields:
- `Message`: `str`


## DeleteProfileObjectTypeResponseTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import DeleteProfileObjectTypeResponseTypeDef
```


Required fields:
- `Message`: `str`




## DeleteProfileResponseTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import DeleteProfileResponseTypeDef
```




Optional fields:
- `Message`: `str`


## FieldSourceProfileIdsTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import FieldSourceProfileIdsTypeDef
```




Optional fields:
- `AccountNumber`: `str`
- `AdditionalInformation`: `str`
- `PartyType`: `str`
- `BusinessName`: `str`
- `FirstName`: `str`
- `MiddleName`: `str`
- `LastName`: `str`
- `BirthDate`: `str`
- `Gender`: `str`
- `PhoneNumber`: `str`
- `MobilePhoneNumber`: `str`
- `HomePhoneNumber`: `str`
- `BusinessPhoneNumber`: `str`
- `EmailAddress`: `str`
- `PersonalEmailAddress`: `str`
- `BusinessEmailAddress`: `str`
- `Address`: `str`
- `ShippingAddress`: `str`
- `MailingAddress`: `str`
- `BillingAddress`: `str`
- `Attributes`: `Dict[str, str]`


## FlowDefinitionTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import FlowDefinitionTypeDef
```


Required fields:
- `FlowName`: `str`
- `KmsArn`: `str`
- `SourceFlowConfig`: `"SourceFlowConfigTypeDef"`
- `Tasks`: `List["TaskTypeDef"]`
- `TriggerConfig`: `"TriggerConfigTypeDef"`



Optional fields:
- `Description`: `str`


## GetDomainResponseTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import GetDomainResponseTypeDef
```


Required fields:
- `DomainName`: `str`
- `CreatedAt`: `datetime`
- `LastUpdatedAt`: `datetime`



Optional fields:
- `DefaultExpirationDays`: `int`
- `DefaultEncryptionKey`: `str`
- `DeadLetterQueueUrl`: `str`
- `Stats`: `"DomainStatsTypeDef"`
- `Matching`: `"MatchingResponseTypeDef"`
- `Tags`: `Dict[str, str]`


## GetIntegrationResponseTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import GetIntegrationResponseTypeDef
```


Required fields:
- `DomainName`: `str`
- `Uri`: `str`
- `ObjectTypeName`: `str`
- `CreatedAt`: `datetime`
- `LastUpdatedAt`: `datetime`



Optional fields:
- `Tags`: `Dict[str, str]`


## GetMatchesResponseTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import GetMatchesResponseTypeDef
```




Optional fields:
- `NextToken`: `str`
- `MatchGenerationDate`: `datetime`
- `PotentialMatches`: `int`
- `Matches`: `List["MatchItemTypeDef"]`


## GetProfileObjectTypeResponseTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import GetProfileObjectTypeResponseTypeDef
```


Required fields:
- `ObjectTypeName`: `str`
- `Description`: `str`



Optional fields:
- `TemplateId`: `str`
- `ExpirationDays`: `int`
- `EncryptionKey`: `str`
- `AllowProfileCreation`: `bool`
- `Fields`: `Dict[str, "ObjectTypeFieldTypeDef"]`
- `Keys`: `Dict[str, List["ObjectTypeKeyTypeDef"]]`
- `CreatedAt`: `datetime`
- `LastUpdatedAt`: `datetime`
- `Tags`: `Dict[str, str]`


## GetProfileObjectTypeTemplateResponseTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import GetProfileObjectTypeTemplateResponseTypeDef
```




Optional fields:
- `TemplateId`: `str`
- `SourceName`: `str`
- `SourceObject`: `str`
- `AllowProfileCreation`: `bool`
- `Fields`: `Dict[str, "ObjectTypeFieldTypeDef"]`
- `Keys`: `Dict[str, List["ObjectTypeKeyTypeDef"]]`


## ListAccountIntegrationsResponseTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import ListAccountIntegrationsResponseTypeDef
```




Optional fields:
- `Items`: `List["ListIntegrationItemTypeDef"]`
- `NextToken`: `str`


## ListDomainsResponseTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import ListDomainsResponseTypeDef
```




Optional fields:
- `Items`: `List["ListDomainItemTypeDef"]`
- `NextToken`: `str`


## ListIntegrationsResponseTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import ListIntegrationsResponseTypeDef
```




Optional fields:
- `Items`: `List["ListIntegrationItemTypeDef"]`
- `NextToken`: `str`


## ListProfileObjectTypeTemplatesResponseTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import ListProfileObjectTypeTemplatesResponseTypeDef
```




Optional fields:
- `Items`: `List["ListProfileObjectTypeTemplateItemTypeDef"]`
- `NextToken`: `str`


## ListProfileObjectTypesResponseTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import ListProfileObjectTypesResponseTypeDef
```




Optional fields:
- `Items`: `List["ListProfileObjectTypeItemTypeDef"]`
- `NextToken`: `str`


## ListProfileObjectsResponseTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import ListProfileObjectsResponseTypeDef
```




Optional fields:
- `Items`: `List["ListProfileObjectsItemTypeDef"]`
- `NextToken`: `str`


## ListTagsForResourceResponseTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import ListTagsForResourceResponseTypeDef
```




Optional fields:
- `tags`: `Dict[str, str]`


## MatchingRequestTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import MatchingRequestTypeDef
```


Required fields:
- `Enabled`: `bool`




## MergeProfilesResponseTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import MergeProfilesResponseTypeDef
```




Optional fields:
- `Message`: `str`


## PutIntegrationResponseTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import PutIntegrationResponseTypeDef
```


Required fields:
- `DomainName`: `str`
- `Uri`: `str`
- `ObjectTypeName`: `str`
- `CreatedAt`: `datetime`
- `LastUpdatedAt`: `datetime`



Optional fields:
- `Tags`: `Dict[str, str]`


## PutProfileObjectResponseTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import PutProfileObjectResponseTypeDef
```




Optional fields:
- `ProfileObjectUniqueKey`: `str`


## PutProfileObjectTypeResponseTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import PutProfileObjectTypeResponseTypeDef
```


Required fields:
- `ObjectTypeName`: `str`
- `Description`: `str`



Optional fields:
- `TemplateId`: `str`
- `ExpirationDays`: `int`
- `EncryptionKey`: `str`
- `AllowProfileCreation`: `bool`
- `Fields`: `Dict[str, "ObjectTypeFieldTypeDef"]`
- `Keys`: `Dict[str, List["ObjectTypeKeyTypeDef"]]`
- `CreatedAt`: `datetime`
- `LastUpdatedAt`: `datetime`
- `Tags`: `Dict[str, str]`


## SearchProfilesResponseTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import SearchProfilesResponseTypeDef
```




Optional fields:
- `Items`: `List["ProfileTypeDef"]`
- `NextToken`: `str`


## UpdateAddressTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import UpdateAddressTypeDef
```




Optional fields:
- `Address1`: `str`
- `Address2`: `str`
- `Address3`: `str`
- `Address4`: `str`
- `City`: `str`
- `County`: `str`
- `State`: `str`
- `Province`: `str`
- `Country`: `str`
- `PostalCode`: `str`


## UpdateDomainResponseTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import UpdateDomainResponseTypeDef
```


Required fields:
- `DomainName`: `str`
- `CreatedAt`: `datetime`
- `LastUpdatedAt`: `datetime`



Optional fields:
- `DefaultExpirationDays`: `int`
- `DefaultEncryptionKey`: `str`
- `DeadLetterQueueUrl`: `str`
- `Matching`: `"MatchingResponseTypeDef"`
- `Tags`: `Dict[str, str]`


## UpdateProfileResponseTypeDef

```python
from mypy_boto3_customer_profiles.type_defs import UpdateProfileResponseTypeDef
```


Required fields:
- `ProfileId`: `str`



