# Type annotations for boto3 CustomerProfiles module

> [Index](../index.md) > CustomerProfiles

Auto-generated documentation for [CustomerProfiles](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles)
type annotations stubs module [mypy_boto3_customer_profiles](https://pypi.org/project/mypy-boto3-customer-profiles/).

```bash
pip install mypy-boto3-customer-profiles
```

- [Type annotations for boto3 CustomerProfiles module](#type-annotations-for-boto3-customerprofiles-module)
  - [CustomerProfilesClient](#customerprofilesclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Literals](#literals)
  - [Structures](#structures)

## CustomerProfilesClient

Type annotations for  `boto3.client("customer-profiles")` as [CustomerProfilesClient](./client.md)

Can be used directly:

```python
from mypy_boto3_customer_profiles.client import CustomerProfilesClient
```


CustomerProfilesClient [exceptions](./client.md#exceptions)



### Methods
- [add_profile_key](./client.md#add-profile-key)
- [can_paginate](./client.md#can-paginate)
- [create_domain](./client.md#create-domain)
- [create_profile](./client.md#create-profile)
- [delete_domain](./client.md#delete-domain)
- [delete_integration](./client.md#delete-integration)
- [delete_profile](./client.md#delete-profile)
- [delete_profile_key](./client.md#delete-profile-key)
- [delete_profile_object](./client.md#delete-profile-object)
- [delete_profile_object_type](./client.md#delete-profile-object-type)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_domain](./client.md#get-domain)
- [get_integration](./client.md#get-integration)
- [get_matches](./client.md#get-matches)
- [get_profile_object_type](./client.md#get-profile-object-type)
- [get_profile_object_type_template](./client.md#get-profile-object-type-template)
- [list_account_integrations](./client.md#list-account-integrations)
- [list_domains](./client.md#list-domains)
- [list_integrations](./client.md#list-integrations)
- [list_profile_object_type_templates](./client.md#list-profile-object-type-templates)
- [list_profile_object_types](./client.md#list-profile-object-types)
- [list_profile_objects](./client.md#list-profile-objects)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [merge_profiles](./client.md#merge-profiles)
- [put_integration](./client.md#put-integration)
- [put_profile_object](./client.md#put-profile-object)
- [put_profile_object_type](./client.md#put-profile-object-type)
- [search_profiles](./client.md#search-profiles)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_domain](./client.md#update-domain)
- [update_profile](./client.md#update-profile)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [BadRequestException](./client.md#badrequestexception)
- [ClientError](./client.md#clienterror)
- [InternalServerException](./client.md#internalserverexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ThrottlingException](./client.md#throttlingexception)










## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_customer_profiles.literals import DataPullMode, ...
```

- [DataPullMode](./literals.md#datapullmode)
- [FieldContentType](./literals.md#fieldcontenttype)
- [Gender](./literals.md#gender)
- [MarketoConnectorOperator](./literals.md#marketoconnectoroperator)
- [OperatorPropertiesKeys](./literals.md#operatorpropertieskeys)
- [PartyType](./literals.md#partytype)
- [S3ConnectorOperator](./literals.md#s3connectoroperator)
- [SalesforceConnectorOperator](./literals.md#salesforceconnectoroperator)
- [ServiceNowConnectorOperator](./literals.md#servicenowconnectoroperator)
- [SourceConnectorType](./literals.md#sourceconnectortype)
- [StandardIdentifier](./literals.md#standardidentifier)
- [TaskType](./literals.md#tasktype)
- [TriggerType](./literals.md#triggertype)
- [ZendeskConnectorOperator](./literals.md#zendeskconnectoroperator)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_customer_profiles.type_defs import AddressTypeDef, ...
```

- [AddressTypeDef](./type_defs.md#addresstypedef)
- [ConnectorOperatorTypeDef](./type_defs.md#connectoroperatortypedef)
- [DomainStatsTypeDef](./type_defs.md#domainstatstypedef)
- [IncrementalPullConfigTypeDef](./type_defs.md#incrementalpullconfigtypedef)
- [ListDomainItemTypeDef](./type_defs.md#listdomainitemtypedef)
- [ListIntegrationItemTypeDef](./type_defs.md#listintegrationitemtypedef)
- [ListProfileObjectTypeItemTypeDef](./type_defs.md#listprofileobjecttypeitemtypedef)
- [ListProfileObjectTypeTemplateItemTypeDef](./type_defs.md#listprofileobjecttypetemplateitemtypedef)
- [ListProfileObjectsItemTypeDef](./type_defs.md#listprofileobjectsitemtypedef)
- [MarketoSourcePropertiesTypeDef](./type_defs.md#marketosourcepropertiestypedef)
- [MatchItemTypeDef](./type_defs.md#matchitemtypedef)
- [MatchingResponseTypeDef](./type_defs.md#matchingresponsetypedef)
- [ObjectTypeFieldTypeDef](./type_defs.md#objecttypefieldtypedef)
- [ObjectTypeKeyTypeDef](./type_defs.md#objecttypekeytypedef)
- [ProfileTypeDef](./type_defs.md#profiletypedef)
- [S3SourcePropertiesTypeDef](./type_defs.md#s3sourcepropertiestypedef)
- [SalesforceSourcePropertiesTypeDef](./type_defs.md#salesforcesourcepropertiestypedef)
- [ScheduledTriggerPropertiesTypeDef](./type_defs.md#scheduledtriggerpropertiestypedef)
- [ServiceNowSourcePropertiesTypeDef](./type_defs.md#servicenowsourcepropertiestypedef)
- [SourceConnectorPropertiesTypeDef](./type_defs.md#sourceconnectorpropertiestypedef)
- [SourceFlowConfigTypeDef](./type_defs.md#sourceflowconfigtypedef)
- [TaskTypeDef](./type_defs.md#tasktypedef)
- [TriggerConfigTypeDef](./type_defs.md#triggerconfigtypedef)
- [TriggerPropertiesTypeDef](./type_defs.md#triggerpropertiestypedef)
- [ZendeskSourcePropertiesTypeDef](./type_defs.md#zendesksourcepropertiestypedef)
- [AddProfileKeyResponseTypeDef](./type_defs.md#addprofilekeyresponsetypedef)
- [CreateDomainResponseTypeDef](./type_defs.md#createdomainresponsetypedef)
- [CreateProfileResponseTypeDef](./type_defs.md#createprofileresponsetypedef)
- [DeleteDomainResponseTypeDef](./type_defs.md#deletedomainresponsetypedef)
- [DeleteIntegrationResponseTypeDef](./type_defs.md#deleteintegrationresponsetypedef)
- [DeleteProfileKeyResponseTypeDef](./type_defs.md#deleteprofilekeyresponsetypedef)
- [DeleteProfileObjectResponseTypeDef](./type_defs.md#deleteprofileobjectresponsetypedef)
- [DeleteProfileObjectTypeResponseTypeDef](./type_defs.md#deleteprofileobjecttyperesponsetypedef)
- [DeleteProfileResponseTypeDef](./type_defs.md#deleteprofileresponsetypedef)
- [FieldSourceProfileIdsTypeDef](./type_defs.md#fieldsourceprofileidstypedef)
- [FlowDefinitionTypeDef](./type_defs.md#flowdefinitiontypedef)
- [GetDomainResponseTypeDef](./type_defs.md#getdomainresponsetypedef)
- [GetIntegrationResponseTypeDef](./type_defs.md#getintegrationresponsetypedef)
- [GetMatchesResponseTypeDef](./type_defs.md#getmatchesresponsetypedef)
- [GetProfileObjectTypeResponseTypeDef](./type_defs.md#getprofileobjecttyperesponsetypedef)
- [GetProfileObjectTypeTemplateResponseTypeDef](./type_defs.md#getprofileobjecttypetemplateresponsetypedef)
- [ListAccountIntegrationsResponseTypeDef](./type_defs.md#listaccountintegrationsresponsetypedef)
- [ListDomainsResponseTypeDef](./type_defs.md#listdomainsresponsetypedef)
- [ListIntegrationsResponseTypeDef](./type_defs.md#listintegrationsresponsetypedef)
- [ListProfileObjectTypeTemplatesResponseTypeDef](./type_defs.md#listprofileobjecttypetemplatesresponsetypedef)
- [ListProfileObjectTypesResponseTypeDef](./type_defs.md#listprofileobjecttypesresponsetypedef)
- [ListProfileObjectsResponseTypeDef](./type_defs.md#listprofileobjectsresponsetypedef)
- [ListTagsForResourceResponseTypeDef](./type_defs.md#listtagsforresourceresponsetypedef)
- [MatchingRequestTypeDef](./type_defs.md#matchingrequesttypedef)
- [MergeProfilesResponseTypeDef](./type_defs.md#mergeprofilesresponsetypedef)
- [PutIntegrationResponseTypeDef](./type_defs.md#putintegrationresponsetypedef)
- [PutProfileObjectResponseTypeDef](./type_defs.md#putprofileobjectresponsetypedef)
- [PutProfileObjectTypeResponseTypeDef](./type_defs.md#putprofileobjecttyperesponsetypedef)
- [SearchProfilesResponseTypeDef](./type_defs.md#searchprofilesresponsetypedef)
- [UpdateAddressTypeDef](./type_defs.md#updateaddresstypedef)
- [UpdateDomainResponseTypeDef](./type_defs.md#updatedomainresponsetypedef)
- [UpdateProfileResponseTypeDef](./type_defs.md#updateprofileresponsetypedef)
