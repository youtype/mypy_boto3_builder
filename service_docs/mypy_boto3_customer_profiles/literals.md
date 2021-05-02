# Literals for boto3 CustomerProfiles module

> [Index](../index.md) > [CustomerProfiles](./index.md) > Literals

Auto-generated documentation for [CustomerProfiles](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles)
type annotations stubs module [mypy_boto3_customer_profiles](https://pypi.org/project/mypy-boto3-customer-profiles/).

- [Literals for boto3 CustomerProfiles module](#literals-for-boto3-customerprofiles-module)
  - [DataPullMode](#datapullmode)
  - [FieldContentType](#fieldcontenttype)
  - [Gender](#gender)
  - [MarketoConnectorOperator](#marketoconnectoroperator)
  - [OperatorPropertiesKeys](#operatorpropertieskeys)
  - [PartyType](#partytype)
  - [S3ConnectorOperator](#s3connectoroperator)
  - [SalesforceConnectorOperator](#salesforceconnectoroperator)
  - [ServiceNowConnectorOperator](#servicenowconnectoroperator)
  - [SourceConnectorType](#sourceconnectortype)
  - [StandardIdentifier](#standardidentifier)
  - [TaskType](#tasktype)
  - [TriggerType](#triggertype)
  - [ZendeskConnectorOperator](#zendeskconnectoroperator)

## DataPullMode

```python
from mypy_boto3_customer_profiles.literals import DataPullMode
```

Values:

- `Complete`
- `Incremental`

## FieldContentType

```python
from mypy_boto3_customer_profiles.literals import FieldContentType
```

Values:

- `EMAIL_ADDRESS`
- `NAME`
- `NUMBER`
- `PHONE_NUMBER`
- `STRING`

## Gender

```python
from mypy_boto3_customer_profiles.literals import Gender
```

Values:

- `FEMALE`
- `MALE`
- `UNSPECIFIED`

## MarketoConnectorOperator

```python
from mypy_boto3_customer_profiles.literals import MarketoConnectorOperator
```

Values:

- `ADDITION`
- `BETWEEN`
- `DIVISION`
- `GREATER_THAN`
- `LESS_THAN`
- `MASK_ALL`
- `MASK_FIRST_N`
- `MASK_LAST_N`
- `MULTIPLICATION`
- `NO_OP`
- `PROJECTION`
- `SUBTRACTION`
- `VALIDATE_NON_NEGATIVE`
- `VALIDATE_NON_NULL`
- `VALIDATE_NON_ZERO`
- `VALIDATE_NUMERIC`

## OperatorPropertiesKeys

```python
from mypy_boto3_customer_profiles.literals import OperatorPropertiesKeys
```

Values:

- `CONCAT_FORMAT`
- `DATA_TYPE`
- `DESTINATION_DATA_TYPE`
- `LOWER_BOUND`
- `MASK_LENGTH`
- `MASK_VALUE`
- `MATH_OPERATION_FIELDS_ORDER`
- `SOURCE_DATA_TYPE`
- `SUBFIELD_CATEGORY_MAP`
- `TRUNCATE_LENGTH`
- `UPPER_BOUND`
- `VALIDATION_ACTION`
- `VALUE`
- `VALUES`

## PartyType

```python
from mypy_boto3_customer_profiles.literals import PartyType
```

Values:

- `BUSINESS`
- `INDIVIDUAL`
- `OTHER`

## S3ConnectorOperator

```python
from mypy_boto3_customer_profiles.literals import S3ConnectorOperator
```

Values:

- `ADDITION`
- `BETWEEN`
- `DIVISION`
- `EQUAL_TO`
- `GREATER_THAN`
- `GREATER_THAN_OR_EQUAL_TO`
- `LESS_THAN`
- `LESS_THAN_OR_EQUAL_TO`
- `MASK_ALL`
- `MASK_FIRST_N`
- `MASK_LAST_N`
- `MULTIPLICATION`
- `NO_OP`
- `NOT_EQUAL_TO`
- `PROJECTION`
- `SUBTRACTION`
- `VALIDATE_NON_NEGATIVE`
- `VALIDATE_NON_NULL`
- `VALIDATE_NON_ZERO`
- `VALIDATE_NUMERIC`

## SalesforceConnectorOperator

```python
from mypy_boto3_customer_profiles.literals import SalesforceConnectorOperator
```

Values:

- `ADDITION`
- `BETWEEN`
- `CONTAINS`
- `DIVISION`
- `EQUAL_TO`
- `GREATER_THAN`
- `GREATER_THAN_OR_EQUAL_TO`
- `LESS_THAN`
- `LESS_THAN_OR_EQUAL_TO`
- `MASK_ALL`
- `MASK_FIRST_N`
- `MASK_LAST_N`
- `MULTIPLICATION`
- `NO_OP`
- `NOT_EQUAL_TO`
- `PROJECTION`
- `SUBTRACTION`
- `VALIDATE_NON_NEGATIVE`
- `VALIDATE_NON_NULL`
- `VALIDATE_NON_ZERO`
- `VALIDATE_NUMERIC`

## ServiceNowConnectorOperator

```python
from mypy_boto3_customer_profiles.literals import ServiceNowConnectorOperator
```

Values:

- `ADDITION`
- `BETWEEN`
- `CONTAINS`
- `DIVISION`
- `EQUAL_TO`
- `GREATER_THAN`
- `GREATER_THAN_OR_EQUAL_TO`
- `LESS_THAN`
- `LESS_THAN_OR_EQUAL_TO`
- `MASK_ALL`
- `MASK_FIRST_N`
- `MASK_LAST_N`
- `MULTIPLICATION`
- `NO_OP`
- `NOT_EQUAL_TO`
- `PROJECTION`
- `SUBTRACTION`
- `VALIDATE_NON_NEGATIVE`
- `VALIDATE_NON_NULL`
- `VALIDATE_NON_ZERO`
- `VALIDATE_NUMERIC`

## SourceConnectorType

```python
from mypy_boto3_customer_profiles.literals import SourceConnectorType
```

Values:

- `Marketo`
- `S3`
- `Salesforce`
- `Servicenow`
- `Zendesk`

## StandardIdentifier

```python
from mypy_boto3_customer_profiles.literals import StandardIdentifier
```

Values:

- `LOOKUP_ONLY`
- `NEW_ONLY`
- `PROFILE`
- `SECONDARY`
- `UNIQUE`

## TaskType

```python
from mypy_boto3_customer_profiles.literals import TaskType
```

Values:

- `Arithmetic`
- `Filter`
- `Map`
- `Mask`
- `Merge`
- `Truncate`
- `Validate`

## TriggerType

```python
from mypy_boto3_customer_profiles.literals import TriggerType
```

Values:

- `Event`
- `OnDemand`
- `Scheduled`

## ZendeskConnectorOperator

```python
from mypy_boto3_customer_profiles.literals import ZendeskConnectorOperator
```

Values:

- `ADDITION`
- `DIVISION`
- `GREATER_THAN`
- `MASK_ALL`
- `MASK_FIRST_N`
- `MASK_LAST_N`
- `MULTIPLICATION`
- `NO_OP`
- `PROJECTION`
- `SUBTRACTION`
- `VALIDATE_NON_NEGATIVE`
- `VALIDATE_NON_NULL`
- `VALIDATE_NON_ZERO`
- `VALIDATE_NUMERIC`
