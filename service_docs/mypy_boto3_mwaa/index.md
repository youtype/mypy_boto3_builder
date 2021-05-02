# Type annotations for boto3 MWAA module

> [Index](../index.md) > MWAA

Auto-generated documentation for [MWAA](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa.html#MWAA)
type annotations stubs module [mypy_boto3_mwaa](https://pypi.org/project/mypy-boto3-mwaa/).

```bash
pip install mypy-boto3-mwaa
```

- [Type annotations for boto3 MWAA module](#type-annotations-for-boto3-mwaa-module)
  - [MWAAClient](#mwaaclient)
    - [Methods](#methods)
    - [Exceptions](#exceptions)
  - [Paginators](#paginators)
  - [Literals](#literals)
  - [Structures](#structures)

## MWAAClient

Type annotations for  `boto3.client("mwaa")` as [MWAAClient](./client.md)

Can be used directly:

```python
from mypy_boto3_mwaa.client import MWAAClient
```


MWAAClient [exceptions](./client.md#exceptions)



### Methods
- [can_paginate](./client.md#can-paginate)
- [create_cli_token](./client.md#create-cli-token)
- [create_environment](./client.md#create-environment)
- [create_web_login_token](./client.md#create-web-login-token)
- [delete_environment](./client.md#delete-environment)
- [generate_presigned_url](./client.md#generate-presigned-url)
- [get_environment](./client.md#get-environment)
- [get_paginator](./client.md#get-paginator)
- [list_environments](./client.md#list-environments)
- [list_tags_for_resource](./client.md#list-tags-for-resource)
- [publish_metrics](./client.md#publish-metrics)
- [tag_resource](./client.md#tag-resource)
- [untag_resource](./client.md#untag-resource)
- [update_environment](./client.md#update-environment)




### Exceptions
- [AccessDeniedException](./client.md#accessdeniedexception)
- [ClientError](./client.md#clienterror)
- [InternalServerException](./client.md#internalserverexception)
- [ResourceNotFoundException](./client.md#resourcenotfoundexception)
- [ValidationException](./client.md#validationexception)






## Paginators

Type annotations for [paginators](./paginators.md) from `boto3.client("mwaa").get_paginator("...")`.

Can be used directly:

```python
from mypy_boto3_mwaa.paginators import ListEnvironmentsPaginator, ...
```

- [ListEnvironmentsPaginator](./paginators.md#listenvironmentspaginator)






## Literals

Type annotations for [literals](./literals.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_mwaa.literals import EnvironmentStatus, ...
```

- [EnvironmentStatus](./literals.md#environmentstatus)
- [ListEnvironmentsPaginatorName](./literals.md#listenvironmentspaginatorname)
- [LoggingLevel](./literals.md#logginglevel)
- [Unit](./literals.md#unit)
- [UpdateStatus](./literals.md#updatestatus)
- [WebserverAccessMode](./literals.md#webserveraccessmode)




## Structures


Type annotations for [typed dictionaries](./type_defs.md) used in methods and schema.

Can be used directly:

```python
from mypy_boto3_mwaa.type_defs import DimensionTypeDef, ...
```

- [DimensionTypeDef](./type_defs.md#dimensiontypedef)
- [EnvironmentTypeDef](./type_defs.md#environmenttypedef)
- [LastUpdateTypeDef](./type_defs.md#lastupdatetypedef)
- [LoggingConfigurationTypeDef](./type_defs.md#loggingconfigurationtypedef)
- [ModuleLoggingConfigurationInputTypeDef](./type_defs.md#moduleloggingconfigurationinputtypedef)
- [ModuleLoggingConfigurationTypeDef](./type_defs.md#moduleloggingconfigurationtypedef)
- [NetworkConfigurationTypeDef](./type_defs.md#networkconfigurationtypedef)
- [ResponseMetadata](./type_defs.md#responsemetadata)
- [StatisticSetTypeDef](./type_defs.md#statisticsettypedef)
- [UpdateErrorTypeDef](./type_defs.md#updateerrortypedef)
- [CreateCliTokenResponseTypeDef](./type_defs.md#createclitokenresponsetypedef)
- [CreateEnvironmentOutputTypeDef](./type_defs.md#createenvironmentoutputtypedef)
- [CreateWebLoginTokenResponseTypeDef](./type_defs.md#createweblogintokenresponsetypedef)
- [GetEnvironmentOutputTypeDef](./type_defs.md#getenvironmentoutputtypedef)
- [ListEnvironmentsOutputTypeDef](./type_defs.md#listenvironmentsoutputtypedef)
- [ListTagsForResourceOutputTypeDef](./type_defs.md#listtagsforresourceoutputtypedef)
- [LoggingConfigurationInputTypeDef](./type_defs.md#loggingconfigurationinputtypedef)
- [MetricDatumTypeDef](./type_defs.md#metricdatumtypedef)
- [PaginatorConfigTypeDef](./type_defs.md#paginatorconfigtypedef)
- [UpdateEnvironmentOutputTypeDef](./type_defs.md#updateenvironmentoutputtypedef)
- [UpdateNetworkConfigurationInputTypeDef](./type_defs.md#updatenetworkconfigurationinputtypedef)
