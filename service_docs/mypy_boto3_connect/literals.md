# Literals for boto3 Connect module

> [Index](../index.md) > [Connect](./index.md) > Literals

Auto-generated documentation for [Connect](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect)
type annotations stubs module [mypy_boto3_connect](https://pypi.org/project/mypy-boto3-connect/).

- [Literals for boto3 Connect module](#literals-for-boto3-connect-module)
  - [Channel](#channel)
  - [Comparison](#comparison)
  - [ContactFlowType](#contactflowtype)
  - [CurrentMetricName](#currentmetricname)
  - [DirectoryType](#directorytype)
  - [EncryptionType](#encryptiontype)
  - [GetMetricDataPaginatorName](#getmetricdatapaginatorname)
  - [Grouping](#grouping)
  - [HistoricalMetricName](#historicalmetricname)
  - [HoursOfOperationDays](#hoursofoperationdays)
  - [InstanceAttributeType](#instanceattributetype)
  - [InstanceStatus](#instancestatus)
  - [InstanceStorageResourceType](#instancestorageresourcetype)
  - [IntegrationType](#integrationtype)
  - [ListApprovedOriginsPaginatorName](#listapprovedoriginspaginatorname)
  - [ListContactFlowsPaginatorName](#listcontactflowspaginatorname)
  - [ListHoursOfOperationsPaginatorName](#listhoursofoperationspaginatorname)
  - [ListInstanceAttributesPaginatorName](#listinstanceattributespaginatorname)
  - [ListInstanceStorageConfigsPaginatorName](#listinstancestorageconfigspaginatorname)
  - [ListInstancesPaginatorName](#listinstancespaginatorname)
  - [ListIntegrationAssociationsPaginatorName](#listintegrationassociationspaginatorname)
  - [ListLambdaFunctionsPaginatorName](#listlambdafunctionspaginatorname)
  - [ListLexBotsPaginatorName](#listlexbotspaginatorname)
  - [ListPhoneNumbersPaginatorName](#listphonenumberspaginatorname)
  - [ListPromptsPaginatorName](#listpromptspaginatorname)
  - [ListQueueQuickConnectsPaginatorName](#listqueuequickconnectspaginatorname)
  - [ListQueuesPaginatorName](#listqueuespaginatorname)
  - [ListQuickConnectsPaginatorName](#listquickconnectspaginatorname)
  - [ListRoutingProfileQueuesPaginatorName](#listroutingprofilequeuespaginatorname)
  - [ListRoutingProfilesPaginatorName](#listroutingprofilespaginatorname)
  - [ListSecurityKeysPaginatorName](#listsecuritykeyspaginatorname)
  - [ListSecurityProfilesPaginatorName](#listsecurityprofilespaginatorname)
  - [ListUseCasesPaginatorName](#listusecasespaginatorname)
  - [ListUserHierarchyGroupsPaginatorName](#listuserhierarchygroupspaginatorname)
  - [ListUsersPaginatorName](#listuserspaginatorname)
  - [PhoneNumberCountryCode](#phonenumbercountrycode)
  - [PhoneNumberType](#phonenumbertype)
  - [PhoneType](#phonetype)
  - [QueueStatus](#queuestatus)
  - [QueueType](#queuetype)
  - [QuickConnectType](#quickconnecttype)
  - [ReferenceType](#referencetype)
  - [SourceType](#sourcetype)
  - [Statistic](#statistic)
  - [StorageType](#storagetype)
  - [Unit](#unit)
  - [UseCaseType](#usecasetype)
  - [VoiceRecordingTrack](#voicerecordingtrack)

## Channel

```python
from mypy_boto3_connect.literals import Channel
```

Values:

- `CHAT`
- `TASK`
- `VOICE`

## Comparison

```python
from mypy_boto3_connect.literals import Comparison
```

Values:

- `LT`

## ContactFlowType

```python
from mypy_boto3_connect.literals import ContactFlowType
```

Values:

- `AGENT_HOLD`
- `AGENT_TRANSFER`
- `AGENT_WHISPER`
- `CONTACT_FLOW`
- `CUSTOMER_HOLD`
- `CUSTOMER_QUEUE`
- `CUSTOMER_WHISPER`
- `OUTBOUND_WHISPER`
- `QUEUE_TRANSFER`

## CurrentMetricName

```python
from mypy_boto3_connect.literals import CurrentMetricName
```

Values:

- `AGENTS_AFTER_CONTACT_WORK`
- `AGENTS_AVAILABLE`
- `AGENTS_ERROR`
- `AGENTS_NON_PRODUCTIVE`
- `AGENTS_ON_CALL`
- `AGENTS_ON_CONTACT`
- `AGENTS_ONLINE`
- `AGENTS_STAFFED`
- `CONTACTS_IN_QUEUE`
- `CONTACTS_SCHEDULED`
- `OLDEST_CONTACT_AGE`
- `SLOTS_ACTIVE`
- `SLOTS_AVAILABLE`

## DirectoryType

```python
from mypy_boto3_connect.literals import DirectoryType
```

Values:

- `CONNECT_MANAGED`
- `EXISTING_DIRECTORY`
- `SAML`

## EncryptionType

```python
from mypy_boto3_connect.literals import EncryptionType
```

Values:

- `KMS`

## GetMetricDataPaginatorName

```python
from mypy_boto3_connect.literals import GetMetricDataPaginatorName
```

Values:

- `get_metric_data`

## Grouping

```python
from mypy_boto3_connect.literals import Grouping
```

Values:

- `CHANNEL`
- `QUEUE`

## HistoricalMetricName

```python
from mypy_boto3_connect.literals import HistoricalMetricName
```

Values:

- `ABANDON_TIME`
- `AFTER_CONTACT_WORK_TIME`
- `API_CONTACTS_HANDLED`
- `CALLBACK_CONTACTS_HANDLED`
- `CONTACTS_ABANDONED`
- `CONTACTS_AGENT_HUNG_UP_FIRST`
- `CONTACTS_CONSULTED`
- `CONTACTS_HANDLED`
- `CONTACTS_HANDLED_INCOMING`
- `CONTACTS_HANDLED_OUTBOUND`
- `CONTACTS_HOLD_ABANDONS`
- `CONTACTS_MISSED`
- `CONTACTS_QUEUED`
- `CONTACTS_TRANSFERRED_IN`
- `CONTACTS_TRANSFERRED_IN_FROM_QUEUE`
- `CONTACTS_TRANSFERRED_OUT`
- `CONTACTS_TRANSFERRED_OUT_FROM_QUEUE`
- `HANDLE_TIME`
- `HOLD_TIME`
- `INTERACTION_AND_HOLD_TIME`
- `INTERACTION_TIME`
- `OCCUPANCY`
- `QUEUE_ANSWER_TIME`
- `QUEUED_TIME`
- `SERVICE_LEVEL`

## HoursOfOperationDays

```python
from mypy_boto3_connect.literals import HoursOfOperationDays
```

Values:

- `FRIDAY`
- `MONDAY`
- `SATURDAY`
- `SUNDAY`
- `THURSDAY`
- `TUESDAY`
- `WEDNESDAY`

## InstanceAttributeType

```python
from mypy_boto3_connect.literals import InstanceAttributeType
```

Values:

- `AUTO_RESOLVE_BEST_VOICES`
- `CONTACT_LENS`
- `CONTACTFLOW_LOGS`
- `EARLY_MEDIA`
- `INBOUND_CALLS`
- `OUTBOUND_CALLS`
- `USE_CUSTOM_TTS_VOICES`

## InstanceStatus

```python
from mypy_boto3_connect.literals import InstanceStatus
```

Values:

- `ACTIVE`
- `CREATION_FAILED`
- `CREATION_IN_PROGRESS`

## InstanceStorageResourceType

```python
from mypy_boto3_connect.literals import InstanceStorageResourceType
```

Values:

- `AGENT_EVENTS`
- `CALL_RECORDINGS`
- `CHAT_TRANSCRIPTS`
- `CONTACT_TRACE_RECORDS`
- `MEDIA_STREAMS`
- `SCHEDULED_REPORTS`

## IntegrationType

```python
from mypy_boto3_connect.literals import IntegrationType
```

Values:

- `EVENT`

## ListApprovedOriginsPaginatorName

```python
from mypy_boto3_connect.literals import ListApprovedOriginsPaginatorName
```

Values:

- `list_approved_origins`

## ListContactFlowsPaginatorName

```python
from mypy_boto3_connect.literals import ListContactFlowsPaginatorName
```

Values:

- `list_contact_flows`

## ListHoursOfOperationsPaginatorName

```python
from mypy_boto3_connect.literals import ListHoursOfOperationsPaginatorName
```

Values:

- `list_hours_of_operations`

## ListInstanceAttributesPaginatorName

```python
from mypy_boto3_connect.literals import ListInstanceAttributesPaginatorName
```

Values:

- `list_instance_attributes`

## ListInstanceStorageConfigsPaginatorName

```python
from mypy_boto3_connect.literals import ListInstanceStorageConfigsPaginatorName
```

Values:

- `list_instance_storage_configs`

## ListInstancesPaginatorName

```python
from mypy_boto3_connect.literals import ListInstancesPaginatorName
```

Values:

- `list_instances`

## ListIntegrationAssociationsPaginatorName

```python
from mypy_boto3_connect.literals import ListIntegrationAssociationsPaginatorName
```

Values:

- `list_integration_associations`

## ListLambdaFunctionsPaginatorName

```python
from mypy_boto3_connect.literals import ListLambdaFunctionsPaginatorName
```

Values:

- `list_lambda_functions`

## ListLexBotsPaginatorName

```python
from mypy_boto3_connect.literals import ListLexBotsPaginatorName
```

Values:

- `list_lex_bots`

## ListPhoneNumbersPaginatorName

```python
from mypy_boto3_connect.literals import ListPhoneNumbersPaginatorName
```

Values:

- `list_phone_numbers`

## ListPromptsPaginatorName

```python
from mypy_boto3_connect.literals import ListPromptsPaginatorName
```

Values:

- `list_prompts`

## ListQueueQuickConnectsPaginatorName

```python
from mypy_boto3_connect.literals import ListQueueQuickConnectsPaginatorName
```

Values:

- `list_queue_quick_connects`

## ListQueuesPaginatorName

```python
from mypy_boto3_connect.literals import ListQueuesPaginatorName
```

Values:

- `list_queues`

## ListQuickConnectsPaginatorName

```python
from mypy_boto3_connect.literals import ListQuickConnectsPaginatorName
```

Values:

- `list_quick_connects`

## ListRoutingProfileQueuesPaginatorName

```python
from mypy_boto3_connect.literals import ListRoutingProfileQueuesPaginatorName
```

Values:

- `list_routing_profile_queues`

## ListRoutingProfilesPaginatorName

```python
from mypy_boto3_connect.literals import ListRoutingProfilesPaginatorName
```

Values:

- `list_routing_profiles`

## ListSecurityKeysPaginatorName

```python
from mypy_boto3_connect.literals import ListSecurityKeysPaginatorName
```

Values:

- `list_security_keys`

## ListSecurityProfilesPaginatorName

```python
from mypy_boto3_connect.literals import ListSecurityProfilesPaginatorName
```

Values:

- `list_security_profiles`

## ListUseCasesPaginatorName

```python
from mypy_boto3_connect.literals import ListUseCasesPaginatorName
```

Values:

- `list_use_cases`

## ListUserHierarchyGroupsPaginatorName

```python
from mypy_boto3_connect.literals import ListUserHierarchyGroupsPaginatorName
```

Values:

- `list_user_hierarchy_groups`

## ListUsersPaginatorName

```python
from mypy_boto3_connect.literals import ListUsersPaginatorName
```

Values:

- `list_users`

## PhoneNumberCountryCode

```python
from mypy_boto3_connect.literals import PhoneNumberCountryCode
```

Values:

- `AD`
- `AE`
- `AF`
- `AG`
- `AI`
- `AL`
- `AM`
- `AN`
- `AO`
- `AQ`
- `AR`
- `AS`
- `AT`
- `AU`
- `AW`
- `AZ`
- `BA`
- `BB`
- `BD`
- `BE`
- `BF`
- `BG`
- `BH`
- `BI`
- `BJ`
- `BL`
- `BM`
- `BN`
- `BO`
- `BR`
- `BS`
- `BT`
- `BW`
- `BY`
- `BZ`
- `CA`
- `CC`
- `CD`
- `CF`
- `CG`
- `CH`
- `CI`
- `CK`
- `CL`
- `CM`
- `CN`
- `CO`
- `CR`
- `CU`
- `CV`
- `CW`
- `CX`
- `CY`
- `CZ`
- `DE`
- `DJ`
- `DK`
- `DM`
- `DO`
- `DZ`
- `EC`
- `EE`
- `EG`
- `EH`
- `ER`
- `ES`
- `ET`
- `FI`
- `FJ`
- `FK`
- `FM`
- `FO`
- `FR`
- `GA`
- `GB`
- `GD`
- `GE`
- `GG`
- `GH`
- `GI`
- `GL`
- `GM`
- `GN`
- `GQ`
- `GR`
- `GT`
- `GU`
- `GW`
- `GY`
- `HK`
- `HN`
- `HR`
- `HT`
- `HU`
- `ID`
- `IE`
- `IL`
- `IM`
- `IN`
- `IO`
- `IQ`
- `IR`
- `IS`
- `IT`
- `JE`
- `JM`
- `JO`
- `JP`
- `KE`
- `KG`
- `KH`
- `KI`
- `KM`
- `KN`
- `KP`
- `KR`
- `KW`
- `KY`
- `KZ`
- `LA`
- `LB`
- `LC`
- `LI`
- `LK`
- `LR`
- `LS`
- `LT`
- `LU`
- `LV`
- `LY`
- `MA`
- `MC`
- `MD`
- `ME`
- `MF`
- `MG`
- `MH`
- `MK`
- `ML`
- `MM`
- `MN`
- `MO`
- `MP`
- `MR`
- `MS`
- `MT`
- `MU`
- `MV`
- `MW`
- `MX`
- `MY`
- `MZ`
- `NA`
- `NC`
- `NE`
- `NG`
- `NI`
- `NL`
- `NO`
- `NP`
- `NR`
- `NU`
- `NZ`
- `OM`
- `PA`
- `PE`
- `PF`
- `PG`
- `PH`
- `PK`
- `PL`
- `PM`
- `PN`
- `PR`
- `PT`
- `PW`
- `PY`
- `QA`
- `RE`
- `RO`
- `RS`
- `RU`
- `RW`
- `SA`
- `SB`
- `SC`
- `SD`
- `SE`
- `SG`
- `SH`
- `SI`
- `SJ`
- `SK`
- `SL`
- `SM`
- `SN`
- `SO`
- `SR`
- `ST`
- `SV`
- `SX`
- `SY`
- `SZ`
- `TC`
- `TD`
- `TG`
- `TH`
- `TJ`
- `TK`
- `TL`
- `TM`
- `TN`
- `TO`
- `TR`
- `TT`
- `TV`
- `TW`
- `TZ`
- `UA`
- `UG`
- `US`
- `UY`
- `UZ`
- `VA`
- `VC`
- `VE`
- `VG`
- `VI`
- `VN`
- `VU`
- `WF`
- `WS`
- `YE`
- `YT`
- `ZA`
- `ZM`
- `ZW`

## PhoneNumberType

```python
from mypy_boto3_connect.literals import PhoneNumberType
```

Values:

- `DID`
- `TOLL_FREE`

## PhoneType

```python
from mypy_boto3_connect.literals import PhoneType
```

Values:

- `DESK_PHONE`
- `SOFT_PHONE`

## QueueStatus

```python
from mypy_boto3_connect.literals import QueueStatus
```

Values:

- `DISABLED`
- `ENABLED`

## QueueType

```python
from mypy_boto3_connect.literals import QueueType
```

Values:

- `AGENT`
- `STANDARD`

## QuickConnectType

```python
from mypy_boto3_connect.literals import QuickConnectType
```

Values:

- `PHONE_NUMBER`
- `QUEUE`
- `USER`

## ReferenceType

```python
from mypy_boto3_connect.literals import ReferenceType
```

Values:

- `URL`

## SourceType

```python
from mypy_boto3_connect.literals import SourceType
```

Values:

- `SALESFORCE`
- `ZENDESK`

## Statistic

```python
from mypy_boto3_connect.literals import Statistic
```

Values:

- `AVG`
- `MAX`
- `SUM`

## StorageType

```python
from mypy_boto3_connect.literals import StorageType
```

Values:

- `KINESIS_FIREHOSE`
- `KINESIS_STREAM`
- `KINESIS_VIDEO_STREAM`
- `S3`

## Unit

```python
from mypy_boto3_connect.literals import Unit
```

Values:

- `COUNT`
- `PERCENT`
- `SECONDS`

## UseCaseType

```python
from mypy_boto3_connect.literals import UseCaseType
```

Values:

- `RULES_EVALUATION`

## VoiceRecordingTrack

```python
from mypy_boto3_connect.literals import VoiceRecordingTrack
```

Values:

- `ALL`
- `FROM_AGENT`
- `TO_AGENT`
